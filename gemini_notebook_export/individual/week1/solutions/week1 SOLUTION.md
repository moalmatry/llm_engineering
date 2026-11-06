# week1 SOLUTION.ipynb

> **Original Path:** `week1/solutions/week1 SOLUTION.ipynb`

---

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
