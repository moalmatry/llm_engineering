# Guides

This unified reference file consolidates **14 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [guides/01_intro.ipynb](#file-guides-01-intro-ipynb)
- [guides/02_command_line.ipynb](#file-guides-02-command-line-ipynb)
- [guides/03_git_and_github.ipynb](#file-guides-03-git-and-github-ipynb)
- [guides/04_technical_foundations.ipynb](#file-guides-04-technical-foundations-ipynb)
- [guides/05_notebooks.ipynb](#file-guides-05-notebooks-ipynb)
- [guides/06_python_foundations.ipynb](#file-guides-06-python-foundations-ipynb)
- [guides/07_vibe_coding_and_debugging.ipynb](#file-guides-07-vibe-coding-and-debugging-ipynb)
- [guides/08_debugging.ipynb](#file-guides-08-debugging-ipynb)
- [guides/09_ai_apis_and_ollama.ipynb](#file-guides-09-ai-apis-and-ollama-ipynb)
- [guides/10_intermediate_python.ipynb](#file-guides-10-intermediate-python-ipynb)
- [guides/11_async_python.ipynb](#file-guides-11-async-python-ipynb)
- [guides/12_starting_your_project.ipynb](#file-guides-12-starting-your-project-ipynb)
- [guides/13_frontend.ipynb](#file-guides-13-frontend-ipynb)
- [guides/14_docker_terraform.ipynb](#file-guides-14-docker-terraform-ipynb)

---

<a id="file-guides-01-intro-ipynb"></a>
## File: `guides/01_intro.ipynb`

> **Path in repository:** `guides/01_intro.ipynb`

# Welcome to the Guides!

## Introduction

I've designed this course to be suitable for a wide range of backgrounds. For those of you relatively new to this, I've prepared some technical briefings to build your expertise.

These are designed to be self-study; you work through them at your own pace, investigating and experimenting.

I've heavily taken advantage of our AI friends to write some guides, and I've tried to frame them so they're as useful as possible and relevant to the course.

There's only one requirement for the course: plenty of patience! Keep in mind that one of the best ways to learn is by solving problems - if you feel frustrated with a challenging puzzle, remember that this is where the learning happens! And, get in touch if I can help.

### Contents (select from the sub-directory in the explorer on the left)

1. Intro - this contents
2. The command line
3. Git and Github
4. Technical foundations (environment variables, networks, APIs, uv)
5. Notebooks
6. Python foundations
7. "Vibe coding" - successfully coding with the help of LLMs
8. Debugging techniques
9. APIs and Ollama
10. Intermediate level python, including decorators and async  
11. Asynchronous Python
12. Starting your project - 3 crucial pieces of advice
13. Frontend Crash Course
14. Briefings on Docker and Terraform

### Also see the community_contributions directory for some awesome Python cookbooks contributed by students! (Thank you!)


---

<a id="file-guides-02-command-line-ipynb"></a>
## File: `guides/02_command_line.ipynb`

> **Path in repository:** `guides/02_command_line.ipynb`

# The command line

Welcome to the guide to build your confidence working at the command line.

By the end of this guide, you should be able to confidently work at the command line, creating directories, moving files and more!

## For Windows PC users

Please see this briefing:

https://chatgpt.com/share/68064acf-4d3c-8012-86a1-fb09a7c6f923

## For Mac users

Please see this briefing:

https://chatgpt.com/share/68064bfe-662c-8012-8073-479c32595459

Please do experiment to build your confidence.

ChatGPT, Claude, Gemini, DeepSeek and others are your friends! They are excellent at explaining any command line commands in detail. This will quickly become second nature.


---

<a id="file-guides-03-git-and-github-ipynb"></a>
## File: `guides/03_git_and_github.ipynb`

> **Path in repository:** `guides/03_git_and_github.ipynb`

# Git and Github

This guide is all about using source code control: Git and Github.

By the end of this, you should be confident with every day code control processes, including fetching the latest code and submitting a PR to merge your own changes.

### Foundational briefing

Here is Git and Github for a PC or Mac audience:

https://chatgpt.com/share/68061486-08b8-8012-97bc-3264ad5ebcd4

### Pulling latest code

I regularly add improvements to the course with new examples, exercises and materials.

Here are instructions for how to bring in the latest - the easy way, and the rigorous way!

https://chatgpt.com/share/6806178b-0700-8012-836f-7e87b2670b7b

### Contributing your changes to the repo to share your contributions with others

I'd be so grateful to include your contributions. It adds value for all other students, and I love to see it myself! As an added benefit, you get recognition in Github as a contributor to the repo.

Here's the overall steps involved in making a PR and the key instructions:  
https://edwarddonner.com/pr  

Please check before submitting:  
1. Your PR only contains changes in community-contributions (unless we've discussed it)  
2. All notebook outputs are clear  
3. Less than 2,000 lines of code in total, and not too many files  
4. Don't include unnecessary test files, or overly wordy README or .env.example or emojis or other LLM artifacts!

Thanks so much!

Detailed steps here: 

https://chatgpt.com/share/6873c22b-2a1c-8012-bc9a-debdcf7c835b

### If you'd like to become a Git pro

If you want to go deep on using Git, here is a brilliant guide. Read this and you will know much more than me!

https://beej.us/guide/bggit/


---

<a id="file-guides-04-technical-foundations-ipynb"></a>
## File: `guides/04_technical_foundations.ipynb`

> **Path in repository:** `guides/04_technical_foundations.ipynb`

# Technical Foundations

It's crucial that you feel comfortable with the basic technical concepts that we work with. This will make your experience of the entire course so much better - it can be very frustrating if you're not sure what's gong on.

These guides should build confidence in the underlying technologies we work with.

## Topic 1: ChatGPT versus OpenAI API

### What’s the difference between ChatGPT and the GPT API, both offered by OpenAI?

#### ChatGPT is an end-user tool. It’s a Chat product designed for consumers who are AI users.
- It has a free plan, and it also has paid subscription plans with more features.
- The subscription plans give the user near-unlimited access to use the Chat product.

#### The API is a service provided for AI engineers - software engineers and data scientists - working on other commercial products.
- It allows technical people, like you and me, to access the underlying models (like “GPT-6 Luna” and “GPT-6.1 Sol”) so that we can build our own products.
- If we wanted to, we could build our own version of ChatGPT using the API, and charge our end-users for it.
- Like most APIs, OpenAI charges a small amount based on API usage. For most examples on the course using gpt-6-luna, it’s of the order of $0.0001 per API call.

### I’m paying $20/month for ChatGPT - why do I need to pay more for the API?

- Hopefully this is now clear. The API is not for consumers; it’s for engineers to build their own platforms that they can charge for.
- If you were to have access to the API based on your subscription, then you could offer ChatGPT tools to others at a cheaper price, and put OpenAI out of business!
- Keep in mind: each API call may require 10,000,000,000,000 floating point calculations - that compute uses electricity!

Instead of calling the API, you can run open source models locally, but typically they have 1,000 times fewer calculations — and even though it’s tiny, that processing still hits your electricity bill..

## Topic 2: Taking a Screenshot

You may already be familiar with "taking a screenshot" on your computer, but if not (or if you think this means taking a photo with your camera..), please review this tutorial:

https://chatgpt.com/share/681f691b-6644-8012-b07d-207c68f259d5

## Topic 3: Environment Variables and the `.env` file

This tutorial walks you through everything you need to know about .env files!

Obiously you don't need to add the .env file to .gitignore, as I've already done that for you. But it hopefully explains the point well.

https://chatgpt.com/share/68061e89-dd84-8012-829d-9f4506c7baaa

## Topic 4: Networking basics

This tutorial covers networking and typical issues with certificates, VPNs, DNS and the like.

The sections give a summary; you should ask ChatGPT to expand on any section if it's relevant to your situation.

https://chatgpt.com/share/680620ec-3b30-8012-8c26-ca86693d0e3d

This is a more in-depth guide to tackling SSL / certificate issues, which is common in corporate environments:

https://chatgpt.com/share/69934d95-85dc-8012-af71-497d17fcb0a6

## Topic 5: APIs and Client Libraries - foundational briefing

We use APIs a lot in this course!

It's essential to understand the fundamentals of what's going on when we make a call to an API, and to be comfortable with words like "endpoint" and "client library".

Please review this guide:

https://chatgpt.com/share/68062432-43c8-8012-ad91-6311d4ad5858

## Topic 6: uv, package management, environment management

This lays out the Dependency Management situation and why we love uv! And a crash course in how to use it.

https://chatgpt.com/share/68c34d46-18a0-8012-8d65-0a0cce615912

Note that this guide suggests `uv run python xxx` which works fine, but simply `uv run xxx` works too and is more common.


---

<a id="file-guides-05-notebooks-ipynb"></a>
## File: `guides/05_notebooks.ipynb`

> **Path in repository:** `guides/05_notebooks.ipynb`

# Notebooks in Cursor

This course makes heavy use of a brilliant thing called Notebooks (also known as Jupyter Notebooks or Labs.) Those from a traditional software engineering background may feel discomfort with the "hacky" nature of Notebooks, but I must assure you: part of working with AI is being comfortable being a Scientist. As a Scientist, there's a lot of exploration and experimentation. And Notebooks are ideal for this kind of activity.

A notebook is a file with the extension ".ipynb" which stands for IPython Notebook, an early name for these.

## Briefing on Notebooks in Cursor

First, here's a briefing on how this fits together, and how to create and run a notebook in Cursor:

https://chatgpt.com/share/6806291a-25f0-8012-a08b-057acb5045ae


## A broader guide to Notebooks with examples

The Notebook is a Data Science playground where you can easily write code and investigate the results. It's an ideal environment for:  
- Research & Development
- Prototyping
- Learning (that's us!)

The notebook consists of a series of square boxes called "cells". Some of them contain text, like this cell, and some of them contain code, like the cell below.

First, you may need to click the `Select Kernel` button on the top right, and then pick `venv (Python 3.12.x)` or similar.

Click in a cell with code and press `Shift + Return` (or `Shift + Enter`) to run the code and print the output.

Do that now for the cell below this:

```python
# Click anywhere in this cell and press Shift + Return

2 + 2
```

## Congrats!

Now run the next cell which sets a value, followed by the cells after it to print the value

```python
# Set a value for a variable

favorite_fruit = "bananas"
```

```python
# The result of the last statement is shown after you run it

favorite_fruit
```

```python
# Use the variable

print(f"My favorite fruit is {favorite_fruit}")
```

```python
# Now change the variable

favorite_fruit = f"anything but {favorite_fruit}"
```

## Now go back and rerun the cell with the print statement, two cells back

See how it prints something different, even though favorite_fruit was changed further down in the notebook? 

The order that code appears in the notebook doesn't matter. What matters is the order that the code is **executed**. There's a python process sitting behind this notebook in which the variables are being changed.

This catches some people out when they first use notebooks.

```python
# Then run this cell twice, and see if you understand what's going on

print(f"My favorite fruit is {favorite_fruit}")

favorite_fruit = "apples"
```

# Explaining the 'kernel'

Sitting behind this notebook is a Python process which executes each cell when you run it. That Python process is known as the Kernel. Each notebook has its own separate Kernel.

You can click the button above "Restart Kernel".

If you then try to run the next cell, you'll get an error, because favorite_fruit is no longer defined. You'll need to run the cells from the top of the notebook again. Then the next cell should run fine.

```python
print(f"My favorite fruit is {favorite_fruit}")
```

# Adding and removing cells

Click in this cell, then click the \[+ Code\] button in the toolbar above to create a new cell immediately below this one. Copy and paste in the code in the prior cell, then run it! There are also icons in the top right of the selected cell to delete it (bin).

# Cell output

When you execute a cell, the standard output and the result of the last statement is written to the area immediately under the code, known as the 'cell output'. When you save a Notebook from the file menu (or ctrl+S or command+S), the output is also saved, making it a useful record of what happened.

You can clean this up by clicking "Clear All Outputs" in the toolbar. It's a good idea to clear outputs before you push code to a repo like GitHub, otherwise the files can be large and harder to read.

```python
spams = ["spam"] * 1000
print(spams)

# Might be worth clearing output after running this!
```

# Using markdown

So what's going on with these areas with writing in them, like this one? Well, there's actually a different kind of cell called a 'Markdown' cell for adding explanations like this. Click the [+ Markdown] button to add a new markdown cell.

Add some comments using Markdown format, perhaps copying and pasting from here:

```
# This is a heading
## This is a sub-head
### And a sub-sub-head

I like Jupyter Lab because it's
- Easy
- Flexible
- Satisfying
```

And to turn this into formatted text simply with Shift+Return in the cell.
Click in the cell and press the Bin icon if you want to remove it.

# The exclamation point

There's a super useful feature of jupyter labs; you can type a command with a ! in front of it in a code cell, like:

!ls  
!pwd

And it will run it at the command line (as if in Windows Powershell or Mac Terminal) and print the result

```python
# list the current directory

!ls
```

```python
# ping cnn.com - press the stop / interrupt button in the toolbar when you're bored

!ping cnn.com
```

# Minor things we encounter on the course

This isn't necessarily a feature of notebooks, but it's a nice package to know about that is useful in notebooks.

The package `tqdm` will print a nice progress bar if you wrap any iterable.

```python
# Here's some code with no progress bar
# It will take 10 seconds while you wonder what's happpening..

import time

spams = ["spam"] * 1000

for spam in spams:
    time.sleep(0.01)
```

```python
# And now, with a nice little progress bar:

import time
from tqdm import tqdm

spams = ["spam"] * 1000

for spam in tqdm(spams):
    time.sleep(0.01)
```

```python
# On a different topic, here's a useful way to print output in markdown

from IPython.display import Markdown, display

display(Markdown("# This is a big heading!\n\n- And this is a bullet-point\n- So is this\n- Me, too!"))
```

# That's it! You're up to speed on Notebooks / Labs in Cursor.

## Want to be even more advanced?

If you want to become a pro at Jupyter Lab (the technology behind this), you can read their tutorial [here](https://jupyterlab.readthedocs.io/en/latest/). But this isn't required for our course; just a good technique for hitting Shift + Return and enjoying the result!


---

<a id="file-guides-06-python-foundations-ipynb"></a>
## File: `guides/06_python_foundations.ipynb`

> **Path in repository:** `guides/06_python_foundations.ipynb`

# Foundations of Python and fixing NameErrors

## First, for a complete beginner

This introductory tutorial gets you started with the basics.

https://chatgpt.com/share/68063082-c2d8-8012-8d45-fa674aa1c1ed

## Next: a comprehensive briefing on Python

I'm going to defer to an AI friend for this, because these explanations are so well written with great examples. Copy and paste the code examples into a new cell to give them a try. Pick whichever section(s) you'd like to brush up on.

**Python imports:**  
https://chatgpt.com/share/672f9f31-8114-8012-be09-29ef0d0140fb

**Python functions** including default arguments:  
https://chatgpt.com/share/672f9f99-7060-8012-bfec-46d4cf77d672

**Python strings**, including slicing, split/join, replace and literals:  
https://chatgpt.com/share/672fb526-0aa0-8012-9e00-ad1687c04518

**Python f-strings** including number and date formatting:  
https://chatgpt.com/share/672fa125-0de0-8012-8e35-27918cbb481c

**Python lists, dicts and sets**, including the `get()` method:  
https://chatgpt.com/share/672fa225-3f04-8012-91af-f9c95287da8d

**Python files** including modes, encoding, context managers, Path, glob.glob:  
https://chatgpt.com/share/673b53b2-6d5c-8012-a344-221056c2f960

**Python classes:**  
https://chatgpt.com/share/672fa07a-1014-8012-b2ea-6dc679552715

**Pickling Python objects and converting to JSON:**  
https://chatgpt.com/share/673b553e-9d0c-8012-9919-f3bb5aa23e31

## With this in mind - understanding NameErrors in Python

It's quite common to hit a NameError in python. With foundational knowledge, you should always feel equipped to debug a NameError and get to the bottom of it.

The most common reason if you're working in a Notebook is that you haven't executed all the cells in order, so the Kernel does not have something defined.

If you're unsure how to fix a NameError, please see this [initial guide](https://chatgpt.com/share/67958312-ada0-8012-a1d3-62b3a5fcbbfc) and this [second guide with exercises](https://chatgpt.com/share/67a57e0b-0194-8012-bb50-8ea76c5995b8), and work through them both until you have high confidence.

There's some repetition here, so feel free to skip it if you're already confident.

After this, a NameError should never give you problems again!


---

<a id="file-guides-07-vibe-coding-and-debugging-ipynb"></a>
## File: `guides/07_vibe_coding_and_debugging.ipynb`

> **Path in repository:** `guides/07_vibe_coding_and_debugging.ipynb`

# Vibe coding and debugging

"Vibe coding" is the affectionate term for coding with the assistance of LLMs. It's particularly easy and wonderful to do with Cursor! But there are some good techniques to make it work well, which I cover on the course. Here are a few essential tips:

1. If you're prompting an LLM like ChatGPT or Claude to write code, include the current date in your prompt, and instruct the LLM to generate code that uses the latest versions of APIs. This is particularly important with the OpenAI API! ChatGPT frequently tries to use outdated versions of its own API...

2. Also in your prompts, ask LLMs to keep their code as short and simple as possible. LLMs seem to love to add lots of extra, unnecessary checks that clutters code and makes it hard to find problems.

3. Ask the same question to multiple LLMs, and pick the answer that is clearest and simplest.

4. Similar: take the answer from 1 LLM, and ask another LLM to verify it for correctness and whether it could be simpler or clearer.

5. Ask an LLM to give you 3 variations for ways to solve a problem, and pick the one that is clearest.

## Vibe Coding for a larger project

Try to avoid having an LLM generate 100-200 lines of code or more; it will be so hard for you to debug and figure out what's going wrong (unless you're already knowledgable).

Instead: start by breaking down your problem into small, independently testable steps, that are each relatively small. If you're not sure how to break down your problem - this is something you can ask the LLM to do!

Then for each of these building blocks:
- Use the tips above to have the LLM build the code
- Also have the LLM write tests to test and verify the code
- Test it yourself and satisfy yourself that it's working correctly

This will allow you to build a larger project with confidence.

## The golden rule: start small, work incrementally!


---

<a id="file-guides-08-debugging-ipynb"></a>
## File: `guides/08_debugging.ipynb`

> **Path in repository:** `guides/08_debugging.ipynb`

# Debugging Survival Guide

## The key is to consistently reproduce your problem in 5-10 lines of code

Hitting an exception can sometimes feel quite frustrating, particularly if you're not sure how to approach it. But this is where the best learning happens! Getting to the bottom of hard problems is a great way to learn, and can be quite satisfying.

But I'm here to help if you can't!

### Preliminaries

Here is a briefing on Exceptions, Stack Traces, Exception Handling and more:

https://chatgpt.com/share/6806383c-ab38-8012-b21f-61af665bb900

Also: see [this guide](https://chatgpt.com/share/681f691b-6644-8012-b07d-207c68f259d5) if you're unsure how to take screenshots.

### Formula for debugging: recreate in 10 lines of code

There is an art and a science to great debugging. The best way to pick it up is by practice! But here are the essentials:

1. Recreate  
Reproduce your problem, consistently

2. Simplify  
Reduce your problem down to the simplest possible way to reproduce it. I can't tell you how many people have sent me 100+ lines of code and said "Ed, this isn't working, please fix it". That's not how it works! The first thing I would try is to reduce this to the core problem - ideally in 10-20 lines of code or less. In one case, I showed a student how to reproduce it with 2 lines of code!

_The thing is, it's much easier for **you** to do this than anybody else._ So while it can be tedious, this is almost always the best way to start. Reduce down to a few lines of code. And by the way, when you do that, you often figure out the problem yourself anyway!

3. Get help  
Once you've recreated the problem with just a few lines of code, if you can't see what's happening - you should get help! It's worth asking ChatGPT and friends of course; give them the short example and the full stack trace.

And reach out to me! I'm here to make your learning experience as awesome as possible and if you are stuck, I will help you get unstuck.

### The best way to work with me for fastest fixes...

1. Simplify the problem as much as possible, with an easy way to reproduce
2. Include the full stack trace, and a screenshot not a photo (see [this guide](https://chatgpt.com/share/681f691b-6644-8012-b07d-207c68f259d5) if you're unsure how to take screenshots)
3. Email me at ed@edwarddonner.com. Or best of all: if you've used Google Colab before, this is a really terrific way to share an issue, because it will be identical for me to reproduce, and I can fix it and share the fix with you directly.

I look forward to helping you!


---

<a id="file-guides-09-ai-apis-and-ollama-ipynb"></a>
## File: `guides/09_ai_apis_and_ollama.ipynb`

> **Path in repository:** `guides/09_ai_apis_and_ollama.ipynb`

# LLM APIs and Ollama - beyond OpenAI

_IMPORTANT: If you're not as familiar with APIs in general, and with Environment Variables on your PC or Mac, please review the APIs section in Guide 4 Technical Foundations before proceeding with this guide (topics 3 and 5 in Guide 4)._

## Crucial context for using models other than OpenAI - please read this first!

Throughout the course, we use APIs for connecting with the strongest LLMs on the planet.

The companies behind these LLMs, such as OpenAI, Anthropic, Google and DeepSeek, have built web endpoints. You call their models by making an HTTP request to a Web Address and passing in all the information about your prompts.

But it would be painful if we needed to build HTTP requests every time we wanted to call an API.

To make this simple, the team at OpenAI wrote a python utility known as a "Python Client Library" which wraps the HTTP call. So you write python code and it calls the web.

And THAT is what the library `openai` is.

### What is the `openai` python client library

It is:
- A lightweight python utility
- Turns your python requests into an HTTP call
- Converts the results coming back from the HTTP call into python objects

### What it is NOT

- It's not got any code to actually run a Large Language Model! No GPT code! It just makes a web request
- There's no scientific computing code, and nothing particularly specialized for OpenAI

### How to use it:

```python
# Create an OpenAI python client for making web calls to OpenAI
openai = OpenAI()

# Make the call
response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=[{"role":"user", "content": "what is 2+2?"}])

# Print the result
print(response.choices[0].message.content)
```

### What does this do

When you make the python call: `openai.chat.completions.create()`  
It simply makes a web request to this url: `https://api.openai.com/v1/chat/completions`  
And it converts the response to python objects.

That's it.

Here's the API documentation if you make [direct web HTTP calls](https://platform.openai.com/docs/guides/text?api-mode=chat&lang=curl)  
And here's the same API documentation if you use the [Python Client Library](https://platform.openai.com/docs/guides/text?api-mode=chat&lang=python)

## With that context - how do I use other LLMs?

It turns out - it's super easy!

All the other major LLMs have API endpoints that are compatible with OpenAI.

And so OpenAI did everyone a favor: they said, hey look - you can all use our utility for converting python to web requests. We'll allow you to change the utility from calling `https://api.openai/com/v1` to calling any web address that you specify.

And so you can use the OpenAI utility even for calling models that are NOT OpenAI, like this:

`not_actually_openai = OpenAI(base_url="https://somewhere.completely.different/", api_key="another_providers_key")`

It's important to appreciate that this OpenAI code is just a utility for making HTTP calls to endpoints. So even though we're using code from the OpenAI team, we can use it to call models other than OpenAI.

Here are all the OpenAI-compatible endpoints from the major providers. It even includes using Ollama, locally. Ollama provides an endpoint on your local machine, and they made it OpenAI compatible too - very convenient.

```python
ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1/"
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROK_BASE_URL = "https://api.x.ai/v1"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
```

## Here are examples for Gemini, DeepSeek, Ollama and OpenRouter

### Example 1: Using Gemini instead of OpenAI

1. Visit Google Studio to set up an account: https://aistudio.google.com/  
2. Add your key as GOOGLE_API_KEY to your `.env`  
3. Also add it a second time as GEMINI_API_KEY to your `.env` - this will be helpful later.

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
response = gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

### Example 2: Using DeepSeek API instead of OpenAI (cheap, and only $2 upfront)

1. Visit DeepSeek API to set up an account: https://platform.deepseek.com/  
2. You will need to add an initial $2 minimum balance.  
3. Add your key as DEEPSEEK_API_KEY to your `.env`  

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek = OpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
response = deepseek.chat.completions.create(model="deepseek-flash", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

### Example 3: Using Ollama to be free and local instead of OpenAI

Ollama allows you to run models locally; it provides an OpenAI compatible API on your machine.  
There's no API key for Ollama; there's no third party with your credit card, so no need for any kind of key.

1. If you're new to Ollama, install it by following the instructions here: https://ollama.com   
2. Then in a Cursor Terminal, do `ollama run llama3.2` to chat with Llama 3.2  
BEWARE: do not use llama3.3 or llama4 - these are massive models not designed for home computing! They will fill up your disk.  

Then:

```python
!ollama pull llama3.2

from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="anything")
response = ollama.chat.completions.create(model="llama3.2", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

### Example 4: Using the popular service [OpenRouter](https://openrouter.ai) which has an easier billing process instead of OpenAI

OpenRouter is very convenient: it gives you free access to many models, and easy access with small upfront to paid models.

1. Sign up at https://openrouter.ai
2. Add the minimum upfront balance as needed
3. Add your key as OPENROUTER_API_KEY to your `.env` file

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
response = openrouter.chat.completions.create(model="openai/gpt-6-luna", reasoning_effort="none", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```


### Using different API providers with Agent Frameworks

The Agent Frameworks make it easy to switch between these providers. You can switch LLMs and pick different ones at any point in the course. There are more notes below on each of them. For OpenAI Agents SDK, see a section later in this notebook. For CrewAI, we cover it on the course, but it's easy: just use the full path to the model that LiteLLM expects.

## Costs of APIs

The cost of each API call is very low indeed - most calls to models we use on this course are fractions of cents.

But it's extremely important to note:

1. A complex Agentic project could involve many LLM calls - perhaps 20-30 - and so it can add up. It's important to set limits and monitor usage.

2. With Agentic AI, there is a risk of Agents getting into a loop or carrying out more processing than intended. You should monitor your API usage, and never put more budget than you are comfortable with. Some APIs have an "auto-refill" setting that can charge automatically to your card - I strongly recommend you keep this off.

3. You should only spend what you are comfortable with. There is a free alternative in Ollama that you can use as a replacement if you wish. DeepSeek, Gemini 3.1 Flash-Lite and GPT-6 Luna are significantly cheaper.

Keep in mind that these LLM calls typically involve trillions of floating point calculations - someone has to pay the electricity bills!

### Ollama: Free alternative to Paid APIs (but please see Warning about llama version)

Ollama is a product that runs locally on your machine. It can run open-source models, and it provides an API endpoint on your computer that is compatible with OpenAI.

First, download Ollama by visiting:
https://ollama.com

Then from your Terminal in Cursor (View menu >> Terminal), run this command to download a model:

```shell
ollama pull llama3.2
```

WARNING: Be careful not to use llama3.3 or llama4 - these are much larger models that are not suitable for home computers.

And now, any time that we have code like:  
`openai = OpenAI()`  
You can use this as a direct replacement:  
`openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')`  
And also replace model names like **gpt-6-luna** with **llama3.2**.  
If you get an error about `reasoning_effort` or thinking, remove that argument: it's an OpenAI setting that not every model accepts.  

You don't need to put anything in your .env file for this; with Ollama, everything is running on your computer. You're not calling out to a third party on the cloud, nobody has your credit card details, so there's no need for a secret key! The code `api_key='ollama'` above is only required because the OpenAI client library expects an api_key to be passed in, but the value is ignored by Ollama.

Below is a full example:

```python
# You need to do this one time on your computer
!ollama pull llama3.2

from openai import OpenAI
MODEL = "llama3.2"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response.choices[0].message.content)
```

You will need to make similar changes to use Ollama within any of the Agent Frameworks - you should be able to google for an exact example, or ask me.

### OpenRouter: Convenient gateway platform for OpenAI and others

OpenRouter is a third party service that allows you to connect to a wide range of LLMs, including OpenAI.

It's known for having a simpler billing process that may be easier for some countries outside the US.

First, check out their website:  
https://openrouter.ai/

Then, take a peak at their quickstart:  
https://openrouter.ai/docs/quickstart

And add your key to your .env file:  
```shell
OPENROUTER_API_KEY=sk-or....
```

And now, any time you have code like this:  
```python
MODEL = "gpt-6-luna"
openai = OpenAI()
```

You can replace it with code like this:

```python
MODEL = "openai/gpt-6-luna"
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openai = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_api_key)

response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response.choices[0].message.content)
```

You will need to make similar changes to use OpenRouter within any of the Agent Frameworks - you should be able to google for an exact example, or ask me.

## OpenAI Agents SDK - specific instructions

With OpenAI Agents SDK (weeks 2 and 6), it's particularly easy to use any model provided by OpenAI themselves. Simply pass in the model name:

`agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-6-luna")`

You can also substitute in any other provider with an OpenAI compatible API. You do it in 3 steps like this:

```python
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
deepseek_client = AsyncOpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
deepseek_model = OpenAIChatCompletionsModel(model="deepseek-flash", openai_client=deepseek_client)
```

And then you simply provide this model when you create an Agent.

`agent = Agent(name="Jokester", instructions="You are a joke teller", model=deepseek_model)`

And you can use a similar approach for any other OpenAI compatible API, with the same 3 steps:

```python
# extra imports
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

# Step 1: specify the base URL endpoints where the provider offers an OpenAI compatible API
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROK_BASE_URL = "https://api.x.ai/v1"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

# Step 2: Create an AsyncOpenAI object for that endpoint
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
grok_client = AsyncOpenAI(base_url=GROK_BASE_URL, api_key=grok_api_key)
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
ollama_client = AsyncOpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

# Step 3: Create a model object to provide when creating an Agent
gemini_model = OpenAIChatCompletionsModel(model="gemini-3.1-flash-lite", openai_client=gemini_client)
grok_model = OpenAIChatCompletionsModel(model="grok-4.3", openai_client=grok_client)
gpt_oss_model = OpenAIChatCompletionsModel(model="openai/gpt-oss-120b", openai_client=groq_client)
grok_via_openrouter_model = OpenAIChatCompletionsModel(model="x-ai/grok-4.3", openai_client=openrouter_client)
llama_3_2_local_model = OpenAIChatCompletionsModel(model="llama3.2", openai_client=ollama_client)
```

### To use Azure with OpenAI Agents SDK

See instructions here:  
https://techcommunity.microsoft.com/blog/azure-ai-services-blog/use-azure-openai-and-apim-with-the-openai-agents-sdk/4392537

Such as this:
```python
from openai import AsyncAzureOpenAI
from agents import set_default_openai_client
from dotenv import load_dotenv
import os
 
# Load environment variables
load_dotenv()
 
# Create OpenAI client using Azure OpenAI
openai_client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")
)
 
# Set the default OpenAI client for the Agents SDK
set_default_openai_client(openai_client)
```

## CrewAI setup

Here's Crew's docs for LLM connections with the model names to use for all models. As student Sadan S. pointed out (thank you!), it's worth knowing that for Google you need to use the environment variable `GEMINI_API_KEY` instead of `GOOGLE_API_KEY`:

https://docs.crewai.com/concepts/llms

And here's their tutorial with some more info:

https://docs.crewai.com/how-to/llm-connections

## LangGraph setup

To use LangGraph with Ollama (and follow similar for other models):  
https://python.langchain.com/docs/integrations/chat/ollama/#installation

First add the package:  
`uv add langchain-ollama`

Then in the lab, make this replacement:   
```python
from langchain_ollama import ChatOllama
# llm = ChatOpenAI(model="gpt-6-luna")
llm = ChatOllama(model="gemma3:4b")
```

And obviously run `!ollama pull gemma3:4b` (or whichever model) beforehand.

Many thanks to Miroslav P. for adding this, and to Arvin F. for the question!

## LangGraph with other models

Just follow the same recipe as above, but use any of the models from here:  
https://python.langchain.com/docs/integrations/chat/

## AutoGen with other models

Here's another contribution from Miroslav P. (thank you!) for using Ollama + local models with AutoGen, and Miroslav has a great example showing gemma3 performing well.

```python
# model_client = OpenAIChatCompletionClient(model="gpt-6-luna")
 
from autogen_ext.models.ollama import OllamaChatCompletionClient
 
model_client = OllamaChatCompletionClient(
    model="gemma3:4b",
    model_info={
        "vision": True,
        "function_calling": False,
        "json_output": True,
        "family": "unknown",
    },
)
```

## Worth keeping in mind

1. If you wish to use Ollama to run models locally, you may find that smaller models struggle with the more advanced projects. You'll need to experiment with different model sizes and capabilities, and plenty of patience may be needed to find something that works well. I expect several of our projects are too challenging for llama3.2. As an alternative, consider the free models on openrouter.ai, or the very cheap models that are almost free - like DeepSeek.

2. Chat models often do better than Reasoning models because Reasoning models can "over-think" some assignments. It's important to experiment. Bigger isn't always better...

3. It's confusing, but there are 2 different providers that sound similar!  
- Grok is the LLM from Elon Musk's X
- Groq is a platform for fast inference of open source models

A student pointed out to me that "Groq" came first!


---

<a id="file-guides-10-intermediate-python-ipynb"></a>
## File: `guides/10_intermediate_python.ipynb`

> **Path in repository:** `guides/10_intermediate_python.ipynb`

# Intermediate Level Python

## A briefing on more advanced features of Python

This section assumes you're up to speed on the foundations - and now we cover some important features of python that we use on the course.

1. Comprehensions  
2. Generators  
3. Sub-classes, Type Hints, Pydantic  
4. Decorators
5. Docker (not really python, but we use it to run python code!)

```python
# First let's create some things:

fruits = ["Apples", "Bananas", "Pears"]

book1 = {"title": "Great Expectations", "author": "Charles Dickens"}
book2 = {"title": "Bleak House", "author": "Charles Dickens"}
book3 = {"title": "An Book By No Author"}
book4 = {"title": "Moby Dick", "author": "Herman Melville"}

books = [book1, book2, book3, book4]
```

# Part 1: List and dict comprehensions

```python
# Simple enough to start

for fruit in fruits:
    print(fruit)
```

```python
# Let's make a new version of fruits

fruits_shouted = []
for fruit in fruits:
    fruits_shouted.append(fruit.upper())

fruits_shouted
```

```python
# You probably already know this
# There's a nice Python construct called "list comprehension" that does this:

fruits_shouted2 = [fruit.upper() for fruit in fruits]
fruits_shouted2
```

```python
# But you may not know that you can do this to create dictionaries, too:

fruit_mapping = {fruit: fruit.upper() for fruit in fruits}
fruit_mapping
```

```python
# you can also use the if statement to filter the results

fruits_with_longer_names_shouted = [fruit.upper() for fruit in fruits if len(fruit)>5]
fruits_with_longer_names_shouted
```

```python
fruit_mapping_unless_starts_with_a = {fruit: fruit.upper() for fruit in fruits if not fruit.startswith('A')}
fruit_mapping_unless_starts_with_a
```

```python
# Another comprehension

[book['title'] for book in books]
```

```python
# This code will fail with an error because one of our books doesn't have an author

[book['author'] for book in books]
```

```python
# But this will work, because get() returns None

[book.get('author') for book in books]
```

```python
# And this variation will filter out the None

[book.get('author') for book in books if book.get('author')]
```

```python
# And this version will convert it into a set, removing duplicates

set([book.get('author') for book in books if book.get('author')])
```

```python
# And finally, this version is even nicer
# curly braces creates a set, so this is a set comprehension

{book.get('author') for book in books if book.get('author')}
```

# Part 2: Generators

We use Generators in the course because AI models can stream back results.

If you've not used Generators before, please start with this excellent intro from ChatGPT:

https://chatgpt.com/share/672faa6e-7dd0-8012-aae5-44fc0d0ec218

Try pasting some of its examples into a cell.

```python
# First define a generator; it looks like a function, but it has yield instead of return

import time

def come_up_with_fruit_names():
    for fruit in fruits:
        time.sleep(1) # thinking of a fruit
        yield fruit
```

```python
# Then use it

for fruit in come_up_with_fruit_names():
    print(fruit)
```

```python
# Here's another one

def authors_generator():
    for book in books:
        if book.get("author"):
            yield book.get("author")
```

```python
# Use it

for author in authors_generator():
    print(author)
```

```python
# Here's the same thing written with list comprehension

def authors_generator():
    for author in [book.get("author") for book in books if book.get("author")]:
        yield author
```

```python
# Use it

for author in authors_generator():
    print(author)
```

```python
# Here's a nice shortcut
# You can use "yield from" to yield each item of an iterable

def authors_generator():
    yield from [book.get("author") for book in books if book.get("author")]
```

```python
# Use it

for author in authors_generator():
    print(author)
```

```python
# And finally - we can replace the list comprehension with a set comprehension

def unique_authors_generator():
    yield from {book.get("author") for book in books if book.get("author")}
```

```python
# Use it

for author in unique_authors_generator():
    print(author)
```

```python
# And for some fun - press the stop button in the toolbar when bored!
# It's like we've made our own Large Language Model... although not particularly large..
# See if you understand why it prints a letter at a time, instead of a word at a time. If you're unsure, try removing the keyword "from" everywhere in the code.

import random
import time

pronouns = ["I", "You", "We", "They"]
verbs = ["eat", "detest", "bathe in", "deny the existence of", "resent", "pontificate about", "juggle", "impersonate", "worship", "misplace", "conspire with", "philosophize about", "tap dance on", "dramatically renounce", "secretly collect"]
adjectives = ["turqoise", "smelly", "arrogant", "festering", "pleasing", "whimsical", "disheveled", "pretentious", "wobbly", "melodramatic", "pompous", "fluorescent", "bewildered", "suspicious", "overripe"]
nouns = ["turnips", "rodents", "eels", "walruses", "kumquats", "monocles", "spreadsheets", "bagpipes", "wombats", "accordions", "mustaches", "calculators", "jellyfish", "thermostats"]

def infinite_random_sentences():
    while True:
        yield from random.choice(pronouns)
        yield " "
        yield from random.choice(verbs)
        yield " "
        yield from random.choice(adjectives)
        yield " "
        yield from random.choice(nouns)
        yield ". "

for letter in infinite_random_sentences():
    print(letter, end="", flush=True)
    time.sleep(0.02)
```

# Exercise

Write some python classes for the books example.

Write a Book class with a title and author. Include a method has_author()

Write a BookShelf class with a list of books. Include a generator method unique_authors()

# Part 3: Sub-classes, Type Hints, Pydantic

Here are some intermediate level details of Classes from our AI friend, including use of type hints, inheritance and class methods. This includes a Book example.

https://chatgpt.com/share/67348aca-65fc-8012-a4a9-fd1b8f04ba59

And here is a comprehensive tutorial on Pydantic classes covering everything you need to know about Pydantic.

https://chatgpt.com/share/68064537-6cfc-8012-93e1-f7dd0932f321

## Part 4: Decorators

Here is a briefing, with an example from OpenAI Agents SDK:

https://chatgpt.com/share/6806474d-3880-8012-b2a2-87b3ee4489da

## Part 5: Docker

Here is a convenient tutorial to introduce Docker.

In the last section, this also covers an answer to a question in Week 6 - what does it mean to run an MCP server in Docker? But you can ignore this question if you're not on week 6 yet.

https://chatgpt.com/share/6814bc1d-2f3c-8012-9b18-dddc82ea421b

```python
# You need to install docker to run this example
# This will download the Docker image for python 3.12, create a container,
# Run some python code and print the result

!docker run --rm python:3.12 python -c "print(2 + 2)"
```


---

<a id="file-guides-11-async-python-ipynb"></a>
## File: `guides/11_async_python.ipynb`

> **Path in repository:** `guides/11_async_python.ipynb`

# Async Python

## A briefing on asynchronous python coding, essential in Agent engineering

Here is a masterful tutorial by you-know-who with exercises and comparisons.

https://chatgpt.com/share/680648b1-b0a0-8012-8449-4f90b540886c

This includes how to run async code from a python module.

### And now some examples:

```python
# Let's define an async function

import asyncio

async def do_some_work():
    print("Starting work")
    await asyncio.sleep(1)
    print("Work complete")
```

```python
# What will this do?

do_some_work()
```

```python
# OK let's try that again!

await do_some_work()
```

```python
# What's wrong with this?

async def do_a_lot_of_work():
    do_some_work()
    do_some_work()
    do_some_work()

await do_a_lot_of_work()
```

```python
# Interesting warning! Let's fix it

async def do_a_lot_of_work():
    await do_some_work()
    await do_some_work()
    await do_some_work()

await do_a_lot_of_work()
```

```python
# And now let's do it in parallel
# It's important to recognize that this is not "multi-threading" in the way that you may be used to
# The asyncio library is running on a single thread, but it's using a loop to switch between tasks while one is waiting

async def do_a_lot_of_work_in_parallel():
    await asyncio.gather(do_some_work(), do_some_work(), do_some_work())

await do_a_lot_of_work_in_parallel()
```

### Finally - try writing a python module that calls do_a_lot_of_work_in_parallel

See the link at the top; you'll need something like this in your module:

```python
if __name__ == "__main__":
    asyncio.run(do_a_lot_of_work_in_parallel())
```


---

<a id="file-guides-12-starting-your-project-ipynb"></a>
## File: `guides/12_starting_your_project.ipynb`

> **Path in repository:** `guides/12_starting_your_project.ipynb`

## How to start working on your idea

So you've had an idea for something you'd like to build.

CONGRATULATIONS! That's the most important part already done. The idea is everything!

But now you're unsure where to begin. I get a lot of questions about this.

I want to give you three essential pieces of advice.

## Advice 1: Be a Scientist

Being an AI Engineer involves wearing 2 hats: being a Software Engineer, and a Data Scientist.

At the start of your project, it's crucial to take off your Software Engineering hat and firmly put on your Data Science hat.

A lot of people from a software engineering background (myself included!) struggle with this. It's common for people to fall into their comfort zone, asking questions about architecture, design, data pipes, scalability, deployment.

These are all great questions, but they are not the critical ones at this early stage. They are not the hard questions. They won't make or break your idea.

For the critical questions, you need to be a Scientist.

Ask yourself:  
1. How will you evaluate success of your model? What will you measure?  
2. What data do you have, and what data do you need?  
3. How can you build small prototypes to test different techniques and understand model performance?

Address the science questions first - what you can achieve with LLMs and how.

And I recommend starting in a Notebook before you work in python modules, to force yourself to operate with this scientific mindset.

This is even more crucial with Agent projects. It can be tempting to draw up a big Agent architecture diagram on how your agents will collaborate, like a technical diagram. But this is thinking like a Software Engineer. I recommend approaching it differently; experiment with different approaches, investigate what works well, test hypotheses and iterate.

## Advice 2: Embrace R&D

OK so this is pretty similar to Advice 1, but worth repeating!

I often get asked questions like: "Ed, I want to build the following solution. Should I use model A, B, or C? Should I use Agents, RAG or fine-tuning?"

My answer is almost always:  
- You should do all of the above! The key is to experiment; (a) come up with an evaluation criteria, (b) develop a curated dataset, (c) test different ideas and see how they perform
- I often have an instinct for which will work best, but my instinct is often wrong! Don't trust me: try it yourself  
- There's simply no substitute for experimentation.

## Advice 3: Dream big but start SMALL!

I also often have students send me 200-300 lines of code saying, "Ed, this isn't performing, please fix it". 😂

As I say in the debugging guide - that's not how it works!

When starting projects, it's crucial to start small and simple. Perfect every prompt; work in detail on every step. Satisfy yourself that each LLM call is performing as you wish, and iterate on the inputs until responses are consistent and reliable.

If you always work incrementally and with small, testable building blocks, you should have complete clarity on what's going on.

And of course, I love helping people with projects and it's great to help fix problems. But if you approach your project incrementally, you should always have clarity on exactly what isn't performing - and then it's super efficient for me to help you.

# In summary

You probably noticed the common theme through these 3 pieces of advice. It can feel jarring for people from a non-Data Science background to approach problems in such an ad-hoc way; it feels "hacky" and unsatisfying. But in my opinion, this is the single most important skill to acquire to be a successful AI engineer: being comfortable with uncertainty, enjoying the experiments, and embracing being a Scientist.


---

<a id="file-guides-13-frontend-ipynb"></a>
## File: `guides/13_frontend.ipynb`

> **Path in repository:** `guides/13_frontend.ipynb`

# Your frontend crash course

Here is a seven part series developed by you-know-who under my direction. It's very nicely done! You should take this in any direction you like.

ChatGPT has written these in note form for someone who wants to experiment; you should ask it to rewrite in a more verbose way if you'd prefer deeper explanations.

1. Refresher on modern HTML, CSS and JavaScript

https://chatgpt.com/share/68c345ee-ae34-8012-9a05-0ce43a816f9c

2. Modern JavaScript

https://chatgpt.com/share/68c3495f-0c94-8012-b048-db1670aefa47

3. From JavaScript to TypeScript

https://chatgpt.com/share/68c34974-b768-8012-9926-5a9ed67d59c3

4. React (TypeScript) basics

https://chatgpt.com/share/68c3498d-e340-8012-b3a3-37a28802db6a

5. React - state, props, hooks

https://chatgpt.com/share/68c349c7-e75c-8012-b1e5-b4f51bb0e27c

6. NextJS introduction

https://chatgpt.com/share/68c349e7-e740-8012-8f0c-ba40ad7e148d

7. NextJS rendering models and Tailwind

https://chatgpt.com/share/68c34a13-3120-8012-9a67-f53d7a0cfc99


---

<a id="file-guides-14-docker-terraform-ipynb"></a>
## File: `guides/14_docker_terraform.ipynb`

> **Path in repository:** `guides/14_docker_terraform.ipynb`

# Briefings on Docker and Terraform

Here's a mutual friend giving an excellent self-study tutorial on Docker essentials:

https://chatgpt.com/share/68c34f21-07bc-8012-b411-35cc97aff6ab

And here is an equally excellent overview of Terraform to get you building infrastructure with code like a pro. No more AWS console!

https://chatgpt.com/share/68c3513a-c194-8012-85c3-c0ea9143af5a


---
