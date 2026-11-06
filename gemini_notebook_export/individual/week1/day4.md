# day4.ipynb

> **Original Path:** `week1/day4.ipynb`

---

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
