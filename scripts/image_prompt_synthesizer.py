"""
Master Image Prompt Synthesizer & Visual AI Engine
Zobar Skill — Midjourney v6, FLUX.1, DALL-E 3 & SDXL Prompt Generator

Mimari:
1. Sinematik ve Fotogerçekçi Optik Motoru (Kamera, lens, diyafram, enstantane).
2. Işık ve Atmosfer Katmanı (Rembrandt, volumetrik sis, kostik yansımalar).
3. Modern UI/UX ve Ürün Render Şablonları (Apple/Linear tarzı 3D mockup).
4. Motor Parametreleri (--ar 16:9, --v 6.1, Negatif prompt filtresi).
"""

import sys
from typing import Dict, Any, List, Optional


class ImagePromptSynthesizer:
    STYLE_PRESETS = {
        "photorealistic_cinematic": {
            "camera": "Shot on Hasselblad H6D-100c, 85mm f/1.4 lens",
            "lighting": "Cinematic volumetric lighting, soft Rembrandt shadows, subtle golden hour rim light",
            "texture": "Ultra-detailed skin textures with natural pores, 8k resolution, photorealistic depth of field",
            "grading": "Kodak Portra 400 film stock color grading, subtle film grain, muted contrast",
        },
        "modern_ui_product_mockup": {
            "camera": "Top-down 45-degree isometric 3D studio render",
            "lighting": "Softbox studio diffusion, ambient occlusion, subtle neon edge reflections",
            "texture": "Clean frosted glassmorphism, matte aluminum frame, OLED deep black screen, Figma-style component layout",
            "grading": "High dynamic range (HDR), crisp vectors, sleek dark mode aesthetic",
        },
        "cyberpunk_scifi": {
            "camera": "35mm anamorphic wide-angle cinema lens, low-angle dynamic framing",
            "lighting": "High-contrast neon cyan and magenta reflections on wet asphalt, volumetric haze, lens flares",
            "texture": "Intricate carbon fiber weave, glowing fiber-optic telemetry, ray-traced reflections",
            "grading": "Blade Runner 2049 cinematic color palette, deep atmospheric blues and harsh neon glows",
        },
        "minimalist_architectural": {
            "camera": "Architectural tilt-shift lens 24mm, straight leading lines",
            "lighting": "Natural diffused skylight, raking sunlight through brutalist concrete slats",
            "texture": "Raw board-formed concrete, warm Scandinavian timber accents, clear water pool reflections",
            "grading": "Architectural Digest editorial look, neutral white balance, sharp clean geometry",
        },
        "master_brandmark_logo": {
            "camera": "Paul Rand and Otl Aicher minimalist Swiss graphic design, flat 2D vector composition",
            "lighting": "Pure monolithic silhouette, high-contrast figure-ground Gestalt closure, zero gradients",
            "texture": "Clean mathematical vector lines, 24x24 grid alignment, uniform stroke weight",
            "grading": "Monochrome archival black ink on white cotton card, razor-sharp edges",
        },
        "anti_ai_pictogram_icon": {
            "camera": "Dieter Rams functionalist iconography, Otl Aicher 1972 Munich Olympic grid system",
            "lighting": "Zero glossy clay, zero neon glows, zero 3D reflections, flat vector silhouette",
            "texture": "Crisp geometric cuts, precision optical balance, sub-pixel curve overshoot",
            "grading": "Museum-grade brandmark, Helvetica Swiss typography harmony",
        },
    }

    NEGATIVE_PROMPT_UNIVERSAL = (
        "glossy 3d clay, bubble plastic, colorful rainbow gradient, photorealistic background, blurry edges, "
        "melted lines, complex internal circuits, floating sparkles, neon lens flare, skeuomorphic reflections, "
        "asymmetrical curves, cartoonish render, low-res artifacts, deformed, bad anatomy, blurry, watermark"
    )

    def synthesize(
        self,
        subject: str,
        style: str = "photorealistic_cinematic",
        aspect_ratio: str = "16:9",
        engine: str = "midjourney",
        extra_details: Optional[str] = None,
    ) -> Dict[str, Any]:
        preset = self.STYLE_PRESETS.get(style, self.STYLE_PRESETS["photorealistic_cinematic"])

        prompt_elements = [
            subject.strip(),
            preset["camera"],
            preset["lighting"],
            preset["texture"],
            preset["grading"],
        ]
        if extra_details:
            prompt_elements.append(extra_details.strip())

        raw_prompt = ", ".join(prompt_elements)

        # Engine-specific formatting
        if engine.lower() in ("midjourney", "mj"):
            final_prompt = f"{raw_prompt} --ar {aspect_ratio} --v 6.1 --style raw --stylize 250"
            negative = None
        elif engine.lower() in ("flux", "flux.1"):
            final_prompt = f"{raw_prompt}, hyper-realistic photography, high fidelity rendering, 8k uhd"
            negative = self.NEGATIVE_PROMPT_UNIVERSAL
        elif engine.lower() in ("dalle", "dalle3", "dall-e 3"):
            final_prompt = f"A highly detailed, professional visual of: {raw_prompt}. Photorealistic, award-winning composition."
            negative = None
        else:  # SDXL
            final_prompt = f"{raw_prompt}, masterpiece, trending on Artstation"
            negative = self.NEGATIVE_PROMPT_UNIVERSAL

        return {
            "subject": subject,
            "style": style,
            "engine": engine,
            "aspect_ratio": aspect_ratio,
            "positive_prompt": final_prompt,
            "negative_prompt": negative,
            "technical_specs": {
                "optics": preset["camera"],
                "lighting_model": preset["lighting"],
                "texture_quality": preset["texture"],
            },
        }

    def generate_ui_app_mockup(self, app_name: str, app_concept: str) -> Dict[str, Any]:
        """
        Generates S-Tier product showcase mockups for app landing pages.
        """
        subject = (
            f"Sleek desktop dashboard UI mockup of '{app_name}', {app_concept}, "
            f"displaying real-time telemetry graphs, dark mode Bento Grid cards, and modern typography"
        )
        return self.synthesize(
            subject=subject,
            style="modern_ui_product_mockup",
            aspect_ratio="16:9",
            engine="midjourney",
        )

    def generate_master_logo_or_icon(
        self,
        brand_name: str,
        concept: str,
        archetype: str = "negative_space_monolith",
        medium: str = "vector_silkscreen",
        engine: str = "midjourney"
    ) -> Dict[str, Any]:
        """
        Generates master graphic design brandmarks and anti-cliché pictograms
        grounded in Paul Rand, Josef Müller-Brockmann, and Dieter Rams principles.
        """
        from scripts.graphic_design_mastery_engine import GraphicDesignMasteryEngine
        gd_engine = GraphicDesignMasteryEngine()
        eval_result = gd_engine.evaluate_paul_rand_test(brand_name, concept, archetype)
        prompt_result = gd_engine.synthesize_master_prompt(f"{brand_name} - {concept}", archetype, medium, engine)
        svg_result = gd_engine.generate_parametric_svg(brand_name, archetype)

        return {
            "brand_name": brand_name,
            "concept": concept,
            "archetype": archetype,
            "paul_rand_evaluation": eval_result,
            "image_prompts": prompt_result,
            "parametric_svg": svg_result
        }


if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    synth = ImagePromptSynthesizer()
    res = synth.synthesize(
        subject="A robotic AI surgeon performing microsurgery in an ultra-modern hospital laboratory",
        style="photorealistic_cinematic",
        aspect_ratio="16:9",
        engine="midjourney",
    )
    print("=" * 65)
    print("[*] GÖRSEL YAPAY ZEKÂ PROMPT SENTEZLEYİCİ")
    print("=" * 65)
    print(f"Pozitif Prompt:\n{res['positive_prompt']}\n")
    if res['negative_prompt']:
        print(f"Negatif Prompt:\n{res['negative_prompt']}\n")
