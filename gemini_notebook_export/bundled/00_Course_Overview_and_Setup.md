# Course Overview and Setup

This unified reference file consolidates **8 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [LICENSE](#file-license)
- [README.md](#file-readme-md)
- [pyproject.toml](#file-pyproject-toml)
- [report.txt](#file-report-txt)
- [setup/SETUP-new.md](#file-setup-setup-new-md)
- [setup/diagnostics.ipynb](#file-setup-diagnostics-ipynb)
- [setup/diagnostics.py](#file-setup-diagnostics-py)
- [setup/troubleshooting.ipynb](#file-setup-troubleshooting-ipynb)

---

<a id="file-license"></a>
## File: `LICENSE`

> **Path in repository:** `LICENSE`

```text
MIT License

Copyright (c) 2024 Ed Donner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


---

<a id="file-readme-md"></a>
## File: `README.md`

> **Path in repository:** `README.md`

# LLM Engineering - Master AI and LLMs

## Your 8 week journey to proficiency starts today

![Voyage](assets/core.jpg)

_If you're looking at this in Cursor, please right click on the filename in the Explorer on the left, and select "Open preview", to view the formatted version._

I'm so happy you're joining me on this path. We'll be building immensely satisfying projects in the coming weeks. Some will be easy, some will be challenging, many will ASTOUND you! The projects build on each other so you develop deeper and deeper expertise each week. One thing's for sure: you're going to have a lot of fun along the way.

Any questions, please ask me on Udemy or at ed@edwarddonner.com. More details at the top of the course resources [here](https://edwarddonner.com/2024/11/13/llm-engineering-resources/).

### Answers to the most common questions

[My Cursor looks different to yours (new splash screen)](https://edwarddonner.com/avatar?q=54)  
[Can I use Gemini or free models instead of OpenAI Yes!](https://edwarddonner.com/avatar?q=8)  
[Where are the course resources](https://edwarddonner.com/2024/11/13/llm-engineering-resources/)   
[How does this course fit in with your others?](https://edwarddonner.com/curriculum)  
[Can I take this course with no programming background?](https://edwarddonner.com/avatar?q=2)  
[What job can I get after taking this course?](https://edwarddonner.com/avatar?q=3)  

### Before you begin

I'm here to help you be most successful with your learning. If you hit any snafus, or if you have any ideas on how I can improve the course, please do reach out in the platform or by emailing me direct (ed@edwarddonner.com). It's always great to connect with people on LinkedIn to build up the community - you'll find me here:  
https://www.linkedin.com/in/eddonner/   

And I'm starting to build a YouTube channel with extra content - please [check it out here](https://youtube.com/@edward.donner).  
And this is new to me, but I'm also trying out X/Twitter at [@edwarddonner](https://x.com/edwarddonner) - if you're on X, please show me how it's done 😂  

Resources to accompany the course, including the slides and useful links, are here:  
https://edwarddonner.com/2024/11/13/llm-engineering-resources/

My digital twin that can answer common FAQ (and get me involved!) is here:  
https://edwarddonner.com/avatar/

## Instant Gratification instructions for Week 1, Day 1 - with Llama 3.2 **not** Llama 3.3

### Important note: see my warning about Llama3.3 below - it's too large for home computers! Stick with llama3.2 - several students have missed this warning...

We will start the course by installing Ollama so you can see results immediately!
1. Download and install Ollama from https://ollama.com noting that on a PC you might need to have administrator permissions for the install to work properly. On a Mac, the current release of Ollama requires MacOS 14.0 or later; for older Macs please check the [Ollama releases](https://github.com/ollama/ollama/releases) page for a version compatible with your Mac.
2. On a PC, start a Command prompt / Powershell (Press Win + R, type `cmd`, and press Enter). On a Mac, start a Terminal (Applications > Utilities > Terminal).
3. Run `ollama run llama3.2` or for smaller machines try `ollama run llama3.2:1b` - **please note** steer clear of Meta's latest model llama3.3 because at 70B parameters that's way too large for most home computers!  
4. If this doesn't work: you may need to run `ollama serve` in another Powershell (Windows) or Terminal (Mac), and try step 3 again. On a PC, you may need to be running in an Admin instance of Powershell.  
5. And if that doesn't work on your box, I've set up this on the cloud. This is on Google Colab, which will need you to have a Google account to sign in, but is free:  https://colab.research.google.com/drive/1-_f5XZPsChvfU1sJ0QqCePtIuc55LSdu?usp=sharing

Any problems, please contact me!

## Before the Setup instructions - a special note

Early on in the course (on Day 2), I give a demo of a very cool, popular product called Claude Code. It's an AI coding tool, similar to Cursor that we use on the course. I'm only showing this as an example of Agentic AI in action; it's not a tool that's covered explicitly on this course, particularly as we're in Cursor. But if you want to use Claude Code yourself, the Quick Start guide from Anthropic is [here](https://docs.claude.com/en/docs/claude-code/quickstart).

## OK - now on to Setup instructions

After we do the Ollama quick project, and after I introduce myself and the course, we get to work with the full environment setup.  

Hopefully I've done a decent job of making these guides bulletproof - but please contact me right away if you hit roadblocks:

Setup instructions: [Setup Instructions All Platforms](setup/SETUP-new.md)

### An important point on API costs (which are optional! No need to spend if you don't wish)

During the course, I'll suggest you try out the leading models at the forefront of progress, known as the Frontier models. I'll also suggest you run open-source models using Google Colab. These services have some charges, but I'll keep cost minimal - like, a few cents at a time. And I'll provide alternatives if you'd prefer not to use them.

Please do monitor your API usage to ensure you're comfortable with spend; I've included links below. There's no need to spend anything more than a couple of dollars for the entire course. Some AI providers such as OpenAI require a minimum credit like \$5 or local equivalent; we should only spend a fraction of it, and you'll have plenty of opportunity to put it to good use in your own projects. During Week 7 you have an option to spend a bit more if you're enjoying the process - I spend about \$10 myself and the results make me very happy indeed! But it's not necessary in the least; the important part is that you focus on learning.

### Free alternative to Paid APIs

See [Guide 9](guides/09_ai_apis_and_ollama.ipynb) in the guides directory for the detailed approach with exact code for Ollama, Gemini, OpenRouter and more!

### How this Repo is organized

There are folders for each of the "weeks", representing modules of the class, culminating in a powerful autonomous Agentic AI solution in Week 8 that draws on many of the prior weeks.    
Follow the setup instructions above, then open the Week 1 folder and prepare for joy.

### The most important part

The mantra of the course is: the best way to learn is by **DOING**. I don't type all the code during the course; I execute it for you to see the results. You should work along with me or after each lecture, running each cell, inspecting the objects to get a detailed understanding of what's happening. Then tweak the code and make it your own. There are juicy challenges for you throughout the course. I'd love it if you wanted to submit a Pull Request for your code (see the Github guide in the guides folder) and I can make your solutions available to others so we share in your progress; as an added benefit, you'll be recognized in GitHub for your contribution to the repo. While the projects are enjoyable, they are first and foremost designed to be _educational_, teaching you business skills that can be put into practice in your work.

## Starting in Week 3, we'll also be using Google Colab for running with GPUs

You should be able to use the free tier or minimal spend to complete all the projects in the class. I personally signed up for Colab Pro+ and I'm loving it - but it's not required.

Learn about Google Colab and set up a Google account (if you don't already have one) [here](https://colab.research.google.com/)

The colab links are in the folders for Week 3 and Week 7 - if you open up the lab for each day, you'll find a direct link to the colab.

### Monitoring API charges

You can keep your API spend very low throughout this course; you can monitor spend at the dashboards: [here](https://platform.openai.com/usage) for OpenAI, [here](https://console.anthropic.com/settings/cost) for Anthropic.

The charges for the exercises in this course should always be quite low, but if you'd prefer to keep them minimal, then be sure to always choose the cheapest versions of models:
1. For OpenAI: Always use model `gpt-6-luna` in the code
2. For Anthropic: Always use model `claude-haiku-5-5` in the code instead of the other Claude models
3. During week 7, look out for my instructions for using the cheaper dataset

Please do message me or email me at ed@edwarddonner.com if this doesn't work or if I can help with anything. I can't wait to hear how you get on.

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">Other resources</h2>
            <span style="color:#f71;">I've put together this webpage with useful resources for the course. This includes links to all the slides.<br/>
            <a href="https://edwarddonner.com/2024/11/13/llm-engineering-resources/">https://edwarddonner.com/2024/11/13/llm-engineering-resources/</a><br/>
            Please keep this bookmarked, and I'll continue to add more useful links there over time.
            </span>
        </td>
    </tr>
</table>


---

<a id="file-pyproject-toml"></a>
## File: `pyproject.toml`

> **Path in repository:** `pyproject.toml`

```toml
[project]
name = "llm-engineering"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "anthropic>=0.69.0",
    "beautifulsoup4>=4.14.2",
    "chromadb>=1.1.0",
    "datasets==3.6.0",
    "feedparser>=6.0.12",
    "google-genai>=1.41.0",
    "google-generativeai>=0.8.5",
    "gradio>=5.47.2,<6.0",
    "ipykernel>=6.30.1",
    "ipywidgets>=8.1.7",
    "jupyter-dash>=0.4.2",
    "langchain>=0.3.27",
    "langchain-chroma>=0.2.6",
    "langchain-community>=0.3.30",
    "langchain-core>=0.3.76",
    "langchain-openai>=0.3.33",
    "langchain-text-splitters>=0.3.11",
    "litellm>=1.77.5",
    "matplotlib>=3.10.6",
    "nbformat>=5.10.4",
    "modal>=1.1.4",
    "numpy>=2.3.3",
    "ollama>=0.6.0",
    "openai>=1.109.1",
    "pandas>=2.3.3",
    "plotly>=6.3.0",
    "protobuf==3.20.2",
    "psutil>=7.1.0",
    "pydub>=0.25.1",
    "python-dotenv>=1.1.1",
    "requests>=2.32.5",
    "scikit-learn>=1.7.2",
    "scipy>=1.16.2",
    "sentence-transformers>=5.1.1",
    "setuptools>=80.9.0",
    "speedtest-cli>=2.1.3",
    "tiktoken>=0.11.0",
    "torch>=2.8.0",
    "tqdm>=4.67.1",
    "transformers>=4.56.2",
    "wandb>=0.22.1",
    "langchain-huggingface>=1.0.0",
    "langchain-ollama>=1.0.0",
    "langchain-anthropic>=1.0.1",
    "langchain-experimental>=0.0.42",
    "groq>=0.33.0",
    "xgboost>=3.1.1",
]
```


---

<a id="file-report-txt"></a>
## File: `report.txt`

> **Path in repository:** `report.txt`

```text
Starting diagnostics at 2026-11-05 14:39:18

===== System Information =====
Operating System: Darwin
MacOS Version: 27.2
Architecture: ('64bit', '')
Machine: arm64
Processor: arm
Total RAM: 16.00 GB
Available RAM: 3.08 GB
Free Disk Space: 96.89 GB

===== File System Information =====
Current Directory: /Users/mohamedalmatry/Documents/Programming/llm_engineering
Write permission: OK

Files in Current Directory:
 - .cursorignore
 - .env
 - .git
 - .gitignore
 - .python-version
 - .venv
 - LICENSE
 - README.md
 - assets
 - community-contributions
 - extras
 - guides
 - pyproject.toml
 - report.txt
 - setup
 - uv.lock
 - week1
 - week2
 - week3
 - week4
 - week5
 - week6
 - week7
 - week8

===== Git Repository Information =====
Git Repository Root: /Users/mohamedalmatry/Documents/Programming/llm_engineering
Current Commit: c00926b9829fa5a364041bd07547692932916962
Remote Origin: ssh://git@github.com/ed-donner/llm_engineering.git

===== Environment File Check =====
.env file exists at: /Users/mohamedalmatry/Documents/Programming/llm_engineering/.env
OPENAI_API_KEY found in .env file

===== Anaconda Environment Check =====
No active Anaconda environment detected

===== Virtualenv Check =====
No active virtualenv detected
WARNING: Neither virtualenv nor Anaconda environment is active

===== Network Connectivity Check =====
SSL Version: OpenSSL 3.5.5 27 Jan 2026
✓ Connected to https://www.google.com
  Response time: 1.11s

Performing bandwidth test using speedtest-cli...
```


---

<a id="file-setup-setup-new-md"></a>
## File: `setup/SETUP-new.md`

> **Path in repository:** `setup/SETUP-new.md`

# LLM Engineering - Master AI and LLMs

## Setup instructions for PC, Mac and Linux

_If you're looking at this in Cursor, please right click on the filename in the Explorer on the left, and select "Open preview", to view the formatted version._

Welcome, LLM engineers in the making!

I should confess up-front: setting up a powerful environment to work at the forefront of AI is not as simple as I'd like. For most people these instructions will go great; but in some cases, for whatever reason, you'll hit a problem. Please don't hesitate to reach out - I am here to get you up and running quickly. There's nothing worse than feeling _stuck_. Message me in Udemy or email me and I will unstick you quickly!

Email: ed@edwarddonner.com  
LinkedIn: https://www.linkedin.com/in/eddonner/  

## Step 0 - Before we begin - addressing the "GOTCHAS" which trip up many people:

Ignore this section at your peril! 80% of the questions I get about setup are solved by these very common system issues.

1. PC people: Permissions. Please take a look at this [tutorial](https://chatgpt.com/share/67b0ae58-d1a8-8012-82ca-74762b0408b0) on permissions on Windows. If you ever have an error that you don't have the rights / permissions / ability to run a script or install software, then read this first. ChatGPT can tell you everything you need to know about Permissions on Windows.

2. Anti-virus, Firewall, VPN. These can interfere with installations and network access; try temporarily disabling them as needed. Use a hotspot on your phone to prove whether it's a network issue.

3. PC people: The evil Windows 260 character limit to filenames - here is a full [explanation and fix](https://chatgpt.com/share/67b0afb9-1b60-8012-a9f7-f968a5a910c7)! 

4. PC people: If you've not worked with Data Science packages on your computer before, you might need to install Microsoft Build Tools. Here are [instructions](https://chatgpt.com/share/67b0b762-327c-8012-b809-b4ec3b9e7be0). A student also mentioned that [these instructions](https://github.com/bycloudai/InstallVSBuildToolsWindows) might be helpful for people on Windows 11. 

5. Mac people: If you're new to developing on your Mac, you may need to install XCode developer tools. Here are [instructions](https://chatgpt.com/share/67b0b8d7-8eec-8012-9a37-6973b9db11f5).

6. SSL and other network issues due to Corporate Security: if you ever get issues with SSL, such as an API Connection issue or any certificate issue, or an error trying to download files from Ollama (a Cloudflare error) then see Q15 [here](https://edwarddonner.com/faq)

## STEP 1 - installing git, projects directory, Cursor

This is the only section with separate steps for PC people and Mac/Linux people! Please pick your section below, then reconvene for Step 2...

___

**STEP 1 FOR PC people:**

1. **Install Git** (if not already installed):

- Open a new Powershell Prompt (start menu >> Powershell). If you ever have permissions errors, try opening the Powershell by right clicking and selecting "run as Administrator"
- Run the command `git` and see if it responds with details of the command or an error
- If you get an error, download Git from https://git-scm.com/download/win
- Run the installer and follow the prompts, using default options (press OK lots of times!)

2. **Create projects directory as needed**

- Open a new Powershell prompt, as in prior step. You should be in your home directory, like `C:\Users\YourUserName`
- Do you have a projects directory? Find out by typing `cd projects`
- If that has an error, then create a projects directory: `mkdir projects` then `cd projects`
- Now you should be in `C:\Users\YourUserName\projects`
- You can locate this anywhere convenient for you, but avoid any directories that are on your OneDrive

3. **Do a git clone:**

Enter the clone command below in the command prompt in the `projects` folder. If this gives you an error about long filenames, please do #3 in the "gotchas" section at the top, and then restart your computer, and you might also need to run this: `git config --system core.longpaths true`

Here's the clone command:

`git clone https://github.com/ed-donner/llm_engineering.git`

This creates a new directory `llm_engineering` within your projects folder and downloads the code for the class.  
Do `cd llm_engineering` to go into it. This `llm_engineering` directory is known as the "project root directory".

4. **Cursor** Install Cursor if needed and open the project:

Visit https://cursor.com

Click Download for Windows. Then run the installer. Accept and pick defaults for everything..

Then go to Start menu, enter cursor. Cursor will come up, and you might need to answer questions. Then you should see the 'new window' screen where you can click "Open Project". If not, go to File menu >> New Window. Then click "Open Project".

[IMPORTANT: Does your Cursor look different to mine? Solution here (bypass new splash screen)](https://edwarddonner.com/avatar?q=54)  

Find your llm_engineering directory within your projects directory. Double click on llm_engineering so you're looking at the contents of llm_engineering. Then click Open or Open Folder.

Cursor should then open up llm_engineering. You know you're in good shape if you see LLM_ENGINEERING in block caps on the top left.

___

**STEP 1 FOR MAC/LINUX PEOPLE**

1. **Install Git** (if not already installed):

Open a Terminal: on Mac, open a Finder window, go to Applications >> Utilities >> Terminal. On Linux, you people live in Terminals.. you hardly need instructions from me!

- Run `git --version` and you should see a git version number. If not, you should get instructions on how to install it, or follow gotcha #5 at the top of this doc.

2.  **Create projects directory as needed**

- Open a new Terminal window, as in prior step. Type `pwd` to see where you are. You should be in your home directory, like `/Users/username`
- Do you have a projects directory? Find out by typing `cd projects`
- If that has an error, then create a projects directory: `mkdir projects` then `cd projects`
- If you now do `pwd` you should be in `/Users/username/projects`
- You can locate this anywhere convenient for you, but avoid any directories that are on your icloud

3. **Do a git clone:**

Enter this in the command prompt in the Projects folder:

`git clone https://github.com/ed-donner/llm_engineering.git`

This creates a new directory `llm_engineering` within your projects folder and downloads the code for the class.  
Do `cd llm_engineering` to go into it. This `llm_engineering` directory is known as the "project root directory".

4. **Cursor** Install Cursor if needed and open the project:

Visit https://cursor.com

Click Download for Mac OS. Or Linux. Then run the installer. Accept and pick defaults for everything..

Then go to Start menu, enter cursor. Cursor will come up, and you might need to answer questions. Then you should see the 'new window' screen where you can click "Open Project". If not, go to File menu >> New Window. Then click "Open Project".

[IMPORTANT: Does your Cursor look different to mine? Solution here (bypass new splash screen)](https://edwarddonner.com/avatar?q=54)  

Find your llm_engineering directory within your projects directory. Double click on llm_engineering so you're looking at the contents of llm_engineering. Then click Open.

Cursor should then open up llm_engineering. You know you're in good shape if you see LLM_ENGINEERING in block caps on the top left.

___

## STEP 2: Installing the fabulous **uv** then doing a `uv sync`

For this course, we're using uv, the blazingly fast package manager. It's really taken off in the Data Science world -- and for good reason.

It's fast and reliable. You're going to love it!

First, within Cursor, select View >> Terminal, to see a Terminal window within Cursor. Type `pwd` to check you're in the project root directory.

Now type `uv --version` to see if uv is installed. If you get a version number, then terrific! But if you get an error, then follow the instructions here to install uv - I recommend using the Standalone Installer approach at the very top, but you can use any approach. Run commands in the Cursor installer. If one approach doesn't work for you, then try another.

https://docs.astral.sh/uv/getting-started/installation/

Once you've installed uv, you need to open a new terminal window in Cursor (the plus sign or Ctrl+shift+backtick) for `uv --version` to work. Please check!

Any problems with uv installation or using uv, please see [Q11 on my FAQ page](https://edwarddonner.com/faq/#11) for a full briefing.

### Now that it's installed:

Run `uv self update` to make sure you're on the latest version of uv.

And now simply run this:  
`uv sync`  
uv should install everything blazingly fast. Any problems, please see [Q11 on my FAQ page](https://edwarddonner.com/faq/#11).

You now have a full spec environment!!

Using uv is simple and fast:  
1. Instead of `pip install xxx` you do `uv add xxx`  
2. You never need to activate an environment - uv does it for you.  
3. Instead of `python xxx` you do `uv run xxx`

___

## STEP 3 - OPTIONAL - Set up OpenAI Account

Alternative: see Guide 9 in the guides folder for free alternatives!

Go to https://platform.openai.com

- Click Sign Up to create an account if you don't have one. You might need to click some buttons to create an Organization first - just put in sensible defaults. See Guide 4 in the Guides folder if you're unsure about the differences between ChatGPT and the OpenAI API.
- Click on the Settings icon on the top right, and then Billing on the left sidebar navigation.
- Ensure Auto-Recharge is off. As needed, "Add to Credit Balance" and pick the $5 up-front payment amount, be sure that you add a proper payment method
- Still in Settings, select API keys in the left sidebar (near the top)
- Press "Create new secret key" - select "Owned by you", give it any name you want, for the project select "Default project", leave Permissions at All
- Press "Create secret key" and you should see your new key. Press Copy to copy it into your clipboard.

___

## STEP 4 - needed for any model like OpenAI or Gemini, but not needed if you only use Ollama - create (and SAVE) your .env file

**Be dilligent with this section!** - any mistakes with your key will be very hard to track down!! I get a huge volume of questions from students who make a mistake with one of these steps... Above all, remember to save the file after you change it.

1. Create your `.env` file

- Go back to Cursor
- In the File Explorer on the left, right click in the blank space at the bottom of all your files, select "New File" and call your file `.env`
- I can't stress this enough: the file needs to be called PRECISELY `.env` - those four characters, no more and no less. Not ".env.txt" and not "john.env" and not "openai.env" and not anything else! And it needs to be within the project root.

If you're wondering why I rant about this: I get many, many frustrated people contacting me who (despite all my appeals) have named the file something else and think it's OK. It's not OK! It needs to be called `.env` in the llm_engineering directory 😂

2. Populate your `.env` file and then Save it:

Select the file on the left. You should see an empty blank file on the right. And type this into the contents of the file in the right:

`OPENAI_API_KEY=`

And then press paste! You should now see something like this:

`OPENAI_API_KEY=sk-proj-lots-and-lots-of-digits`

But obviously with your actual key there, not the words "sk-proj-lots-and-lots-of-digits"..

Now be sure to SAVE the file! File >> Save or Ctrl+S (PC) or Command+S (Mac). Many people forget to Save. You need to Save the file!

You should see a Stop sign by the .env file - don't be concerned.. this is a good thing! See Q7 [here](https://edwarddonner.com/faq) if you want to understand why.

__

## STEP 5 - Install Cursor Extensions, Open Day 1, Set the Kernel and GO!

(If you are prompted in Cursor to install recommended extensions, just say yes! That is a nice shortcut for this step.)

- Go to view menu and select Extensions.  
- Search for "python" to bring up the Python extensions. Select the Python extension made by "ms-python" or by "anysphere" and install it if not already installed.  
- Search for "jupyter" and select the extension made by "ms-toolsai" and install it if not already installed.

Now go to View >> Explorer. Open the week1 folder, and click on `day1.ipynb`.

- See where it says "Select Kernel" near the top right? Click that.. then pick "Python Environments"
- Pick the top option with a star that should say something like `.venv (Python 3.12.x) .venv/bin/python Recommended`
- If this doesn't come up, please go to the troubleshooting lab in the Setup folder.

# CONGRATULATIONS!! You made it! The rest of the course is easy 😂

**One final note:**

Early on in the course (on Day 2), I give a demo of a very cool, popular product called Claude Code. It's an AI coding tool, similar to Cursor that we use on the course. I'm only showing this as an example of Agentic AI in action; it's not a tool that's covered explicitly on this course, particularly as we're in Cursor. But if you want to use Claude Code yourself, the Quick Start guide from Anthropic is [here](https://docs.claude.com/en/docs/claude-code/quickstart).


---

<a id="file-setup-diagnostics-ipynb"></a>
## File: `setup/diagnostics.ipynb`

> **Path in repository:** `setup/diagnostics.ipynb`

# Gathering Essential Diagnostic information

## Please run this next cell to gather some important data

Please run the next cell; it should take a minute or so to run (mostly the network test).
Then email me the output of the last cell to ed@edwarddonner.com.  
Alternatively: this will create a file called report.txt - just attach the file to your email.

```python
# Run my diagnostics report to collect key information for debugging
# Please email me the results. Either copy & paste the output, or attach the file report.txt

!pip install -q requests speedtest-cli psutil setuptools
from diagnostics import Diagnostics
Diagnostics().run()
```


---

<a id="file-setup-diagnostics-py"></a>
## File: `setup/diagnostics.py`

> **Path in repository:** `setup/diagnostics.py`

```python
import os
import sys
import platform
import subprocess
import shutil
import time
import ssl
import tempfile
from pathlib import Path
from datetime import datetime

class Diagnostics:

    FILENAME = 'report.txt'
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        if os.path.exists(self.FILENAME):
            os.remove(self.FILENAME)

    def log(self, message):
        print(message)
        with open(self.FILENAME, 'a', encoding='utf-8') as f:
            f.write(message + "\n")

    def start(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log(f"Starting diagnostics at {now}\n")

    def end(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log(f"\n\nCompleted diagnostics at {now}\n")
        print("\nPlease send these diagnostics to me at ed@edwarddonner.com")
        print(f"Either copy & paste the above output into an email, or attach the file {self.FILENAME} that has been created in this directory.")
    

    def _log_error(self, message):
        self.log(f"ERROR: {message}")
        self.errors.append(message)

    def _log_warning(self, message):
        self.log(f"WARNING: {message}")
        self.warnings.append(message)

    def run(self):
        self.start()
        self._step1_system_info()
        self._step2_check_files()
        self._step3_git_repo()
        self._step4_check_env_file()
        self._step5_anaconda_check()
        self._step6_virtualenv_check()
        self._step7_network_connectivity()
        self._step8_environment_variables()
        self._step9_additional_diagnostics()

        if self.warnings:
            self.log("\n===== Warnings Found =====")
            self.log("The following warnings were detected. They might not prevent the program from running but could cause unexpected behavior:")
            for warning in self.warnings:
                self.log(f"- {warning}")

        if self.errors:
            self.log("\n===== Errors Found =====")
            self.log("The following critical issues were detected. Please address them before proceeding:")
            for error in self.errors:
                self.log(f"- {error}")

        if not self.errors and not self.warnings:
            self.log("\n✅ All diagnostics passed successfully!")

        self.end()

    def _step1_system_info(self):
        self.log("===== System Information =====")
        try:
            system = platform.system()
            self.log(f"Operating System: {system}")

            if system == "Windows":
                release, version, csd, ptype = platform.win32_ver()
                self.log(f"Windows Release: {release}")
                self.log(f"Windows Version: {version}")
            elif system == "Darwin":
                release, version, machine = platform.mac_ver()
                self.log(f"MacOS Version: {release}")
            else:
                self.log(f"Platform: {platform.platform()}")

            self.log(f"Architecture: {platform.architecture()}")
            self.log(f"Machine: {platform.machine()}")
            self.log(f"Processor: {platform.processor()}")

            try:
                import psutil
                ram = psutil.virtual_memory()
                total_ram_gb = ram.total / (1024 ** 3)
                available_ram_gb = ram.available / (1024 ** 3)
                self.log(f"Total RAM: {total_ram_gb:.2f} GB")
                self.log(f"Available RAM: {available_ram_gb:.2f} GB")

                if available_ram_gb < 2:
                    self._log_warning(f"Low available RAM: {available_ram_gb:.2f} GB")
            except ImportError:
                self._log_warning("psutil module not found. Cannot determine RAM information.")

            total, used, free = shutil.disk_usage(os.path.expanduser("~"))
            free_gb = free / (1024 ** 3)
            self.log(f"Free Disk Space: {free_gb:.2f} GB")

            if free_gb < 5:
                self._log_warning(f"Low disk space: {free_gb:.2f} GB free")

        except Exception as e:
            self._log_error(f"System information check failed: {e}")

    def _step2_check_files(self):
        self.log("\n===== File System Information =====")
        try:
            current_dir = os.getcwd()
            self.log(f"Current Directory: {current_dir}")

            # Check write permissions
            test_file = Path(current_dir) / ".test_write_permission"
            try:
                test_file.touch(exist_ok=True)
                test_file.unlink()
                self.log("Write permission: OK")
            except Exception as e:
                self._log_error(f"No write permission in current directory: {e}")

            self.log("\nFiles in Current Directory:")
            try:
                for item in sorted(os.listdir(current_dir)):
                    self.log(f" - {item}")
            except Exception as e:
                self._log_error(f"Cannot list directory contents: {e}")

        except Exception as e:
            self._log_error(f"File system check failed: {e}")

    def _step3_git_repo(self):
        self.log("\n===== Git Repository Information =====")
        try:
            result = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                git_root = result.stdout.strip()
                self.log(f"Git Repository Root: {git_root}")

                result = subprocess.run(['git', 'rev-parse', 'HEAD'],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    self.log(f"Current Commit: {result.stdout.strip()}")
                else:
                    self._log_warning(f"Could not get current commit: {result.stderr.strip()}")

                result = subprocess.run(['git', 'remote', 'get-url', 'origin'],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    self.log(f"Remote Origin: {result.stdout.strip()}")
                else:
                    self._log_warning("No remote 'origin' configured")
            else:
                self._log_warning("Not a git repository")
        except FileNotFoundError:
            self._log_warning("Git is not installed or not in PATH")
        except Exception as e:
            self._log_error(f"Git check failed: {e}")

    def _step4_check_env_file(self):
        self.log("\n===== Environment File Check =====")
        try:
            result = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                git_root = result.stdout.strip()
                env_path = os.path.join(git_root, '.env')

                if os.path.isfile(env_path):
                    self.log(f".env file exists at: {env_path}")
                    try:
                        with open(env_path, 'r') as f:
                            has_api_key = any(line.strip().startswith('OPENAI_API_KEY=') for line in f)
                        if has_api_key:
                            self.log("OPENAI_API_KEY found in .env file")
                        else:
                            self._log_warning("OPENAI_API_KEY not found in .env file")
                    except Exception as e:
                        self._log_error(f"Cannot read .env file: {e}")
                else:
                    self._log_warning(".env file not found in project root")

                # Check for additional .env files
                for root, _, files in os.walk(git_root):
                    if '.env' in files and os.path.join(root, '.env') != env_path:
                        self._log_warning(f"Additional .env file found at: {os.path.join(root, '.env')}")
            else:
                self._log_warning("Git root directory not found. Cannot perform .env file check.")
        except FileNotFoundError:
            self._log_warning("Git is not installed or not in PATH")
        except Exception as e:
            self._log_error(f"Environment file check failed: {e}")

    def _step5_anaconda_check(self):
        self.log("\n===== Anaconda Environment Check =====")
        try:
            conda_prefix = os.environ.get('CONDA_PREFIX')
            if conda_prefix:
                self.log("Anaconda environment is active:")
                self.log(f"Environment Path: {conda_prefix}")
                self.log(f"Environment Name: {os.path.basename(conda_prefix)}")

                conda_exe = os.environ.get('CONDA_EXE', 'conda')
                result = subprocess.run([conda_exe, '--version'],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    self.log(f"Conda Version: {result.stdout.strip()}")
                else:
                    self._log_warning("Could not determine Conda version")

                self._check_python_packages()
            else:
                self.log("No active Anaconda environment detected")
        except Exception as e:
            self._log_error(f"Anaconda environment check failed: {e}")

    def _step6_virtualenv_check(self):
        self.log("\n===== Virtualenv Check =====")
        try:
            virtual_env = os.environ.get('VIRTUAL_ENV')
            if virtual_env:
                self.log("Virtualenv is active:")
                self.log(f"Environment Path: {virtual_env}")
                self.log(f"Environment Name: {os.path.basename(virtual_env)}")

                self._check_python_packages()
            else:
                self.log("No active virtualenv detected")

            if not virtual_env and not os.environ.get('CONDA_PREFIX'):
                self._log_warning("Neither virtualenv nor Anaconda environment is active")
        except Exception as e:
            self._log_error(f"Virtualenv check failed: {e}")

    def _check_python_packages(self):
        self.log("\nPython Environment:")
        self.log(f"Python Version: {sys.version}")
        self.log(f"Python Executable: {sys.executable}")

        required_packages = ['openai', 'python-dotenv', 'requests', 'gradio', 'transformers']

        try:
            import pkg_resources
            installed = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

            self.log("\nRequired Package Versions:")
            for package in required_packages:
                if package in installed:
                    self.log(f"{package}: {installed[package]}")
                else:
                    self._log_error(f"Required package '{package}' is not installed")

            # Check for potentially conflicting packages
            problem_pairs = [
                ('openai', 'openai-python'),
                ('python-dotenv', 'dotenv')
            ]

            for pkg1, pkg2 in problem_pairs:
                if pkg1 in installed and pkg2 in installed:
                    self._log_warning(f"Potentially conflicting packages: {pkg1} and {pkg2}")
        except ImportError:
            self._log_error("Could not import 'pkg_resources' to check installed packages")
        except Exception as e:
            self._log_error(f"Package check failed: {e}")

    def _step7_network_connectivity(self):
        self.log("\n===== Network Connectivity Check =====")
        try:
            self.log(f"SSL Version: {ssl.OPENSSL_VERSION}")
    
            import requests
            import speedtest  # Importing the speedtest-cli library
    
            # Basic connectivity check
            urls = [
                'https://www.google.com',
                'https://www.cloudflare.com'
            ]
    
            connected = False
            for url in urls:
                try:
                    start_time = time.time()
                    response = requests.get(url, timeout=10)
                    elapsed_time = time.time() - start_time
                    response.raise_for_status()
                    self.log(f"✓ Connected to {url}")
                    self.log(f"  Response time: {elapsed_time:.2f}s")
    
                    if elapsed_time > 2:
                        self._log_warning(f"Slow response from {url}: {elapsed_time:.2f}s")
                    connected = True
                    break
                except requests.exceptions.RequestException as e:
                    self._log_warning(f"Failed to connect to {url}: {e}")
                else:
                    self.log("Basic connectivity OK")
    
            if not connected:
                self._log_error("Failed to connect to any test URLs")
                return
    
            # Bandwidth test using speedtest-cli
            self.log("\nPerforming bandwidth test using speedtest-cli...")
            try:
                st = speedtest.Speedtest()
                st.get_best_server()
                download_speed = st.download()  # Bits per second
                upload_speed = st.upload()      # Bits per second
    
                download_mbps = download_speed / 1e6  # Convert to Mbps
                upload_mbps = upload_speed / 1e6
    
                self.log(f"Download speed: {download_mbps:.2f} Mbps")
                self.log(f"Upload speed: {upload_mbps:.2f} Mbps")
    
                if download_mbps < 1:
                    self._log_warning("Download speed is low")
                if upload_mbps < 0.5:
                    self._log_warning("Upload speed is low")
            except speedtest.ConfigRetrievalError:
                self._log_error("Failed to retrieve speedtest configuration")
            except Exception as e:
                self._log_warning(f"Bandwidth test failed: {e}")
    
        except ImportError:
            self._log_error("Required packages are not installed. Please install them using 'pip install requests speedtest-cli'")
        except Exception as e:
            self._log_error(f"Network connectivity check failed: {e}")


    def _step8_environment_variables(self):
        self.log("\n===== Environment Variables Check =====")
        try:
            # Check Python paths
            pythonpath = os.environ.get('PYTHONPATH')
            if pythonpath:
                self.log("\nPYTHONPATH:")
                for path in pythonpath.split(os.pathsep):
                    self.log(f" - {path}")
            else:
                self.log("\nPYTHONPATH is not set.")

            self.log("\nPython sys.path:")
            for path in sys.path:
                self.log(f" - {path}")

            # Check OPENAI_API_KEY
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.environ.get('OPENAI_API_KEY')
            if api_key:
                self.log("OPENAI_API_KEY is set after calling load_dotenv()")
                if not api_key.startswith('sk-proj-') or len(api_key)<12:
                    self._log_warning("OPENAI_API_KEY format looks incorrect after calling load_dotenv()")
            else:
                self._log_warning("OPENAI_API_KEY environment variable is not set after calling load_dotenv()")
        except Exception as e:
            self._log_error(f"Environment variables check failed: {e}")

    def _step9_additional_diagnostics(self):
        self.log("\n===== Additional Diagnostics =====")
        try:
            # Get the site-packages directory paths
            import site
            site_packages_paths = site.getsitepackages()
            if hasattr(site, 'getusersitepackages'):
                site_packages_paths.append(site.getusersitepackages())
    
            # Function to check if a path is within site-packages
            def is_in_site_packages(path):
                return any(os.path.commonpath([path, sp]) == sp for sp in site_packages_paths)
    
            # Check for potential name conflicts in the current directory and sys.path
            conflict_names = ['openai.py', 'dotenv.py']
    
            # Check current directory
            current_dir = os.getcwd()
            for name in conflict_names:
                conflict_path = os.path.join(current_dir, name)
                if os.path.isfile(conflict_path):
                    self._log_warning(f"Found '{name}' in the current directory, which may cause import conflicts: {conflict_path}")
    
            # Check sys.path directories
            for path in sys.path:
                if not path or is_in_site_packages(path):
                    continue  # Skip site-packages and empty paths
                for name in conflict_names:
                    conflict_file = os.path.join(path, name)
                    if os.path.isfile(conflict_file):
                        self._log_warning(f"Potential naming conflict: {conflict_file}")
    
            # Check temp directory
            try:
                with tempfile.NamedTemporaryFile() as tmp:
                    self.log(f"Temp directory is writable: {os.path.dirname(tmp.name)}")
            except Exception as e:
                self._log_error(f"Cannot write to temp directory: {e}")
    
        except Exception as e:
            self._log_error(f"Additional diagnostics failed: {e}")


if __name__ == "__main__":
    diagnostics = Diagnostics()
    diagnostics.run()
```


---

<a id="file-setup-troubleshooting-ipynb"></a>
## File: `setup/troubleshooting.ipynb`

> **Path in repository:** `setup/troubleshooting.ipynb`

# Oh dear!

If you've got here, then you're still having problems setting up your environment. I'm so sorry! Hang in there and we should have you up and running in no time.

Setting up a Data Science environment can be challenging because there's a lot going on under the hood. But we will get there.

And please remember - I'm standing by to help out. Message me or email ed@edwarddonner.com and I'll get on the case. The very last cell in this notebook has some diagnostics that will help me figure out what's happening.

You might want to have a quick look at the [faq](https://edwarddonner.com/faq) on my homepage in case your problem is specifically addressed.

## Before we start - does Cursor look commletely different?

You may be looking at the new "Agents" screen in Cursor. Please check out Q54 here:  
https://edwarddonner.com/faq/

## 1. Check Cursor extensions

Just to confirm that the extensions are installed:
- Open extensions (View >> extensions)
- Search for python, and when the results show, click on the ms-python one, and Install it if not already installed
- Search for jupyter, and when the results show, click on the Microsoft one, and Install it if not already installed  
Then View >> Explorer to bring back the File Explorer.

## 2. Connect this Kernel:

If you see the words `Select Kernel` in a button near the top right of this Window, then press the button!

You should see a drop down titled "Select kernel for.." or you might need to pick "Python environment" first.

Pick the one that begins `.venv python 3.12` - it should be the top choice. You might need to click "Python Environments" first.

It should now say `.venv (Python 3.12.x)` where it used to say `Select Kernel`.

After you click "Select Kernel", if there is no option like `.venv (Python 3.12.x)` then please do the following:  
1. On Mac: From the Cursor menu, choose Settings >> VS Code Settings (NOTE: be sure to select `VSCode Settings` not `Cursor Settings`);  
Or on Windows PC: From the File menu, choose Preferences >> VS Code Settings (NOTE: be sure to select `VSCode Settings` not `Cursor Settings`)  
2. In the Settings search bar, type "venv"  
3. In the field "Path to folder with a list of Virtual Environments" put the path to the project root, like C:\Users\username\projects\llm_engineering (on a Windows PC) or /Users/username/projects/llm_engineering (on Mac or Linux).  
And then try again.

## 3. Any uv problems

Please check out this comprehensive guide on my [FAQ Q11](https://edwarddonner.com/faq/#11)

# Starting with the basics

## Checking your internet connection

First let's check that there's no VPN or Firewall or Certs problem.

Click in the cell below and press Shift+Return to run it.  

If this gives you problems, then please work through Q15 in the [FAQ](https://edwarddonner.com/faq) to address.

```python
import urllib.request

try:
    response = urllib.request.urlopen("https://www.google.com", timeout=10)
    if response.status != 200:
        print("Unable to reach google - there may be issues with your internet / VPN / firewall?")
    else:
        print("Connected to the internet and can reach Google")
except Exception as e:
    print(f"Failed to connect with this error: {e}")
```

## Another mention of occasional "gotchas" for PC people

There are 4 snafus on Windows to be aware of:  
1. Permissions. Please take a look at this [tutorial](https://chatgpt.com/share/67b0ae58-d1a8-8012-82ca-74762b0408b0) on permissions on Windows
2. Anti-virus, Firewall, VPN. These can interfere with installations and network access; try temporarily disabling them as needed
3. The evil Windows 260 character limit to filenames - here is a full [explanation and fix](https://chatgpt.com/share/67b0afb9-1b60-8012-a9f7-f968a5a910c7)!
4. If you've not worked with Data Science packages on your computer before, you might need to install Microsoft Build Tools. Here are [instructions](https://chatgpt.com/share/67b0b762-327c-8012-b809-b4ec3b9e7be0). A student also mentioned that [these instructions](https://github.com/bycloudai/InstallVSBuildToolsWindows) might be helpful for people on Windows 11.  

## And for Mac people

1. If you're new to developing on your Mac, you may need to install XCode developer tools. Here are [instructions](https://chatgpt.com/share/67b0b8d7-8eec-8012-9a37-6973b9db11f5).
2. As with PC people, Anti-virus, Firewall, VPN can be problematic. These can interfere with installations and network access; try temporarily disabling them as needed

# Step 1

Try running the next cell (click in the cell under this one and hit shift+return).

```python
import os
conda_name, venv_name = "", ""

conda_prefix = os.environ.get('CONDA_PREFIX')
if conda_prefix:
    print("Anaconda environment is active:")
    print(f"Environment Path: {conda_prefix}")
    conda_name = os.path.basename(conda_prefix)
    print(f"Environment Name: {conda_name}")

virtual_env = os.environ.get('VIRTUAL_ENV')
if virtual_env:
    print("Virtualenv is active:")
    print(f"Environment Path: {virtual_env}")
    venv_name = os.path.basename(virtual_env)
    print(f"Environment Name: {venv_name}")

if conda_name != "llms" and venv_name != "llms" and venv_name != "venv" and venv_name != ".venv":
    print("Neither Anaconda nor Virtualenv seem to be activated with the expected name 'llms' or 'venv' or '.venv'")
    print("Did you run 'jupyter lab' from an activated environment with (llms) showing on the command line?")
    print("If in doubt, close down all jupyter lab, and follow Part 5 in the SETUP-PC or SETUP-mac guide.")
```

# Step 1.1

## It's time to check that the environment is good and dependencies are installed

And now, this next cell should run with no output - no import errors.  

An error would suggest that you don't have the right kernel, in which case please see Q5 and Q25 on the [FAQ](https://edwarddonner.com/faq)

```python
# This import should work if your environment is active and dependencies are installed!

from openai import OpenAI
```

# Step 2

Let's check your .env file exists and has the OpenAI key set properly inside it.  
Please run this code and check that it prints a successful message, otherwise follow its instructions.

If it isn't successful, then it's not able to find a file called `.env` in the `llm_engineering` folder.  
The name of the file must be exactly `.env` - it won't work if it's called `my-keys.env` or `.env.doc`.  
Is it possible that `.env` is actually called `.env.txt`?

Nasty gotchas to watch out for:  
- In the .env file, there should be no space between the equals sign and the key. Like: `OPENAI_API_KEY=sk-proj-...`
- If you copied and pasted your API key from another application, make sure that it didn't replace hyphens in your key with long dashes  

If you're having challenges creating the `.env` file, we can also do it with code! See the cell after the next one.

```python
from pathlib import Path

parent_dir = Path("..")
env_path = parent_dir / ".env"

if env_path.exists() and env_path.is_file():
    print(".env file found.")

    # Read the contents of the .env file
    with env_path.open("r") as env_file:
        contents = env_file.readlines()

    key_exists = any(line.startswith("OPENAI_API_KEY=") for line in contents)
    good_key = any(line.startswith("OPENAI_API_KEY=sk-proj-") for line in contents)
    classic_problem = any("OPEN_" in line for line in contents)
    
    if key_exists and good_key:
        print("SUCCESS! OPENAI_API_KEY found and it has the right prefix")
    elif key_exists:
        print("Found an OPENAI_API_KEY although it didn't have the expected prefix sk-proj- \nPlease double check your key in the file..")
    elif classic_problem:
        print("Didn't find an OPENAI_API_KEY, but I notice that 'OPEN_' appears - do you have a typo like OPEN_API_KEY instead of OPENAI_API_KEY?")
    else:
        print("Didn't find an OPENAI_API_KEY in the .env file")
else:
    print(".env file not found in the llm_engineering directory. It needs to have exactly the name: .env")
    
    possible_misnamed_files = list(parent_dir.glob("*.env*"))
    
    if possible_misnamed_files:
        print("\nWarning: No '.env' file found, but the following files were found in the llm_engineering directory that contain '.env' in the name. Perhaps this needs to be renamed?")
        for file in possible_misnamed_files:
            print(file.name)
```

## Fallback plan - python code to create the .env file for you

Only run the next cell if you're having problems making the .env file.  
Replace the text in the first line of code with your key from OpenAI.

```python
# Only run this code in this cell if you want to have a .env file created for you!

# Put your key inside the quote marks
make_me_a_file_with_this_key = "put your key here inside these quotes.. it should start sk-proj-"

# Change this to True if you already have a .env file and you want me to replace it
overwrite_if_already_exists = False 

from pathlib import Path

parent_dir = Path("..")
env_path = parent_dir / ".env"

if env_path.exists() and not overwrite_if_already_exists:
    print("There is already a .env file - if you want me to create a new one, change the variable overwrite_if_already_exists to True above")
else:
    try:
        with env_path.open(mode='w', encoding='utf-8') as env_file:
            env_file.write(f"OPENAI_API_KEY={make_me_a_file_with_this_key}")
        print(f"Successfully created the .env file at {env_path}")
        if not make_me_a_file_with_this_key.startswith("sk-proj-"):
            print(f"The key that you provided started with '{make_me_a_file_with_this_key[:8]}' which is different to sk-proj- is that what you intended?")
        print("Now rerun the previous cell to confirm that the file is created and the key is correct.")
    except Exception as e:
        print(f"An error occurred while creating the .env file: {e}")
```

# Step 3

Now let's check that your API key is correct set up in your `.env` file, and available using the dotenv package.
Try running the next cell.

```python
# This should print your API key to the output - please follow the instructions that get printed

import os
from dotenv import load_dotenv
load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("No API key was found - please try Kernel menu >> Restart Kernel And Clear Outputs of All Cells")
elif not api_key.startswith("sk-proj-"):
    print(f"An API key was found, but it starts with {api_key[:8]} rather than sk-proj- please double check this is as expected.")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them")
else:
    print("API key found and looks good so far!")

if api_key:
    problematic_unicode_chars = ['\u2013', '\u2014', '\u201c', '\u201d', '\u2026', '\u2018', '\u2019']
    forbidden_chars = ["'", " ", "\n", "\r", '"']
    
    if not all(32 <= ord(char) <= 126 for char in api_key):
        print("Potential problem: there might be unprintable characters accidentally included in the key?")
    elif any(char in api_key for char in problematic_unicode_chars):
        print("Potential problem: there might be special characters, like long hyphens or curly quotes in the key - did you copy it via a word processor?")
    elif any(char in api_key for char in forbidden_chars):
        print("Potential problem: there are quote marks, spaces or empty lines in your key?")
    else:
        print("The API key contains valid characters")
    
print(f"\nHere is the key --> {api_key} <--")
print()
print("If this key looks good, please go to the Edit menu >> Clear Cell Output so that your key is no longer displayed here!")
```

## It should print some checks including something like:

`Here is the key --> sk-proj-blahblahblah <--`

If it didn't print a key, then hopefully it's given you enough information to figure this out. Or contact me!

There is a final fallback approach if you wish: you can avoid using .env files altogether, and simply always provide your API key manually.  
Whenever you see this in the code:  
`openai = OpenAI()`  
You can replace it with:  
`openai = OpenAI(api_key="sk-proj-xxx")`

# Step 4

Now run the below code and you will hopefully see that GPT can handle basic arithmetic!!

If not, see the cell below.

```python
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

my_api_key = os.getenv("OPENAI_API_KEY")

print(f"Using API key --> {my_api_key} <--")

openai = OpenAI()
completion = openai.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{"role":"user", "content": "What's 2+2?"}],
)
print(completion.choices[0].message.content)
print("Now go to Edit menu >> Clear Cell Output to remove the display of your key.")
```

## If the key was set correctly, and this still didn't work

### If there's an error from OpenAI about your key, or a Rate Limit Error, then there's something up with your API key!

Please see Q18 here in the [FAQ](https://edwarddonner.com/faq) for the detailed steps to fix.

Any more problems? Email me at ed@edwarddonner.com or reach out in Udemy..


---
