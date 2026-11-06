import os
import re
import json
import shutil
from pathlib import Path
from collections import defaultdict

WORKSPACE_ROOT = Path("/Users/mohamedalmatry/Documents/Programming/llm_engineering")
EXPORT_DIR = WORKSPACE_ROOT / "gemini_notebook_export"
INDIVIDUAL_DIR = EXPORT_DIR / "individual"
BUNDLED_DIR = EXPORT_DIR / "bundled"

SKIP_EXTENSIONS = {'.pyc', '.png', '.jpg', '.jpeg', '.lock', '.db'}
SKIP_FILENAMES = {'.env', '.gitignore', '.cursorignore', '.python-version', '.gitkeep', 'export_to_gemini_notebook.py'}
SKIP_PARTS = {'community-contributions', 'community_contributions', '.git', '.venv', '__pycache__', 'gemini_notebook_export'}

ANSI_REGEX = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def strip_ansi(text: str) -> str:
    return ANSI_REGEX.sub('', text)

def clean_output_text(text: str, max_lines: int = 100, max_chars: int = 15000) -> str:
    cleaned = strip_ansi(text).strip()
    lines = cleaned.splitlines()
    if len(lines) > max_lines:
        lines = lines[:max_lines] + [f"\n... [Output truncated: {len(lines) - max_lines} more lines] ..."]
        cleaned = "\n".join(lines)
    if len(cleaned) > max_chars:
        cleaned = cleaned[:max_chars] + f"\n... [Output truncated: {len(cleaned) - max_chars} more characters] ..."
    return cleaned

def convert_notebook_to_markdown_body(filepath: Path) -> str:
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        try:
            nb = json.load(f)
        except Exception as e:
            return f"```\nError reading notebook {filepath.name}: {e}\n```"

    md_lines = []
    cells = nb.get('cells', [])
    for cell in cells:
        cell_type = cell.get('cell_type', '')
        source_raw = cell.get('source', [])
        source = "".join(source_raw) if isinstance(source_raw, list) else str(source_raw)

        if cell_type == 'markdown':
            content = source.strip()
            if content:
                md_lines.append(content)
                md_lines.append("")
        elif cell_type == 'code':
            code = source.strip()
            if code:
                md_lines.append("```python")
                md_lines.append(code)
                md_lines.append("```")
                md_lines.append("")

            # Process outputs if any
            outputs = cell.get('outputs', [])
            out_texts = []
            for out in outputs:
                out_type = out.get('output_type', '')
                if out_type == 'stream':
                    text_data = "".join(out.get('text', []))
                    if text_data.strip():
                        out_texts.append(clean_output_text(text_data))
                elif out_type in ('execute_result', 'display_data'):
                    data = out.get('data', {})
                    if 'text/plain' in data:
                        text_data = "".join(data['text/plain'])
                        if text_data.strip():
                            out_texts.append(clean_output_text(text_data))
                    for k in data.keys():
                        if k.startswith('image/'):
                            out_texts.append("[Note: Visual plot/image omitted for text token efficiency]")
                elif out_type == 'error':
                    ename = out.get('ename', 'Error')
                    evalue = out.get('evalue', '')
                    out_texts.append(clean_output_text(f"{ename}: {evalue}"))

            if out_texts:
                md_lines.append("**Cell Output:**")
                md_lines.append("```text")
                md_lines.append("\n".join(out_texts))
                md_lines.append("```")
                md_lines.append("")

    return "\n".join(md_lines).strip()

def convert_code_or_text_body(filepath: Path) -> str:
    ext = filepath.suffix.lower().lstrip('.')
    lang_map = {
        'py': 'python',
        'json': 'json',
        'jsonl': 'json',
        'csv': 'csv',
        'toml': 'toml',
        'txt': 'text',
        'sh': 'bash',
        'yaml': 'yaml',
        'yml': 'yaml'
    }
    lang = lang_map.get(ext, 'text')

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read().strip()

    if ext == 'md':
        return content
    else:
        return f"```{lang}\n{content}\n```"

