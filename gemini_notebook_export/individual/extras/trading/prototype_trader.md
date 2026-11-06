# prototype_trader.ipynb

> **Original Path:** `extras/trading/prototype_trader.ipynb`

---

# Extra Project - Trading Code Generator

This is an example extra project to show fine-tuning in action, and applied to code generation.

## Project Brief

Build a prototype LLM that can generate example code to suggest trading decisions to buy or sell stocks!

I generated test data using frontier models, in the other files in this directory. Use this to train an open source code model.

In this notebook we generate the dataset; then we move over to Google Colab for the fine-tuning.

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../../resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">This project is provided as an extra resource</h2>
            <span style="color:#f71;">It will make most sense after completing Week 7, and might trigger some ideas for your own projects.<br/><br/>
                This is provided without a detailed walk-through; the output from the colab has been saved (see last cell) so you can review the results if you have any problems running yourself.
            </span>
        </td>
    </tr>
</table>
<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../../important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Do not use for actual trading decisions!!</h2>
            <span style="color:#900;">It hopefully goes without saying: this project will generate toy trading code that is over-simplified and untrusted.<br/><br/>Please do not make actual trading decisions based on this!</span>
        </td>
    </tr>
</table>

## First step - generate training data from examples

There are 3 sample python files generated (via multiple queries) by GPT-4o, Claude 3 Opus and Gemini 1.5 Pro.  

This notebook creates training data from these files, then converts to the HuggingFace format and uploads to the hub.

Afterwards, we will move to Google Colab to fine-tune.

```python
import os
import glob
import matplotlib.pyplot as plt
import random
from datasets import Dataset
from dotenv import load_dotenv
from huggingface_hub import login
import transformers
from transformers import AutoTokenizer
```

```python
# Load environment variables in a file called .env
from datasets import load_dataset, Dataset
load_dotenv()
hf_token = os.getenv('HF_TOKEN')
if hf_token and hf_token.startswith("hf_") and len(hf_token)>5:
    print("HuggingFace Token looks good so far")
else:
    print("Potential problem with HuggingFace token - please check your .env file, and see the Troubleshooting notebook for more")
```

```python
# Constants

DATASET_NAME = "trade_code_data"
BASE_MODEL = "Qwen/CodeQwen1.5-7B"
```

```python
# A utility method to convert the text contents of a file into a list of methods

def extract_method_bodies(text):
    chunks = text.split('def trade')[1:]
    results = []
    for chunk in chunks:
        lines = chunk.split('\n')[1:]
        body = '\n'.join(line for line in lines if line!='\n')
        results.append(body)
    return results
```

```python
# Read all .py files and convert into training data

bodies = []
for filename in glob.glob("*.py"):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        extracted = extract_method_bodies(content)
        bodies += extracted

print(f"Extracted {len(bodies)} trade method bodies")
```

```python
# Let's look at one

print(random.choice(bodies))
```

```python
# To visualize the lines of code in each 

%matplotlib inline
fig, ax = plt.subplots(1, 1)
lengths = [len(body.split('\n')) for body in bodies]
ax.set_xlabel('Lines of code')
ax.set_ylabel('Count of training samples');
_ = ax.hist(lengths, rwidth=0.7, color="green", bins=range(0, max(lengths)))
```

```python
# Add the prompt to the start of every training example

prompt = """
# tickers is a list of stock tickers
import tickers

# prices is a dict; the key is a ticker and the value is a list of historic prices, today first
import prices

# Trade represents a decision to buy or sell a quantity of a ticker
import Trade

import random
import numpy as np

def trade():
"""

data = [prompt + body for body in bodies]
print(random.choice(data))
```

```python
# Distribution of tokens in our dataset

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
tokenized_data = [tokenizer.encode(each) for each in data]
token_counts = [len(tokens) for tokens in tokenized_data]

%matplotlib inline
fig, ax = plt.subplots(1, 1)
ax.set_xlabel('Number of tokens')
ax.set_ylabel('Count of training samples');
_ = ax.hist(token_counts, rwidth=0.7, color="purple", bins=range(0, max(token_counts), 20))
```

# Enforcing a maximum token length

We need to specify a maximum number of tokens when we fine-tune.

Let's pick a cut-off, and only keep training data points that fit within this number of tokens,

```python
CUTOFF = 320
truncated = len([tokens for tokens in tokenized_data if len(tokens) > CUTOFF])
percentage = truncated/len(tokenized_data)*100
print(f"With cutoff at {CUTOFF}, we truncate {truncated} datapoints which is {percentage:.1f}% of the dataset")
```

```python
# Let's only keep datapoints that wouldn't get truncated

filtered_data = [datapoint for datapoint in data if len(tokenizer.encode(datapoint))<=CUTOFF]
print(f"After e now have {len(filtered_data)} datapoints")
```

```python
# Mix up the data

random.seed(42)
random.shuffle(filtered_data)
```

```python
# I don't make a Training / Test split - if we had more training data, we would!

dataset = Dataset.from_dict({'text':filtered_data})
```

```python
login(hf_token)
```

```python
# Push your dataset to your hub
# I've also pushed the data to my account and made it public, which you can use from the colab below

dataset.push_to_hub(DATASET_NAME, private=True)
```

## And now to head over to a Google Colab for fine-tuning in the cloud

Follow this link for the Colab:

https://colab.research.google.com/drive/1wry2-4AGw-U7K0LQ_jEgduoTQqVIvo1x?usp=sharing

I've also saved this Colab with output included, so you can see the results without needing to train if you'd prefer.
