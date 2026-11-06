# Week1 Prompt Engineering and APIs

This unified reference file consolidates **10 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [week1/day1.ipynb](#file-week1-day1-ipynb)
- [week1/day2.ipynb](#file-week1-day2-ipynb)
- [week1/day4.ipynb](#file-week1-day4-ipynb)
- [week1/day5.ipynb](#file-week1-day5-ipynb)
- [week1/scraper.py](#file-week1-scraper-py)
- [week1/solution.py](#file-week1-solution-py)
- [week1/solutions/day1_with_ollama.ipynb](#file-week1-solutions-day1-with-ollama-ipynb)
- [week1/solutions/day2 SOLUTION.ipynb](#file-week1-solutions-day2-solution-ipynb)
- [week1/solutions/week1 SOLUTION.ipynb](#file-week1-solutions-week1-solution-ipynb)
- [week1/week1 EXERCISE.ipynb](#file-week1-week1-exercise-ipynb)

---

<a id="file-week1-day1-ipynb"></a>
## File: `week1/day1.ipynb`

> **Path in repository:** `week1/day1.ipynb`

# YOUR FIRST LAB
### Please read this section. This is valuable to get you prepared, even if it's a long read -- it's important stuff.

### Also, be sure to read [README.md](../README.md)!

### Answers to the most common questions

[My Cursor looks different to yours (new splash screen)](https://edwarddonner.com/avatar?q=54)  
[Can I use Gemini or free models instead of OpenAI Yes!](https://edwarddonner.com/avatar?q=8)  
[Where are the course resources](https://edwarddonner.com/2024/11/13/llm-engineering-resources/)   
[How does this course fit in with your others?](https://edwarddonner.com/curriculum)  
[Can I take this course with no programming background?](https://edwarddonner.com/avatar?q=2)  
[What job can I get after taking this course?](https://edwarddonner.com/avatar?q=3)  

## Your first Frontier LLM Project

By the end of this course, you will have built an autonomous Agentic AI solution with 7 agents that collaborate to solve a business problem. All in good time! We will start with something smaller...

Our goal is to code a new kind of Web Browser. Give it a URL, and it will respond with a summary. The Reader's Digest of the internet!!

Before starting, you should have completed the setup linked in the README.

### If you're new to working in "Notebooks" (also known as Labs or Jupyter Lab)

Welcome to the wonderful world of Data Science experimentation! Simply click in each "cell" with code in it, such as the cell immediately below this text, and hit Shift+Return to execute that cell. Be sure to run every cell, starting at the top, in order.

Please look in the [Guides folder](../guides/01_intro.ipynb) for all the guides.

## I am here to help

If you have any problems at all, please do reach out.  
I'm available through the platform, or at ed@edwarddonner.com, or at https://www.linkedin.com/in/eddonner/ if you'd like to connect (and I love connecting!)   
And I also have a [YouTube channel with extra content](https://youtube.com/@edward.donner).  
And this is new to me, but I'm also trying out X at [@edwarddonner](https://x.com/edwarddonner) - if you're on X, please show me how it's done 😂  

## More troubleshooting

Please see the [troubleshooting](../setup/troubleshooting.ipynb) notebook in the setup folder to diagnose and fix common problems. At the very end of it is a diagnostics script with some useful debug info.

## If this is old hat!

If you're already comfortable with today's material, please hang in there; you can move swiftly through the first few labs - we will get much more in depth as the weeks progress. Ultimately we will fine-tune our own LLM to compete with OpenAI!

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Please read - important note</h2>
            <span style="color:#900;">The way I collaborate with you may be different to other courses you've taken. I prefer not to type code while you watch. Rather, I execute Jupyter Labs, like this, and give you an intuition for what's going on. My suggestion is that you carefully execute this yourself, <b>after</b> watching the lecture. Add print statements to understand what's going on, and then come up with your own variations. If you have a Github account, use this to showcase your variations. Not only is this essential practice, but it demonstrates your skills to others, including perhaps future clients or employers...</span>
        </td>
    </tr>
</table>
<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">This code is a live resource - keep an eye out for my emails</h2>
            <span style="color:#f71;">I push updates to the code regularly. As people ask questions, I add more examples or improved commentary. As a result, you'll notice that the code below isn't identical to the videos. Everything from the videos is here; but I've also added better explanations and new models like DeepSeek. Consider this like an interactive book.<br/><br/>
                I try to send emails regularly with important updates related to the course. You can find this in the 'Announcements' section of Udemy in the left sidebar. You can also choose to receive my emails via your Notification Settings in Udemy. I'm respectful of your inbox and always try to add value with my emails!
            </span>
        </td>
    </tr>
</table>
<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business value of these exercises</h2>
            <span style="color:#181;">A final thought. While I've designed these notebooks to be educational, I've also tried to make them enjoyable. We'll do fun things like have LLMs tell jokes and argue with each other. But fundamentally, my goal is to teach skills you can apply in business. I'll explain business implications as we go, and it's worth keeping this in mind: as you build experience with models and techniques, think of ways you could put this into action at work today. Please do contact me if you'd like to discuss more or if you have ideas to bounce off me.</span>
        </td>
    </tr>
</table>

### If necessary, install Cursor Extensions

1. From the View menu, select Extensions
2. Search for Python
3. Click on "Python" made by "ms-python" and select Install if not already installed
4. Search for Jupyter
5. Click on "Jupyter" made by "ms-toolsai" and select Install if not already installed


### Next Select the Kernel

Click on "Select Kernel" on the Top Right

Choose "Python Environments..."

Then choose the one that looks like `.venv (Python 3.12.x) .venv/bin/python` - it should be marked as "Recommended" and have a big star next to it.

Any problems with this? Head over to the troubleshooting.

### Note: you'll need to set the Kernel with every notebook..

```python
# imports

import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI

# If you get an error running this cell, then please head over to the troubleshooting notebook!
```

# Connecting to Gemini (via Google AI API)

The next cell is where we load in the environment variables in your `.env` file and connect to Gemini.

We are using Google's cheapest model: **gemini-flash-lite-latest** via Google's OpenAI-compatible endpoint.

## Troubleshooting if you have problems:

If you get a "Name Error" - have you run all cells from the top down? Head over to the Python Foundations guide for a bulletproof way to find and fix all Name Errors.

If that doesn't fix it, head over to the [troubleshooting](../setup/troubleshooting.ipynb) notebook for step by step code to identify the root cause and fix it!

Or, contact me! Message me or email ed@edwarddonner.com and we will get this to work.

```python
# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('GOOGLE_API_KEY')

# Check the key

if not api_key:
    print("No GOOGLE_API_KEY was found in .env - please add it to your .env file!")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them")
else:
    print("Google API key found and looks good!")
```

**Cell Output:**
```text
Google API key found and looks good!
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Models have been updated since the video</h2>
            <span style="color:#900;">AI companies retire their older models every few months, so some of the models in this lab are newer than the ones you'll see in the video, and your results will look a bit different from mine. If a model in this course ever stops working, please pick a similar model from that company's latest line-up.</span>
        </td>
    </tr>
</table>

# Let's make a quick call to a Frontier model to get started, as a preview!

```python
# To give you a preview -- calling Gemini with these messages is this easy.

message = "Hello, Gemini! This is my first ever message to you! Hi!"

messages = [{"role": "user", "content": message}]

messages
```

**Cell Output:**
```text
[{'role': 'user',
  'content': 'Hello, Gemini! This is my first ever message to you! Hi!'}]
```

```python
# Connect to Gemini using Google's OpenAI-compatible endpoint
gemini = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
openai = gemini  # Alias for compatibility

# Cheapest Gemini model
MODEL = "gemini-flash-lite-latest"

response = gemini.chat.completions.create(model=MODEL, messages=messages)
response.choices[0].message.content
```

**Cell Output:**
```text
"Hello and welcome! 👋 \n\nI'm so glad you reached out. How are you doing today, and how can I help you with your very first message?"
```

## OK onwards with our first project

```python
# Let's try out this utility

ed = fetch_website_contents("https://edwarddonner.com")
print(ed)
```

**Cell Output:**
```text
Home - Edward Donner

Skip to content
Avatar
Curriculum
Proficiency
C4
Outsmart
An arena that pits LLMs against each other in a battle of diplomacy and deviousness
About
Posts
Well, hi there.
I’m Ed. I like writing code and experimenting with LLMs, and hopefully you’re here because you do too. I also enjoy amateur electronic music production (
very
amateur) and losing myself in
Hacker News
, nodding my head sagely to things I only half understand.
I’m the co-founder and CTO of AI startup
Nebula.io
. I was previously founder and CEO of AI startup untapt,
acquired in 2021
, and a Managing Director at JPMorgan.
I will happily drone on for hours about LLMs to anyone in my vicinity. My friends got fed up with my impromptu lectures, and convinced me to make some Udemy courses. To my total joy (and shock) they’ve become best-selling, top-rated courses, with over a million enrollments across 194 countries. The
full curriculum is here
. If you’re visiting from one of my courses – I’m super grateful!
For more on me and my courses, please
chat with me and my Digital Avatar here
.
October 14, 2026
AI FDE: The Forward Deployed Engineer & Agentic AI Architect
February 17, 2026
AI Coder: Vibe Coder to Agentic Engineer – RESOURCES
January 4, 2026
AI Builder with n8n – Create Agents and Voice Agents – RESOURCES
September 15, 2025
AI Engineering MLOps Track – Deploy AI to Production – RESOURCES
Navigation
Avatar
Curriculum
Proficiency
C4
Outsmart
An arena that pits LLMs against each other in a battle of diplomacy and deviousness
About
Posts
Get in touch
ed [at] edwarddonner [dot] com
www.edwarddonner.com
Follow me
LinkedIn
Twitter
Facebook
```

## Types of prompts

You may know this already - but if not, you will get very familiar with it!

Models like GPT have been trained to receive instructions in a particular way.

They expect to receive:

**A system prompt** that tells them what task they are performing and what tone they should use

**A user prompt** -- the conversation starter that they should reply to

```python
# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""
```

```python
# Define our user prompt

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""
```

## Messages

The API from OpenAI expects to receive messages in a particular structure.
Many of the other APIs share this structure:

```python
[
    {"role": "system", "content": "system message goes here"},
    {"role": "user", "content": "user message goes here"}
]
```
To give you a preview, the next 2 cells make a rather simple call - we won't stretch the mighty GPT (yet!)

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is 2 + 2?"}
]

response = gemini.chat.completions.create(model=MODEL, messages=messages)
response.choices[0].message.content
```

**Cell Output:**
```text
'2 + 2 = 4.'
```

## And now let's build useful messages for Gemini Flash-Lite, using a function

```python
# See how this function creates exactly the format above

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]
```

```python
# Try this out, and then try for a few more websites

messages_for(ed)
```

**Cell Output:**
```text
[{'role': 'system',
  'content': '\nYou are a snarky assistant that analyzes the contents of a website,\nand provides a short, snarky, humorous summary, ignoring text that might be navigation related.\nRespond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.\n'},
 {'role': 'user',
  'content': '\nHere are the contents of a website.\nProvide a short summary of this website.\nIf it includes news or announcements, then summarize these too.\n\nHome - Edward Donner\n\nSkip to content\nAvatar\nCurriculum\nProficiency\nC4\nOutsmart\nAn arena that pits LLMs against each other in a battle of diplomacy and deviousness\nAbout\nPosts\nWell, hi there.\nI’m Ed. I like writing code and experimenting with LLMs, and hopefully you’re here because you do too. I also enjoy amateur electronic music production (\nvery\namateur) and losing myself in\nHacker News\n, nodding my head sagely to things I only half understand.\nI’m the co-founder and CTO of AI startup\nNebula.io\n. I was previously founder and CEO of AI startup untapt,\nacquired in 2021\n, and a Managing Director at JPMorgan.\nI will happily drone on for hours about LLMs to anyone in my vicinity. My friends got fed up with my impromptu lectures, and convinced me to make some Udemy courses. To my total joy (and shock) they’ve become best-selling, top-rated courses, with over a million enrollments across 194 countries. The\nfull curriculum is here\n. If you’re visiting from one of my courses – I’m super grateful!\nFor more on me and my courses, please\nchat with me and my Digital Avatar here\n.\nOctober 14, 2026\nAI FDE: The Forward Deployed Engineer & Agentic AI Architect\nFebruary 17, 2026\nAI Coder: Vibe Coder to Agentic Engineer – RESOURCES\nJanuary 4, 2026\nAI Builder with n8n – Create Agents and Voice Agents – RESOURCES\nSeptember 15, 2025\nAI Engineering MLOps Track – Deploy AI to Production – RESOURCES\nNavigation\nAvatar\nCurriculum\nProficiency\nC4\nOutsmart\nAn arena that pits LLMs against each other in a battle of diplomacy and deviousness\nAbout\nPosts\nGet in touch\ned [at] edwarddonner [dot] com\nwww.edwarddonner.com\nFollow me\nLinkedIn\nTwitter\nFacebook'}]
```

## Time to bring it together - the API for Gemini is very simple!

```python
# And now: call the Gemini API. You will get very familiar with this!

def summarize(url):
    website = fetch_website_contents(url)
    response = gemini.chat.completions.create(
        model = MODEL,
        messages = messages_for(website)
    )
    return response.choices[0].message.content
```

```python
summarize("https://edwarddonner.com")
```

**Cell Output:**
```text
"### Welcome to Ed’s Corner of the Internet\n\nThis is the digital shrine of Edward Donner: startup founder, ex-Wall Street bigwig, and a man whose friends were so thoroughly sick of his unprompted AI rants that they forced him to make Udemy courses just to get some peace and quiet. Miraculously, over a million people actually signed up. Now he spends his time pretending to scroll Hacker News wisely, building AI agents, and hosting digital clone chats so you don't even have to talk to the real Ed. \n\n### Latest Dispatches from the AI Hype Train\n* **October 2026:** *AI FDE: The Forward Deployed Engineer & Agentic AI Architect* — Because normal software engineering titles aren't buzzword-heavy enough yet.\n* **February 2026:** *AI Coder: Vibe Coder to Agentic Engineer – RESOURCES* — For when you want to vibe your way into writing production code.\n* **January 2026:** *AI Builder with n8n – Create Agents and Voice Agents – RESOURCES* — Build more annoying voice bots to call people about their car's extended warranty.\n* **September 2025:** *AI Engineering MLOps Track – Deploy AI to Production – RESOURCES* — How to take your chaotic AI experiments and successfully break them in front of real users."
```

```python
# A function to display this nicely in the output, using markdown

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))
```

```python
display_summary("https://edwarddonner.com")
```

**Cell Output:**
```text
<IPython.core.display.Markdown object>
```

# Let's try more websites

Note that this will only work on websites that can be scraped using this simplistic approach.

Websites that are rendered with Javascript, like React apps, won't show up. See the community-contributions folder for a Selenium implementation that gets around this. You'll need to read up on installing Selenium (ask ChatGPT!)

Also Websites protected with CloudFront (and similar) may give 403 errors - many thanks Andy J for pointing this out.

But many websites will work just fine!

```python
display_summary("https://cnn.com")
```

**Cell Output:**
```text
<IPython.core.display.Markdown object>
```

```python
display_summary("https://anthropic.com")
```

**Cell Output:**
```text
<IPython.core.display.Markdown object>
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business applications</h2>
            <span style="color:#181;">In this exercise, you experienced calling the Cloud API of a Frontier Model (a leading model at the frontier of AI) for the first time. We will be using APIs like OpenAI at many stages in the course, in addition to building our own LLMs.

More specifically, we've applied this to Summarization - a classic Gen AI use case to make a summary. This can be applied to any business vertical - summarizing the news, summarizing financial performance, summarizing a resume in a cover letter - the applications are limitless. Consider how you could apply Summarization in your business, and try prototyping a solution.</span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Before you continue - now try yourself</h2>
            <span style="color:#900;">Use the cell below to make your own simple commercial example. Stick with the summarization use case for now. Here's an idea: write something that will take the contents of an email, and will suggest an appropriate short subject line for the email. That's the kind of feature that might be built into a commercial email tool.</span>
        </td>
    </tr>
</table>

```python
# Step 1: Create your prompts

system_prompt = "You are a helpful and polite assistant."
user_prompt = "How are you today and who are you"

# Step 2: Make the messages list

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# Step 3: Call Gemini
gemini = OpenAI(
    api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
openai = gemini  # Alias for compatibility

# Cheapest Gemini model
MODEL = "gemini-flash-lite-latest"

response = gemini.chat.completions.create(model=MODEL, messages=messages)

# Step 4: print the result
print(response.choices[0].message.content)
```

**Cell Output:**
```text
Hello! I'm doing very well today, thank you for asking. 

As for who I am, I am a large language model, trained by Google. Think of me as a virtual assistant here to help you answer questions, write things, solve problems, or just chat! 

How are you doing today? Is there anything I can help you with?
```

## An extra exercise for those who enjoy web scraping

You may notice that if you try `display_summary("https://openai.com")` - it doesn't work! That's because OpenAI has a fancy website that uses Javascript. There are many ways around this that some of you might be familiar with. For example, Selenium is a hugely popular framework that runs a browser behind the scenes, renders the page, and allows you to query it. If you have experience with Selenium, Playwright or a similar browser automation framework, then feel free to implement an alternative version of the scraping functions in `scraper.py` (or in a separate module) using one of these tools. In the community-contributions folder, you'll find examples contributed by other students, including a Selenium implementation (thank you!)

# Sharing your code

I'd love it if you share your code afterwards so I can share it with others! You'll notice that some students have already made changes (including a Selenium implementation) which you will find in the community-contributions folder. If you'd like add your changes to that folder, submit a Pull Request with your new versions in that folder and I'll merge your changes.

If you're not an expert with git (and I am not!) then I've given you complete instructions in the guides folder, guide 3, and pasting here:

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


---

<a id="file-week1-day2-ipynb"></a>
## File: `week1/day2.ipynb`

> **Path in repository:** `week1/day2.ipynb`

# Welcome to the Day 2 Lab!

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">Just before we get started --</h2>
            <span style="color:#f71;">I thought I'd take a second to point you at this page of useful resources for the course. This includes links to all the slides.<br/>
            <a href="https://edwarddonner.com/2024/11/13/llm-engineering-resources/">https://edwarddonner.com/2024/11/13/llm-engineering-resources/</a><br/>
            Please keep this bookmarked, and I'll continue to add more useful links there over time.
            </span>
        </td>
    </tr>
</table>

## First - let's talk about the Chat Completions API

1. The simplest way to call an LLM
2. It's called Chat Completions because it's saying: "here is a conversation, please predict what should come next"
3. The Chat Completions API was invented by OpenAI, but it's so popular that everybody uses it!

### We will start by calling Gemini (using Google's OpenAI-compatible endpoint) with its cheapest model: gemini-flash-lite-latest!

```python
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    print("No GOOGLE_API_KEY was found in .env - please add it to your .env file!")
elif not api_key.startswith(("AIz", "AQ.")):
    print("An API key was found, but it doesn't start with AIz or AQ.")
else:
    print("Google API key found and looks good so far!")
```

**Cell Output:**
```text
Google API key found and looks good so far!
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Models have been updated since the video</h2>
            <span style="color:#900;">AI companies retire their older models every few months, so some of the models in this lab are newer than the ones you'll see in the video, and your results will look a bit different from mine. If a model in this course ever stops working, please pick a similar model from that company's latest line-up.</span>
        </td>
    </tr>
</table>

## Do you know what an Endpoint is?

If not, please review the Technical Foundations guide in the guides folder

And, here is an endpoint that might interest you...

```python
import requests

headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

payload = {
    "model": "gemini-flash-lite-latest",
    "messages": [
        {"role": "user", "content": "Tell me a fun fact"}]
}

payload
```

**Cell Output:**
```text
{'model': 'gemini-flash-lite-latest',
 'messages': [{'role': 'user', 'content': 'Tell me a fun fact'}]}
```

```python
response = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
    headers=headers,
    json=payload
)

response.json()
```

**Cell Output:**
```text
{'choices': [{'finish_reason': 'stop',
   'index': 0,
   'message': {'content': 'Sea otters hold hands when they sleep so they don’t drift apart from each other. A group of holding-hands otters is called a "raft"!',
    'extra_content': {'google': {'thought_signature': 'EmAKXgFpFH0Thgc5NYq9bfc6/bBMTUtZzWtIw2FmEzvbiE6AiUqwzhQyCOUun60z7cAoT15l3pionad5KRmXF8TSYeVQiSGrSanGKbe0yCMYfUYP4Fmk24VD4770/J2/Xnw='}},
    'role': 'assistant'}}],
 'created': 1793951396,
 'id': 'pIbtaoKbI5SJvdIP-cjy-Qk',
 'model': 'gemini-flash-lite-latest',
 'object': 'chat.completion',
 'usage': {'completion_tokens': 33, 'prompt_tokens': 6, 'total_tokens': 39}}
```

```python
response.json()["choices"][0]["message"]["content"]
```

**Cell Output:**
```text
'Sea otters hold hands when they sleep so they don’t drift apart from each other. A group of holding-hands otters is called a "raft"!'
```

# What is the openai package?

It's known as a Python Client Library.

It's nothing more than a wrapper around making this exact call to the http endpoint.

It just allows you to work with nice Python code instead of messing around with janky json objects.

But that's it. It's open-source and lightweight. Some people think it contains OpenAI model code - it doesn't!

```python
# Create OpenAI client pointing to Gemini

from openai import OpenAI
gemini = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
# openai = gemini  # Alias for compatibility

response = gemini.chat.completions.create(model="gemini-flash-lite-latest", messages=[{"role": "user", "content": "Tell me a fun fact"}])

response.choices[0].message.content

# hello world what are you d
```

**Cell Output:**
```text
'Here is a fun fact for you:\n\n**Sea otters hold hands while they sleep.** \n\nThey do this so they don’t drift apart and get separated from each other in the current. A group of resting otters is actually called a "raft"!'
```

## And then this great thing happened:

OpenAI's Chat Completions API was so popular, that the other model providers created endpoints that are identical.

They are known as the "OpenAI Compatible Endpoints".

For example, google made one here: https://generativelanguage.googleapis.com/v1beta/openai/

And OpenAI decided to be kind: they said, hey, you can just use the same client library that we made for GPT. We'll allow you to specify a different endpoint URL and a different key, to use another provider.

So you can use:

```python
gemini = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key="AIz....")
gemini.chat.completions.create(...)
```

And to be clear - even though OpenAI is in the code, we're only using this lightweight python client library to call the endpoint - there's no OpenAI model involved here.

If you're confused, please review Guide 9 in the Guides folder!

And now let's try it!

## THIS IS OPTIONAL - but if you wish to try out Google Gemini, please visit:

https://aistudio.google.com/

And set up your API key at

https://aistudio.google.com/api-keys

And then add your key to the `.env` file, being sure to Save the .env file after you change it:

`GOOGLE_API_KEY=AIz...`

```python
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

load_dotenv(override=True)

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("No API key was found - please be sure to add your key to the .env file, and save the file! Or you can skip the next 2 cells if you don't want to use Gemini")
elif not google_api_key.startswith(("AIz", "AQ.")):
    print("An API key was found, but it doesn't start with AIz or AQ.")
else:
    print("API key found and looks good so far!")
```

```python
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

response = gemini.chat.completions.create(model="gemini-flash-lite-latest", messages=[{"role": "user", "content": "Tell me a fun fact"}])

response.choices[0].message.content
```

## And Ollama also gives an OpenAI compatible endpoint

...and it's on your local machine!

If the next cell doesn't print "Ollama is running" then please open a terminal and run `ollama serve`

```python
requests.get("http://localhost:11434").content
```

### Download llama3.2 from meta

Change this to llama3.2:1b if your computer is smaller.

Don't use llama3.3 or llama4! They are too big for your computer..

```python
!ollama pull llama3.2
```

**Cell Output:**
```text
11;?pulling manifest ⠋ pulling manifest ⠙ pulling manifest ⠹ pulling manifest ⠸ pulling manifest ⠼ pulling manifest ⠴ pulling manifest ⠦ pulling manifest ⠧ pulling manifest ⠇ pulling manifest ⠏ pulling manifest ⠋ pulling manifest ⠙ pulling manifest ⠹ pulling manifest ⠸ pulling manifest ⠼ pulling manifest ⠴ pulling manifest ⠦ pulling manifest ⠧ pulling manifest ⠇ pulling manifest ⠏ pulling manifest ⠋ pulling manifest ⠙ pulling manifest ⠹ pulling manifest ⠸ pulling manifest ⠼ pulling manifest ⠴ pulling manifest ⠦ pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏  83 KB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏  98 KB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 249 KB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 608 KB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 716 KB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 948 KB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 1.1 MB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 1.1 MB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 1.4 MB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 1.4 MB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 1.9 MB/2.0 GB                  pulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 2.7 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 2.9 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 3.0 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 3.3 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 3.4 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 3.4 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 4.1 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 4.2 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 4.3 MB/2.0 GB  2.4 MB/s  13m47spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 4.5 MB/2.0 GB  2.4 MB/s  13m46spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 5.7 MB/2.0 GB  2.6 MB/s  12m40spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 5.8 MB/2.0 GB  2.6 MB/s  12m40spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 5.8 MB/2.0 GB  2.6 MB/s  12m40spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 6.2 MB/2.0 GB  2.6 MB/s  12m39spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 6.4 MB/2.0 GB  2.6 MB/s  12m39spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 6.7 MB/2.0 GB  2.6 MB/s  12m39spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 6.8 MB/2.0 GB  2.6 MB/s  12m39spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 6.9 MB/2.0 GB  2.6 MB/s  12m39spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 7.4 MB/2.0 GB  2.6 MB/s  12m39spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 7.9 MB/2.0 GB  2.6 MB/s  12m39spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 8.1 MB/2.0 GB  2.7 MB/s  12m32spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 8.1 MB/2.0 GB  2.7 MB/s  12m32spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 8.4 MB/2.0 GB  2.7 MB/s  12m32spulling manifest 
pulling dde5aa3fc5ff:   0% ▕                  ▏ 8.7 MB/2.0 GB  2.7 MB/s  12m32spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  10 MB/2.0 GB  2.7 MB/s  12m31spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  11 MB/2.0 GB  2.7 MB/s  12m31spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  11 MB/2.0 GB  2.7 MB/s  12m31spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  11 MB/2.0 GB  2.7 MB/s  12m31spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  2.7 MB/s  12m30spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  2.7 MB/s  12m30spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  3.1 MB/s  10m48spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  3.1 MB/s  10m48spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  3.1 MB/s  10m48spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  3.1 MB/s  10m48spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  3.1 MB/s  10m48spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  12 MB/2.0 GB  3.1 MB/s  10m48spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  15 MB/2.0 GB  3.1 MB/s  10m47spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  16 MB/2.0 GB  3.1 MB/s  10m47spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  16 MB/2.0 GB  3.1 MB/s  10m47spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  16 MB/2.0 GB  3.1 MB/s  10m47spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  16 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  16 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  18 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  18 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  18 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  18 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  19 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  19 MB/2.0 GB  3.3 MB/s   9m57spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  19 MB/2.0 GB  3.3 MB/s   9m56spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  20 MB/2.0 GB  3.3 MB/s   9m56spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  20 MB/2.0 GB  3.3 MB/s   9m56spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  20 MB/2.0 GB  3.4 MB/s   9m44spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  21 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  21 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  22 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  22 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  22 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  23 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  23 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  23 MB/2.0 GB  3.4 MB/s   9m43spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  25 MB/2.0 GB  3.4 MB/s   9m42spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  25 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  25 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  25 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  25 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  26 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  26 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  26 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  27 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  27 MB/2.0 GB  3.7 MB/s    9m3spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  28 MB/2.0 GB  3.7 MB/s    9m2spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  28 MB/2.0 GB  3.5 MB/s   9m28spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  28 MB/2.0 GB  3.5 MB/s   9m28spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  28 MB/2.0 GB  3.5 MB/s   9m28spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  28 MB/2.0 GB  3.5 MB/s   9m28spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  28 MB/2.0 GB  3.5 MB/s   9m28spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  29 MB/2.0 GB  3.5 MB/s   9m28spulling manifest 
pulling dde5aa3fc5ff:   1% ▕                  ▏  29 MB/2.0 GB  3.5 MB/s   9m27spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  30 MB/2.0 GB  3.5 MB/s   9m27spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  30 MB/2.0 GB  3.5 MB/s   9m27spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  30 MB/2.0 GB  3.5 MB/s   9m27spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  30 MB/2.0 GB  3.4 MB/s   9m45spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  31 MB/2.0 GB  3.4 MB/s   9m45spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  32 MB/2.0 GB  3.4 MB/s   9m45spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  32 MB/2.0 GB  3.4 MB/s   9m45spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  32 MB/2.0 GB  3.4 MB/s   9m45spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  32 MB/2.0 GB  3.4 MB/s   9m45spulling manifest 
pulling dde5aa3fc5ff:   2% ▕                  ▏  33 MB/2.0 GB  3.4 MB/s   9m45spulling manifest 

... [Output truncated: 5598 more lines] ...
```

```python
OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(base_url=OLLAMA_BASE_URL)
```

```python
# Get a fun fact

response = ollama.chat.completions.create(model="llama3.2", messages=[{"role": "user", "content": "Tell me a fun fact"}])

print(response.choices[0].message.content)
```

**Cell Output:**
```text
Here's a fun fact:

Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible. Honey's unique composition, with its low water content and high acidity, makes it a preservative that can survive for eternity. Isn't that sweet?
```

```python
# Now let's try deepseek-r1:1.5b - this is DeepSeek "distilled" into Qwen from Alibaba Cloud

!ollama pull deepseek-r1:1.5b
```

**Cell Output:**
```text
11;?pulling manifest ⠋ pulling manifest ⠙ pulling manifest ⠹ pulling manifest ⠸ pulling manifest ⠼ pulling manifest ⠴ pulling manifest ⠦ pulling manifest ⠧ pulling manifest ⠇ pulling manifest ⠏ pulling manifest ⠋ pulling manifest ⠙ pulling manifest ⠹ pulling manifest ⠸ pulling manifest ⠼ pulling manifest ⠴ pulling manifest ⠦ pulling manifest ⠧ pulling manifest ⠇ pulling manifest ⠏ pulling manifest ⠋ pulling manifest ⠙ pulling manifest ⠹ pulling manifest ⠸ pulling manifest ⠼ pulling manifest ⠴ pulling manifest ⠦ pulling manifest ⠧ pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 258 KB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 531 KB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 612 KB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 1.0 MB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 1.4 MB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 1.6 MB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 2.7 MB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 2.8 MB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 2.8 MB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 2.9 MB/1.1 GB                  pulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 4.1 MB/1.1 GB  4.0 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 4.1 MB/1.1 GB  4.0 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 4.7 MB/1.1 GB  4.0 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 4.7 MB/1.1 GB  4.0 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 5.1 MB/1.1 GB  4.0 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   0% ▕                  ▏ 5.6 MB/1.1 GB  4.0 MB/s   4m37spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 5.8 MB/1.1 GB  4.0 MB/s   4m37spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 5.8 MB/1.1 GB  4.0 MB/s   4m37spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 6.0 MB/1.1 GB  4.0 MB/s   4m37spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 7.5 MB/1.1 GB  4.0 MB/s   4m37spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 7.7 MB/1.1 GB  3.8 MB/s   4m49spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 7.8 MB/1.1 GB  3.8 MB/s   4m49spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 8.2 MB/1.1 GB  3.8 MB/s   4m49spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 8.5 MB/1.1 GB  3.8 MB/s   4m49spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 8.9 MB/1.1 GB  3.8 MB/s   4m49spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 9.3 MB/1.1 GB  3.8 MB/s   4m49spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏ 9.5 MB/1.1 GB  3.8 MB/s   4m49spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  10 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  10 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  10 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  11 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  11 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  12 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  12 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  13 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  13 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  14 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  14 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  14 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  14 MB/1.1 GB  3.8 MB/s   4m48spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  16 MB/1.1 GB  4.0 MB/s   4m34spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  16 MB/1.1 GB  4.0 MB/s   4m34spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  16 MB/1.1 GB  4.0 MB/s   4m34spulling manifest 
pulling aabd4debf0c8:   1% ▕                  ▏  16 MB/1.1 GB  4.0 MB/s   4m34spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  17 MB/1.1 GB  4.0 MB/s   4m33spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  17 MB/1.1 GB  4.0 MB/s   4m33spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  18 MB/1.1 GB  4.0 MB/s   4m33spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  18 MB/1.1 GB  4.0 MB/s   4m33spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  19 MB/1.1 GB  4.0 MB/s   4m33spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  19 MB/1.1 GB  4.0 MB/s   4m33spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  19 MB/1.1 GB  4.0 MB/s   4m33spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  19 MB/1.1 GB  3.9 MB/s   4m39spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  20 MB/1.1 GB  3.9 MB/s   4m39spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  21 MB/1.1 GB  3.9 MB/s   4m39spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  21 MB/1.1 GB  3.9 MB/s   4m39spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  22 MB/1.1 GB  3.9 MB/s   4m39spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  22 MB/1.1 GB  3.9 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  23 MB/1.1 GB  3.9 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  23 MB/1.1 GB  3.9 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  23 MB/1.1 GB  3.9 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  23 MB/1.1 GB  3.9 MB/s   4m38spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  24 MB/1.1 GB  4.0 MB/s   4m32spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  25 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  25 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  26 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  26 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  26 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  27 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   2% ▕                  ▏  27 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  28 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  28 MB/1.1 GB  4.0 MB/s   4m31spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  28 MB/1.1 GB  4.1 MB/s   4m26spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  29 MB/1.1 GB  4.1 MB/s   4m26spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  29 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  30 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  30 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  31 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  31 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  32 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  32 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  32 MB/1.1 GB  4.1 MB/s   4m25spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  33 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  33 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  34 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  34 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  35 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  35 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  36 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  36 MB/1.1 GB  4.1 MB/s   4m22spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  36 MB/1.1 GB  4.1 MB/s   4m21spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  37 MB/1.1 GB  4.1 MB/s   4m21spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  37 MB/1.1 GB  4.1 MB/s   4m20spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  37 MB/1.1 GB  4.1 MB/s   4m20spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  37 MB/1.1 GB  4.1 MB/s   4m20spulling manifest 
pulling aabd4debf0c8:   3% ▕                  ▏  39 MB/1.1 GB  4.1 MB/s   4m20spulling manifest 
pulling aabd4debf0c8:   4% ▕                  ▏  39 MB/1.1 GB  4.1 MB/s   4m20spulling manifest 
pulling aabd4debf0c8:   4% ▕                  ▏  39 MB/1.1 GB  4.1 MB/s   4m20spulling manifest 
pulling aabd4debf0c8:   4% ▕                  ▏  39 MB/1.1 GB  4.1 MB/s   4m19spulling manifest 
pulling aabd4debf0c8:   4% ▕                  ▏  40 MB/1.1 GB  4.1 MB/s   4m19spulling manifest 

... [Output truncated: 2815 more lines] ...
```

```python
response = ollama.chat.completions.create(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": "Tell me a fun fact"}])

response.choices[0].message.content
```

# HOMEWORK EXERCISE ASSIGNMENT

Upgrade the day 1 project to summarize a webpage to use an Open Source model running locally via Ollama rather than OpenAI

You'll be able to use this technique for all subsequent projects if you'd prefer not to use paid APIs.

**Benefits:**
1. No API charges - open-source
2. Data doesn't leave your box

**Disadvantages:**
1. Significantly less power than Frontier Model

## Recap on installation of Ollama

Simply visit [ollama.com](https://ollama.com) and install!

Once complete, the ollama server should already be running locally.  
If you visit:  
[http://localhost:11434/](http://localhost:11434/)

You should see the message `Ollama is running`.  

If not, bring up a new Terminal (Mac) or Powershell (Windows) and enter `ollama serve`  
And in another Terminal (Mac) or Powershell (Windows), enter `ollama pull llama3.2`  
Then try [http://localhost:11434/](http://localhost:11434/) again.

If Ollama is slow on your machine, try using `llama3.2:1b` as an alternative. Run `ollama pull llama3.2:1b` from a Terminal or Powershell, and change the code from `MODEL = "llama3.2"` to `MODEL = "llama3.2:1b"`


---

<a id="file-week1-day4-ipynb"></a>
## File: `week1/day4.ipynb`

> **Path in repository:** `week1/day4.ipynb`

# Day 4

## Tokenizing with code

```python
import tiktoken

# gpt-6-luna isn't in tiktoken yet, so we use the encoding of recent OpenAI models
encoding = tiktoken.get_encoding("o200k_base")

tokens = encoding.encode("Hi my name is Ed and I like banoffee pie")
```

```python
tokens
```

```python
for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id} = {token_text}")
```

```python
encoding.decode([326])
```

# And another topic!

### The Illusion of "memory"

Many of you will know this already. But for those that don't -- this might be an "AHA" moment!

```python
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")
```

### You should be very comfortable with what the next cell is doing!

_I'm creating a new instance of the OpenAI Python Client library, a lightweight wrapper around making HTTP calls to an endpoint for calling the GPT LLM, or other LLM providers_

```python
from openai import OpenAI

openai = OpenAI()
```

### A message to OpenAI is a list of dicts

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm Ed!"}
    ]
```

```python
response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=messages)
response.choices[0].message.content
```

### OK let's now ask a follow-up question

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What's my name?"}
    ]
```

```python
response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=messages)
response.choices[0].message.content
```

### Wait, wha??

We just told you!

What's going on??

Here's the thing: every call to an LLM is completely STATELESS. It's a totally new call, every single time. As AI engineers, it's OUR JOB to devise techniques to give the impression that the LLM has a "memory".

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm Ed!"},
    {"role": "assistant", "content": "Hi Ed! How can I assist you today?"},
    {"role": "user", "content": "What's my name?"}
    ]
```

```python
response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=messages)
response.choices[0].message.content
```

## To recap

With apologies if this is obvious to you - but it's still good to reinforce:

1. Every call to an LLM is stateless
2. We pass in the entire conversation so far in the input prompt, every time
3. This gives the illusion that the LLM has memory - it apparently keeps the context of the conversation
4. But this is a trick; it's a by-product of providing the entire conversation, every time
5. An LLM just predicts the most likely next tokens in the sequence; if that sequence contains "My name is Ed" and later "What's my name?" then it will predict.. Ed!

The ChatGPT product uses exactly this trick - every time you send a message, it's the entire conversation that gets passed in.

"Does that mean we have to pay extra each time for all the conversation so far"

For sure it does. And that's what we WANT. We want the LLM to predict the next tokens in the sequence, looking back on the entire conversation. We want that compute to happen, so we need to pay the electricity bill for it!


---

<a id="file-week1-day5-ipynb"></a>
## File: `week1/day5.ipynb`

> **Path in repository:** `week1/day5.ipynb`

# A full business solution

## Now we will take our project from Day 1 to the next level

### BUSINESS CHALLENGE:

Create a product that builds a Brochure for a company to be used for prospective clients, investors and potential recruits.

We will be provided a company name and their primary website.

See the end of this notebook for examples of real-world business applications.

And remember: I'm always available if you have problems or ideas! Please do reach out.

```python
# imports
# If these fail, please check you're running from an 'activated' environment with (llms) in the command prompt

import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI
```

```python
# Initialize and constants

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
    
MODEL = 'gpt-6-luna'
openai = OpenAI()
```

```python
links = fetch_website_links("https://edwarddonner.com")
links
```

## First step: Have GPT-6 Luna figure out which links are relevant

### Use a call to GPT-6 Luna to read the links on a webpage, and respond in structured JSON.  
It should decide which links are relevant, and replace relative links such as "/about" with "https://company.com/about".  
We will use "one shot prompting" in which we provide an example of how it should respond in the prompt.

This is an excellent use case for an LLM, because it requires nuanced understanding. Imagine trying to code this without LLMs by parsing and analyzing the webpage - it would be very hard!

Sidenote: there is a more advanced technique called "Structured Outputs" in which we require the model to respond according to a spec. We cover this technique in Week 8 during our autonomous Agentic AI project.

```python
link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""
```

```python
def get_links_user_prompt(url):
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt
```

```python
print(get_links_user_prompt("https://edwarddonner.com"))
```

```python
def select_relevant_links(url):
    response = openai.chat.completions.create(
        model=MODEL,
        reasoning_effort="none",
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(url)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    links = json.loads(result)
    return links
```

```python
select_relevant_links("https://edwarddonner.com")
```

```python
def select_relevant_links(url):
    print(f"Selecting relevant links for {url} by calling {MODEL}")
    response = openai.chat.completions.create(
        model=MODEL,
        reasoning_effort="none",
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(url)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    links = json.loads(result)
    print(f"Found {len(links['links'])} relevant links")
    return links
```

```python
select_relevant_links("https://edwarddonner.com")
```

```python
select_relevant_links("https://huggingface.co")
```

## Second step: make the brochure!

Assemble all the details into another prompt to GPT-6 Luna

```python
def fetch_page_and_all_relevant_links(url):
    contents = fetch_website_contents(url)
    relevant_links = select_relevant_links(url)
    result = f"## Landing Page:\n\n{contents}\n## Relevant Links:\n"
    for link in relevant_links['links']:
        result += f"\n\n### Link: {link['type']}\n"
        result += fetch_website_contents(link["url"])
    return result
```

```python
print(fetch_page_and_all_relevant_links("https://huggingface.co"))
```

```python
brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""

# Or uncomment the lines below for a more humorous brochure - this demonstrates how easy it is to incorporate 'tone':

# brochure_system_prompt = """
# You are an assistant that analyzes the contents of several relevant pages from a company website
# and creates a short, humorous, entertaining, witty brochure about the company for prospective customers, investors and recruits.
# Respond in markdown without code blocks.
# Include details of company culture, customers and careers/jobs if you have the information.
# """
```

```python
def get_brochure_user_prompt(company_name, url):
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
"""
    user_prompt += fetch_page_and_all_relevant_links(url)
    user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
    return user_prompt
```

```python
get_brochure_user_prompt("HuggingFace", "https://huggingface.co")
```

```python
def create_brochure(company_name, url):
    response = openai.chat.completions.create(
        model="gpt-6-luna",
        reasoning_effort="none",
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
    )
    result = response.choices[0].message.content
    display(Markdown(result))
```

```python
create_brochure("HuggingFace", "https://huggingface.co")
```

## Finally - a minor improvement

With a small adjustment, we can change this so that the results stream back from OpenAI,
with the familiar typewriter animation

```python
def stream_brochure(company_name, url):
    stream = openai.chat.completions.create(
        model="gpt-6-luna",
        reasoning_effort="none",
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
          ],
        stream=True
    )    
    response = ""
    display_handle = display(Markdown(""), display_id=True)
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        update_display(Markdown(response), display_id=display_handle.display_id)
```

```python
stream_brochure("HuggingFace", "https://huggingface.co")
```

```python
# Try changing the system prompt to the humorous version when you make the Brochure for Hugging Face:

stream_brochure("HuggingFace", "https://huggingface.co")
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business applications</h2>
            <span style="color:#181;">In this exercise we extended the Day 1 code to make multiple LLM calls, and generate a document.

This is perhaps the first example of Agentic AI design patterns, as we combined multiple calls to LLMs. This will feature more in Week 2, and then we will return to Agentic AI in a big way in Week 8 when we build a fully autonomous Agent solution.

Generating content in this way is one of the very most common Use Cases. As with summarization, this can be applied to any business vertical. Write marketing content, generate a product tutorial from a spec, create personalized email content, and so much more. Explore how you can apply content generation to your business, and try making yourself a proof-of-concept prototype. See what other students have done in the community-contributions folder -- so many valuable projects -- it's wild!</span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Before you move to Week 2 (which is tons of fun)</h2>
            <span style="color:#900;">Please see the week1 EXERCISE notebook for your challenge for the end of week 1. This will give you some essential practice working with Frontier APIs, and prepare you well for Week 2.</span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">A reminder on 3 useful resources</h2>
            <span style="color:#f71;">1. The resources for the course are available <a href="https://edwarddonner.com/2024/11/13/llm-engineering-resources/">here.</a><br/>
            2. I'm on LinkedIn <a href="https://www.linkedin.com/in/eddonner/">here</a> and I love connecting with people taking the course!<br/>
            3. I'm trying out X/Twitter and I'm at <a href="https://x.com/edwarddonner">@edwarddonner<a> and hoping people will teach me how it's done..  
            </span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/thankyou.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#090;">Finally! I have a special request for you</h2>
            <span style="color:#090;">
                My editor tells me that it makes a MASSIVE difference when students rate this course on Udemy - it's one of the main ways that Udemy decides whether to show it to others. If you're able to take a minute to rate this, I'd be so very grateful! And regardless - always please reach out to me at ed@edwarddonner.com if I can help at any point.
            </span>
        </td>
    </tr>
</table>


---

<a id="file-week1-scraper-py"></a>
## File: `week1/scraper.py`

> **Path in repository:** `week1/scraper.py`

```python
from bs4 import BeautifulSoup
import requests


# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]


def fetch_website_links(url):
    """
    Return the links on the webiste at the given url
    I realize this is inefficient as we're parsing twice! This is to keep the code in the lab simple.
    Feel free to use a class and optimize it!
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]
```


---

<a id="file-week1-solution-py"></a>
## File: `week1/solution.py`

> **Path in repository:** `week1/solution.py`

```python
"""
Website summarizer using Ollama instead of OpenAI.
"""

from openai import OpenAI
from scraper import fetch_website_contents

OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.2"

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""


def messages_for(website):
    """Create message list for the LLM."""
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]


def summarize(url):
    """Fetch and summarize a website using Ollama."""
    ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')
    website = fetch_website_contents(url)
    response = ollama.chat.completions.create(
        model=MODEL,
        messages=messages_for(website)
    )
    return response.choices[0].message.content


def main():
    """Main entry point for testing."""
    url = input("Enter a URL to summarize: ")
    print("\nFetching and summarizing...\n")
    summary = summarize(url)
    print(summary)


if __name__ == "__main__":
    main()
```


---

<a id="file-week1-solutions-day1-with-ollama-ipynb"></a>
## File: `week1/solutions/day1_with_ollama.ipynb`

> **Path in repository:** `week1/solutions/day1_with_ollama.ipynb`

# ALTERNATIVE DAY 1 WITH OLLAMA

### Please read this section. This is valuable to get you prepared, even if it's a long read -- it's important stuff.

## Your first Frontier LLM Project

Let's build a useful LLM solution - in a matter of minutes.

By the end of this course, you will have built an autonomous Agentic AI solution with 7 agents that collaborate to solve a business problem. All in good time! We will start with something smaller...

Our goal is to code a new kind of Web Browser. Give it a URL, and it will respond with a summary. The Reader's Digest of the internet!!

Before starting, you should have completed the setup linked in the [README](../../README.md).

## If you're new to Jupyter Lab

Welcome to the wonderful world of Data Science experimentation! Once you've used Jupyter Lab, you'll wonder how you ever lived without it. Simply click in each "cell" with code in it, such as the cell immediately below this text, and hit Shift+Return to execute that cell. As you wish, you can add a cell with the + button in the toolbar, and print values of variables, or try out variations.  

I've written a guide called [Notebooks in Cursor](../../guides/05_notebooks.ipynb) to help you get more familiar with notebooks, including adding Markdown comments, using `!` to run shell commands, and `tqdm` to show progress. All the guides are in the [Guides folder](../../guides/01_intro.ipynb).

## If you're new to the Command Line

Please see these excellent guides: [Command line on PC](https://chatgpt.com/share/67b0acea-ba38-8012-9c34-7a2541052665) and [Command line on Mac](https://chatgpt.com/canvas/shared/67b0b10c93a081918210723867525d2b).  

## If you'd prefer to work in IDEs

If you're more comfortable in IDEs like VSCode or Pycharm, they both work great with these lab notebooks too.  
If you'd prefer to work in VSCode, [here](https://chatgpt.com/share/676f2e19-c228-8012-9911-6ca42f8ed766) are instructions from an AI friend on how to configure it for the course.

## If you'd like to brush up your Python

I've added a notebook called [Intermediate Python](../../guides/10_intermediate_python.ipynb) to get you up to speed. But you should give it a miss if you already have a good idea what this code does:    
`yield from {book.get("author") for book in books if book.get("author")}`

## I am here to help

If you have any problems at all, please do reach out.  
I'm available through the platform, or at ed@edwarddonner.com, or at https://www.linkedin.com/in/eddonner/ if you'd like to connect (and I love connecting!)  
And this is new to me, but I'm also trying out X/Twitter at [@edwarddonner](https://x.com/edwarddonner) - if you're on X, please show me how it's done 😂  

## More troubleshooting

Please see the [troubleshooting](../../setup/troubleshooting.ipynb) notebook in the setup folder to diagnose and fix common problems. At the very end of it is a diagnostics script with some useful debug info.

## If this is old hat!

If you're already comfortable with today's material, please hang in there; you can move swiftly through the first few labs - we will get much more in depth as the weeks progress.

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Please read - important note</h2>
            <span style="color:#900;">The way I collaborate with you may be different to other courses you've taken. I prefer not to type code while you watch. Rather, I execute Jupyter Labs, like this, and give you an intuition for what's going on. My suggestion is that you carefully execute this yourself, <b>after</b> watching the lecture. Add print statements to understand what's going on, and then come up with your own variations. If you have a Github account, use this to showcase your variations. Not only is this essential practice, but it demonstrates your skills to others, including perhaps future clients or employers...</span>
        </td>
    </tr>
</table>
<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../../assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">Treat these labs as a resource</h2>
            <span style="color:#f71;">I push updates to the code regularly. When people ask questions or have problems, I incorporate it in the code, adding more examples or improved commentary. As a result, you'll notice that the code below isn't identical to the videos. Everything from the videos is here; but in addition, I've added more steps and better explanations, and occasionally added new models like DeepSeek. Consider this like an interactive book that accompanies the lectures.
            </span>
        </td>
    </tr>
</table>
<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business value of these exercises</h2>
            <span style="color:#181;">A final thought. While I've designed these notebooks to be educational, I've also tried to make them enjoyable. We'll do fun things like have LLMs tell jokes and argue with each other. But fundamentally, my goal is to teach skills you can apply in business. I'll explain business implications as we go, and it's worth keeping this in mind: as you build experience with models and techniques, think of ways you could put this into action at work today. Please do contact me if you'd like to discuss more or if you have ideas to bounce off me.</span>
        </td>
    </tr>
</table>

```python
# imports

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

# If you get an error running this cell, then please head over to the troubleshooting notebook!
```

# Connecting to OpenAI

The next cell is where we load in the environment variables in your `.env` file and connect to OpenAI.

## Troubleshooting if you have problems:

Head over to the [troubleshooting](../../setup/troubleshooting.ipynb) notebook in the setup folder for step by step code to identify the root cause and fix it!

If you make a change, try restarting the "Kernel" (the python process sitting behind this notebook) by Kernel menu >> Restart Kernel and Clear Outputs of All Cells. Then try this notebook again, starting at the top.

Or, contact me! Message me or email ed@edwarddonner.com and we will get this to work.

Any concerns about API costs? See my notes in the README - costs should be minimal, and you can control it at every point. You can also use Ollama as a free alternative, which we discuss during Day 2.

# And now the change for Ollama

1. No environment variables are needed (no keys) so this part has been removed

2. The OpenAI client library is being initialized to point to your local computer for Ollama

3. You need to have installed Ollama on your computer, and run `ollama run llama3.2` in a Powershell or Terminal if you haven't already

4. Anywhere in this lab that it used to have **gpt-4o-mini** it now has **llama3.2**

```python
# Here it is - see the base_url

openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
```

# Let's make a quick call to a Frontier model to get started, as a preview!

```python
# To give you a preview -- calling OpenAI with these messages is this easy. Any problems, head over to the Troubleshooting notebook.

message = "Hello, Llama! This is my first ever message to you! Hi!"
response = openai.chat.completions.create(model="llama3.2", messages=[{"role":"user", "content":message}])
print(response.choices[0].message.content)
```

## OK onwards with our first project

```python
# A class to represent a Webpage
# If you're not familiar with Classes, check out the "Intermediate Python" notebook

# Some websites need you to use proper headers when fetching them:
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
```

```python
# Let's try one out. Change the website and add print statements to follow along.

ed = Website("https://edwarddonner.com")
print(ed.title)
print(ed.text)
```

## Types of prompts

You may know this already - but if not, you will get very familiar with it!

Models like GPT4o have been trained to receive instructions in a particular way.

They expect to receive:

**A system prompt** that tells them what task they are performing and what tone they should use

**A user prompt** -- the conversation starter that they should reply to

```python
# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."
```

```python
# A function that writes a User Prompt that asks for summaries of websites:

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt
```

```python
print(user_prompt_for(ed))
```

## Messages

The API from OpenAI expects to receive messages in a particular structure.
Many of the other APIs share this structure:

```
[
    {"role": "system", "content": "system message goes here"},
    {"role": "user", "content": "user message goes here"}
]

To give you a preview, the next 2 cells make a rather simple call - we won't stretch the mighty GPT (yet!)

```python
messages = [
    {"role": "system", "content": "You are a snarky assistant"},
    {"role": "user", "content": "What is 2 + 2?"}
]
```

```python
# To give you a preview -- calling OpenAI with system and user messages:

response = openai.chat.completions.create(model="llama3.2", messages=messages)
print(response.choices[0].message.content)
```

## And now let's build useful messages for GPT-4o-mini, using a function

```python
# See how this function creates exactly the format above

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]
```

```python
# Try this out, and then try for a few more websites

messages_for(ed)
```

## Time to bring it together - the API for OpenAI is very simple!

```python
# And now: call the OpenAI API. You will get very familiar with this!

def summarize(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model = "llama3.2",
        messages = messages_for(website)
    )
    return response.choices[0].message.content
```

```python
summarize("https://edwarddonner.com")
```

```python
# A function to display this nicely in the Jupyter output, using markdown

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))
```

```python
display_summary("https://edwarddonner.com")
```

# Let's try more websites

Note that this will only work on websites that can be scraped using this simplistic approach.

Websites that are rendered with Javascript, like React apps, won't show up. See the community-contributions folder for a Selenium implementation that gets around this. You'll need to read up on installing Selenium (ask ChatGPT!)

Also Websites protected with CloudFront (and similar) may give 403 errors - many thanks Andy J for pointing this out.

But many websites will work just fine!

```python
display_summary("https://cnn.com")
```

```python
display_summary("https://anthropic.com")
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business applications</h2>
            <span style="color:#181;">In this exercise, you experienced calling the Cloud API of a Frontier Model (a leading model at the frontier of AI) for the first time. We will be using APIs like OpenAI at many stages in the course, in addition to building our own LLMs.

More specifically, we've applied this to Summarization - a classic Gen AI use case to make a summary. This can be applied to any business vertical - summarizing the news, summarizing financial performance, summarizing a resume in a cover letter - the applications are limitless. Consider how you could apply Summarization in your business, and try prototyping a solution.</span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Before you continue - now try yourself</h2>
            <span style="color:#900;">Use the cell below to make your own simple commercial example. Stick with the summarization use case for now. Here's an idea: write something that will take the contents of an email, and will suggest an appropriate short subject line for the email. That's the kind of feature that might be built into a commercial email tool.</span>
        </td>
    </tr>
</table>

```python
# Step 1: Create your prompts

system_prompt = "something here"
user_prompt = """
    Lots of text
    Can be pasted here
"""

# Step 2: Make the messages list

messages = [] # fill this in

# Step 3: Call OpenAI

response =

# Step 4: print the result

print(
```

## An extra exercise for those who enjoy web scraping

You may notice that if you try `display_summary("https://openai.com")` - it doesn't work! That's because OpenAI has a fancy website that uses Javascript. There are many ways around this that some of you might be familiar with. For example, Selenium is a hugely popular framework that runs a browser behind the scenes, renders the page, and allows you to query it. If you have experience with Selenium, Playwright or similar, then feel free to improve the Website class to use them. In the community-contributions folder, you'll find an example Selenium solution from a student (thank you!)

# Sharing your code

I'd love it if you share your code afterwards so I can share it with others! You'll notice that some students have already made changes (including a Selenium implementation) which you will find in the community-contributions folder. If you'd like add your changes to that folder, submit a Pull Request with your new versions in that folder and I'll merge your changes.

If you're not an expert with git (and I am not!) then I've given you complete instructions in the guides folder, guide 3, and pasting here:

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


---

<a id="file-week1-solutions-day2-solution-ipynb"></a>
## File: `week1/solutions/day2 SOLUTION.ipynb`

> **Path in repository:** `week1/solutions/day2 SOLUTION.ipynb`

# EXERCISE SOLUTION

Upgrade the day 1 project to summarize a webpage to use an Open Source model running locally via Ollama rather than OpenAI

You'll be able to use this technique for all subsequent projects if you'd prefer not to use paid APIs.

**Benefits:**
1. No API charges - open-source
2. Data doesn't leave your box

**Disadvantages:**
1. Significantly less power than Frontier Model

## Recap on installation of Ollama

Simply visit [ollama.com](https://ollama.com) and install!

Once complete, the ollama server should already be running locally.  
If you visit:  
[http://localhost:11434/](http://localhost:11434/)

You should see the message `Ollama is running`.  

If not, bring up a new Terminal (Mac) or Powershell (Windows) and enter `ollama serve`  
Then try [http://localhost:11434/](http://localhost:11434/) again.

```python
# imports

import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import ollama
```

```python
# Constants

MODEL = "llama3.2"
```

```python
# A class to represent a Webpage

class Website:
    """
    A utility class to represent a Website that we have scraped
    """
    url: str
    title: str
    text: str

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
```

```python
# Let's try one out

ed = Website("https://edwarddonner.com")
print(ed.title)
print(ed.text)
```

## Types of prompts

You may know this already - but if not, you will get very familiar with it!

Models like GPT4o have been trained to receive instructions in a particular way.

They expect to receive:

**A system prompt** that tells them what task they are performing and what tone they should use

**A user prompt** -- the conversation starter that they should reply to

```python
# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."
```

```python
# A function that writes a User Prompt that asks for summaries of websites:

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "The contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt
```

## Messages

The API from Ollama expects the same message format as OpenAI:

```
[
    {"role": "system", "content": "system message goes here"},
    {"role": "user", "content": "user message goes here"}
]

```python
# See how this function creates exactly the format above

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]
```

## Time to bring it together - now with Ollama instead of OpenAI

```python
# And now: call the Ollama function instead of OpenAI

def summarize(url):
    website = Website(url)
    messages = messages_for(website)
    response = ollama.chat(model=MODEL, messages=messages)
    return response['message']['content']
```

```python
summarize("https://edwarddonner.com")
```

```python
# A function to display this nicely in the Jupyter output, using markdown

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))
```

```python
display_summary("https://edwarddonner.com")
```

# Let's try more websites

Note that this will only work on websites that can be scraped using this simplistic approach.

Websites that are rendered with Javascript, like React apps, won't show up. See the community-contributions folder for a Selenium implementation that gets around this. You'll need to read up on installing Selenium (ask ChatGPT!)

Also Websites protected with CloudFront (and similar) may give 403 errors - many thanks Andy J for pointing this out.

But many websites will work just fine!

```python
display_summary("https://cnn.com")
```

```python
display_summary("https://anthropic.com")
```

# Sharing your code

I'd love it if you share your code afterwards so I can share it with others! You'll notice that some students have already made changes (including a Selenium implementation) which you will find in the community-contributions folder. If you'd like add your changes to that folder, submit a Pull Request with your new versions in that folder and I'll merge your changes.

If you're not an expert with git (and I am not!) then GPT has given some nice instructions on how to submit a Pull Request. It's a bit of an involved process, but once you've done it once it's pretty clear. As a pro-tip: it's best if you clear the outputs of your Jupyter notebooks (Edit >> Clean outputs of all cells, and then Save) for clean notebooks.

PR instructions courtesy of an AI friend: https://chatgpt.com/share/670145d5-e8a8-8012-8f93-39ee4e248b4c


---

<a id="file-week1-solutions-week1-solution-ipynb"></a>
## File: `week1/solutions/week1 SOLUTION.ipynb`

> **Path in repository:** `week1/solutions/week1 SOLUTION.ipynb`

# End of week 1 solution

To demonstrate your familiarity with OpenAI API, and also Ollama, build a tool that takes a technical question,  
and responds with an explanation. This is a tool that you will be able to use yourself during the course!

After week 2 you'll be able to add a User Interface to this tool, giving you a valuable application.

```python
# imports

from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import ollama
```

```python
# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'
```

```python
# set up environment

load_dotenv()
openai = OpenAI()
```

```python
# here is the question; type over this to ask something new

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""
```

```python
# prompts

system_prompt = "You are a helpful technical tutor who answers questions about python code, software engineering, data science and LLMs"
user_prompt = "Please give a detailed explanation to the following question: " + question
```

```python
# messages

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]
```

```python
# Get gpt-4o-mini to answer, with streaming

stream = openai.chat.completions.create(model=MODEL_GPT, messages=messages,stream=True)
    
response = ""
display_handle = display(Markdown(""), display_id=True)
for chunk in stream:
    response += chunk.choices[0].delta.content or ''
    response = response.replace("```","").replace("markdown", "")
    update_display(Markdown(response), display_id=display_handle.display_id)
```

```python
# Get Llama 3.2 to answer

response = ollama.chat(model=MODEL_LLAMA, messages=messages)
reply = response['message']['content']
display(Markdown(reply))
```

# Congratulations!

You could make it better by taking in the question using  
`my_question = input("Please enter your question:")`

And then creating the prompts and making the calls interactively.


---

<a id="file-week1-week1-exercise-ipynb"></a>
## File: `week1/week1 EXERCISE.ipynb`

> **Path in repository:** `week1/week1 EXERCISE.ipynb`

# End of week 1 exercise

To demonstrate your familiarity with OpenAI API, and also Ollama, build a tool that takes a technical question,  
and responds with an explanation. This is a tool that you will be able to use yourself during the course!

```python
# imports
```

```python
# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'
```

```python
# set up environment
```

```python
# here is the question; type over this to ask something new

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""
```

```python
# Get gpt-4o-mini to answer, with streaming
```

```python
# Get Llama 3.2 to answer
```


---