def should_skip(path: Path) -> bool:
    for part in path.parts:
        if part in SKIP_PARTS:
            return True
        if part.startswith('.') and part != '.':
            return True
    if path.name in SKIP_FILENAMES:
        return True
    if path.suffix.lower() in SKIP_EXTENSIONS:
        return True
    return False

def collect_core_files():
    all_files = []
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        root_path = Path(root)
        if any(part in SKIP_PARTS for part in root_path.parts) or any(part.startswith('.') and part != '.' for part in root_path.parts):
            continue
        for file in sorted(files):
            full_path = root_path / file
            if should_skip(full_path):
                continue
            all_files.append(full_path)
    return sorted(all_files)

def assign_bundle(rel_path: Path) -> str:
    parts = rel_path.parts
    first = parts[0]
    if first in ('README.md', 'LICENSE', 'pyproject.toml', 'report.txt', 'setup'):
        return "00_Course_Overview_and_Setup.md"
    elif first == 'guides':
        return "01_Guides.md"
    elif first == 'week1':
        return "02_Week1_Prompt_Engineering_and_APIs.md"
    elif first == 'week2':
        return "03_Week2_Structured_Outputs_and_RAG.md"
    elif first == 'week3':
        return "04_Week3_Visualizer_and_Tools.md"
    elif first == 'week4':
        return "05_Week4_System_Info_and_Styles.md"
    elif first == 'week5':
        return "06_Week5_Knowledge_Base_and_Evaluations.md"
    elif first == 'week6':
        return "07_Week6_Pricer_and_Fine_Tuning.md"
    elif first == 'week7':
        return "08_Week7_Pricer_Enhancements.md"
    elif first == 'week8':
        return "09_Week8_Deal_Agents_and_Frameworks.md"
    elif first == 'extras':
        return "10_Extras.md"
    else:
        return "11_Other.md"

def get_individual_target_path(filepath: Path) -> Path:
    rel_path = filepath.relative_to(WORKSPACE_ROOT)
    parent = rel_path.parent
    stem = filepath.stem
    suffix = filepath.suffix.lower()

    if parent == Path('setup') and stem == 'diagnostics':
        if suffix == '.py':
            md_name = 'diagnostics_py.md'
        elif suffix == '.ipynb':
            md_name = 'diagnostics_ipynb.md'
        else:
            md_name = f"{stem}{suffix}.md"
    elif suffix == '.md':
        md_name = filepath.name
    elif suffix == '.ipynb':
        md_name = f"{stem}.md"
    elif suffix == '':
        md_name = f"{stem}.md"
    else:
        md_name = f"{stem}_{suffix.lstrip('.')}.md"

    return INDIVIDUAL_DIR / parent / md_name

