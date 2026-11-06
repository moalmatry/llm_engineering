# Week4 System Info and Styles

This unified reference file consolidates **5 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [week4/day3.ipynb](#file-week4-day3-ipynb)
- [week4/day4.ipynb](#file-week4-day4-ipynb)
- [week4/day5.ipynb](#file-week4-day5-ipynb)
- [week4/styles.py](#file-week4-styles-py)
- [week4/system_info.py](#file-week4-system-info-py)

---

<a id="file-week4-day3-ipynb"></a>
## File: `week4/day3.ipynb`

> **Path in repository:** `week4/day3.ipynb`

# Code Generator

The requirement: use a Frontier model to generate high performance C++ code from Python code

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">Reminder: fetch latest code</h2>
            <span style="color:#f71;">I'm continually improving these labs, adding more examples and exercises.
            At the start of each week, it's worth checking you have the latest code.<br/>
            First do a <a href="https://chatgpt.com/share/6734e705-3270-8012-a074-421661af6ba9">git pull and merge your changes as needed</a>. Any problems? Try asking ChatGPT to clarify how to merge - or contact me!<br/><br/>
            After you've pulled the code, from the llm_engineering directory, in a Cursor Terminal, run:<br/>
            <code>uv sync</code><br/>
            </span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h1 style="color:#900;">Important Note</h1>
            <span style="color:#900;">
            In this lab, I use high end models GPT-6.1 Sol, Claude Sonnet 5.5, Gemini 4 Argon, Grok 4.3, which are the slightly higher priced models. The costs are still low, but if you'd prefer to keep costs ultra low, please pick lower cost models like gpt-6-luna.
            </span>
        </td>
    </tr>
</table>

```python
# imports

import os
from dotenv import load_dotenv
from openai import OpenAI
import subprocess
from IPython.display import Markdown, display
```

```python
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if grok_api_key:
    print(f"Grok API Key exists and begins {grok_api_key[:4]}")
else:
    print("Grok API Key not set (and this is optional)")
```

```python
# Connect to client libraries

openai = OpenAI()

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
grok_url = "https://api.x.ai/v1"

anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
grok = OpenAI(api_key=grok_api_key, base_url=grok_url)
```

```python
OPENAI_MODEL = "gpt-6.1-sol"
CLAUDE_MODEL = "claude-sonnet-5-5"
GROK_MODEL = "grok-4.3"
GEMINI_MODEL = "gemini-4-argon"

# Want to keep costs ultra-low? Uncomment these lines:

# OPENAI_MODEL = "gpt-6-luna"
# CLAUDE_MODEL = "claude-haiku-4-5"
# GROK_MODEL = "grok-4-fast-non-reasoning"
# GEMINI_MODEL = "gemini-3.1-flash-lite"
```

## PLEASE NOTE:

We will be writing a solution to convert Python into efficient, optimized C++ code for your machine, which can be compiled to native machine code and executed.

It is not necessary for you to execute the code yourself - that's not the point of the exercise!

But if you would like to (because it's satisfying!) then I'm including the steps here. Very optional!

As an alternative, I'll also show you a website where you can run the C++ code.

```python
from system_info import retrieve_system_info

system_info = retrieve_system_info()
system_info
```

```python
message = f"""
Here is a report of the system information for my computer.
I want to run a C++ compiler to compile a single C++ file called main.cpp and then execute it in the simplest way possible.
Please reply with whether I need to install any C++ compiler to do this. If so, please provide the simplest step by step instructions to do so.

If I'm already set up to compile C++ code, then I'd like to run something like this in Python to compile and execute the code:
```python
compile_command = # something here - to achieve the fastest possible runtime performance
compile_result = subprocess.run(compile_command, check=True, text=True, capture_output=True)
run_command = # something here
run_result = subprocess.run(run_command, check=True, text=True, capture_output=True)
return run_result.stdout
```
Please tell me exactly what I should use for the compile_command and run_command.

System information:
{system_info}
"""

response = openai.chat.completions.create(model=OPENAI_MODEL, messages=[{"role": "user", "content": message}])
display(Markdown(response.choices[0].message.content))
```

## If you need to install something

If you would like to, please follow GPTs instructions! Then rerun the analysis afterwards (you might need to Restart the notebook) to confirm you're set.

You should now be equipped with the command to compile the code, and the command to run it!

Enter that in the cell below:

```python
compile_command = ["clang++", "-std=c++17", "-Ofast", "-mcpu=native", "-flto=thin", "-fvisibility=hidden", "-DNDEBUG", "main.cpp", "-o", "main"]
run_command = ["./main"]
```

## And now, on with the main task

```python
system_prompt = """
Your task is to convert Python code into high performance C++ code.
Respond only with C++ code. Do not provide any explanation other than occasional comments.
The C++ response needs to produce an identical output in the fastest possible time.
"""

def user_prompt_for(python):
    return f"""
Port this Python code to C++ with the fastest possible implementation that produces identical output in the least time.
The system information is:
{system_info}
Your response will be written to a file called main.cpp and then compiled and executed; the compilation command is:
{compile_command}
Respond only with C++ code.
Python code to port:

```python
{python}
```
"""
```

```python
def messages_for(python):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(python)}
    ]
```

```python
def write_output(cpp):
    with open("main.cpp", "w", encoding="utf-8") as f:
        f.write(cpp)
```

```python
def port(client, model, python):
    reasoning_effort = "high" if 'gpt' in model else None
    response = client.chat.completions.create(model=model, messages=messages_for(python), reasoning_effort=reasoning_effort)
    reply = response.choices[0].message.content
    reply = reply.replace('```cpp','').replace('```','')
    write_output(reply)
```

```python
pi = """
import time

def calculate(iterations, param1, param2):
    result = 1.0
    for i in range(1, iterations+1):
        j = i * param1 - param2
        result -= (1/j)
        j = i * param1 + param2
        result += (1/j)
    return result

start_time = time.time()
result = calculate(200_000_000, 4, 1) * 4
end_time = time.time()

print(f"Result: {result:.12f}")
print(f"Execution Time: {(end_time - start_time):.6f} seconds")
"""
```

```python
def run_python(code):
    globals = {"__builtins__": __builtins__}
    exec(code, globals)
```

```python
run_python(pi)
```

```python
port(openai, OPENAI_MODEL, pi)
```

# Compiling C++ and executing

This next cell contains the command to compile a C++ file based on the instructions from GPT.

Again, it's not crucial to do this step if you don't wish to!

OR alternatively: student Sandeep K.G. points out that you can run Python and C++ code online to test it out that way. Thank you Sandeep!  
> Not an exact comparison but you can still get the idea of performance difference.  
> For example here: https://www.programiz.com/cpp-programming/online-compiler/

```python
# Use the commands from GPT-6.1 Sol

def compile_and_run():
    subprocess.run(compile_command, check=True, text=True, capture_output=True)
    print(subprocess.run(run_command, check=True, text=True, capture_output=True).stdout)
    print(subprocess.run(run_command, check=True, text=True, capture_output=True).stdout)
    print(subprocess.run(run_command, check=True, text=True, capture_output=True).stdout)
```

```python
compile_and_run()
```

```python
19.178207/0.082168
```

## OK let's try the other contenders!

```python
port(anthropic, CLAUDE_MODEL, pi)
compile_and_run()
```

```python
port(grok, GROK_MODEL, pi)
compile_and_run()
```

```python
port(gemini, GEMINI_MODEL, pi)
compile_and_run()
```

```python
print(f"""
In Ed's experiments, the performance speedups were:

4th place: Claude Sonnet 4.5: {19.178207/0.104241:.0f}X speedup
3rd place: GPT-5: {19.178207/0.082168:.0f}X speedup
2nd place: Grok 4: {19.178207/0.018092:.0f}X speedup
1st place: Gemini 2.5 Pro: {19.178207/0.013314:.0f}X speedup
""")
```


---

<a id="file-week4-day4-ipynb"></a>
## File: `week4/day4.ipynb`

> **Path in repository:** `week4/day4.ipynb`

# Code Generator

The requirement: use a Frontier model to generate high performance C++ code from Python code

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">Reminder: OPTIONAL to execute C++ code</h2>
            <span style="color:#f71;">As an alternative, you can run it on the website given yesterday</span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h1 style="color:#900;">Important Note</h1>
            <span style="color:#900;">
            In this lab, I use free open source models on Ollama. I also use paid open-source models via Groq and OpenRouter. Only pick the models you want to!
            </span>
        </td>
    </tr>
</table>

```python
# imports

import os
import io
import sys
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import subprocess
```

```python
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if grok_api_key:
    print(f"Grok API Key exists and begins {grok_api_key[:4]}")
else:
    print("Grok API Key not set (and this is optional)")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:
    print("Groq API Key not set (and this is optional)")

if openrouter_api_key:
    print(f"OpenRouter API Key exists and begins {openrouter_api_key[:6]}")
else:
    print("OpenRouter API Key not set (and this is optional)")
```

```python
# Connect to client libraries

openai = OpenAI()

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
grok_url = "https://api.x.ai/v1"
groq_url = "https://api.groq.com/openai/v1"
ollama_url = "http://localhost:11434/v1"
openrouter_url = "https://openrouter.ai/api/v1"

anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
grok = OpenAI(api_key=grok_api_key, base_url=grok_url)
groq = OpenAI(api_key=groq_api_key, base_url=groq_url)
ollama = OpenAI(api_key="ollama", base_url=ollama_url)
openrouter = OpenAI(api_key=openrouter_api_key, base_url=openrouter_url)
```

```python
models = ["gpt-6.1-sol", "claude-sonnet-5-5", "grok-4.3", "gemini-4-argon", "qwen2.5-coder", "deepseek-coder-v2", "gpt-oss:20b", "qwen/qwen3-coder-30b-a3b-instruct", "openai/gpt-oss-120b", ]

clients = {"gpt-6.1-sol": openai, "claude-sonnet-5-5": anthropic, "grok-4.3": grok, "gemini-4-argon": gemini, "openai/gpt-oss-120b": groq, "qwen2.5-coder": ollama, "deepseek-coder-v2": ollama, "gpt-oss:20b": ollama, "qwen/qwen3-coder-30b-a3b-instruct": openrouter}

# Want to keep costs ultra-low? Replace this with models of your choice, using the examples from yesterday
```

```python
from system_info import retrieve_system_info

system_info = retrieve_system_info()
system_info
```

## Overwrite this with the commands from yesterday

Or just use the website like yesterday:

 https://www.programiz.com/cpp-programming/online-compiler/

```python
compile_command = ["clang++", "-std=c++17", "-Ofast", "-mcpu=native", "-flto=thin", "-fvisibility=hidden", "-DNDEBUG", "main.cpp", "-o", "main"]
run_command = ["./main"]
```

## And now, on with the main task

```python
system_prompt = """
Your task is to convert Python code into high performance C++ code.
Respond only with C++ code. Do not provide any explanation other than occasional comments.
The C++ response needs to produce an identical output in the fastest possible time.
"""

def user_prompt_for(python):
    return f"""
Port this Python code to C++ with the fastest possible implementation that produces identical output in the least time.
The system information is:
{system_info}
Your response will be written to a file called main.cpp and then compiled and executed; the compilation command is:
{compile_command}
Respond only with C++ code.
Python code to port:

```python
{python}
```
"""
```

```python
def messages_for(python):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(python)}
    ]
```

```python
def write_output(cpp):
    with open("main.cpp", "w") as f:
        f.write(cpp)
```

```python
def port(model, python):
    client = clients[model]
    openai_reasoning_models = {"gpt-6.1-sol"}
    reasoning_effort = "high" if model in openai_reasoning_models else None
    response = client.chat.completions.create(model=model, messages=messages_for(python), reasoning_effort=reasoning_effort)
    reply = response.choices[0].message.content
    reply = reply.replace('```cpp','').replace('```','')
    write_output(reply)
    return reply
```

```python
pi = """
import time

def calculate(iterations, param1, param2):
    result = 1.0
    for i in range(1, iterations+1):
        j = i * param1 - param2
        result -= (1/j)
        j = i * param1 + param2
        result += (1/j)
    return result

start_time = time.time()
result = calculate(200_000_000, 4, 1) * 4
end_time = time.time()

print(f"Result: {result:.12f}")
print(f"Execution Time: {(end_time - start_time):.6f} seconds")
"""
```

```python
def run_python(code):
    globals_dict = {"__builtins__": __builtins__}

    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer

    try:
        exec(code, globals_dict)
        output = buffer.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout

    return output
```

```python
def compile_and_run():
    try:
        subprocess.run(compile_command, check=True, text=True, capture_output=True)
        print(subprocess.run(run_command, check=True, text=True, capture_output=True).stdout)
        print(subprocess.run(run_command, check=True, text=True, capture_output=True).stdout)
        print(subprocess.run(run_command, check=True, text=True, capture_output=True).stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred:\n{e.stderr}")
```

```python
with gr.Blocks() as ui:
    with gr.Row():
        python = gr.Textbox(label="Python code:", lines=28, value=pi)
        cpp = gr.Textbox(label="C++ code:", lines=28)
    with gr.Row():
        model = gr.Dropdown(models, label="Select model", value=models[0])
        convert = gr.Button("Convert code")

    convert.click(port, inputs=[model, python], outputs=[cpp])

ui.launch(inbrowser=True)
```

```python
compile_and_run()
```

Qwen 2.5 Coder: Fail  
DeepSeek Coder v2: 0.114050084  
OpenAI gpt-oss 20B: 0.080438  
Qwen 30B: 0.113734  
OpenAI gpt-oss 120B: 1.407383

In Ed's experiments, the performance speedups were:

9th place: Qwen 2.5 Coder: Fail  
8th place: OpenAI GPT-OSS 120B: 14X speedup    
7th place: DeepSeek Coder v2: 168X speedup  
6th place: Qwen3 Coder 30B: 168X speedup   
5th place: Claude Sonnet 4.5: 184X speedup   
4th place: GPT-5: 233X speedup  
**3rd place: oss-20B: 238X speedup**  
2nd place: Grok 4: 1060X speedup  
1st place: Gemini 2.5 Pro: 1440X speedup


---

<a id="file-week4-day5-ipynb"></a>
## File: `week4/day5.ipynb`

> **Path in repository:** `week4/day5.ipynb`

# Code Generator

The requirement: use a Frontier model to generate high performance C++ code from Python code

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">Reminder: OPTIONAL to execute C++ code or Rust code</h2>
            <span style="color:#f71;">As an alternative, you can run it on the website given yesterday</span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h1 style="color:#900;">Important Note</h1>
            <span style="color:#900;">
            In this lab, I use high end models GPT-6.1 Sol, Claude Sonnet 5.5, Gemini 4 Argon, Grok 4.3, which are the slightly higher priced models. The costs are still low, but if you'd prefer to keep costs ultra low, please pick lower cost models like gpt-6-luna.
            </span>
        </td>
    </tr>
</table>

```python
# imports

import os
import io
import sys
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import subprocess
from IPython.display import Markdown, display
```

```python
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if grok_api_key:
    print(f"Grok API Key exists and begins {grok_api_key[:4]}")
else:
    print("Grok API Key not set (and this is optional)")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:
    print("Groq API Key not set (and this is optional)")

if openrouter_api_key:
    print(f"OpenRouter API Key exists and begins {openrouter_api_key[:6]}")
else:
    print("OpenRouter API Key not set (and this is optional)")
```

```python
# Connect to client libraries

openai = OpenAI()

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
grok_url = "https://api.x.ai/v1"
groq_url = "https://api.groq.com/openai/v1"
ollama_url = "http://localhost:11434/v1"
openrouter_url = "https://openrouter.ai/api/v1"

anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
grok = OpenAI(api_key=grok_api_key, base_url=grok_url)
groq = OpenAI(api_key=groq_api_key, base_url=groq_url)
ollama = OpenAI(api_key="ollama", base_url=ollama_url)
openrouter = OpenAI(api_key=openrouter_api_key, base_url=openrouter_url)
```

```python
models = ["gpt-6.1-sol", "claude-sonnet-5-5", "grok-4.3", "gemini-4-argon", "qwen2.5-coder", "deepseek-coder-v2", "gpt-oss:20b", "qwen/qwen3-coder-30b-a3b-instruct", "openai/gpt-oss-120b", ]

clients = {"gpt-6.1-sol": openai, "claude-sonnet-5-5": anthropic, "grok-4.3": grok, "gemini-4-argon": gemini, "openai/gpt-oss-120b": groq, "qwen2.5-coder": ollama, "deepseek-coder-v2": ollama, "gpt-oss:20b": ollama, "qwen/qwen3-coder-30b-a3b-instruct": openrouter}

# Want to keep costs ultra-low? Replace this with models of your choice, using the examples from yesterday
```

```python
from system_info import retrieve_system_info, rust_toolchain_info

system_info = retrieve_system_info()
rust_info = rust_toolchain_info()
rust_info
```

```python
message = f"""
Here is a report of the system information for my computer.
I want to run a Rust compiler to compile a single rust file called main.rs and then execute it in the simplest way possible.
Please reply with whether I need to install a Rust toolchain to do this. If so, please provide the simplest step by step instructions to do so.

If I'm already set up to compile Rust code, then I'd like to run something like this in Python to compile and execute the code:
```python
compile_command = # something here - to achieve the fastest possible runtime performance
compile_result = subprocess.run(compile_command, check=True, text=True, capture_output=True)
run_command = # something here
run_result = subprocess.run(run_command, check=True, text=True, capture_output=True)
return run_result.stdout
```
Please tell me exactly what I should use for the compile_command and run_command.
Have the maximum possible runtime performance in mind; compile time can be slow. Fastest possible runtime performance for this platform is key.
Reply with the commands in markdown.

System information:
{system_info}

Rust toolchain information:
{rust_info}
"""

response = openai.chat.completions.create(model=models[0], messages=[{"role": "user", "content": message}])
display(Markdown(response.choices[0].message.content))
```

## For C++, overwrite this with the commands from yesterday, or for Rust, use the new commands

Or just use the website like yesterday:

 https://www.programiz.com/cpp-programming/online-compiler/

```python
compile_command = [
    "/Users/ed/.cargo/bin/rustc",
    "main.rs",
    "-C", "opt-level=3",
    "-C", "target-cpu=native",
    "-C", "codegen-units=1",
    "-C", "lto=fat",
    "-C", "panic=abort",
    "-C", "strip=symbols",
    "-o", "main",
]

run_command = ["./main"]
```

## And now, on with the main task

```python
language = "Rust" # or "C++"
extension = "rs" if language == "Rust" else "cpp"

system_prompt = f"""
Your task is to convert Python code into high performance {language} code.
Respond only with {language} code. Do not provide any explanation other than occasional comments.
The {language} response needs to produce an identical output in the fastest possible time.
"""

def user_prompt_for(python):
    return f"""
Port this Python code to {language} with the fastest possible implementation that produces identical output in the least time.
The system information is:
{system_info}
Your response will be written to a file called main.{language} and then compiled and executed; the compilation command is:
{compile_command}
Respond only with {language} code.
Python code to port:

```python
{python}
```
"""
```

```python
def messages_for(python):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(python)}
    ]
```

```python
def write_output(code):
    with open(f"main.{extension}", "w") as f:
        f.write(code)
```

```python
def port(model, python):
    client = clients[model]
    reasoning_effort = "high" if 'gpt' in model else None
    response = client.chat.completions.create(model=model, messages=messages_for(python), reasoning_effort=reasoning_effort)
    reply = response.choices[0].message.content
    reply = reply.replace('```cpp','').replace('```rust','').replace('```','')
    return reply
```

```python
def run_python(code):
    globals_dict = {"__builtins__": __builtins__}

    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer

    try:
        exec(code, globals_dict)
        output = buffer.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout

    return output
```

```python
# Use the commands from GPT-6.1 Sol

def compile_and_run(code):
    write_output(code)
    try:
        subprocess.run(compile_command, check=True, text=True, capture_output=True)
        run_result = subprocess.run(run_command, check=True, text=True, capture_output=True)
        return run_result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred:\n{e.stderr}"
```

```python
python_hard = """# Be careful to support large numbers

def lcg(seed, a=1664525, c=1013904223, m=2**32):
    value = seed
    while True:
        value = (a * value + c) % m
        yield value
        
def max_subarray_sum(n, seed, min_val, max_val):
    lcg_gen = lcg(seed)
    random_numbers = [next(lcg_gen) % (max_val - min_val + 1) + min_val for _ in range(n)]
    max_sum = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += random_numbers[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def total_max_subarray_sum(n, initial_seed, min_val, max_val):
    total_sum = 0
    lcg_gen = lcg(initial_seed)
    for _ in range(20):
        seed = next(lcg_gen)
        total_sum += max_subarray_sum(n, seed, min_val, max_val)
    return total_sum

# Parameters
n = 10000         # Number of random numbers
initial_seed = 42 # Initial seed for the LCG
min_val = -10     # Minimum value of random numbers
max_val = 10      # Maximum value of random numbers

# Timing the function
import time
start_time = time.time()
result = total_max_subarray_sum(n, initial_seed, min_val, max_val)
end_time = time.time()

print("Total Maximum Subarray Sum (20 runs):", result)
print("Execution Time: {:.6f} seconds".format(end_time - start_time))
"""
```

```python
from styles import CSS

with gr.Blocks(css=CSS, theme=gr.themes.Monochrome(), title=f"Port from Python to {language}") as ui:
    with gr.Row(equal_height=True):
        with gr.Column(scale=6):
            python = gr.Code(
                label="Python (original)",
                value=python_hard,
                language="python",
                lines=26
            )
        with gr.Column(scale=6):
            cpp = gr.Code(
                label=f"{language} (generated)",
                value="",
                language="cpp",
                lines=26
            )

    with gr.Row(elem_classes=["controls"]):
        python_run = gr.Button("Run Python", elem_classes=["run-btn", "py"])
        model = gr.Dropdown(models, value=models[0], show_label=False)
        convert = gr.Button(f"Port to {language}", elem_classes=["convert-btn"])
        cpp_run = gr.Button(f"Run {language}", elem_classes=["run-btn", "cpp"])

    with gr.Row(equal_height=True):
        with gr.Column(scale=6):
            python_out = gr.TextArea(label="Python result", lines=8, elem_classes=["py-out"])
        with gr.Column(scale=6):
            cpp_out = gr.TextArea(label=f"{language} result", lines=8, elem_classes=["cpp-out"])

    convert.click(fn=port, inputs=[model, python], outputs=[cpp])
    python_run.click(fn=run_python, inputs=[python], outputs=[python_out])
    cpp_run.click(fn=compile_and_run, inputs=[cpp], outputs=[cpp_out])

ui.launch(inbrowser=True)
```

## RESULTS!

Qwen 2.5 Coder: FAIL  
Gemini 2.5 Pro: FAIL  
DeepSeek Coder v2: FAIL  
Qwen3 Coder 30B: FAIL  
Claude Sonnet 4.5: FAIL    
GPT-5: FAIL    

3rd place: GPT-oss-20B: 0.000341  
2nd place: Grok 4: 0.000317  
**1st place: OpenAI GPT-OSS 120B: 0.000304**

```python
print(f"In Ed's experimenet, the GPT-OSS 120B model outcome is {33.755209/0.000304:,.0f} times faster than the Python code.")
```


---

<a id="file-week4-styles-py"></a>
## File: `week4/styles.py`

> **Path in repository:** `week4/styles.py`

```python
CSS = """
:root {
  --py-color: #209dd7;
  --cpp-color: #ecad0a;
  --accent:   #753991;
  --card:     #161a22;
  --text:     #e9eef5;
}

/* Full-width layout */
.gradio-container {
  max-width: 100% !important;
  padding: 0 40px !important;
}

/* Code card styling */
.card {
  background: var(--card);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 14px;
  padding: 10px;
}

/* Buttons */
.convert-btn button {
  background: var(--accent) !important;
  border-color: rgba(255,255,255,.12) !important;
  color: white !important;
  font-weight: 700;
}
.run-btn button {
  background: #202631 !important;
  color: var(--text) !important;
  border-color: rgba(255,255,255,.12) !important;
}
.run-btn.py button:hover  { box-shadow: 0 0 0 2px var(--py-color) inset; }
.run-btn.cpp button:hover { box-shadow: 0 0 0 2px var(--cpp-color) inset; }
.convert-btn button:hover { box-shadow: 0 0 0 2px var(--accent) inset; }

/* Outputs with color tint */
.py-out textarea {
  background: linear-gradient(180deg, rgba(32,157,215,.18), rgba(32,157,215,.10));
  border: 1px solid rgba(32,157,215,.35) !important;
  color: rgba(32,157,215,1) !important;
  font-weight: 600;
}
.cpp-out textarea {
  background: linear-gradient(180deg, rgba(236,173,10,.22), rgba(236,173,10,.12));
  border: 1px solid rgba(236,173,10,.45) !important;
  color: rgba(236,173,10,1) !important;
  font-weight: 600;
}

/* Align controls neatly */
.controls .wrap {
  gap: 10px;
  justify-content: center;
  align-items: center;
}
"""
```


---

<a id="file-week4-system-info-py"></a>
## File: `week4/system_info.py`

> **Path in repository:** `week4/system_info.py`

```python
import os
import platform
import shutil
import subprocess

# ------------------------- helpers -------------------------


def _run(cmd, timeout=3):
    """Run a command safely. Returns stdout text or ''.
    Accepts either a string (shell) or list (no shell)."""
    try:
        if isinstance(cmd, str):
            return subprocess.check_output(
                cmd, shell=True, text=True, stderr=subprocess.DEVNULL, timeout=timeout
            ).strip()
        else:
            return subprocess.check_output(
                cmd, shell=False, text=True, stderr=subprocess.DEVNULL, timeout=timeout
            ).strip()
    except Exception:
        return ""


def _first_line(s: str) -> str:
    s = (s or "").strip()
    return s.splitlines()[0].strip() if s else ""


def _which(name: str) -> str:
    return shutil.which(name) or ""


def _bool_from_output(s: str) -> bool:
    return s.strip() in {"1", "true", "True", "YES", "Yes", "yes"}


# ------------------------- OS & env -------------------------


def _os_block():
    sysname = platform.system()  # 'Windows', 'Darwin', 'Linux'
    machine = platform.machine() or ""
    release = platform.release() or ""
    version = platform.version() or ""
    kernel = release if sysname == "Windows" else (_run(["uname", "-r"]) or release)

    distro = {"name": "", "version": ""}
    if sysname == "Linux":
        # Best-effort parse of /etc/os-release
        try:
            with open("/etc/os-release", "r") as f:
                data = {}
                for line in f:
                    if "=" in line:
                        k, v = line.rstrip().split("=", 1)
                        data[k] = v.strip('"')
                distro["name"] = data.get("PRETTY_NAME") or data.get("NAME", "")
                distro["version"] = data.get("VERSION_ID") or data.get("VERSION", "")
        except Exception:
            pass

    # WSL / Rosetta detection (harmless if not present)
    wsl = False
    if sysname != "Windows":
        try:
            with open("/proc/version", "r") as f:
                v = f.read().lower()
                wsl = ("microsoft" in v) or ("wsl" in v)
        except Exception:
            wsl = False

    rosetta = False
    if sysname == "Darwin":
        rosetta = _bool_from_output(_run(["sysctl", "-in", "sysctl.proc_translated"]))

    # Target triple (best effort)
    target = ""
    for cc in ("clang", "gcc"):
        if _which(cc):
            out = _run([cc, "-dumpmachine"])
            if out:
                target = _first_line(out)
                break

    return {
        "system": sysname,
        "arch": machine,
        "release": release,
        "version": version,
        "kernel": kernel,
        "distro": distro if sysname == "Linux" else None,
        "wsl": wsl,
        "rosetta2_translated": rosetta,
        "target_triple": target,
    }


# ------------------------- package managers -------------------------


def _package_managers():
    sysname = platform.system()
    pms = []
    if sysname == "Windows":
        for pm in ("winget", "choco", "scoop"):
            if _which(pm):
                pms.append(pm)
    elif sysname == "Darwin":
        if _run(["xcode-select", "-p"]):
            pms.append("xcode-select (CLT)")
        for pm in ("brew", "port"):
            if _which(pm):
                pms.append(pm)
    else:
        for pm in ("apt", "dnf", "yum", "pacman", "zypper", "apk", "emerge"):
            if _which(pm):
                pms.append(pm)
    return pms


# ------------------------- CPU (minimal) -------------------------


def _cpu_block():
    sysname = platform.system()
    brand = ""
    # A simple brand/model read per OS; ignore failures
    if sysname == "Linux":
        brand = _run("grep -m1 'model name' /proc/cpuinfo | cut -d: -f2").strip()
    elif sysname == "Darwin":
        brand = _run(["sysctl", "-n", "machdep.cpu.brand_string"])
    elif sysname == "Windows":
        brand = _run('powershell -NoProfile -Command "(Get-CimInstance Win32_Processor).Name"')
        if not brand:
            brand = _run("wmic cpu get Name /value").replace("Name=", "").strip()

    # Logical cores always available; physical is best-effort
    cores_logical = os.cpu_count() or 0
    cores_physical = 0
    if sysname == "Darwin":
        cores_physical = int(_run(["sysctl", "-n", "hw.physicalcpu"]) or "0")
    elif sysname == "Windows":
        cores_physical = int(
            _run('powershell -NoProfile -Command "(Get-CimInstance Win32_Processor).NumberOfCores"')
            or "0"
        )
    elif sysname == "Linux":
        # This is a quick approximation; fine for our use (parallel -j suggestions)
        try:
            # Count unique "core id" per physical id
            mapping = _run("LC_ALL=C lscpu -p=CORE,SOCKET | grep -v '^#'").splitlines()
            unique = set(tuple(line.split(",")) for line in mapping if "," in line)
            cores_physical = len(unique) or 0
        except Exception:
            cores_physical = 0

    # A tiny SIMD hint set (best-effort, optional)
    simd = []
    if sysname == "Linux":
        flags = _run("grep -m1 'flags' /proc/cpuinfo | cut -d: -f2")
        if flags:
            fset = set(flags.upper().split())
            for x in ("AVX512F", "AVX2", "AVX", "FMA", "SSE4_2", "NEON", "SVE"):
                if x in fset:
                    simd.append(x)
    elif sysname == "Darwin":
        feats = (
            (
                _run(["sysctl", "-n", "machdep.cpu.features"])
                + " "
                + _run(["sysctl", "-n", "machdep.cpu.leaf7_features"])
            )
            .upper()
            .split()
        )
        for x in ("AVX512F", "AVX2", "AVX", "FMA", "SSE4_2", "NEON", "SVE"):
            if x in feats:
                simd.append(x)
    # On Windows, skip flags — brand typically suffices for MSVC /arch choice.

    return {
        "brand": brand.strip(),
        "cores_logical": cores_logical,
        "cores_physical": cores_physical,
        "simd": sorted(set(simd)),
    }


# ------------------------- toolchain presence -------------------------


def _toolchain_block():
    def ver_line(exe, args=("--version",)):
        p = _which(exe)
        if not p:
            return ""
        out = _run([p, *args])
        return _first_line(out)

    gcc = ver_line("gcc")
    gpp = ver_line("g++")
    clang = ver_line("clang")

    # MSVC cl (only available inside proper dev shell; handle gracefully)
    msvc_cl = ""
    cl_path = _which("cl")
    if cl_path:
        msvc_cl = _first_line(_run("cl 2>&1"))

    # Build tools (presence + short version line)
    cmake = ver_line("cmake")
    ninja = _first_line(_run([_which("ninja"), "--version"])) if _which("ninja") else ""
    make = ver_line("make")

    # Linker (we only care if lld is available)
    lld = ver_line("ld.lld")
    return {
        "compilers": {"gcc": gcc, "g++": gpp, "clang": clang, "msvc_cl": msvc_cl},
        "build_tools": {"cmake": cmake, "ninja": ninja, "make": make},
        "linkers": {"ld_lld": lld},
    }


# ------------------------- public API -------------------------


def retrieve_system_info():
    """
    Returns a compact dict with enough info for an LLM to:
      - Pick an install path (winget/choco/scoop, Homebrew/Xcode CLT, apt/dnf/...),
      - Choose a compiler family (MSVC/clang/gcc),
      - Suggest safe optimization flags (e.g., -O3/-march=native or MSVC /O2),
      - Decide on a build system (cmake+ninja) and parallel -j value.
    """
    return {
        "os": _os_block(),
        "package_managers": _package_managers(),
        "cpu": _cpu_block(),
        "toolchain": _toolchain_block(),
    }


def rust_toolchain_info():
    """
    Return a dict with Rust-related settings:
      - presence and paths for rustc / cargo / rustup / rust-analyzer
      - versions
      - active/default toolchain (if rustup is present)
      - installed targets
      - common env vars (CARGO_HOME, RUSTUP_HOME, RUSTFLAGS, CARGO_BUILD_TARGET)
      - simple execution examples
    Works on Windows, macOS, and Linux. Uses the existing helpers: _run, _which, _first_line.
    """
    info = {
        "installed": False,
        "rustc": {"path": "", "version": "", "host_triple": "", "release": "", "commit_hash": ""},
        "cargo": {"path": "", "version": ""},
        "rustup": {
            "path": "",
            "version": "",
            "active_toolchain": "",
            "default_toolchain": "",
            "toolchains": [],
            "targets_installed": [],
        },
        "rust_analyzer": {"path": ""},
        "env": {
            "CARGO_HOME": os.environ.get("CARGO_HOME", ""),
            "RUSTUP_HOME": os.environ.get("RUSTUP_HOME", ""),
            "RUSTFLAGS": os.environ.get("RUSTFLAGS", ""),
            "CARGO_BUILD_TARGET": os.environ.get("CARGO_BUILD_TARGET", ""),
        },
        "execution_examples": [],
    }

    # Paths
    rustc_path = _which("rustc")
    cargo_path = _which("cargo")
    rustup_path = _which("rustup")
    ra_path = _which("rust-analyzer")

    info["rustc"]["path"] = rustc_path or ""
    info["cargo"]["path"] = cargo_path or ""
    info["rustup"]["path"] = rustup_path or ""
    info["rust_analyzer"]["path"] = ra_path or ""

    # Versions & verbose details
    if rustc_path:
        ver_line = _first_line(_run([rustc_path, "--version"]))
        info["rustc"]["version"] = ver_line
        verbose = _run([rustc_path, "--version", "--verbose"])
        host = release = commit = ""
        for line in verbose.splitlines():
            if line.startswith("host:"):
                host = line.split(":", 1)[1].strip()
            elif line.startswith("release:"):
                release = line.split(":", 1)[1].strip()
            elif line.startswith("commit-hash:"):
                commit = line.split(":", 1)[1].strip()
        info["rustc"]["host_triple"] = host
        info["rustc"]["release"] = release
        info["rustc"]["commit_hash"] = commit

    if cargo_path:
        info["cargo"]["version"] = _first_line(_run([cargo_path, "--version"]))

    if rustup_path:
        info["rustup"]["version"] = _first_line(_run([rustup_path, "--version"]))
        # Active toolchain
        active = _first_line(_run([rustup_path, "show", "active-toolchain"]))
        info["rustup"]["active_toolchain"] = active

        # Default toolchain (best effort)
        # Try parsing `rustup toolchain list` and pick the line with "(default)"
        tlist = _run([rustup_path, "toolchain", "list"]).splitlines()
        info["rustup"]["toolchains"] = [t.strip() for t in tlist if t.strip()]
        default_tc = ""
        for line in tlist:
            if "(default)" in line:
                default_tc = line.strip()
                break
        if not default_tc:
            # Fallback: sometimes `rustup show` includes "default toolchain: ..."
            for line in _run([rustup_path, "show"]).splitlines():
                if "default toolchain:" in line:
                    default_tc = line.split(":", 1)[1].strip()
                    break
        info["rustup"]["default_toolchain"] = default_tc

        # Installed targets
        targets = _run([rustup_path, "target", "list", "--installed"]).split()
        info["rustup"]["targets_installed"] = targets

    # Execution examples (only include what will work on this system)
    exec_examples = []
    if cargo_path:
        exec_examples.append(f'"{cargo_path}" build')
        exec_examples.append(f'"{cargo_path}" run')
        exec_examples.append(f'"{cargo_path}" test')
    if rustc_path:
        exec_examples.append(f'"{rustc_path}" hello.rs -o hello')
    info["execution_examples"] = exec_examples

    # Installed?
    info["installed"] = bool(rustc_path or cargo_path or rustup_path)

    # Fill in default homes if env vars are empty but typical locations exist
    def _maybe_default_home(env_val, default_basename):
        if env_val:
            return env_val
        home = os.path.expanduser("~") or ""
        candidate = os.path.join(home, default_basename) if home else ""
        return candidate if candidate and os.path.isdir(candidate) else ""

    info["env"]["CARGO_HOME"] = _maybe_default_home(info["env"]["CARGO_HOME"], ".cargo")
    info["env"]["RUSTUP_HOME"] = _maybe_default_home(info["env"]["RUSTUP_HOME"], ".rustup")

    return info
```


---
