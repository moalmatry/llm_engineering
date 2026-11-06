# day1.ipynb

> **Original Path:** `week1/day1.ipynb`

---

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