def main():
    if EXPORT_DIR.exists():
        shutil.rmtree(EXPORT_DIR)

    INDIVIDUAL_DIR.mkdir(parents=True, exist_ok=True)
    BUNDLED_DIR.mkdir(parents=True, exist_ok=True)

    print("Collecting core curriculum files...")
    files = collect_core_files()
    print(f"Found {len(files)} files to export.\n")

    bundles = defaultdict(list)

    for filepath in files:
        rel_path = filepath.relative_to(WORKSPACE_ROOT)
        suffix = filepath.suffix.lower()

        if suffix == '.ipynb':
            body = convert_notebook_to_markdown_body(filepath)
        else:
            body = convert_code_or_text_body(filepath)

        # Build individual MD file content
        individual_content = f"# {filepath.name}\n\n> **Original Path:** `{rel_path}`\n\n---\n\n{body}\n"

        target_md_path = get_individual_target_path(filepath)
        target_md_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_md_path, 'w', encoding='utf-8') as f:
            f.write(individual_content)

        # Store for bundle
        bundle_name = assign_bundle(rel_path)
        bundles[bundle_name].append((rel_path, body))

    print(f"Successfully generated {len(files)} individual Markdown files in {INDIVIDUAL_DIR.relative_to(WORKSPACE_ROOT)}")

    # Generate bundled documents
    bundle_summaries = []
    for bundle_name in sorted(bundles.keys()):
        bundle_path = BUNDLED_DIR / bundle_name
        items = bundles[bundle_name]

        clean_title = bundle_name.replace('.md', '')[3:].replace('_', ' ')
        bundle_lines = [
            f"# {clean_title}",
            "",
            f"This unified reference file consolidates **{len(items)} source files** from the LLM Engineering course repository.",
            "Optimized for **Google NotebookLM** and **Gemini Context Windows**.",
            "",
            "## Table of Contents",
            ""
        ]

        for rel_p, _ in items:
            anchor = str(rel_p).lower().replace('/', '-').replace('.', '-').replace(' ', '-').replace('_', '-')
            bundle_lines.append(f"- [{rel_p}](#file-{anchor})")

        bundle_lines.append("\n---\n")

        for rel_p, body in items:
            anchor = str(rel_p).lower().replace('/', '-').replace('.', '-').replace(' ', '-').replace('_', '-')
            bundle_lines.append(f'<a id="file-{anchor}"></a>')
            bundle_lines.append(f"## File: `{rel_p}`\n")
            bundle_lines.append(f"> **Path in repository:** `{rel_p}`\n")
            bundle_lines.append(body)
            bundle_lines.append("\n\n---\n")

        with open(bundle_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(bundle_lines))

        file_size_kb = bundle_path.stat().st_size / 1024
        bundle_summaries.append((bundle_name, len(items), file_size_kb))
        print(f"Bundled: {bundle_name} ({len(items)} files, {file_size_kb:.1f} KB)")

    # Generate master README in export folder
    readme_path = EXPORT_DIR / "README.md"
    readme_content = f"""# LLM Engineering - Markdown Export for Gemini & NotebookLM

This folder contains the complete core curriculum of the **LLM Engineering** course, exported and optimized as Markdown (`.md`) documents.

All Jupyter Notebooks (`.ipynb`) have been parsed into clean Markdown cells and syntax-highlighted Python blocks, with base64 images stripped to maximize context token efficiency. All Python scripts, markdown documentation, and data files are formatted cleanly with language-specific blocks.

---

## Folder Organization

### 1. `bundled/` (Recommended for Google NotebookLM)
NotebookLM has a limit of **50 source documents per notebook**. 
Uploading separate files quickly hits that limit. The `bundled/` folder aggregates the course into **11 comprehensive modules** (only ~1.3 MB total), each with an integrated Table of Contents:

| Bundle File | Sources Included | Size |
| :--- | :---: | :---: |
"""
    for b_name, count, size_kb in bundle_summaries:
        readme_content += f"| [`{b_name}`](file://{BUNDLED_DIR / b_name}) | {count} files | {size_kb:.1f} KB |\n"

    readme_content += f"""
### 2. `individual/` (For granular reference / Gemini AI Studio)
Contains **{len(files)} individual `.md` files**, mirroring the repository's folder structure:
- `guides/` (14 foundational guide notebooks)
- `setup/` (diagnostics, troubleshooting, and setup instructions)
- `week1/` through `week8/` (daily lab notebooks, exercises, solutions, and scripts)
- `week5/knowledge-base/` (company background, employee profiles, contracts, products)
- `extras/` (trading and community prototypes)

---

## How to Import into Google NotebookLM

1. Go to [Google NotebookLM](https://notebooklm.google.com).
2. Click **Create New Notebook** (e.g. name it *"LLM Engineering"*).
3. Click **Add Sources** > **Upload Sources**.
4. Navigate to:
   `{BUNDLED_DIR}`
5. Select all 11 `.md` files and click **Upload**.
6. You now have the entire course indexed! You can:
   - Ask cross-week conceptual questions.
   - Generate study guides and FAQs.
   - Generate Deep Dive audio podcasts on any week's topic.
   - Query code patterns, agent architectures, and fine-tuning formulas.

---

## How to Import into Gemini / Google AI Studio

- Drag and drop any individual `.md` file or bundled week into the prompt box or file attachment area in Gemini Advanced or Google AI Studio.
"""

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"\nAll operations finished successfully! Created {readme_path}")

if __name__ == '__main__':
    main()
