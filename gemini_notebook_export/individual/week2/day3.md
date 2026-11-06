# day3.ipynb

> **Original Path:** `week2/day3.ipynb`

---

# Day 3 - Conversational AI - aka Chatbot!

```python
# imports

import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
```

```python
# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
```

```python
# Initialize

openai = OpenAI()
MODEL = 'gpt-6-luna'
```

```python
# Again, I'll be in scientist-mode and change this global during the lab

system_message = "You are a helpful assistant"
```

## And now, writing a new callback

We now need to write a function called:

`chat(message, history)`

Which will be a callback function we will give gradio.

### The job of this function

Take a message, take the prior conversation, and return the response.

```python
def chat(message, history):
    return "bananas"
```

```python
gr.ChatInterface(fn=chat, type="messages").launch()
```

```python
def chat(message, history):
    return f"You said {message} and the history is {history} but I still say bananas"
```

```python
gr.ChatInterface(fn=chat, type="messages").launch()
```

## OK! Let's write a slightly better chat callback!

```python
def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL, reasoning_effort="none", messages=messages)
    return response.choices[0].message.content
```

```python
gr.ChatInterface(fn=chat, type="messages").launch()
```

```python
def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    stream = openai.chat.completions.create(model=MODEL, reasoning_effort="none", messages=messages, stream=True)
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response
```

```python
gr.ChatInterface(fn=chat, type="messages").launch()
```

## OK let's keep going!

Using a system message to add context, and to give an example answer.. this is "one shot prompting" again

```python
system_message = "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get."
```

```python
gr.ChatInterface(fn=chat, type="messages").launch()
```

```python
system_message += "\nIf the customer asks for shoes, you should respond that shoes are not on sale today, \
but remind the customer to look at hats!"
```

```python
gr.ChatInterface(fn=chat, type="messages").launch()
```

```python
def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    relevant_system_message = system_message
    if 'belt' in message.lower():
        relevant_system_message += " The store does not sell belts; if you are asked for belts, be sure to point out other items on sale."
    
    messages = [{"role": "system", "content": relevant_system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, reasoning_effort="none", messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response
```

```python
gr.ChatInterface(fn=chat, type="messages").launch()
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business Applications</h2>
            <span style="color:#181;">Conversational Assistants are of course a hugely common use case for Gen AI, and the latest frontier models are remarkably good at nuanced conversation. And Gradio makes it easy to have a user interface. Another crucial skill we covered is how to use prompting to provide context, information and examples.
<br/><br/>
Consider how you could apply an AI Assistant to your business, and make yourself a prototype. Use the system prompt to give context on your business, and set the tone for the LLM.</span>
        </td>
    </tr>
</table>
