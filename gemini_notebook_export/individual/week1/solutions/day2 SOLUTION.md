# day2 SOLUTION.ipynb

> **Original Path:** `week1/solutions/day2 SOLUTION.ipynb`

---

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
