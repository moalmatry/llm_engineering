# LLM Engineering - Markdown Export for Gemini & NotebookLM

This folder contains the complete core curriculum of the **LLM Engineering** course, exported and optimized as Markdown (`.md`) documents.

All Jupyter Notebooks (`.ipynb`) have been parsed into clean Markdown cells and syntax-highlighted Python blocks, with base64 images stripped to maximize context token efficiency. All Python scripts, markdown documentation, and data files are formatted cleanly with language-specific blocks.

---

## Folder Organization

### 1. `bundled/` (Recommended for Google NotebookLM)
NotebookLM has a limit of **50 source documents per notebook**. 
Uploading separate files quickly hits that limit. The `bundled/` folder aggregates the course into **11 comprehensive modules** (only ~1.3 MB total), each with an integrated Table of Contents:

| Bundle File | Sources Included | Size |
| :--- | :---: | :---: |
| [`00_Course_Overview_and_Setup.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/00_Course_Overview_and_Setup.md) | 8 files | 58.2 KB |
| [`01_Guides.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/01_Guides.md) | 14 files | 53.8 KB |
| [`02_Week1_Prompt_Engineering_and_APIs.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/02_Week1_Prompt_Engineering_and_APIs.md) | 10 files | 96.9 KB |
| [`03_Week2_Structured_Outputs_and_RAG.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/03_Week2_Structured_Outputs_and_RAG.md) | 10 files | 249.2 KB |
| [`04_Week3_Visualizer_and_Tools.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/04_Week3_Visualizer_and_Tools.md) | 6 files | 8.9 KB |
| [`05_Week4_System_Info_and_Styles.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/05_Week4_System_Info_and_Styles.md) | 5 files | 42.8 KB |
| [`06_Week5_Knowledge_Base_and_Evaluations.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/06_Week5_Knowledge_Base_and_Evaluations.md) | 90 files | 429.2 KB |
| [`07_Week6_Pricer_and_Fine_Tuning.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/07_Week6_Pricer_and_Fine_Tuning.md) | 17 files | 142.6 KB |
| [`08_Week7_Pricer_Enhancements.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/08_Week7_Pricer_Enhancements.md) | 8 files | 23.2 KB |
| [`09_Week8_Deal_Agents_and_Frameworks.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/09_Week8_Deal_Agents_and_Frameworks.md) | 29 files | 109.8 KB |
| [`10_Extras.md`](file:///Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled/10_Extras.md) | 5 files | 115.4 KB |

### 2. `individual/` (For granular reference / Gemini AI Studio)
Contains **202 individual `.md` files**, mirroring the repository's folder structure:
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
   `/Users/mohamedalmatry/Documents/Programming/llm_engineering/gemini_notebook_export/bundled`
5. Select all 11 `.md` files and click **Upload**.
6. You now have the entire course indexed! You can:
   - Ask cross-week conceptual questions.
   - Generate study guides and FAQs.
   - Generate Deep Dive audio podcasts on any week's topic.
   - Query code patterns, agent architectures, and fine-tuning formulas.

---

## How to Import into Gemini / Google AI Studio

- Drag and drop any individual `.md` file or bundled week into the prompt box or file attachment area in Gemini Advanced or Google AI Studio.
