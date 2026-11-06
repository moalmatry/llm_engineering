# day2.ipynb

> **Original Path:** `week1/day2.ipynb`

---

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
