# troubleshooting.ipynb

> **Original Path:** `setup/troubleshooting.ipynb`

---

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
