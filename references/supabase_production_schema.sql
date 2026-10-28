-- ==============================================================================
-- ZOBAR SKILL: Production-Grade Supabase & PostgreSQL 16+ Architecture
-- Features: Multi-tenancy, Row Level Security (RLS), pgvector (HNSW), Realtime, WAL Tuning
-- ==============================================================================

-- 1. Enable Critical Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";      -- pgvector for semantic search & RAG
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 2. Organizations / Multi-Tenant Workspaces
CREATE TABLE IF NOT EXISTS public.organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    plan TEXT NOT NULL DEFAULT 'free' CHECK (plan IN ('free', 'pro', 'enterprise')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 3. User Profiles linked to Supabase Auth (auth.users)
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    org_id UUID REFERENCES public.organizations(id) ON DELETE SET NULL,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT,
    avatar_url TEXT,
    role TEXT NOT NULL DEFAULT 'member' CHECK (role IN ('owner', 'admin', 'member')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 4. Vector Documents / Semantic Cache Store in Postgres
CREATE TABLE IF NOT EXISTS public.documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID NOT NULL REFERENCES public.organizations(id) ON DELETE CASCADE,
    created_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    -- 1536-dim vector for OpenAI / 384-dim for MiniLM. Here we use 1536 for universal compatibility
    embedding vector(1536),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 5. Sub-Millisecond HNSW Index for Vector Similarity Search (Cosine distance)
-- m=16, ef_construction=64 provides the optimal tradeoff between index speed and recall
CREATE INDEX IF NOT EXISTS idx_documents_embedding_hnsw 
ON public.documents 
USING hnsw (embedding vector_cosine_ops) 
WITH (m = 16, ef_construction = 64);

-- Standard high-throughput B-tree indexes for foreign keys & filtering
CREATE INDEX IF NOT EXISTS idx_documents_org_id ON public.documents(org_id);
CREATE INDEX IF NOT EXISTS idx_profiles_org_id ON public.profiles(org_id);
CREATE INDEX IF NOT EXISTS idx_documents_metadata_gin ON public.documents USING gin (metadata);

-- ==============================================================================
-- ROW LEVEL SECURITY (RLS) POLICIES — Zero-Leak Security Layer
-- ==============================================================================

ALTER TABLE public.organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.documents ENABLE ROW LEVEL SECURITY;

-- Helper function: Get the current user's org_id securely
CREATE OR REPLACE FUNCTION public.get_auth_org_id()
RETURNS UUID
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
    SELECT org_id FROM public.profiles WHERE id = auth.uid() LIMIT 1;
$$;

-- Policies for Organizations
CREATE POLICY "Users can view their own organization"
ON public.organizations
FOR SELECT
USING (id = public.get_auth_org_id());

-- Policies for Profiles
CREATE POLICY "Users can view members in their own organization"
ON public.profiles
FOR SELECT
USING (org_id = public.get_auth_org_id());

CREATE POLICY "Users can update their own profile"
ON public.profiles
FOR UPDATE
USING (id = auth.uid())
WITH CHECK (id = auth.uid());

-- Policies for Documents (Multi-Tenant Isolation)
CREATE POLICY "Tenant isolation for document read"
ON public.documents
FOR SELECT
USING (org_id = public.get_auth_org_id());

CREATE POLICY "Tenant isolation for document write"
ON public.documents
FOR INSERT
WITH CHECK (org_id = public.get_auth_org_id());

CREATE POLICY "Tenant isolation for document update"
ON public.documents
FOR UPDATE
USING (org_id = public.get_auth_org_id())
WITH CHECK (org_id = public.get_auth_org_id());

CREATE POLICY "Tenant isolation for document delete"
ON public.documents
FOR DELETE
USING (org_id = public.get_auth_org_id());

-- ==============================================================================
-- REALTIME PUBLICATION & STREAMING (Elixir Phoenix WebSocket Gateway)
-- ==============================================================================

-- Enable Realtime publication only on necessary tables to prevent WAL saturation
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_publication_tables 
        WHERE pubname = 'supabase_realtime' AND tablename = 'documents'
    ) THEN
        ALTER PUBLICATION supabase_realtime ADD TABLE public.documents;
    END IF;
END $$;

-- Set replica identity to FULL so that update/delete broadcasts carry old and new records
ALTER TABLE public.documents REPLICA IDENTITY FULL;

-- ==============================================================================
-- AUTOMATIC TIMESTAMP TRIGGER
-- ==============================================================================
CREATE OR REPLACE FUNCTION public.handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trigger_documents_updated_at ON public.documents;
CREATE TRIGGER trigger_documents_updated_at
    BEFORE UPDATE ON public.documents
    FOR EACH ROW
    EXECUTE FUNCTION public.handle_updated_at();
