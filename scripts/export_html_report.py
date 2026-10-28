#!/usr/bin/env python3
"""
Fully Hardened HTML Dashboard Exporter for Frontier Innovator.
Converts markdown research dossiers or innovation reports into a self-contained,
dark-mode HTML visual report with comprehensive XSS protection, safe Mermaid.js
sanitization, and Content Security Policy (CSP).
"""

import sys
import re
import html
import argparse
from urllib.parse import urlparse

# Ensure UTF-8 output across all operating systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self' https://cdn.tailwindcss.com https://cdn.jsdelivr.net 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; font-src https: data:; img-src https: data:; connect-src 'none';">
    <title>{{title}}</title>
    <!-- Tailwind CSS (via CDN) -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        frontier: {
                            50: '#f0fdf4',
                            500: '#22c55e',
                            900: '#14532d',
                            bg: '#0a0f1d',
                            card: '#111827',
                            border: '#1f2937',
                            accent: '#38bdf8'
                        }
                    }
                }
            }
        }
    </script>
    <!-- Mermaid.js (via CDN) -->
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({ startOnLoad: true, theme: 'dark', securityLevel: 'strict' });
    </script>
    <style>
        body { background-color: #0b0f19; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        .mermaid { background: #111827; padding: 1.5rem; border-radius: 0.75rem; border: 1px solid #1f2937; margin: 1.5rem 0; overflow-x: auto; }
        pre code { background: #111827; border-radius: 0.5rem; padding: 1rem; display: block; overflow-x: auto; border: 1px solid #1f2937; }
        blockquote { border-left: 4px solid #38bdf8; padding-left: 1rem; color: #94a3b8; font-style: italic; margin: 1rem 0; }
        table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; }
        th, td { border: 1px solid #374151; padding: 0.75rem 1rem; text-align: left; }
        th { background-color: #1f2937; color: #38bdf8; }
        tr:nth-child(even) { background-color: #111827; }
        h1 { font-size: 2.25rem; font-weight: 800; color: #f8fafc; margin-bottom: 1rem; border-bottom: 2px solid #1f2937; padding-bottom: 0.5rem; }
        h2 { font-size: 1.5rem; font-weight: 700; color: #38bdf8; margin-top: 2rem; margin-bottom: 0.75rem; }
        h3 { font-size: 1.25rem; font-weight: 600; color: #a5f3fc; margin-top: 1.25rem; margin-bottom: 0.5rem; }
        a { color: #38bdf8; text-decoration: underline; }
        a:hover { color: #7dd3fc; }
    </style>
</head>
<body class="p-6 md:p-12 max-w-5xl mx-auto">
    <header class="mb-8 flex items-center justify-between border-b border-gray-800 pb-4">
        <div class="flex items-center space-x-3">
            <span class="text-3xl" aria-hidden="true">⚡</span>
            <div>
                <h2 class="text-xl font-bold text-white tracking-wide uppercase !m-0">Frontier Innovator</h2>
                <p class="text-xs text-gray-400">Deep-Tech & Radical Invention Dashboard</p>
            </div>
        </div>
        <span class="px-3 py-1 text-xs font-semibold rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800">
            Frontier Production Grade
        </span>
    </header>

    <main class="space-y-6">
        {{content}}
    </main>

    <footer class="mt-16 pt-6 border-t border-gray-800 text-center text-xs text-gray-500">
        Frontier Innovator Engine • MIT Open Source • Sanitized & Hardened Export
    </footer>
</body>
</html>
"""

def is_safe_url(target_url: str) -> bool:
    """Validates that a URL strictly uses safe protocols (http, https, or relative anchor)."""
    if not target_url or not isinstance(target_url, str):
        return False
    clean_url = target_url.strip()
    # Reject dangerous URI schemes
    lowered = clean_url.lower()
    if lowered.startswith(('javascript:', 'data:', 'vbscript:', 'file:')):
        return False
    parsed = urlparse(clean_url)
    if parsed.scheme in ('http', 'https'):
        return True
    if clean_url.startswith(('#', './', '/')):
        return True
    return False

def sanitize_mermaid_diagram(raw_diagram: str) -> str:
    """
    Sanitizes Mermaid syntax to prevent DOM breakout or HTML injection.
    Mermaid v10 parses text inside .mermaid. To prevent injection:
    - Strips all HTML/XML tags (<...>) from node labels and labels.
    - Neutralizes closing </div> or </script> tags.
    """
    # Remove any HTML tags completely inside the diagram definition
    stripped = re.sub(r'</?[a-zA-Z][^>]*>', '', raw_diagram)
    # Neutralize any residual angle brackets
    neutralized = stripped.replace('<', '&lt;').replace('>', '&gt;')
    return neutralized.strip()

def format_inline_markdown(text: str) -> str:
    """Escapes HTML and applies safe inline formatting (bold, italic, links, code)."""
    escaped = html.escape(text, quote=True)

    # Inline code: `code`
    escaped = re.sub(r'`([^`]+)`', r'<code class="px-1.5 py-0.5 rounded bg-gray-800 text-cyan-300 text-xs font-mono">\1</code>', escaped)

    # Bold: **text**
    escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong class="text-white font-semibold">\1</strong>', escaped)

    # Italic: *text*
    escaped = re.sub(r'\*([^\*]+)\*', r'<em class="italic text-gray-300">\1</em>', escaped)

    # Links: [label](url)
    def render_link(match):
        raw_label = match.group(1)
        raw_url = html.unescape(match.group(2)).strip()
        if is_safe_url(raw_url):
            safe_href = html.escape(raw_url, quote=True)
            return f'<a href="{safe_href}" target="_blank" rel="noopener noreferrer" class="text-cyan-400 hover:text-cyan-300 underline">{raw_label}</a>'
        return raw_label

    escaped = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', render_link, escaped)
    return escaped

def parse_markdown_to_html(md_text: str) -> str:
    """Hardened, secure Markdown-to-HTML parser with strict XSS protection and Mermaid sanitization."""
    if not md_text:
        return ""

    # 1. Isolate and strictly sanitize Mermaid blocks
    mermaid_blocks = []
    def stash_mermaid(match):
        clean_diagram = sanitize_mermaid_diagram(match.group(1))
        idx = len(mermaid_blocks)
        mermaid_blocks.append(clean_diagram)
        return f"__MERMAID_BLOCK_{idx}__"

    processed = re.sub(r'```mermaid\s*([\s\S]*?)\s*```', stash_mermaid, md_text)

    # 2. Isolate generic code blocks
    code_blocks = []
    def stash_code(match):
        lang = match.group(1) or ""
        code = match.group(2).strip()
        idx = len(code_blocks)
        escaped_code = html.escape(code)
        safe_lang = re.sub(r'[^a-zA-Z0-9_-]', '', lang)
        code_blocks.append(f'<pre><code class="language-{safe_lang}">{escaped_code}</code></pre>')
        return f"__CODE_BLOCK_{idx}__"

    processed = re.sub(r'```([a-zA-Z0-9_-]*)\s*([\s\S]*?)\s*```', stash_code, processed)

    lines = processed.split('\n')
    html_lines = []
    in_table = False
    in_list = False

    for line in lines:
        line_stripped = line.strip()

        # Handle stashed Mermaid blocks
        if line_stripped.startswith('__MERMAID_BLOCK_') and line_stripped.endswith('__'):
            m_idx = int(line_stripped.replace('__MERMAID_BLOCK_', '').replace('__', ''))
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<div class="mermaid">\n{mermaid_blocks[m_idx]}\n</div>')
            continue

        # Handle stashed Code blocks
        if line_stripped.startswith('__CODE_BLOCK_') and line_stripped.endswith('__'):
            c_idx = int(line_stripped.replace('__CODE_BLOCK_', '').replace('__', ''))
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_table:
                html_lines.append('</table>')
                in_table = False
            html_lines.append(code_blocks[c_idx])
            continue

        # Tables
        if line_stripped.startswith('|') and line_stripped.endswith('|'):
            if re.match(r'^\|[\s\-:|]+\|$', line_stripped):
                continue
            cells = [format_inline_markdown(c.strip()) for c in line_stripped.split('|')[1:-1]]
            tag = 'th' if not in_table else 'td'
            row_html = '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>'
            if not in_table:
                html_lines.append('<table class="w-full text-sm">')
                in_table = True
            html_lines.append(row_html)
            continue
        elif in_table:
            html_lines.append('</table>')
            in_table = False

        # Lists
        if line_stripped.startswith(('- ', '* ')):
            item_text = format_inline_markdown(line_stripped[2:])
            if not in_list:
                html_lines.append('<ul class="list-disc pl-6 space-y-1 text-gray-300">')
                in_list = True
            html_lines.append(f'<li>{item_text}</li>')
            continue
        elif in_list and not line_stripped.startswith(('- ', '* ')):
            html_lines.append('</ul>')
            in_list = False

        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{format_inline_markdown(line[2:].strip())}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{format_inline_markdown(line[3:].strip())}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{format_inline_markdown(line[4:].strip())}</h3>')
        elif line.startswith('> '):
            html_lines.append(f'<blockquote>{format_inline_markdown(line[2:].strip())}</blockquote>')
        elif line_stripped.startswith('---'):
            html_lines.append('<hr class="border-gray-800 my-6" />')
        elif line_stripped == '':
            pass
        else:
            html_lines.append(f'<p class="text-gray-300 leading-relaxed">{format_inline_markdown(line)}</p>')

    if in_table:
        html_lines.append('</table>')
    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)

def export_to_html(markdown_content: str, title: str = "Frontier Innovator Report") -> str:
    """
    Primary canonical entry point for generating HTML.
    Safely escapes the title and parses markdown content through hardened pipeline.
    """
    safe_title = html.escape(str(title).strip(), quote=True)
    parsed_content = parse_markdown_to_html(markdown_content)
    return HTML_TEMPLATE.replace("{{title}}", safe_title).replace("{{content}}", parsed_content)

def main():
    parser = argparse.ArgumentParser(description="Secure HTML Dashboard Exporter for Frontier Innovator.")
    parser.add_argument("input_file", help="Path to markdown file (e.g. dossier.md)")
    parser.add_argument("--output", "-o", help="Target HTML file path")
    args = parser.parse_args()

    output_path = args.output or (args.input_file.rsplit('.', 1)[0] + '.html')

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        print(f"[-] Dosya okunamadı: {e}", file=sys.stderr)
        sys.exit(1)

    rendered_html = export_to_html(md_content, title="Frontier Innovator Report")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print(f"[+] Güvenlik zırhlı görsel HTML Dashboard oluşturuldu: {output_path}")

if __name__ == "__main__":
    main()
