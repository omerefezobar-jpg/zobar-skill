#!/usr/bin/env python3
"""
HTML Dashboard Exporter for Frontier Innovator.
Converts markdown research dossiers or innovation reports into a self-contained,
dark-mode HTML visual report with embedded Mermaid.js rendering.
"""

import sys
import re
import html
import argparse

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        mermaid.initialize({ startOnLoad: true, theme: 'dark' });
    </script>
    <style>
        body { background-color: #0b0f19; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        .mermaid { background: #111827; padding: 1.5rem; border-radius: 0.75rem; border: 1px solid #1f2937; margin: 1.5rem 0; }
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
    <div class="mb-8 flex items-center justify-between border-b border-gray-800 pb-4">
        <div class="flex items-center space-x-3">
            <span class="text-3xl">⚡</span>
            <div>
                <h2 class="text-xl font-bold text-white tracking-wide uppercase !m-0">Frontier Innovator</h2>
                <p class="text-xs text-gray-400">Deep-Tech & Radical Invention Dashboard</p>
            </div>
        </div>
        <span class="px-3 py-1 text-xs font-semibold rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800">
            Frontier Grade
        </span>
    </div>

    <main class="space-y-6">
        {{content}}
    </main>

    <footer class="mt-16 pt-6 border-t border-gray-800 text-center text-xs text-gray-500">
        Frontier Innovator Engine • MIT Open Source • Generated for Autonomous Deep-Tech R&D
    </footer>
</body>
</html>
"""

def parse_markdown_to_html(md_text: str) -> str:
    """Simple, lightweight markdown-to-html converter supporting Mermaid diagrams."""
    # Convert Mermaid blocks
    def replace_mermaid(match):
        diagram = match.group(1).strip()
        return f'<div class="mermaid">\n{diagram}\n</div>'

    processed = re.sub(r'```mermaid\s*([\s\S]*?)\s*```', replace_mermaid, md_text)

    # Convert generic code blocks
    def replace_code(match):
        lang = match.group(1) or ""
        code = html.escape(match.group(2).strip())
        return f'<pre><code class="language-{lang}">{code}</code></pre>'

    processed = re.sub(r'```([a-zA-Z0-9_-]*)\s*([\s\S]*?)\s*```', replace_code, processed)

    lines = processed.split('\n')
    html_lines = []
    in_table = False
    in_list = False

    for line in lines:
        line_stripped = line.strip()

        # Table detection
        if line_stripped.startswith('|') and line_stripped.endswith('|'):
            if '---' in line_stripped:
                continue
            cells = [c.strip() for c in line_stripped.split('|')[1:-1]]
            tag = 'th' if not in_table else 'td'
            row_html = '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>'
            if not in_table:
                html_lines.append('<table>')
                in_table = True
            html_lines.append(row_html)
            continue
        elif in_table:
            html_lines.append('</table>')
            in_table = False

        # Lists
        if line_stripped.startswith('- ') or line_stripped.startswith('* '):
            item_text = line_stripped[2:]
            if not in_list:
                html_lines.append('<ul class="list-disc pl-6 space-y-1 text-gray-300">')
                in_list = True
            html_lines.append(f'<li>{item_text}</li>')
            continue
        elif in_list and not (line_stripped.startswith('- ') or line_stripped.startswith('* ')):
            html_lines.append('</ul>')
            in_list = False

        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:].strip()}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:].strip()}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:].strip()}</h3>')
        elif line.startswith('> '):
            html_lines.append(f'<blockquote>{line[2:].strip()}</blockquote>')
        elif line_stripped.startswith('---'):
            html_lines.append('<hr class="border-gray-800 my-6" />')
        elif line_stripped == '':
            html_lines.append('<br />')
        else:
            # Inline formatting
            p_line = line
            p_line = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-white">\1</strong>', p_line)
            p_line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p_line)
            p_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', p_line)
            html_lines.append(f'<p class="text-gray-300 leading-relaxed">{p_line}</p>')

    if in_table:
        html_lines.append('</table>')
    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)

def main():
    parser = argparse.ArgumentParser(description="Export Markdown Report to Interactive HTML Dashboard.")
    parser.add_argument("input_file", help="Path to markdown file (e.g. dossier.md or examples/sample-innovator-report.md)")
    parser.add_argument("--output", "-o", help="Target HTML file path (default: report.html)")
    args = parser.parse_args()

    output_path = args.output or args.input_file.rsplit('.', 1)[0] + '.html'

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        print(f"[-] Dosya okunamadı: {e}", file=sys.stderr)
        sys.exit(1)

    parsed_html = parse_markdown_to_html(md_content)
    full_html = HTML_TEMPLATE.replace("{{title}}", "Frontier Innovator Report").replace("{{content}}", parsed_html)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"[+] Görsel HTML Dashboard başarıyla oluşturuldu: {output_path}")

if __name__ == "__main__":
    main()
