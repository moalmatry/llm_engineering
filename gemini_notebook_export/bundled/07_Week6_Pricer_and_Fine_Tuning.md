# Week6 Pricer and Fine Tuning

This unified reference file consolidates **17 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [week6/day1.ipynb](#file-week6-day1-ipynb)
- [week6/day2.ipynb](#file-week6-day2-ipynb)
- [week6/day3.ipynb](#file-week6-day3-ipynb)
- [week6/day4.ipynb](#file-week6-day4-ipynb)
- [week6/day5.ipynb](#file-week6-day5-ipynb)
- [week6/human_in.csv](#file-week6-human-in-csv)
- [week6/human_out.csv](#file-week6-human-out-csv)
- [week6/pricer/batch.py](#file-week6-pricer-batch-py)
- [week6/pricer/deep_neural_network.py](#file-week6-pricer-deep-neural-network-py)
- [week6/pricer/evaluator.py](#file-week6-pricer-evaluator-py)
- [week6/pricer/items.py](#file-week6-pricer-items-py)
- [week6/pricer/loaders.py](#file-week6-pricer-loaders-py)
- [week6/pricer/parser.py](#file-week6-pricer-parser-py)
- [week6/pricer/preprocessor.py](#file-week6-pricer-preprocessor-py)
- [week6/redemption_run.ipynb](#file-week6-redemption-run-ipynb)
- [week6/redemption_train.ipynb](#file-week6-redemption-train-ipynb)
- [week6/results.ipynb](#file-week6-results-ipynb)

---

<a id="file-week6-day1-ipynb"></a>
## File: `week6/day1.ipynb`

> **Path in repository:** `week6/day1.ipynb`

## The Big Project begins!!

# "THE PRICE IS RIGHT" Capstone Project

This week - build a model that predicts how much something costs from a description, based on a scrape of Amazon data

# Order of play

DAY 1: Data Curation  
DAY 2: Data Pre-processing  
DAY 3: Evaluation, Baselines, Traditional ML  
DAY 4: Deep Learning and LLMs  
DAY 5: Fine-tuning a Frontier Model  

## DAY 1: Data Curation

Today we'll scrub our dataset and curate our data

The dataset is here:  
https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023

And the folder with all the product datasets is here:  
https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023/tree/main/raw/meta_categories

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business value of Data Curation</h2>
            <span style="color:#181;">Data Curation can be considered the less glamorous work of a Data Scientist. I say that's nonsense!
            This is where the science happens - what could be more glamorous than that?! R&D with your
            dataset can often have a greater impact on performance than the fashionable 'hyper-parameter optimization' that we do later.
            So: prepare for Quality Time with Data Quality.</span>
        </td>
    </tr>
</table>

```python
# imports

import os
from dotenv import load_dotenv
from huggingface_hub import login
from datasets import load_dataset
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
import numpy as np
import random
from pricer.items import Item
from pricer.parser import parse
load_dotenv(override=True)
```

```python
# Log in to HuggingFace - if you get a "Note" about Environment variable being set, ignore it

hf_token = os.environ['HF_TOKEN']
login(hf_token, add_to_git_credential=True)
```

## Load our dataset

In the next cell, we load in the dataset from huggingface.

If this gives you an error like "trust_remote_code is no longer supported", then please run this command in a new cell: `!uv add --upgrade datasets==3.6.0` and then restart the Kernel, and try again.

```python
dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Appliances", split="full", trust_remote_code=True)
```

```python
print(f"Number of Appliances: {len(dataset):,}")
```

```python
# Investigate a particular datapoint

dataset[6]
```

```python
# What's the most expensive item?

max_price = 0
max_item = None

for datapoint in tqdm(dataset):
    try:
        price = float(datapoint["price"])
        if price > max_price:
            max_item = datapoint
            max_price = price
    except ValueError:
        pass

print(f"The most expensive item is {max_item['title']} and it costs {max_price:,.2f}")
```

This is the closest I can find - looks like it's going at a bargain price!!

https://www.amazon.com/TurboChef-Electric-Countertop-Microwave-Convection/dp/B01D05U9NO/

```python
# Load into Item objects if they have a price range $1-$1000 and enough details

items = [parse(datapoint, "Appliances") for datapoint in tqdm(dataset)]
items = [item for item in items if item is not None]
print(f"There are {len(items):,} items from {len(dataset):,} datapoints")
```

```python
items[0]
```

```python
print(items[0].full)
```

```python
prices = [item.price for item in items]
lengths = [len(item.full) for item in items]
```

```python
# Plot the distribution of lengths

plt.figure(figsize=(15, 6))
plt.title(f"Lengths: Avg {sum(lengths)/len(lengths):,.0f} and highest {max(lengths):,}\n")
plt.xlabel('Length (chars)')
plt.ylabel('Count')
plt.hist(lengths, rwidth=0.7, color="lightblue", bins=range(0, 6000, 100))
plt.show()
```

```python
max_length = max(lengths)
max_length_item = items[lengths.index(max_length)]
print(max_length_item.full)
```

```python
# Plot the distribution of prices
plt.figure(figsize=(15, 6))
plt.title(f"Prices: Avg {sum(prices)/len(prices):,.2f} and highest {max(prices):,}\n")
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.hist(prices, rwidth=0.7, color="orange", bins=range(0, 1000, 10))
plt.show()
```

```python
print(items[3].full)
```

```python
from pricer.loaders import ItemLoader
loader = ItemLoader("Appliances")
items = loader.load()
```

```python
dataset_names = [
    "Automotive",
    "Electronics",
    "Office_Products",
    "Tools_and_Home_Improvement",
    "Cell_Phones_and_Accessories",
    "Toys_and_Games",
    "Appliances",
    "Musical_Instruments",
]
```

```python
items = []
for dataset_name in dataset_names:
    loader = ItemLoader(dataset_name)
    items.extend(loader.load())
```

```python
print(f"A grand total of {len(items):,} items")
```

```python
items[1000]
```

```python
random.seed(42)
random.shuffle(items)

seen = set()
items = [x for x in tqdm(items) if not (x.title in seen or seen.add(x.title))]

seen = set()
items = [x for x in tqdm(items) if not (x.full in seen or seen.add(x.full))]

del seen
print(f"After deduplication, we have {len(items):,} items")
```

```python
lengths = [len(item.full) for item in items]
plt.figure(figsize=(15, 6))
plt.title(f"Text length: Avg {sum(lengths)/len(lengths):,.1f} and highest {max(lengths):,}\n")
plt.xlabel('Length (characters)')
plt.ylabel('Count')
plt.hist(lengths, rwidth=0.7, color="skyblue", bins=range(0, 4050, 50))
plt.show()
```

```python
# Plot the distribution of prices

prices = [item.price for item in items]
plt.figure(figsize=(15, 6))
plt.title(f"Prices: Avg {sum(prices)/len(prices):,.1f} and highest {max(prices):,}\n")
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.hist(prices, rwidth=0.7, color="blueviolet", bins=range(0, 1000, 10))
plt.show()
```

```python
from collections import Counter
category_counts = Counter([item.category for item in items])

categories = category_counts.keys()
counts = [category_counts[category] for category in categories]

plt.figure(figsize=(15, 6))
plt.bar(categories, counts, color="goldenrod")
plt.title('How many in each category')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.xticks(rotation=30, ha='right')

for i, v in enumerate(counts):
    plt.text(i, v, f"{v:,}", ha='center', va='bottom')

plt.show()
```

```python
np.random.seed(42)

SIZE = 820_000

prices = np.array([it.price for it in items], dtype=float)
categories = np.array([it.category for it in items])
p = (prices - prices.min()) / (prices.max() - prices.min() + 1e-9)

w = p**2
w[categories == "Tools_and_Home_Improvement"] *= 0.5
w[categories == "Automotive"] *= 0.05

w = w / w.sum()
idx = np.random.choice(len(items), size=SIZE, replace=False, p=w)
sample = [items[i] for i in idx]
```

```python
prices = [item.price for item in sample]
plt.figure(figsize=(15, 6))
plt.title(f"Prices: Avg {sum(prices)/len(prices):,.1f} lowest {min(prices):,} and highest {max(prices):,}\n")
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.hist(prices, rwidth=0.7, color="blueviolet", bins=range(0, 1000, 10))
plt.show()
```

```python
# Just for good measure, let's shuffle the sample again for the final dataset

random.seed(42)
random.shuffle(sample)
```

```python
prices = [item.price for item in sample]
plt.figure(figsize=(15, 6))
plt.title(f"Prices: Avg {sum(prices)/len(prices):,.1f} lowest {min(prices):,} and highest {max(prices):,}\n")
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.hist(prices, rwidth=0.7, color="blueviolet", bins=range(0, 1000, 10))
plt.show()
```

```python
from collections import Counter
category_counts = Counter([item.category for item in sample])

categories = category_counts.keys()
counts = [category_counts[category] for category in categories]

# Bar chart by category
plt.figure(figsize=(15, 6))
plt.bar(categories, counts, color="goldenrod")
plt.title('How many in each category')
plt.xlabel('Categories')
plt.ylabel('Count')

plt.xticks(rotation=30, ha='right')

# Add value labels on top of each bar
for i, v in enumerate(counts):
    plt.text(i, v, f"{v:,}", ha='center', va='bottom')

# Display the chart
plt.show()
```

```python
# Automotive still in the lead, but improved somewhat
# For another perspective, let's look at a pie

plt.figure(figsize=(12, 10))
plt.pie(counts, labels=categories, autopct='%1.0f%%', startangle=90)

# Add a circle at the center to create a donut chart (optional)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Categories')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

plt.show()
```

```python
# How does the price vary with the character count?

sizes = [len(item.full) for item in sample]
prices = [item.price for item in sample]

# Create the scatter plot
plt.figure(figsize=(15, 8))
plt.scatter(sizes, prices, s=0.2, color="red")

# Add labels and title
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Is there a simple correlation with text length?')

# Display the plot
plt.show()
```

```python
# How does the price vary with the weight?

ounces = [item.weight for item in sample]
prices = [item.price for item in sample]

# Create the scatter plot
plt.figure(figsize=(15, 8))
plt.scatter(ounces, prices, s=0.2, color="darkorange")

# Add labels and title
plt.xlabel('Weight (ounces)')
plt.ylabel('Price')
plt.xlim(0, 400)
plt.title('Is there a simple correlation with weight?')

# Display the plot
plt.show()
```

## Now push this dataset to the HuggingFace Hub

Replace the username with your HF username if you've crafted your own dataset

Or, ignore this cell and you can load my dataset tomorrow!

```python
username = "ed-donner"
full = f"{username}/items_raw_full"
lite = f"{username}/items_raw_lite"

train = sample[:800_000]
val = sample[800_000:810_000]
test = sample[810_000:]

Item.push_to_hub(full, train, val, test)

train_lite = train[:20_000]
val_lite = val[:1_000]
test_lite = test[:1_000]

Item.push_to_hub(lite, train_lite, val_lite, test_lite)
```

## Sidenote

If you like the variety of colors that matplotlib can use in its charts, you should bookmark this:

https://matplotlib.org/stable/gallery/color/named_colors.html


---

<a id="file-week6-day2-ipynb"></a>
## File: `week6/day2.ipynb`

> **Path in repository:** `week6/day2.ipynb`

# "THE PRICE IS RIGHT" Capstone Project

This week - build a model that predicts how much something costs from a description, based on a scrape of Amazon data


A model that can estimate how much something costs, from its description.

# Order of play

DAY 1: Data Curation  
DAY 2: Data Pre-processing  
DAY 3: Evaluation, Baselines, Traditional ML  
DAY 4: Deep Learning and LLMs  
DAY 5: Fine-tuning a Frontier Model  

## DAY 2: Data Pre-processing

Today we'll rewrite the products into a standard format.  
LLMs are great at this!

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business value of Data Pre-processing / Re-writing</h2>
            <span style="color:#181;">LLMs have made it simple to do something that was considered impossible only a few years ago.
            This approach can be applied to almost any business vertical, and it's similar to the advanced techniques
            we used on Week 5.</span>
        </td>
    </tr>
</table>

```python
from litellm import completion
from dotenv import load_dotenv
import json
from pricer.batch import Batch
from pricer.items import Item

load_dotenv(override=True)
```

# The next cell is where you choose Dataset

Use `LITE_MODE = True` for the free, fast version with training data size of 20,000

USe `LITE_MODE =  False` for the powerful, full version with training data size of 800,000

## For this lab

You can skip altogether and load the dataset from HuggingFace: $0

You can run pre-processing for the lite dataset: under $1

You can run pre-processing for the full dataset: $30

```python
LITE_MODE = True
```

```python
username = "ed-donner"
dataset = f"{username}/items_raw_lite" if LITE_MODE else f"{username}/items_raw_full"

train, val, test = Item.from_hub(dataset)

items = train + val + test

print(f"Loaded {len(items):,} items")
print(items[0])
```

```python
items[2].id
```

```python
# Give every item an id

for index, item in enumerate(items):
    item.id = index
```

```python
SYSTEM_PROMPT = """Create a concise description of a product. Respond only in this format. Do not include part numbers.
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features"""
```

```python
print(items[0].full)
```

```python
messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": items[0].full}]
response = completion(messages=messages, model="groq/openai/gpt-oss-20b", reasoning_effort="low")

print(response.choices[0].message.content)
print()
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Cost: {response._hidden_params['response_cost']*100:.3f} cents")
```

```python
messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": items[0].full}]
response = completion(messages=messages, model="ollama/llama3.2", api_base="http://localhost:11434")
print(response.choices[0].message.content)
print()
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Cost: {response._hidden_params['response_cost']*100:.3f} cents")
```

```python
MODEL = "openai/gpt-oss-20b"
```

```python
def make_jsonl(item):
    body = {"model": MODEL, "messages": [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": item.full}], "reasoning_effort": "low"}
    line = {"custom_id": str(item.id), "method": "POST", "url": "/v1/chat/completions", "body": body}
    return json.dumps(line)
```

```python
items[0]
```

```python
make_jsonl(items[0])
```

```python
def make_file(start, end, filename):
    batch_file = filename
    with open(batch_file, "w", encoding="utf-8") as f:
        for i in range(start, end):
            f.write(make_jsonl(items[i]))
            f.write("\n")
```

```python
make_file(0, 1000, "jsonl/0_1000.jsonl")
```

```python
import os
from groq import Groq

groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))
```

```python
with open("jsonl/0_1000.jsonl", "rb") as f:
    response = groq.files.create(file=f, purpose="batch")
response
```

```python
file_id = response.id
file_id
```

```python
response = groq.batches.create(completion_window="24h", endpoint="/v1/chat/completions", input_file_id=file_id)
response
```

```python
result = groq.batches.retrieve(response.id)
result
```

```python
response = groq.files.content(result.output_file_id)
response.write_to_file("jsonl/batch_results.jsonl")
```

```python
with open("jsonl/batch_results.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        json_line = json.loads(line)
        id = int(json_line["custom_id"])
        summary = json_line["response"]["body"]["choices"][0]["message"]["content"]
        items[id].summary = summary
```

```python
print(items[0].full)
```

```python
print(items[1000].summary)
```

## I've put exactly this logic into a Batch class

- Divides items into groups of 1,000
- Kicks off batches for each
- Allows us to monitor and collect the results when complete

## COSTS

Using Groq, for me - this cost under $1 for the Lite dataset and under $30 for the big dataset

But you don't need to pay anything! In the next lab, you can load my pre-processed results

```python
Batch.create(items, LITE_MODE)
```

```python
Batch.run()
```

```python
Batch.fetch()
```

```python
for index, item in enumerate(items):
    if not item.summary:
        print(index)
```

```python
print(items[10234].summary)
```

```python
# Remove the fields that we don't need in the hub

for item in items:
    item.full = None
    item.id = None
```

## Push the final dataset to the hub

If lite mode, we'll only push the lite dataset

If full mode, we'll push both datasets (in case you decide to use lite later)

```python
username = "ed-donner"
full = f"{username}/items_full"
lite = f"{username}/items_lite"

if LITE_MODE:
    train = items[:20_000]
    val = items[20_000:21_000]
    test = items[21_000:]
    Item.push_to_hub(lite, train, val, test)
else:
    train = items[:800_000]
    val = items[800_000:810_000]
    test = items[810_000:]
    Item.push_to_hub(full, train, val, test)

    train_lite = train[:20_000]
    val_lite = val[:1_000]
    test_lite = test[:1_000]
    Item.push_to_hub(lite, train_lite, val_lite, test_lite)
```

## And here they are!

https://huggingface.co/datasets/ed-donner/items_lite

https://huggingface.co/datasets/ed-donner/items_full


---

<a id="file-week6-day3-ipynb"></a>
## File: `week6/day3.ipynb`

> **Path in repository:** `week6/day3.ipynb`

# "THE PRICE IS RIGHT" Capstone Project

This week - build a model that predicts how much something costs from a description, based on a scrape of Amazon data

# Order of play

DAY 1: Data Curation  
DAY 2: Data Pre-processing  
DAY 3: Evaluation, Baselines, Traditional ML  
DAY 4: Deep Learning and LLMs  
DAY 5: Fine-tuning a Frontier Model  

## DAY 3: Evaluation, Baselines, Traditional ML

Today we'll write some simple models to predict the price of a product

We'll use an approach to evaluate the performance of the model

And we'll test some Baseline Models using Traditional machine learning

```python
import random
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor
from pricer.evaluator import evaluate
from pricer.items import Item
```

```python
LITE_MODE = False
```

```python
username = "ed-donner"
dataset = f"{username}/items_lite" if LITE_MODE else f"{username}/items_full"

train, val, test = Item.from_hub(dataset)

print(f"Loaded {len(train):,} training items, {len(val):,} validation items, {len(test):,} test items")
```

```python
def random_pricer(item):
    return random.randrange(1,1000)
```

```python
random.seed(42)
evaluate(random_pricer, test)
```

```python
# That was fun!
# We can do better - here's another rather trivial model

training_prices = [item.price for item in train]
training_average = sum(training_prices) / len(training_prices)
print(training_average)

def constant_pricer(item):
    return training_average
```

```python
evaluate(constant_pricer, test)
```

```python
def get_features(item):
    return {
        "weight": item.weight,
        "weight_unknown": 1 if item.weight==0 else 0,
        "text_length": len(item.summary)
    }
```

```python
def list_to_dataframe(items):
    features = [get_features(item) for item in items]
    df = pd.DataFrame(features)
    df['price'] = [item.price for item in items]
    return df

train_df = list_to_dataframe(train)
test_df = list_to_dataframe(test)
```

```python
# Traditional Linear Regression!

np.random.seed(42)

# Separate features and target
feature_columns = ['weight', 'weight_unknown', 'text_length']

X_train = train_df[feature_columns]
y_train = train_df['price']
X_test = test_df[feature_columns]
y_test = test_df['price']

# Train a Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

for feature, coef in zip(feature_columns, model.coef_):
    print(f"{feature}: {coef}")
print(f"Intercept: {model.intercept_}")

# Predict the test set and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")
```

```python
def linear_regression_pricer(item):
    features = get_features(item)
    features_df = pd.DataFrame([features])
    return model.predict(features_df)[0]
```

```python
evaluate(linear_regression_pricer, test)
```

```python
prices = np.array([float(item.price) for item in train])
documents = [item.summary for item in train]
```

```python
np.random.seed(42)
vectorizer = CountVectorizer(max_features=2000, stop_words='english')
X = vectorizer.fit_transform(documents)
```

```python
# Here are the 1,000 most common words that it picked, not including "stop words":

selected_words = vectorizer.get_feature_names_out()
print(f"Number of selected words: {len(selected_words)}")
print("Selected words:", selected_words[1000:1020])
```

```python
regressor = LinearRegression()
regressor.fit(X, prices)
```

```python
def natural_language_linear_regression_pricer(item):
    x = vectorizer.transform([item.summary])
    return max(regressor.predict(x)[0], 0)
```

```python
evaluate(natural_language_linear_regression_pricer, test)
```

```python
subset = 15_000
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=4)
rf_model.fit(X[:subset], prices[:subset])
```

## Random Forest model

The Random Forest is a type of "**ensemble**" algorithm, meaning that it combines many smaller algorithms to make better predictions.

It uses a very simple kind of machine learning algorithm called a **decision tree**. A decision tree makes predictions by examining the values of features in the input. Like a flow chart with IF statements. Decision trees are very quick and simple, but they tend to overfit.

In our case, the "features" are the elements of the Vector - in other words, it's the number of times that a particular word appears in the product description.

So you can think of it something like this:

**Decision Tree**  
\- IF the word "TV" appears more than 3 times THEN  
-- IF the word "LED" appears more than 2 times THEN  
--- IF the word "HD" appears at least once THEN  
---- Price = $500


With Random Forest, multiple decision trees are created. Each one is trained with a different random subset of the data, and a different random subset of the features. You can see above that we specify 100 trees, which is the default.

Then the Random Forest model simply takes the average of all its trees to product the final result.

```python
def random_forest(item):
    x = vectorizer.transform([item.summary])
    return max(0, rf_model.predict(x)[0])
```

```python
evaluate(random_forest, test)
```

```python
# This is how to save the model if you want to, particularly if you run this on a larger dataset

# import joblib
# joblib.dump(rf_model, "random_forest.joblib")
```

## Introducing XGBoost

Like Random Forest, XGBoost is also an ensemble model that combines multiple decision trees.

But unlike Random Forest, XGBoost builds one tree after another, with each next tree correcting for errors in the prior trees, using 'gradient descent'.

It's much faster than Random Forest, so we can run it for the full dataset, and it's typically better at generalizing.

**If this import doesn't work, please skip this! It's not required. On a Mac, you might need to do `brew install libomp` in the terminal.**

```python
import xgboost as xgb
```

```python
np.random.seed(42)

xgb_model = xgb.XGBRegressor(n_estimators=1000, random_state=42, n_jobs=4, learning_rate=0.1)
xgb_model.fit(X, prices)
```

```python
def xg_boost(item):
    x = vectorizer.transform([item.summary])
    return max(0, xgb_model.predict(x)[0])
```

```python
evaluate(xg_boost, test)
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business applications</h2>
            <span style="color:#181;">Traditional ML isn't just useful for learning the history; it's still heavily used in industry today, particularly for tasks where there are clearly identifiable features. It's worth spending time exploring the algorithms and experimenting here. See if you can beat my numbers with Traditional ML! I ran the Random Forest for the entire 800,000 training dataset. It took about 15 hours to run, and it ended up getting a low error of $56.40. Traditional ML can do well - try it for yourself.</span>
        </td>
    </tr>
</table>


---

<a id="file-week6-day4-ipynb"></a>
## File: `week6/day4.ipynb`

> **Path in repository:** `week6/day4.ipynb`

# "THE PRICE IS RIGHT" Capstone Project

This week - build a model that predicts how much something costs from a description, based on a scrape of Amazon data


A model that can estimate how much something costs, from its description.

# Order of play

DAY 1: Data Curation  
DAY 2: Data Pre-processing  
DAY 3: Evaluation, Baselines, Traditional ML  
DAY 4: Deep Learning and LLMs  
DAY 5: Fine-tuning a Frontier Model  

## DAY 4: Neural Networks and LLMs

Today we'll work from Traditional ML to Neural Networks to Large Language Models!!

```python
# imports

import os
from dotenv import load_dotenv
from huggingface_hub import login
from pricer.evaluator import evaluate
from litellm import completion
from pricer.items import Item
import numpy as np
from tqdm.notebook import tqdm
import csv
from sklearn.feature_extraction.text import HashingVectorizer
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from torch.optim.lr_scheduler import CosineAnnealingLR
```

```python
LITE_MODE = False

load_dotenv(override=True)
hf_token = os.environ['HF_TOKEN']
login(hf_token, add_to_git_credential=True)
```

```python
username = "ed-donner"
dataset = f"{username}/items_lite" if LITE_MODE else f"{username}/items_full"

train, val, test = Item.from_hub(dataset)

print(f"Loaded {len(train):,} training items, {len(val):,} validation items, {len(test):,} test items")
```

# Before we look at the Artificial Neural Networks

## There is a different kind of Neural Network we could consider

```python
# Write the test set to a CSV

with open('human_in.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for t in test[:100]:
        writer.writerow([t.summary, 0])
```

```python
# Read it back in

human_predictions = []
with open('human_out.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        human_predictions.append(float(row[1]))
```

```python
def human_pricer(item):
    idx = test.index(item)
    return human_predictions[idx]
```

```python
human = human_pricer(test[0])
actual = test[0].price
print(f"Human predicted {human} for an item that actually costs {actual}")
```

```python
evaluate(human_pricer, test, size=100)
```

# And now - a vanilla Neural Network

During the remainder of this course we will get deeper into how Neural Networks work, and how to train a neural network.

This is just a sneak preview - let's make our own Neural Network, from scratch, using Pytorch.

Use this to get intuition; it's not important to know all about Neural networks at this point..

```python
# Prepare our documents and prices

y = np.array([float(item.price) for item in train])
documents = [item.summary for item in train]
```

```python
# Use the HashingVectorizer for a Bag of Words model
# Using binary=True with the CountVectorizer makes "one-hot vectors"

np.random.seed(42)
vectorizer = HashingVectorizer(n_features=5000, stop_words='english', binary=True)
X = vectorizer.fit_transform(documents)
```

```python
# Define the neural network - here is Pytorch code to create a 8 layer neural network

class NeuralNetwork(nn.Module):
    def __init__(self, input_size):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(input_size, 128)
        self.layer2 = nn.Linear(128, 64)
        self.layer3 = nn.Linear(64, 64)
        self.layer4 = nn.Linear(64, 64)
        self.layer5 = nn.Linear(64, 64)
        self.layer6 = nn.Linear(64, 64)
        self.layer7 = nn.Linear(64, 64)
        self.layer8 = nn.Linear(64, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        output1 = self.relu(self.layer1(x))
        output2 = self.relu(self.layer2(output1))
        output3 = self.relu(self.layer3(output2))
        output4 = self.relu(self.layer4(output3))
        output5 = self.relu(self.layer5(output4))
        output6 = self.relu(self.layer6(output5))
        output7 = self.relu(self.layer7(output6))
        output8 = self.layer8(output7)
        return output8
```

```python
# Convert data to PyTorch tensors
X_train_tensor = torch.FloatTensor(X.toarray())
y_train_tensor = torch.FloatTensor(y).unsqueeze(1)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train_tensor, y_train_tensor, test_size=0.01, random_state=42)

# Create the loader
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# Initialize the model
input_size = X_train_tensor.shape[1]
model = NeuralNetwork(input_size)
```

```python
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f"Number of trainable parameters: {trainable_params:,}")
```

```python
# Define loss function and optimizer

loss_function = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# We will do 2 complete runs through the data

EPOCHS = 2

for epoch in range(EPOCHS):
    model.train()
    for batch_X, batch_y in tqdm(train_loader):
        optimizer.zero_grad()

        # The next 4 lines are the 4 stages of training: forward pass, loss calculation, backward pass, optimize
        
        outputs = model(batch_X)
        loss = loss_function(outputs, batch_y)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        val_outputs = model(X_val)
        val_loss = loss_function(val_outputs, y_val)

    print(f'Epoch [{epoch+1}/{EPOCHS}], Train Loss: {loss.item():.3f}, Val Loss: {val_loss.item():.3f}')
```

```python
def neural_network(item):
    model.eval()
    with torch.no_grad():
        vector = vectorizer.transform([item.summary])
        vector = torch.FloatTensor(vector.toarray())
        result = model(vector)[0].item()
    return max(0, result)
```

```python
evaluate(neural_network, test)
```

# And now - to the frontier!

Let's see how Frontier models do out of the box; no training, just inference based on their world knowledge.

Tomorrow we will do some training.

```python
def messages_for(item):
    message = f"Estimate the price of this product. Respond with the price, no explanation\n\n{item.summary}"
    return [{"role": "user", "content": message}]
```

```python
print(test[0].summary)
```

```python
messages_for(test[0])
```

```python
# The function for gpt-6-luna

def gpt_6_luna(item):
    response = completion(model="openai/gpt-6-luna", extra_body={"reasoning_effort": "none"}, messages=messages_for(item))
    return response.choices[0].message.content
```

```python
gpt_6_luna(test[0])
```

```python
test[0].price
```

```python
evaluate(gpt_6_luna, test)
```

```python
def claude_opus_4_5(item):
    response = completion(model="anthropic/claude-opus-4-5", messages=messages_for(item))
    return response.choices[0].message.content
```

```python
evaluate(claude_opus_4_5, test)
```

```python
def gemini_4_argon(item):
    response = completion(model="gemini/gemini-4-argon", messages=messages_for(item))
    return response.choices[0].message.content
```

```python
evaluate(gemini_4_argon, test, size=50, workers=2)
```

```python
def gemini_2__5_flash_lite(item):
    response = completion(model="gemini/gemini-3.1-flash-lite", messages=messages_for(item))
    return response.choices[0].message.content
```

```python
evaluate(gemini_2__5_flash_lite, test)
```

```python
def grok_4__3(item):
    response = completion(model="xai/grok-4.3", messages=messages_for(item), reasoning_effort="none", seed=42)
    return response.choices[0].message.content
```

```python
evaluate(grok_4__3, test)
```

```python
# The function for gpt-5.1

def gpt_5__1(item):
    response = completion(model="gpt-5.1", messages=messages_for(item), reasoning_effort='high', seed=42)
    return response.choices[0].message.content
```

```python
evaluate(gpt_5__1, test)
```


---

<a id="file-week6-day5-ipynb"></a>
## File: `week6/day5.ipynb`

> **Path in repository:** `week6/day5.ipynb`

# "THE PRICE IS RIGHT" Capstone Project

This week - build a model that predicts how much something costs from a description, based on a scrape of Amazon data

# Order of play

DAY 1: Data Curation  
DAY 2: Data Pre-processing  
DAY 3: Evaluation, Baselines, Traditional ML  
DAY 4: Deep Learning and LLMs  
DAY 5: Fine-tuning a Frontier Model  

## DAY 5: Fine-tuning a Frontier Model

Now we will use OpenAI's API to fine-tune our own private variant of GPT-4.1-nano

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#900;">Please watch this one rather than run it</h2>
            <span style="color:#900;">OpenAI no longer offers fine-tuning to new users, and the model I fine-tune in this video has been retired. This FAQ explains more: <a href="https://edwarddonner.com/avatar/?q=59">https://edwarddonner.com/avatar/?q=59</a>. I recommend skipping fine-tuning a frontier model and watching me do it instead. Fine-tuning in week 7 is where the action happens!</span>
        </td>
    </tr>
</table>

```python
# imports

import os
import re
import json
from dotenv import load_dotenv
from huggingface_hub import login
from openai import OpenAI
from pricer.items  import Item
from pricer.evaluator import evaluate
```

```python
# environment

LITE_MODE = False

load_dotenv(override=True)
hf_token = os.environ['HF_TOKEN']
login(hf_token, add_to_git_credential=True)
```

```python
username = "ed-donner"
dataset = f"{username}/items_lite" if LITE_MODE else f"{username}/items_full"

train, val, test = Item.from_hub(dataset)

print(f"Loaded {len(train):,} training items, {len(val):,} validation items, {len(test):,} test items")
```

```python
openai = OpenAI()
```

# Data size

OpenAI recommends fine-tuning with a small population of 50-100 examples

I'm going to go with 20,000 points.

This cost me $3.42 - you should stick with 100 examples and the cost will be minimal!

```python
# OpenAI recommends fine-tuning with populations of 50-100 examples
# But as our examples are very small, I'm suggesting we go with 100 examples (and 1 epoch)


fine_tune_train = train[:100]
fine_tune_validation = val[:50]
```

```python
len(fine_tune_train)
```

# Step 1

Prepare our data for fine-tuning in JSONL (JSON Lines) format and upload to OpenAI

```python
def messages_for(item):
    message = f"Estimate the price of this product. Respond with the price, no explanation\n\n{item.summary}"
    return [
        {"role": "user", "content": message},
        {"role": "assistant", "content": f"${item.price:.2f}"}
    ]
```

```python
messages_for(fine_tune_train[0])
```

```python
# Convert the items into a list of json objects - a "jsonl" string
# Each row represents a message in the form:
# {"messages" : [{"role": "system", "content": "You estimate prices...


def make_jsonl(items):
    result = ""
    for item in items:
        messages = messages_for(item)
        messages_str = json.dumps(messages)
        result += '{"messages": ' + messages_str +'}\n'
    return result.strip()
```

```python
print(make_jsonl(train[:3]))
```

```python
# Convert the items into jsonl and write them to a file

def write_jsonl(items, filename):
    with open(filename, "w") as f:
        jsonl = make_jsonl(items)
        f.write(jsonl)
```

```python
write_jsonl(fine_tune_train, "jsonl/fine_tune_train.jsonl")
```

```python
write_jsonl(fine_tune_validation, "jsonl/fine_tune_validation.jsonl")
```

```python
with open("jsonl/fine_tune_train.jsonl", "rb") as f:
    train_file = openai.files.create(file=f, purpose="fine-tune")
```

```python
train_file
```

```python
with open("jsonl/fine_tune_validation.jsonl", "rb") as f:
    validation_file = openai.files.create(file=f, purpose="fine-tune")
```

```python
validation_file
```

https://platform.openai.com/storage/files/

# Step 2

## And now time to Fine-tune!

```python
openai.fine_tuning.jobs.create(
    training_file=train_file.id,
    validation_file=validation_file.id,
    model="gpt-4.1-nano-2025-04-14",
    seed=42,
    hyperparameters={"n_epochs": 1, "batch_size": 1},
    suffix="pricer"
)
```

```python
openai.fine_tuning.jobs.list(limit=1)
```

```python
job_id = openai.fine_tuning.jobs.list(limit=1).data[0].id
```

```python
job_id
```

```python
openai.fine_tuning.jobs.retrieve(job_id)
```

```python
openai.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10).data
```

https://platform.openai.com/finetune

# Step 3

Test our fine tuned model

```python
fine_tuned_model_name = openai.fine_tuning.jobs.retrieve(job_id).fine_tuned_model
```

```python
fine_tuned_model_name
```

```python
# The prompt

def test_messages_for(item):
    message = f"Estimate the price of this product. Respond with the price, no explanation\n\n{item.summary}"
    return [
        {"role": "user", "content": message},
    ]
```

```python
# Try this out

test_messages_for(test[0])
```

```python
# The inference function


def gpt_4__1_nano_fine_tuned(item):
    response = openai.chat.completions.create(
        model=fine_tuned_model_name,
        messages=test_messages_for(item),
        max_tokens=7
    )
    return response.choices[0].message.content
```

```python
print(test[0].price)
print(gpt_4__1_nano_fine_tuned(test[0]))
```

```python
evaluate(gpt_4__1_nano_fine_tuned, test)
```

```python
# 96.58 - mini 200
# 79.29 - mini 2000
# 82.26 - nano 2000
# 67.75 - nano 20,000
```


---

<a id="file-week6-human-in-csv"></a>
## File: `week6/human_in.csv`

> **Path in repository:** `week6/human_in.csv`

```csv
"Title: Excess V2 Distortion/Modulation Pedal  
Category: Music Pedals  
Brand: Old Blood Noise  
Description: A versatile pedal offering distortion and three modulation modes—delay, chorus, and harmonized fifths—with full control over signal routing and expression.  
Details: Features include separate gain, tone, and volume controls; time, depth, and volume per modulation; order switching, soft‑touch bypass, and expression jack for dynamic control.",0
"Title: Telpo Headlight Assembly for 2015‑2017 Toyota Camry  
Category: Automotive Accessories  
Brand: Telpo  
Description: Dual headlight assembly that fits the 2015‑2017 Toyota Camry front driver and passenger sides.  
Details: Direct replacement with DOT & SAE‑certified lenses, high/low beam, waterproof construction, and a 1‑year limited warranty.",0
"Title: NewPower99 6000 mAh Battery Replacement Kit for Samsung Galaxy Tab S3 9.7  
Category: Electronics  
Brand: NewPower99  
Description: Replace or backup the battery on your Samsung Galaxy Tab S3 9.7 with a 6000 mAh lithium‑polymer pack.  
Details: Includes a new battery, step‑by‑step video instructions, special opening tools, and a one‑year money‑back guarantee.",0
"Title: EXMAX NG-10X Fresnel Lens Focusing Adapter  
Category: Lighting Accessories  
Brand: EXMAX  
Description: A telescoping Bowens‑mount adapter that concentrates LED studio light into a 10–40° spot, boosting brightness 5–10× and offering quick color filter swaps.  
Details: Features a durable black plastic construction, adjustable focus, integrated four‑color gel filters, and compatibility with most LED or flash lights up to 150 W.",0
"Title: Raven Pro Document Scanner Stand  
Category: Accessories  
Brand: Raven  
Description: Elevates the Raven Pro Document Scanner to provide a comfortable seated viewing angle.  
Details: Enhances visibility of the LCD touchscreen for easy use and includes a stable, compact design.",0
"Title: UPC RBC12-UPC Replacement Battery Cartridge  
Category: Electronics  
Brand: UPC  
Description: A precharged, maintenance‑free lead‑acid battery cartridge for APC RBC12 UPS systems that delivers reliable power during outages.  
Details: Sealed, leak‑proof design with all connectors, cable, and fuses included for instant plug‑and‑play, hot‑swappable installation, and a 2‑year limited warranty.",0
"Title: Lexmark X651 Compatible Toner Cartridge – Black, 1 Pack  
Category: Office Supplies  
Brand: SuppliesOutlet  
Description: High‑yield, OEM‑compatible toner cartridge for Lexmark X651 series, delivering up to 25,000 pages.  
Details: Features a 1‑year performance guarantee, 25,000 page yield at 5% coverage, and uses high‑quality new/recycled components.",0
"Title: ACDelco GM FW339 Front Wheel Hub & Bearing Assembly  
Category: Automotive Parts  
Brand: ACDelco  
Description: Original equipment wheel hub and bearing assembly with integrated wheel speed sensor for GM vehicles.  
Details: Features dual sealed ball bearings, lifetime lubrication, and factory-fit wheel studs.",0
"Title: Dryer Heating Element & Thermostat/Fuse Kit  
Category: Electronics  
Brand: SUMNEW  
Description: A complete replacement kit for dryer heating elements, thermostats, and thermal fuses compatible with major brands.  
Details: Includes a durable metal heating element, 279816 thermostat cut‑off, and 279973 thermal fuse for reliable dryer operation.",0
"Title: High‑Efficiency Twin‑Cylinder Air Compressor Pump Head  
Category: Industrial Equipment  
Brand: Unknown  
Description: A double‑stage V‑type air compressor pump head delivering 21 CFM at 175 PSI with 4 kW (5.5 HP) power.  
Details: Features high‑precision valve steel, strong cooling blades, low noise operation, and energy‑efficient design for reliable, fast inflation.",0
"Title: Bam France 2002XL Contoured Hightech 4/4 Violin Case  
Category: Musical Instruments  
Brand: Bam France  
Description: Ultra‑light, shock‑resistant case for 4/4 violins featuring a sleek black carbon‑look exterior and contoured interior for maximum protection.  
Details: 3.5‑lb, 30×12×9 in, three‑layer construction (AIREX, ABS, PVC), foam suspension, two bow holders, accessory pouch, and anti‑skid rubber guards.",0
"Title: Metabo HPT 36V MultiVolt Cordless Rotary Hammer  
Category: Power Tools  
Brand: Metabo HPT  
Description: A 36V brushless rotary hammer that delivers high impact energy and versatile power with both cordless and AC plug-in options.  
Details: Features Reactive Force Control for safety, three speed modes, ergonomic low-vibration handle, one-push bit change, and built-in LED lighting.",0
"Title: UltraPro 46mm Close‑Up Macro Filter Kit  
Category: Photography Accessories  
Brand: Ultra Pro  
Description: A set of four high‑resolution close‑up filters (+1, +2, +4, +10 diopters) that attach to 46 mm lenses, paired with a durable nylon carry case.  
Details: Double‑threaded design allows stacking for higher magnification and compatibility with additional optics such as polarizers; features multi‑coating for sharp, clear images.",0
"Title: CB-6 Extra Hard Chamois Bass Drum Mallet  
Category: Musical Instruments  
Brand: Innovative Percussion  
Description: A heavy, red‑oak‑handled mallet with a chamois‑covered wooden ball core for powerful, articulate bass drum strikes.  
Details: Features a felt liner, 1” handle, and a dense core that delivers a large, crisp sound.",0
"Title: Panasonic KX-DECT 6.0 PLUS Digital Cordless Phone  
Category: Electronics  
Brand: Panasonic  
Description: A single‑handset cordless phone with DECT 6.0 PLUS technology for clear, extended-range communication.  
Details: Includes a headset jack, non‑slip handset design, and eco‑friendly power‑saving mode.",0
"Title: LOVE MEI Galaxy S10 Lite Heavy Duty Shockproof Case  
Category: Electronics  
Brand: LOVE MEI  
Description: A rugged, waterproof case that combines a metal frame, silicone bumper, and built‑in tempered glass to protect the Samsung Galaxy S10 Lite from drops, dust, and splashes.  
Details: Features military‑grade impact resistance, raised edge screen protection, wireless charging compatibility, and easy button access.",0
"Title: GJY 10.6"" Portable TV with Built‑in ATSC Tuner  
Category: Electronics  
Brand: GJY  
Description: A compact 10.6"" LCD TV that works on ATSC digital signals and includes a rechargeable battery for on‑the‑go viewing.  
Details: Features dual antennas, USB/TF card slots, AV and HDMI inputs, 12V power compatibility, and built‑in speakers for versatile use in home or outdoor settings.",0
"Title: LD Products High Yield Toner Cartridge – Black  
Category: Office Supplies  
Brand: LD Products  
Description: A high-yield replacement toner cartridge designed for HP LaserJet Pro printers.  
Details: Compatible with HP LaserJet Pro M118dw, M148dw, and M148fdw, offering a 2,800-page yield and a shelf life of 24-36 months.",0
"Title: APS iBoard 6‑inch Aluminum Running Boards  
Category: Automotive Accessories  
Brand: APS  
Description: Heavy‑duty 6‑inch aluminum running boards for Nissan Frontier Crew Cab, finished in matte black powder coating.  
Details: Features anti‑slip tread, aircraft‑grade T6061 aluminum construction, and factory‑style metal backsplash with tapered ends for a sleek look.",0
"Title: PEMP E65/E66 Optical Fiber Box for BMW  
Category: Automotive Electronics  
Brand: PEMP  
Description: Adds an aux-compatible optical fiber input to BMW E65/E66 models for Android screen audio.  
Details: Connects to the car’s ACC power, replaces the CDC channel, and enables external audio playback.",0
"Title: Intermatic PX300 12V 300W Transformer with Built‑In Circuit Breaker  
Category: Electronics  
Brand: Intermatic  
Description: A 12‑V transformer that safely powers pool and garden lights with a built‑in circuit breaker.  
Details: Features a grounded shield, automatic overload protection, and a compact 7.25"" high, 5.25"" wide, 4.5"" deep enclosure.",0
"Title: Dominator Platinum RGB 32GB DDR4 3200MHz  
Category: Computer Memory  
Brand: Corsair  
Description: 32 GB of high‑performance DDR4 memory with 3200 MHz speed, designed for AMD optimized systems.  
Details: Features dual 16 GB modules, 12 individually addressable RGB LEDs, DHX cooling PCB, and Intel XMP 2.0 compatibility.",0
"Title: HK 13"" Heavy Duty Black Push-Open Cash Drawer  
Category: Retail Hardware  
Brand: HK  
Description: A compact 13"" black metal cash drawer that opens manually with a push mechanism and mounts under counter with a metal bracket.  
Details: Features a 4-bill/5-coin capacity, 2 media slots, a 3-position lock, and includes a key lock for secure operation.",0
"Title: SKB iSeries 3i-13096-6KP Camera Case  
Category: Photography Accessories  
Brand: SKB Cases  
Description: A MIL‑STD 810G waterproof case with custom foam interior designed for the Blackmagic Design Pocket Cinema Camera 6K Pro, featuring lens, battery, and memory card compartments plus an extra lens slot.  
Details: Ultra‑high‑strength polypropylene construction, gasket‑sealed, water and dust tight, with padlock loops, trigger release latches, and an automatic pressure equalization valve.",0
"Title: Bam Trekking 3027SB Black Clarinet Backpack Case  
Category: Musical Instruments  
Brand: Bam  
Description: A waterproof, lightweight backpack case that securely cradles a clarinet with a molded polyurethane foam insert for thermal shock protection.  
Details: Features 2000‑denier Cordura fabric, adjustable padded shoulder straps, a removable handle, an expandable sheet‑music pocket, and space for two barrels.",0
"Title: DEWALT 20V MAX XR Impact Driver with Bluetooth Kit  
Category: Power Tools  
Brand: DEWALT  
Description: A lightweight, 20V brushless impact driver that connects to the Tool Connect app for real‑time tracking, diagnostics, and custom settings.  
Details: Includes a 5‑Ah XR battery, charger, and a 3‑year warranty, offering variable speed, 75% longer run time, and compact 5.3‑in design for tight spaces.",0
"Title: Compact High‑Performance Mini PC  
Category: Electronics  
Brand: Kinupute  
Description: Powerful mini desktop with Intel Xeon E3‑1231v3, 16 GB RAM, 256 GB SSD, and GeForce GT 1030 2 GB GPU, running Windows 11 Pro.  
Details: Supports dual 4K displays via HDMI/DVI, dual‑band Wi‑Fi, Bluetooth 4.0, Gigabit Ethernet, and multiple USB ports for versatile gaming, office, and server use.",0
"Title: June Garden Sweet Dolly Charlotte 10"" Soft Bunny Doll  
Category: Toys & Games – Plush Toys  
Brand: June Garden  
Description: A 10‑inch ultra‑soft rabbit plush doll perfect for newborns and toddlers.  
Details: Features a removable fleece jumpsuit, embroidered eyes, and a warm smile for gentle play and imaginative role‑play.",0
"Title: Oil‑Rubbed Bronze Freestanding Tub Filler  
Category: Plumbing Fixtures  
Brand: Aolemi  
Description: A single‑handle, floor‑mounted bathtub faucet in oil‑rubbed bronze finish.  
Details: Made from solid brass, it offers a sleek, modern look with corrosion‑resistant construction and easy DIY installation.",0
"Title: Clementoni 1000‑Piece Jigsaw Puzzle – The Brilliance  
Category: Toys & Games  
Brand: Clementoni  
Description: A 1,000‑piece jigsaw puzzle featuring a vibrant art theme suitable for beginners to adults.  
Details: Designed for ages 9 and up, this puzzle offers an engaging challenge while encouraging creativity and patience.",0
"Title: Handar 10GBase‑LR SFP+ Transceiver  
Category: Networking  
Brand: Handar  
Description: 10GBase‑LR SFP+ module for single‑mode fiber, 1310 nm wavelength, supporting up to 10 km.  
Details: LC duplex connector, fully compatible with Cisco, Ubiquiti, UniFi UF‑SM‑10G and other open‑switch platforms.",0
"Title: Deco Mount Pro Tripod Mic Stand Bundle  
Category: Audio Equipment  
Brand: Deco Mount  
Description: A lightweight, adjustable tripod mic stand with a boom arm and universal pop filter for professional recording.  
Details: Features durable construction, leg adjustment for uneven surfaces, a double‑layer pop filter with goose neck, and a microfiber cleaning cloth.",0
"Title: GanFindX Portable Hand Control System  
Category: Automotive Accessories  
Brand: GanFindX  
Description: A lightweight, tool‑free hand control device that lets drivers operate the accelerator and brake with their hands.  
Details: Constructed from aluminum alloy and stainless steel, adjustable length (51‑70 cm), comes with a soft carry bag, and is compatible with most LHD/RHD vehicles.",0
"Title: 4GB DDR2 1066MHz Desktop Memory Kit  
Category: Computer Components  
Brand: Komputerbay  
Description: Dual 2GB DDR2 1066MHz modules in a 4GB kit for desktop systems.  
Details: Heatspreaders on each DIMM, 240-pin PC2-8500, dual‑channel support, lifetime warranty.",0
"Title: 3-Drawer Mobile File Cabinet  
Category: Office Furniture  
Brand: Scranton & Co  
Description: A slim, lockable file cabinet with three high‑side drawers, ideal for small home or office spaces.  
Details: Features smooth glide drawers, casters for easy mobility, and a non‑porous painted steel finish.",0
"Title: Canon EOS Rebel T7 DSLR Bundle with EF-S 18‑55mm, EF 75‑300mm, 500mm Lens & T‑Mount Adapter  
Category: Camera & Photo Equipment  
Brand: Canon  
Description: 24‑megapixel APS‑C DSLR kit featuring a versatile zoom range, 1080p video, and Wi‑Fi/NFC connectivity.  
Details: Includes EF‑mount lenses, professional accessories, and a 500mm preset lens with a T‑mount adapter for extended reach.",0
"Title: Evergreen Cylinder Head Gasket Set & Head Bolts  
Category: Automotive  
Brand: Evergreen  
Description: Premium head gasket set and head bolts engineered for precise OEM fit and superior sealing.  
Details: Made with non‑asbestos silicone rubber, Viton valve stem seals, and MLS graphite gaskets for durability and reliable performance.",0
"Title: Task Roman Ogee Router Bit 1/4"" Shank, 1"" Dia., ½"" Carbide Height, 5/32"" Radius  
Category: Power Tool Accessories  
Brand: Task  
Description: A precision double‑flute router bit that cuts smooth ogee profiles with minimal vibration.  
Details: Features a 1/4‑inch hardened steel shank, super fine grain tungsten carbide tip, and a non‑stick powder‑coat finish for long‑lasting performance.",0
"Title: Travelpro Platinum Elite Slim Business Laptop Briefcase  
Category: Accessories  
Brand: Travelpro  
Description: A sleek, durable slim briefcase that fits a 15.6"" laptop and keeps work essentials organized on the go.  
Details: Features padded laptop and tablet sleeves, multiple organizational pockets, RFID‑blocking safety pocket, genuine leather handles, stain‑ and abrasion‑resistant nylon, and an unobtrusive rear strap for easy stacking.",0
"Title: 120 V/15 A Right‑Angle GFCI Plug, Yellow  
Category: Electronics  
Brand: Coleman Cable  
Description: A rain‑proof, UL‑listed right‑angle GFCI plug that attaches to existing equipment cords.  
Details: Features a 4‑6 mA trip, <25 ms response time, and manual reset for outdoor power tools and appliances.",0
"Title: JRready Deutsch DT Series Connector Kit  
Category: Electronics  
Brand: JRready  
Description: A versatile connector kit featuring 2‑12 pin, size‑16 DT connectors with solid nickel‑plated contacts for 14‑20AWG wire.  
Details: Waterproof, dust‑proof, and corrosion‑resistant connectors with sealing plugs, a built‑in contact extraction tool, and options for in‑line, flange, or PCB mounting.",0
"Title: 15"" Oil‑Rubbed Bronze Locking Shower Head Extension Arm  
Category: Home & Garden – Bathroom Fixtures  
Brand: Neatitems  
Description: Extend and securely lock a heavy shower head 15 inches from the wall.  
Details: Made of solid brass with a durable oil‑rubbed bronze finish; easy one‑hand installation and adjustable height.",0
"Title: Mylites+ Standard Comic Book Mylar Sleeves  
Category: Electronics  
Brand: E. Gerber  
Description: 50 protective mylar sleeves for 7¼"" x 10½"" comics with 1½"" flap.  
Details: Made of archival‑grade mylar, zero off‑gassing, highly resistant to oxygen and moisture.",0
"Title: Tidal Front & Rear Fender Flares – 4‑Pack Pocket Rivet Style  
Category: Automotive Accessories  
Brand: Tidal Automotive  
Description: Rugged fender flares with a textured black finish designed for 2010‑2017 RAM 2500/3500 trucks.  
Details: Made from UV‑protected ABS plastic, these flares bolt on easily without drilling and come with all necessary mounting hardware.",0
"Title: Dakota Alert MURS Driveway Probe Sensor  
Category: Electronics  
Brand: Dakota Alert  
Description: A wireless driveway sensor that detects large metal vehicles and sends alerts to MURS receivers up to 50 feet away.  
Details: Features battery-powered operation, a 50‑foot direct‑burial cable, and false‑alarm suppression for animals and wind.",0
"Title: LED Light Kit for Lego Sonic Green Hill Zone 21331  
Category: Home & Garden > Décor > Lighting  
Brand: DALDED  
Description: Brighten your Lego Sonic Green Hill Zone set with this safe, battery‑ or USB‑powered LED kit.  
Details: Features heat‑resistant, non‑combustible wiring that can be hidden inside the model, easy installation, and suitable for ages 12 and up.",0
"Title: 152mm Bi-Metal Hole Saw  
Category: Tool Accessories  
Brand: Aoktorkit  
Description: A 152mm high‑speed steel hole saw for precise drilling in wood, metal, and plastic.  
Details: Features M42 HSS teeth, heat‑treated for durability, and a sharp, low‑vibration blade for stable hole cuts.",0
"Title: TropicalLife 18‑Inch Large Backpack  
Category: Accessories → Backpacks  
Brand: TropicalLife  
Description: A lightweight, eco‑friendly 18‑inch backpack with waterproof polyester construction.  
Details: Features a zipper main compartment, small zip pockets, two inner pockets, and two breathable side pouches for water bottles or umbrellas.",0
"Title: Wenger City Upgrade 16"" Laptop Backpack  
Category: Bags & Backpacks  
Brand: Wenger  
Description: A slim 16"" laptop backpack designed for commuters, featuring dual A4 compartments, a dedicated laptop pocket, and a tablet sleeve.  
Details: Includes two water‑resistant quick‑access front pockets, a trolley sleeve, padded back and shoulder straps, and a flexible open side pocket.",0
"Title: LED Tail Light Assembly for 2014‑2021 Toyota Tundra  
Category: Automotive Lighting  
Brand: OEM Grade  
Description: A high‑brightness LED tail light kit for Toyota Tundra pickups, featuring a black housing and clear acrylic lens.  
Details: Plug‑and‑play installation with no rewiring, waterproof construction, and full compliance with federal and international safety standards.",0
"Title: Adams Check Payment & Deposit Register – 44‑Page 8.5”×11” White  
Category: Office Supplies  
Brand: Adams  
Description: A nondated register for recording checks and deposits with ready‑to‑use forms and a summary page.  
Details: Includes 44 pages, a wire‑o spiral for flat‑laying, bank reconciliation worksheet, and a water‑resistant polypropylene cover.",0
"Title: 3D Tree Hole Stair Risers Vinyl Mural  
Category: Home Décor  
Brand: AJ  
Description: A waterproof, self‑adhesive vinyl mural that transforms stair risers into a 3D tree hole scene.  
Details: 15 × 18 cm (7″ × 37″) rectangular design suitable for stairs, walls, mirrors, doors, windows, and furniture.",0
"Title: Kohler Filtered Water Faucet  
Category: Bathroom Fixtures  
Brand: Kohler  
Description: A single‑lever, deck‑mounted faucet that delivers filtered water directly from the tap.  
Details: Features a polished chrome finish, 2.2 GPM flow rate, and lifetime warranty.",0
"Title: Fjallraven Kanken 15"" Laptop Backpack  
Category: Backpack  
Brand: Fjallraven  
Description: Classic Kanken design now sized for a 15"" laptop, featuring a padded laptop compartment, water‑resistant Vinylon F fabric, and multiple pockets for everyday items.  
Details: Comes with dual top snap handles, padded shoulder straps, a rain flap on the main zipper, and 18 L of storage space.",0
"Title: Portable 7500L Mini Projector  
Category: Electronics  
Brand: (Brand not specified)  
Description: A compact projector that delivers up to 100"" HD 1080P image with WiFi and Bluetooth connectivity.  
Details: Features 7500L LED lamp, 2400–7500 lumens, 360° stereo speakers, multiple input ports (HDMI, VGA, USB, AV) and a built‑in cooling system for extended lamp life.",0
"Title: Diversitech 1/3 HP 115V Grey Motor  
Category: Motors & Drives  
Brand: Diversitech  
Description: 115V, 1/3 horsepower motor for industrial and hobby applications.  
Details: Grey color, 7"" square footprint, 9 lb weight, efficient and easy to install.",0
"Title: Retevis RT68 Soft Earhook Walkie Talkie Earpiece  
Category: Electronics  
Brand: Retevis  
Description: Lightweight, on‑ear earpiece with integrated microphone designed for RT68 and other 2‑pin walkie talkies.  
Details: Features a soft ear hook, rotatable earplug, durable push‑to‑talk button, adjustable clip, and replaceable sponge cuff for comfort and hygiene.",0
"Title: Dual‑Intensity Amber Pindicator  
Category: Motorcycle Lighting  
Brand: Morimoto  
Description: A compact, switchback LED turn signal that toggles between bright white and amber, with optional dual‑intensity mode.  
Details: Features a custom clear lens for directional lighting, waterproof and wash‑proof construction, hard‑anodized CNC aluminum base, and CAN‑BUS compatible for modern bikes.",0
"Title: Evan‑Fischer Front Bumper Cover for 2015‑2017 BMW X3 (Primed)  
Category: Automotive Parts  
Brand: Evan Fischer  
Description: A primed front bumper cover that fits 2015‑2017 BMW X3 models, designed to accommodate standard front and side holes for surround‑view camera wiring.  
Details: Lightweight 13.79 lb cover features a durable finish, ready‑to‑install design, and a 1‑year warranty when purchased through Auto Parts Giant.",0
"Title: Laisomeke IP67 Waterproof Junction Box  
Category: Electrical Enclosures  
Brand: Laisomeke  
Description: A compact, dust‑proof, IP67 rated ABS plastic box with a clear grey cover for secure outdoor electrical connections.  
Details: Features easy screw‑in installation, durable impact resistance, and includes mounting plate, screws, and connectors.",0
"Title: Sumerain LED Waterfall Bathroom Faucet  
Category: Plumbing Fixtures  
Brand: Sumerain  
Description: A dual‑handle, widespan chrome faucet with integrated LED lighting that changes color with water temperature.  
Details: Constructed from durable brass, it includes pre‑assembled handles, valves, spout, and all necessary hardware in one unit.",0
"Title: Solar Pendant Shed Light with Remote Control  
Category: Lighting  
Brand: Webcem  
Description: Solar-powered LED pendant light for outdoor and indoor use, featuring 136 LEDs and 1000 lumens with remote control and multiple lighting modes.  
Details: IP65 waterproof, 4+1 leaf design with 90° adjustable angles, 360° solar panel rotation, and a 2‑hour, 4‑hour, or 6‑hour timer.",0
"Title: Festool Platin 2 6‑Inch S1000 Grit Sanding Discs  
Category: Construction Tools  
Brand: Festool  
Description: 15‑pack fine‑grit sanding discs for smooth, high‑gloss finishes on closed‑surface materials.  
Details: Foam‑backed, silicone carbide abrasives with stearate coating and a multi‑jetstream design for 30% longer life.",0
"Title: Western Digital 2TB Enterprise RE4-GP SATA Hard Drive  
Category: Electronics  
Brand: Western Digital  
Description: 2TB enterprise-grade 3.5"" hard drive with SATA 3 Gb/s interface.  
Details: Features 64 MB cache, IntelliPower power‑saving technology, 7200 RPM spin speed, and TLER for reliability.",0
"Title: Poison Spyder Rocker Knocker 10-08-020  
Category: Automotive Accessories  
Brand: Poison Spyder  
Description: High‑strength 3/16"" steel rocker panel protection with optional DOM tubular sliders.  
Details: CNC laser‑cut plate steel, precision fit, stainless flat‑head hardware, and durable DOM tubing for added side protection.",0
"Title: DiMarzio DP 163 BluesBucker Pickup  
Category: Musical Instruments  
Brand: DiMarzio  
Description: A humbucker‑shaped pickup that delivers P90‑style tone with virtually no hum.  
Details: Features patented Virtual Vintage and Airbucker technology, 6‑slot adjustable pole, and dual‑coil design for dynamic sensitivity.",0
"Title: VLAND LED Smoked Taillights for Toyota Camry 2012‑2014  
Category: Automotive Lighting  
Brand: VLAND  
Description: LED smoked taillight assembly compatible with 2012, 2013 and 2014 Toyota Camry.  
Details: Includes driver‑side and passenger‑side units, LED red parking/running lights with factory halogen bulbs for turn and reverse signals; DOT/SAE approved, hermetically sealed for durable performance.",0
"Title: Lighted Triangle Mirror Cabinet with Door  
Category: Bathroom Furniture  
Brand: Zheng Hui Home  
Description: A sleek white triangular mirror cabinet with built‑in LED lighting, ideal for organizing bathroom essentials while adding modern décor.  
Details: Features a durable wood construction, two doors, one drawer, and a polished finish, measuring 47 × 60 × 33 cm and wall‑mountable.",0
"Title: PM Auto Front Right Quick Complete Strut‑Coil Spring  
Category: Automotive Parts  
Brand: PM Auto  
Description: Quick‑install complete strut‑coil spring for 2018‑2021 Honda Accord L4 1.5L front right.  
Details: OEM‑quality, no disassembly of existing assembly, no specialized tools needed, and includes a limited lifetime warranty.",0
"Title: Wall Mounted Shower Faucet Set  
Category: Bathroom Fixtures  
Brand: Bestill  
Description: A complete wall-mounted shower faucet set with a single-lever valve and adjustable spray head in oil rubbed bronze.  
Details: Features a solid brass valve body with American Standard plumbing connections, a pressure-balanced ceramic disc cartridge, a 3.6"" high‑pressure showerhead with three spray options, and a 6"" stainless steel shower arm.",0
"Title: Flip Cover with Stand & Card Slot for Lenovo Tab M10 HD 10.1""  
Category: Electronics  
Brand: Yuseng  
Description: A lightweight, PU leather flip case with a folding stand, card slots, and magnetic closure for the Lenovo Tab M10 HD.  
Details: Features shock‑proof TPU, polycarbonate shell, and a secure magnetic buckle that wakes the tablet on opening.",0
"Title: Miyaya Funny Horse Mask  
Category: Costume Accessories  
Brand: Miyaya  
Description: A realistic latex horse head mask featuring a bushy mane that fits most adult heads.  
Details: Made from 100% natural, non‑toxic latex, it is breathable with eye, nose, and mouth holes for clear vision.",0
"Title: Trail Gear Twin Stick Shift Kit  
Category: Automotive Accessories  
Brand: Trail Gear  
Description: A high‑performance twin‑stick kit that enables independent control of high and low transfer‑case gears.  
Details: Features polished cast aluminum shifter bases, heat‑treated steel keys, and an oil breather for reliable, ready‑to‑install performance.",0
"Title: Allmotorparts Engine Thermostat for Honda  
Category: Auto Parts  
Brand: Allmotorparts  
Description: Replacement thermostat designed to regulate engine temperature for a wide range of Honda models from 1990-2020.  
Details: Features a stainless‑steel mounting flange and spring frame for durable, OE‑level performance.",0
"Title: Ultra Duster Canned Air Net – 10 oz 6‑Pack  
Category: Electronics Cleaning Supplies  
Brand: Electronics More  
Description: Powerful, ozone‑safe canned air that removes dust and micro‑debris from electronic devices without residue.  
Details: Each can delivers fine‑spray compressed air via a straw nozzle, contains a bitterant to prevent abuse, and ships in one business day.",0
"Title: Beck/Arnley Air Filter  
Category: Automotive Accessories  
Brand: Beck/Arnley  
Description: A high‑performance air filter that matches OE form, fit, and function for specific vehicle models.  
Details: Constructed with premium filter materials for optimal airflow, durable build for underhood conditions, and designed for vehicle‑specific fit.",0
"Title: Dell Optiplex 390 19"" Desktop Bundle  
Category: Computer & Peripherals  
Brand: Dell  
Description: All-in-one Dell Optiplex 390 desktop with i3 processor, 4 GB RAM, 1 TB HDD, Windows 10 Home and 19"" monitor.  
Details: Includes Wi‑Fi adapter, keyboard, and mouse for immediate use.",0
"Title: IQShield LiquidSkin Screen Protector  
Category: Electronics  
Brand: IQShield  
Description: Ultra‑thin, bubble‑free TPU film that fully covers the Samsung Galaxy S5 Sport screen.  
Details: Features self‑healing, anti‑scratch protection, true‑feel sensitivity, UV‑protected clarity, and a lifetime replacement warranty.",0
"Title: 12 Pack Military Toy Soldiers Action Figures  
Category: Toys & Games  
Brand: Liberty Imports  
Description: A set of twelve realistic army soldiers with weapons and accessories for imaginative battle play.  
Details: Each 4‑inch figure offers 10 points of articulation and comes with a range of combat gear for dynamic, story‑driven adventures.",0
"Title: Neporal Full Spectrum 6000K A19 LED Light Bulbs (Pack of 3)  
Category: Electronics  
Brand: Neporal  
Description: Energy‑efficient full spectrum LED bulbs that mimic natural daylight to boost focus and comfort.  
Details: Each 9W bulb delivers 800 lumens, high CRI 85, 60W equivalent, and lasts 30,000 hours.",0
"Title: Pidoko Kids Train Table – Grey 90‑Piece Train Set  
Category: Toys & Games  
Brand: Pidoko Kids  
Description: A sturdy, large wooden train table with a 90‑piece train set, ideal for children aged 3 and up.  
Details: Features round edges, non‑toxic paint, and dimensions 37.4"" × 22.04"" × 15.8"", compatible with most brand tracks.",0
"Title: Satco 4-Count LED A19 Light Bulbs  
Category: Lighting  
Brand: Satco  
Description: Four non‑dimmable, 9.5W LED bulbs replacing 60W incandescent, warm white, 2700K.  
Details: 800 lumens each, 80° beam spread, E26 medium base, damp‑location rated, 10,000‑hour life.",0
"Title: Ceramic Talavera Mexican Tile 4x4"" – 9‑Piece Set  
Category: Home Décor  
Brand: DRT Wholesales  
Description: Bright, hand‑fired Talavera tiles that instantly add vibrant color to any wall.  
Details: Each 4"" square is fired above 2000°F for durability, easy cleaning, and long‑term color retention.",0
"Title: Archangel 6‑Inch Action Figure  
Category: Toys & Games  
Brand: Hasbro  
Description: A collectible 6‑inch figure of Archangel from Marvel’s X‑Men.  
Details: Features dynamic pose and detailed paintwork, suitable for ages 4+.",0
"Title: Stick‑On Dressage Course Letters  
Category: Equestrian Supplies  
Brand: Intrepid International  
Description: Eight waterproof vinyl letters with adhesive backing for easy placement on dressage markers.  
Details: Each set includes English‑style letters (A, B, C, E, F, H, K, M) and measures 7.9 × 7.7 × 0.4 in., weighing 0.25 lb.",0
"Title: LEGO Marvel Avengers War Machine Buster  
Category: Toys  
Brand: LEGO  
Description: Build the posable War Machine Buster mech with an opening cockpit, rapid shooter, cannons, and missiles.  
Details: Includes 4 minifigures (War Machine, Ant‑Man, and two Outriders) and 362 pieces.",0
"Title: ANZO USA 111207 Crystal Headlights  
Category: Automotive Lighting  
Brand: ANZO USA  
Description: Black crystal headlights with halo and LED amber lighting for GMC Sierra 99‑06/Yukon/XL 00‑06/Denali models.  
Details: Features halogen bulbs, waterproof design, and a clear lens.",0
"Title: Kingston Brass Clawfoot Tub Faucet  
Category: Bathroom Fixtures  
Brand: Kingston Brass  
Description: A wall‑mounted clawfoot tub faucet in brushed nickel, crafted from solid brass for durable, vintage style.  
Details: Features a drip‑free ceramic disc cartridge, adjustable mounting range, and a 7‑in. spout with an included 59‑inch handheld shower.",0
"Title: EMART 10ft Adjustable C‑Stand with Boom Arm  
Category: Photography Equipment  
Brand: EMART  
Description: Heavy‑duty aluminum C‑stand with a 10‑ft adjustable center stand and a 4.2‑ft boom arm for lighting and reflector setups.  
Details: Features a built‑in buffer spring, turtle base with sandbag slots, and 1/4”/3/8” screw grips for secure mounting and easy transport.",0
"Title: KOHLER K--CP Slider Assembly  
Category: Kitchen & Bath Fixtures  
Brand: KOHLER  
Description: A polished chrome metal slider assembly that holds kitchen sink faucet attachments for easy access.  
Details: Lightweight 8‑ounce unit measures 5 × 3 × 1 in., includes one component, and is not discontinued.",0
"Title: KUNN Compact Electrician Tool Pouch  
Category: Tools  
Brand: KUNN  
Description: A durable, zip‑top pouch that holds up to 17 small tools, perfect for electricians and tradespeople.  
Details: Features a sturdy hard bottom, top drawstring closure, adjustable shoulder strap, and versatile clips for belt attachment.",0
"Title: Trim Kit for 2‑Handle Shower & Tub Valve (Delta/Peerless)  
Category: Plumbing Fixtures  
Brand: Plumb USA  
Description: A complete trim kit that converts a Delta or Peerless washerless 2‑handle shower faucet to a brushed nickel finish.  
Details: Includes two metal lever handles, flanges, sleeves, a showerhead, and a diverter spout for a modern, elegant look.",0
"Title: iPhone 12/12 Pro Nicaragua Guardabarranco Case  
Category: Electronics  
Brand: Nicaraguense  
Description: A durable bumper case featuring the Nicaraguan Guardabarranco bird.  
Details: Made of scratch‑resistant polycarbonate and shock‑absorbent TPU for heavy‑duty protection.",0
"Title: Custom Replacement Infrared Remote  
Category: Electronics  
Brand: REDI REMOTE  
Description: A no‑programming required infrared remote designed to replace specific models of units.  
Details: Features 58 buttons, measures 7½""×2¼""×¾"", uses four AAA batteries, and includes a sliding cover for lower buttons.",0
"Title: KS K-STORM Silicone Mushroom EarTips  
Category: Accessories  
Brand: KS K-STORM  
Description: Replacement silicone ear tips for acoustic tube earpieces.  
Details: Made from durable silicone, fits standard tube earpieces for both left and right ears, and requires no modification.",0
"Title: Pioneer 2‑Handle Kitchen Faucet  
Category: Plumbing  
Brand: Pioneer  
Description: A deck‑mount two‑handle kitchen faucet with a 1.5 GPM flow rate and 360° swivel spout.  
Details: Features PVD brushed nickel finish, ceramic‑disc cartridges, side‑spray assembly, and ADA compliance.",0
"Title: Water‑Resistant USB Laptop Backpack for Teens  
Category: Accessories  
Brand: LSSAGOON  
Description: A stylish, waterproof daypack that fits a 15.4‑inch laptop and includes an external USB charging port.  
Details: Features breathable straps, adjustable waist belt, multiple pockets, and a cute Pompon keychain.",0
"Title: Grey Pneumatic 1311SD 8‑Point Impact Socket Set  
Category: Tools & Equipment  
Brand: Grey Pneumatic  
Description: A lightweight 11‑piece impact socket set featuring 1/2"" to 1‑1/8"" deep‑length 8‑point sockets.  
Details: Made from high‑strength chromoly alloy steel, the set includes a GP High Torque Drive design for enhanced durability and a lifetime warranty.",0
"Title: Aeromotive X1 Adjustable Fuel Regulator  
Category: Fuel System Components  
Brand: Aeromotive  
Description: Adjustable fuel regulator for carbureted or EFI systems, ranging 3‑15 psi.  
Details: Features dual 0.08″ inlet/outlet ports, 0.08″ return port, 0.313″ bypass, and NPT gauge/boost ports.",0
"Title: Walker Exhaust Ultra EPA 16478 Direct Fit Catalytic Converter  
Category: Automotive Parts  
Brand: Walker  
Description: Direct‑fit catalytic converter with integrated exhaust manifold for OBDII vehicles (1996+), meeting EPA emissions standards.  
Details: Features a durable OE‑style design, thick flanges, heat‑shielded manifold, and a 25,000‑mile/40,000‑km warranty.",0
```


---

<a id="file-week6-human-out-csv"></a>
## File: `week6/human_out.csv`

> **Path in repository:** `week6/human_out.csv`

```csv
"Title: Excess V2 Distortion/Modulation Pedal  
Category: Music Pedals  
Brand: Old Blood Noise  
Description: A versatile pedal offering distortion and three modulation modes—delay, chorus, and harmonized fifths—with full control over signal routing and expression.  
Details: Features include separate gain, tone, and volume controls; time, depth, and volume per modulation; order switching, soft‑touch bypass, and expression jack for dynamic control.",120
"Title: Telpo Headlight Assembly for 2015‑2017 Toyota Camry  
Category: Automotive Accessories  
Brand: Telpo  
Description: Dual headlight assembly that fits the 2015‑2017 Toyota Camry front driver and passenger sides.  
Details: Direct replacement with DOT & SAE‑certified lenses, high/low beam, waterproof construction, and a 1‑year limited warranty.",300
"Title: NewPower99 6000 mAh Battery Replacement Kit for Samsung Galaxy Tab S3 9.7  
Category: Electronics  
Brand: NewPower99  
Description: Replace or backup the battery on your Samsung Galaxy Tab S3 9.7 with a 6000 mAh lithium‑polymer pack.  
Details: Includes a new battery, step‑by‑step video instructions, special opening tools, and a one‑year money‑back guarantee.",43
"Title: EXMAX NG-10X Fresnel Lens Focusing Adapter  
Category: Lighting Accessories  
Brand: EXMAX  
Description: A telescoping Bowens‑mount adapter that concentrates LED studio light into a 10–40° spot, boosting brightness 5–10× and offering quick color filter swaps.  
Details: Features a durable black plastic construction, adjustable focus, integrated four‑color gel filters, and compatibility with most LED or flash lights up to 150 W.",55
"Title: Raven Pro Document Scanner Stand  
Category: Accessories  
Brand: Raven  
Description: Elevates the Raven Pro Document Scanner to provide a comfortable seated viewing angle.  
Details: Enhances visibility of the LCD touchscreen for easy use and includes a stable, compact design.",12
"Title: UPC RBC12-UPC Replacement Battery Cartridge  
Category: Electronics  
Brand: UPC  
Description: A precharged, maintenance‑free lead‑acid battery cartridge for APC RBC12 UPS systems that delivers reliable power during outages.  
Details: Sealed, leak‑proof design with all connectors, cable, and fuses included for instant plug‑and‑play, hot‑swappable installation, and a 2‑year limited warranty.",220
"Title: Lexmark X651 Compatible Toner Cartridge – Black, 1 Pack  
Category: Office Supplies  
Brand: SuppliesOutlet  
Description: High‑yield, OEM‑compatible toner cartridge for Lexmark X651 series, delivering up to 25,000 pages.  
Details: Features a 1‑year performance guarantee, 25,000 page yield at 5% coverage, and uses high‑quality new/recycled components.",25
"Title: ACDelco GM FW339 Front Wheel Hub & Bearing Assembly  
Category: Automotive Parts  
Brand: ACDelco  
Description: Original equipment wheel hub and bearing assembly with integrated wheel speed sensor for GM vehicles.  
Details: Features dual sealed ball bearings, lifetime lubrication, and factory-fit wheel studs.",80
"Title: Dryer Heating Element & Thermostat/Fuse Kit  
Category: Electronics  
Brand: SUMNEW  
Description: A complete replacement kit for dryer heating elements, thermostats, and thermal fuses compatible with major brands.  
Details: Includes a durable metal heating element, 279816 thermostat cut‑off, and 279973 thermal fuse for reliable dryer operation.",30
"Title: High‑Efficiency Twin‑Cylinder Air Compressor Pump Head  
Category: Industrial Equipment  
Brand: Unknown  
Description: A double‑stage V‑type air compressor pump head delivering 21 CFM at 175 PSI with 4 kW (5.5 HP) power.  
Details: Features high‑precision valve steel, strong cooling blades, low noise operation, and energy‑efficient design for reliable, fast inflation.",60
"Title: Bam France 2002XL Contoured Hightech 4/4 Violin Case  
Category: Musical Instruments  
Brand: Bam France  
Description: Ultra‑light, shock‑resistant case for 4/4 violins featuring a sleek black carbon‑look exterior and contoured interior for maximum protection.  
Details: 3.5‑lb, 30×12×9 in, three‑layer construction (AIREX, ABS, PVC), foam suspension, two bow holders, accessory pouch, and anti‑skid rubber guards.",70
"Title: Metabo HPT 36V MultiVolt Cordless Rotary Hammer  
Category: Power Tools  
Brand: Metabo HPT  
Description: A 36V brushless rotary hammer that delivers high impact energy and versatile power with both cordless and AC plug-in options.  
Details: Features Reactive Force Control for safety, three speed modes, ergonomic low-vibration handle, one-push bit change, and built-in LED lighting.",50
"Title: UltraPro 46mm Close‑Up Macro Filter Kit  
Category: Photography Accessories  
Brand: Ultra Pro  
Description: A set of four high‑resolution close‑up filters (+1, +2, +4, +10 diopters) that attach to 46 mm lenses, paired with a durable nylon carry case.  
Details: Double‑threaded design allows stacking for higher magnification and compatibility with additional optics such as polarizers; features multi‑coating for sharp, clear images.",35
"Title: CB-6 Extra Hard Chamois Bass Drum Mallet  
Category: Musical Instruments  
Brand: Innovative Percussion  
Description: A heavy, red‑oak‑handled mallet with a chamois‑covered wooden ball core for powerful, articulate bass drum strikes.  
Details: Features a felt liner, 1” handle, and a dense core that delivers a large, crisp sound.",28
"Title: Panasonic KX-DECT 6.0 PLUS Digital Cordless Phone  
Category: Electronics  
Brand: Panasonic  
Description: A single‑handset cordless phone with DECT 6.0 PLUS technology for clear, extended-range communication.  
Details: Includes a headset jack, non‑slip handset design, and eco‑friendly power‑saving mode.",55
"Title: LOVE MEI Galaxy S10 Lite Heavy Duty Shockproof Case  
Category: Electronics  
Brand: LOVE MEI  
Description: A rugged, waterproof case that combines a metal frame, silicone bumper, and built‑in tempered glass to protect the Samsung Galaxy S10 Lite from drops, dust, and splashes.  
Details: Features military‑grade impact resistance, raised edge screen protection, wireless charging compatibility, and easy button access.",15
"Title: GJY 10.6"" Portable TV with Built‑in ATSC Tuner  
Category: Electronics  
Brand: GJY  
Description: A compact 10.6"" LCD TV that works on ATSC digital signals and includes a rechargeable battery for on‑the‑go viewing.  
Details: Features dual antennas, USB/TF card slots, AV and HDMI inputs, 12V power compatibility, and built‑in speakers for versatile use in home or outdoor settings.",50
"Title: LD Products High Yield Toner Cartridge – Black  
Category: Office Supplies  
Brand: LD Products  
Description: A high-yield replacement toner cartridge designed for HP LaserJet Pro printers.  
Details: Compatible with HP LaserJet Pro M118dw, M148dw, and M148fdw, offering a 2,800-page yield and a shelf life of 24-36 months.",25
"Title: APS iBoard 6‑inch Aluminum Running Boards  
Category: Automotive Accessories  
Brand: APS  
Description: Heavy‑duty 6‑inch aluminum running boards for Nissan Frontier Crew Cab, finished in matte black powder coating.  
Details: Features anti‑slip tread, aircraft‑grade T6061 aluminum construction, and factory‑style metal backsplash with tapered ends for a sleek look.",185
"Title: PEMP E65/E66 Optical Fiber Box for BMW  
Category: Automotive Electronics  
Brand: PEMP  
Description: Adds an aux-compatible optical fiber input to BMW E65/E66 models for Android screen audio.  
Details: Connects to the car’s ACC power, replaces the CDC channel, and enables external audio playback.",66
"Title: Intermatic PX300 12V 300W Transformer with Built‑In Circuit Breaker  
Category: Electronics  
Brand: Intermatic  
Description: A 12‑V transformer that safely powers pool and garden lights with a built‑in circuit breaker.  
Details: Features a grounded shield, automatic overload protection, and a compact 7.25"" high, 5.25"" wide, 4.5"" deep enclosure.",99
"Title: Dominator Platinum RGB 32GB DDR4 3200MHz  
Category: Computer Memory  
Brand: Corsair  
Description: 32 GB of high‑performance DDR4 memory with 3200 MHz speed, designed for AMD optimized systems.  
Details: Features dual 16 GB modules, 12 individually addressable RGB LEDs, DHX cooling PCB, and Intel XMP 2.0 compatibility.",250
"Title: HK 13"" Heavy Duty Black Push-Open Cash Drawer  
Category: Retail Hardware  
Brand: HK  
Description: A compact 13"" black metal cash drawer that opens manually with a push mechanism and mounts under counter with a metal bracket.  
Details: Features a 4-bill/5-coin capacity, 2 media slots, a 3-position lock, and includes a key lock for secure operation.",110
"Title: SKB iSeries 3i-13096-6KP Camera Case  
Category: Photography Accessories  
Brand: SKB Cases  
Description: A MIL‑STD 810G waterproof case with custom foam interior designed for the Blackmagic Design Pocket Cinema Camera 6K Pro, featuring lens, battery, and memory card compartments plus an extra lens slot.  
Details: Ultra‑high‑strength polypropylene construction, gasket‑sealed, water and dust tight, with padlock loops, trigger release latches, and an automatic pressure equalization valve.",48
"Title: Bam Trekking 3027SB Black Clarinet Backpack Case  
Category: Musical Instruments  
Brand: Bam  
Description: A waterproof, lightweight backpack case that securely cradles a clarinet with a molded polyurethane foam insert for thermal shock protection.  
Details: Features 2000‑denier Cordura fabric, adjustable padded shoulder straps, a removable handle, an expandable sheet‑music pocket, and space for two barrels.",59
"Title: DEWALT 20V MAX XR Impact Driver with Bluetooth Kit  
Category: Power Tools  
Brand: DEWALT  
Description: A lightweight, 20V brushless impact driver that connects to the Tool Connect app for real‑time tracking, diagnostics, and custom settings.  
Details: Includes a 5‑Ah XR battery, charger, and a 3‑year warranty, offering variable speed, 75% longer run time, and compact 5.3‑in design for tight spaces.",55
"Title: Compact High‑Performance Mini PC  
Category: Electronics  
Brand: Kinupute  
Description: Powerful mini desktop with Intel Xeon E3‑1231v3, 16 GB RAM, 256 GB SSD, and GeForce GT 1030 2 GB GPU, running Windows 11 Pro.  
Details: Supports dual 4K displays via HDMI/DVI, dual‑band Wi‑Fi, Bluetooth 4.0, Gigabit Ethernet, and multiple USB ports for versatile gaming, office, and server use.",550
"Title: June Garden Sweet Dolly Charlotte 10"" Soft Bunny Doll  
Category: Toys & Games – Plush Toys  
Brand: June Garden  
Description: A 10‑inch ultra‑soft rabbit plush doll perfect for newborns and toddlers.  
Details: Features a removable fleece jumpsuit, embroidered eyes, and a warm smile for gentle play and imaginative role‑play.",14
"Title: Oil‑Rubbed Bronze Freestanding Tub Filler  
Category: Plumbing Fixtures  
Brand: Aolemi  
Description: A single‑handle, floor‑mounted bathtub faucet in oil‑rubbed bronze finish.  
Details: Made from solid brass, it offers a sleek, modern look with corrosion‑resistant construction and easy DIY installation.",200
"Title: Clementoni 1000‑Piece Jigsaw Puzzle – The Brilliance  
Category: Toys & Games  
Brand: Clementoni  
Description: A 1,000‑piece jigsaw puzzle featuring a vibrant art theme suitable for beginners to adults.  
Details: Designed for ages 9 and up, this puzzle offers an engaging challenge while encouraging creativity and patience.",29
"Title: Handar 10GBase‑LR SFP+ Transceiver  
Category: Networking  
Brand: Handar  
Description: 10GBase‑LR SFP+ module for single‑mode fiber, 1310 nm wavelength, supporting up to 10 km.  
Details: LC duplex connector, fully compatible with Cisco, Ubiquiti, UniFi UF‑SM‑10G and other open‑switch platforms.",50
"Title: Deco Mount Pro Tripod Mic Stand Bundle  
Category: Audio Equipment  
Brand: Deco Mount  
Description: A lightweight, adjustable tripod mic stand with a boom arm and universal pop filter for professional recording.  
Details: Features durable construction, leg adjustment for uneven surfaces, a double‑layer pop filter with goose neck, and a microfiber cleaning cloth.",55
"Title: GanFindX Portable Hand Control System  
Category: Automotive Accessories  
Brand: GanFindX  
Description: A lightweight, tool‑free hand control device that lets drivers operate the accelerator and brake with their hands.  
Details: Constructed from aluminum alloy and stainless steel, adjustable length (51‑70 cm), comes with a soft carry bag, and is compatible with most LHD/RHD vehicles.",195
"Title: 4GB DDR2 1066MHz Desktop Memory Kit  
Category: Computer Components  
Brand: Komputerbay  
Description: Dual 2GB DDR2 1066MHz modules in a 4GB kit for desktop systems.  
Details: Heatspreaders on each DIMM, 240-pin PC2-8500, dual‑channel support, lifetime warranty.",89
"Title: 3-Drawer Mobile File Cabinet  
Category: Office Furniture  
Brand: Scranton & Co  
Description: A slim, lockable file cabinet with three high‑side drawers, ideal for small home or office spaces.  
Details: Features smooth glide drawers, casters for easy mobility, and a non‑porous painted steel finish.",125
"Title: Canon EOS Rebel T7 DSLR Bundle with EF-S 18‑55mm, EF 75‑300mm, 500mm Lens & T‑Mount Adapter  
Category: Camera & Photo Equipment  
Brand: Canon  
Description: 24‑megapixel APS‑C DSLR kit featuring a versatile zoom range, 1080p video, and Wi‑Fi/NFC connectivity.  
Details: Includes EF‑mount lenses, professional accessories, and a 500mm preset lens with a T‑mount adapter for extended reach.",400
"Title: Evergreen Cylinder Head Gasket Set & Head Bolts  
Category: Automotive  
Brand: Evergreen  
Description: Premium head gasket set and head bolts engineered for precise OEM fit and superior sealing.  
Details: Made with non‑asbestos silicone rubber, Viton valve stem seals, and MLS graphite gaskets for durability and reliable performance.",35
"Title: Task Roman Ogee Router Bit 1/4"" Shank, 1"" Dia., ½"" Carbide Height, 5/32"" Radius  
Category: Power Tool Accessories  
Brand: Task  
Description: A precision double‑flute router bit that cuts smooth ogee profiles with minimal vibration.  
Details: Features a 1/4‑inch hardened steel shank, super fine grain tungsten carbide tip, and a non‑stick powder‑coat finish for long‑lasting performance.",45
"Title: Travelpro Platinum Elite Slim Business Laptop Briefcase  
Category: Accessories  
Brand: Travelpro  
Description: A sleek, durable slim briefcase that fits a 15.6"" laptop and keeps work essentials organized on the go.  
Details: Features padded laptop and tablet sleeves, multiple organizational pockets, RFID‑blocking safety pocket, genuine leather handles, stain‑ and abrasion‑resistant nylon, and an unobtrusive rear strap for easy stacking.",28
"Title: 120 V/15 A Right‑Angle GFCI Plug, Yellow  
Category: Electronics  
Brand: Coleman Cable  
Description: A rain‑proof, UL‑listed right‑angle GFCI plug that attaches to existing equipment cords.  
Details: Features a 4‑6 mA trip, <25 ms response time, and manual reset for outdoor power tools and appliances.",5
"Title: JRready Deutsch DT Series Connector Kit  
Category: Electronics  
Brand: JRready  
Description: A versatile connector kit featuring 2‑12 pin, size‑16 DT connectors with solid nickel‑plated contacts for 14‑20AWG wire.  
Details: Waterproof, dust‑proof, and corrosion‑resistant connectors with sealing plugs, a built‑in contact extraction tool, and options for in‑line, flange, or PCB mounting.",39
"Title: 15"" Oil‑Rubbed Bronze Locking Shower Head Extension Arm  
Category: Home & Garden – Bathroom Fixtures  
Brand: Neatitems  
Description: Extend and securely lock a heavy shower head 15 inches from the wall.  
Details: Made of solid brass with a durable oil‑rubbed bronze finish; easy one‑hand installation and adjustable height.",29
"Title: Mylites+ Standard Comic Book Mylar Sleeves  
Category: Electronics  
Brand: E. Gerber  
Description: 50 protective mylar sleeves for 7¼"" x 10½"" comics with 1½"" flap.  
Details: Made of archival‑grade mylar, zero off‑gassing, highly resistant to oxygen and moisture.",12
"Title: Tidal Front & Rear Fender Flares – 4‑Pack Pocket Rivet Style  
Category: Automotive Accessories  
Brand: Tidal Automotive  
Description: Rugged fender flares with a textured black finish designed for 2010‑2017 RAM 2500/3500 trucks.  
Details: Made from UV‑protected ABS plastic, these flares bolt on easily without drilling and come with all necessary mounting hardware.",100
"Title: Dakota Alert MURS Driveway Probe Sensor  
Category: Electronics  
Brand: Dakota Alert  
Description: A wireless driveway sensor that detects large metal vehicles and sends alerts to MURS receivers up to 50 feet away.  
Details: Features battery-powered operation, a 50‑foot direct‑burial cable, and false‑alarm suppression for animals and wind.",70
"Title: LED Light Kit for Lego Sonic Green Hill Zone 21331  
Category: Home & Garden > Décor > Lighting  
Brand: DALDED  
Description: Brighten your Lego Sonic Green Hill Zone set with this safe, battery‑ or USB‑powered LED kit.  
Details: Features heat‑resistant, non‑combustible wiring that can be hidden inside the model, easy installation, and suitable for ages 12 and up.",29
"Title: 152mm Bi-Metal Hole Saw  
Category: Tool Accessories  
Brand: Aoktorkit  
Description: A 152mm high‑speed steel hole saw for precise drilling in wood, metal, and plastic.  
Details: Features M42 HSS teeth, heat‑treated for durability, and a sharp, low‑vibration blade for stable hole cuts.",49
"Title: TropicalLife 18‑Inch Large Backpack  
Category: Accessories → Backpacks  
Brand: TropicalLife  
Description: A lightweight, eco‑friendly 18‑inch backpack with waterproof polyester construction.  
Details: Features a zipper main compartment, small zip pockets, two inner pockets, and two breathable side pouches for water bottles or umbrellas.",50
"Title: Wenger City Upgrade 16"" Laptop Backpack  
Category: Bags & Backpacks  
Brand: Wenger  
Description: A slim 16"" laptop backpack designed for commuters, featuring dual A4 compartments, a dedicated laptop pocket, and a tablet sleeve.  
Details: Includes two water‑resistant quick‑access front pockets, a trolley sleeve, padded back and shoulder straps, and a flexible open side pocket.",30
"Title: LED Tail Light Assembly for 2014‑2021 Toyota Tundra  
Category: Automotive Lighting  
Brand: OEM Grade  
Description: A high‑brightness LED tail light kit for Toyota Tundra pickups, featuring a black housing and clear acrylic lens.  
Details: Plug‑and‑play installation with no rewiring, waterproof construction, and full compliance with federal and international safety standards.",120
"Title: Adams Check Payment & Deposit Register – 44‑Page 8.5”×11” White  
Category: Office Supplies  
Brand: Adams  
Description: A nondated register for recording checks and deposits with ready‑to‑use forms and a summary page.  
Details: Includes 44 pages, a wire‑o spiral for flat‑laying, bank reconciliation worksheet, and a water‑resistant polypropylene cover.",10
"Title: 3D Tree Hole Stair Risers Vinyl Mural  
Category: Home Décor  
Brand: AJ  
Description: A waterproof, self‑adhesive vinyl mural that transforms stair risers into a 3D tree hole scene.  
Details: 15 × 18 cm (7″ × 37″) rectangular design suitable for stairs, walls, mirrors, doors, windows, and furniture.",19
"Title: Kohler Filtered Water Faucet  
Category: Bathroom Fixtures  
Brand: Kohler  
Description: A single‑lever, deck‑mounted faucet that delivers filtered water directly from the tap.  
Details: Features a polished chrome finish, 2.2 GPM flow rate, and lifetime warranty.",65
"Title: Fjallraven Kanken 15"" Laptop Backpack  
Category: Backpack  
Brand: Fjallraven  
Description: Classic Kanken design now sized for a 15"" laptop, featuring a padded laptop compartment, water‑resistant Vinylon F fabric, and multiple pockets for everyday items.  
Details: Comes with dual top snap handles, padded shoulder straps, a rain flap on the main zipper, and 18 L of storage space.",45
"Title: Portable 7500L Mini Projector  
Category: Electronics  
Brand: (Brand not specified)  
Description: A compact projector that delivers up to 100"" HD 1080P image with WiFi and Bluetooth connectivity.  
Details: Features 7500L LED lamp, 2400–7500 lumens, 360° stereo speakers, multiple input ports (HDMI, VGA, USB, AV) and a built‑in cooling system for extended lamp life.",120
"Title: Diversitech 1/3 HP 115V Grey Motor  
Category: Motors & Drives  
Brand: Diversitech  
Description: 115V, 1/3 horsepower motor for industrial and hobby applications.  
Details: Grey color, 7"" square footprint, 9 lb weight, efficient and easy to install.",100
"Title: Retevis RT68 Soft Earhook Walkie Talkie Earpiece  
Category: Electronics  
Brand: Retevis  
Description: Lightweight, on‑ear earpiece with integrated microphone designed for RT68 and other 2‑pin walkie talkies.  
Details: Features a soft ear hook, rotatable earplug, durable push‑to‑talk button, adjustable clip, and replaceable sponge cuff for comfort and hygiene.",15
"Title: Dual‑Intensity Amber Pindicator  
Category: Motorcycle Lighting  
Brand: Morimoto  
Description: A compact, switchback LED turn signal that toggles between bright white and amber, with optional dual‑intensity mode.  
Details: Features a custom clear lens for directional lighting, waterproof and wash‑proof construction, hard‑anodized CNC aluminum base, and CAN‑BUS compatible for modern bikes.",30
"Title: Evan‑Fischer Front Bumper Cover for 2015‑2017 BMW X3 (Primed)  
Category: Automotive Parts  
Brand: Evan Fischer  
Description: A primed front bumper cover that fits 2015‑2017 BMW X3 models, designed to accommodate standard front and side holes for surround‑view camera wiring.  
Details: Lightweight 13.79 lb cover features a durable finish, ready‑to‑install design, and a 1‑year warranty when purchased through Auto Parts Giant.",80
"Title: Laisomeke IP67 Waterproof Junction Box  
Category: Electrical Enclosures  
Brand: Laisomeke  
Description: A compact, dust‑proof, IP67 rated ABS plastic box with a clear grey cover for secure outdoor electrical connections.  
Details: Features easy screw‑in installation, durable impact resistance, and includes mounting plate, screws, and connectors.",40
"Title: Sumerain LED Waterfall Bathroom Faucet  
Category: Plumbing Fixtures  
Brand: Sumerain  
Description: A dual‑handle, widespan chrome faucet with integrated LED lighting that changes color with water temperature.  
Details: Constructed from durable brass, it includes pre‑assembled handles, valves, spout, and all necessary hardware in one unit.",120
"Title: Solar Pendant Shed Light with Remote Control  
Category: Lighting  
Brand: Webcem  
Description: Solar-powered LED pendant light for outdoor and indoor use, featuring 136 LEDs and 1000 lumens with remote control and multiple lighting modes.  
Details: IP65 waterproof, 4+1 leaf design with 90° adjustable angles, 360° solar panel rotation, and a 2‑hour, 4‑hour, or 6‑hour timer.",95
"Title: Festool Platin 2 6‑Inch S1000 Grit Sanding Discs  
Category: Construction Tools  
Brand: Festool  
Description: 15‑pack fine‑grit sanding discs for smooth, high‑gloss finishes on closed‑surface materials.  
Details: Foam‑backed, silicone carbide abrasives with stearate coating and a multi‑jetstream design for 30% longer life.",110
"Title: Western Digital 2TB Enterprise RE4-GP SATA Hard Drive  
Category: Electronics  
Brand: Western Digital  
Description: 2TB enterprise-grade 3.5"" hard drive with SATA 3 Gb/s interface.  
Details: Features 64 MB cache, IntelliPower power‑saving technology, 7200 RPM spin speed, and TLER for reliability.",50
"Title: Poison Spyder Rocker Knocker 10-08-020  
Category: Automotive Accessories  
Brand: Poison Spyder  
Description: High‑strength 3/16"" steel rocker panel protection with optional DOM tubular sliders.  
Details: CNC laser‑cut plate steel, precision fit, stainless flat‑head hardware, and durable DOM tubing for added side protection.",30
"Title: DiMarzio DP 163 BluesBucker Pickup  
Category: Musical Instruments  
Brand: DiMarzio  
Description: A humbucker‑shaped pickup that delivers P90‑style tone with virtually no hum.  
Details: Features patented Virtual Vintage and Airbucker technology, 6‑slot adjustable pole, and dual‑coil design for dynamic sensitivity.",30
"Title: VLAND LED Smoked Taillights for Toyota Camry 2012‑2014  
Category: Automotive Lighting  
Brand: VLAND  
Description: LED smoked taillight assembly compatible with 2012, 2013 and 2014 Toyota Camry.  
Details: Includes driver‑side and passenger‑side units, LED red parking/running lights with factory halogen bulbs for turn and reverse signals; DOT/SAE approved, hermetically sealed for durable performance.",80
"Title: Lighted Triangle Mirror Cabinet with Door  
Category: Bathroom Furniture  
Brand: Zheng Hui Home  
Description: A sleek white triangular mirror cabinet with built‑in LED lighting, ideal for organizing bathroom essentials while adding modern décor.  
Details: Features a durable wood construction, two doors, one drawer, and a polished finish, measuring 47 × 60 × 33 cm and wall‑mountable.",90
"Title: PM Auto Front Right Quick Complete Strut‑Coil Spring  
Category: Automotive Parts  
Brand: PM Auto  
Description: Quick‑install complete strut‑coil spring for 2018‑2021 Honda Accord L4 1.5L front right.  
Details: OEM‑quality, no disassembly of existing assembly, no specialized tools needed, and includes a limited lifetime warranty.",50
"Title: Wall Mounted Shower Faucet Set  
Category: Bathroom Fixtures  
Brand: Bestill  
Description: A complete wall-mounted shower faucet set with a single-lever valve and adjustable spray head in oil rubbed bronze.  
Details: Features a solid brass valve body with American Standard plumbing connections, a pressure-balanced ceramic disc cartridge, a 3.6"" high‑pressure showerhead with three spray options, and a 6"" stainless steel shower arm.",110
"Title: Flip Cover with Stand & Card Slot for Lenovo Tab M10 HD 10.1""  
Category: Electronics  
Brand: Yuseng  
Description: A lightweight, PU leather flip case with a folding stand, card slots, and magnetic closure for the Lenovo Tab M10 HD.  
Details: Features shock‑proof TPU, polycarbonate shell, and a secure magnetic buckle that wakes the tablet on opening.",15
"Title: Miyaya Funny Horse Mask  
Category: Costume Accessories  
Brand: Miyaya  
Description: A realistic latex horse head mask featuring a bushy mane that fits most adult heads.  
Details: Made from 100% natural, non‑toxic latex, it is breathable with eye, nose, and mouth holes for clear vision.",19
"Title: Trail Gear Twin Stick Shift Kit  
Category: Automotive Accessories  
Brand: Trail Gear  
Description: A high‑performance twin‑stick kit that enables independent control of high and low transfer‑case gears.  
Details: Features polished cast aluminum shifter bases, heat‑treated steel keys, and an oil breather for reliable, ready‑to‑install performance.",350
"Title: Allmotorparts Engine Thermostat for Honda  
Category: Auto Parts  
Brand: Allmotorparts  
Description: Replacement thermostat designed to regulate engine temperature for a wide range of Honda models from 1990-2020.  
Details: Features a stainless‑steel mounting flange and spring frame for durable, OE‑level performance.",95
"Title: Ultra Duster Canned Air Net – 10 oz 6‑Pack  
Category: Electronics Cleaning Supplies  
Brand: Electronics More  
Description: Powerful, ozone‑safe canned air that removes dust and micro‑debris from electronic devices without residue.  
Details: Each can delivers fine‑spray compressed air via a straw nozzle, contains a bitterant to prevent abuse, and ships in one business day.",9
"Title: Beck/Arnley Air Filter  
Category: Automotive Accessories  
Brand: Beck/Arnley  
Description: A high‑performance air filter that matches OE form, fit, and function for specific vehicle models.  
Details: Constructed with premium filter materials for optimal airflow, durable build for underhood conditions, and designed for vehicle‑specific fit.",45
"Title: Dell Optiplex 390 19"" Desktop Bundle  
Category: Computer & Peripherals  
Brand: Dell  
Description: All-in-one Dell Optiplex 390 desktop with i3 processor, 4 GB RAM, 1 TB HDD, Windows 10 Home and 19"" monitor.  
Details: Includes Wi‑Fi adapter, keyboard, and mouse for immediate use.",350
"Title: IQShield LiquidSkin Screen Protector  
Category: Electronics  
Brand: IQShield  
Description: Ultra‑thin, bubble‑free TPU film that fully covers the Samsung Galaxy S5 Sport screen.  
Details: Features self‑healing, anti‑scratch protection, true‑feel sensitivity, UV‑protected clarity, and a lifetime replacement warranty.",15
"Title: 12 Pack Military Toy Soldiers Action Figures  
Category: Toys & Games  
Brand: Liberty Imports  
Description: A set of twelve realistic army soldiers with weapons and accessories for imaginative battle play.  
Details: Each 4‑inch figure offers 10 points of articulation and comes with a range of combat gear for dynamic, story‑driven adventures.",12
"Title: Neporal Full Spectrum 6000K A19 LED Light Bulbs (Pack of 3)  
Category: Electronics  
Brand: Neporal  
Description: Energy‑efficient full spectrum LED bulbs that mimic natural daylight to boost focus and comfort.  
Details: Each 9W bulb delivers 800 lumens, high CRI 85, 60W equivalent, and lasts 30,000 hours.",15
"Title: Pidoko Kids Train Table – Grey 90‑Piece Train Set  
Category: Toys & Games  
Brand: Pidoko Kids  
Description: A sturdy, large wooden train table with a 90‑piece train set, ideal for children aged 3 and up.  
Details: Features round edges, non‑toxic paint, and dimensions 37.4"" × 22.04"" × 15.8"", compatible with most brand tracks.",120
"Title: Satco 4-Count LED A19 Light Bulbs  
Category: Lighting  
Brand: Satco  
Description: Four non‑dimmable, 9.5W LED bulbs replacing 60W incandescent, warm white, 2700K.  
Details: 800 lumens each, 80° beam spread, E26 medium base, damp‑location rated, 10,000‑hour life.",19
"Title: Ceramic Talavera Mexican Tile 4x4"" – 9‑Piece Set  
Category: Home Décor  
Brand: DRT Wholesales  
Description: Bright, hand‑fired Talavera tiles that instantly add vibrant color to any wall.  
Details: Each 4"" square is fired above 2000°F for durability, easy cleaning, and long‑term color retention.",35
"Title: Archangel 6‑Inch Action Figure  
Category: Toys & Games  
Brand: Hasbro  
Description: A collectible 6‑inch figure of Archangel from Marvel’s X‑Men.  
Details: Features dynamic pose and detailed paintwork, suitable for ages 4+.",25
"Title: Stick‑On Dressage Course Letters  
Category: Equestrian Supplies  
Brand: Intrepid International  
Description: Eight waterproof vinyl letters with adhesive backing for easy placement on dressage markers.  
Details: Each set includes English‑style letters (A, B, C, E, F, H, K, M) and measures 7.9 × 7.7 × 0.4 in., weighing 0.25 lb.",20
"Title: LEGO Marvel Avengers War Machine Buster  
Category: Toys  
Brand: LEGO  
Description: Build the posable War Machine Buster mech with an opening cockpit, rapid shooter, cannons, and missiles.  
Details: Includes 4 minifigures (War Machine, Ant‑Man, and two Outriders) and 362 pieces.",50
"Title: ANZO USA 111207 Crystal Headlights  
Category: Automotive Lighting  
Brand: ANZO USA  
Description: Black crystal headlights with halo and LED amber lighting for GMC Sierra 99‑06/Yukon/XL 00‑06/Denali models.  
Details: Features halogen bulbs, waterproof design, and a clear lens.",250
"Title: Kingston Brass Clawfoot Tub Faucet  
Category: Bathroom Fixtures  
Brand: Kingston Brass  
Description: A wall‑mounted clawfoot tub faucet in brushed nickel, crafted from solid brass for durable, vintage style.  
Details: Features a drip‑free ceramic disc cartridge, adjustable mounting range, and a 7‑in. spout with an included 59‑inch handheld shower.",380
"Title: EMART 10ft Adjustable C‑Stand with Boom Arm  
Category: Photography Equipment  
Brand: EMART  
Description: Heavy‑duty aluminum C‑stand with a 10‑ft adjustable center stand and a 4.2‑ft boom arm for lighting and reflector setups.  
Details: Features a built‑in buffer spring, turtle base with sandbag slots, and 1/4”/3/8” screw grips for secure mounting and easy transport.",125
"Title: KOHLER K--CP Slider Assembly  
Category: Kitchen & Bath Fixtures  
Brand: KOHLER  
Description: A polished chrome metal slider assembly that holds kitchen sink faucet attachments for easy access.  
Details: Lightweight 8‑ounce unit measures 5 × 3 × 1 in., includes one component, and is not discontinued.",43
"Title: KUNN Compact Electrician Tool Pouch  
Category: Tools  
Brand: KUNN  
Description: A durable, zip‑top pouch that holds up to 17 small tools, perfect for electricians and tradespeople.  
Details: Features a sturdy hard bottom, top drawstring closure, adjustable shoulder strap, and versatile clips for belt attachment.",39
"Title: Trim Kit for 2‑Handle Shower & Tub Valve (Delta/Peerless)  
Category: Plumbing Fixtures  
Brand: Plumb USA  
Description: A complete trim kit that converts a Delta or Peerless washerless 2‑handle shower faucet to a brushed nickel finish.  
Details: Includes two metal lever handles, flanges, sleeves, a showerhead, and a diverter spout for a modern, elegant look.",50
"Title: iPhone 12/12 Pro Nicaragua Guardabarranco Case  
Category: Electronics  
Brand: Nicaraguense  
Description: A durable bumper case featuring the Nicaraguan Guardabarranco bird.  
Details: Made of scratch‑resistant polycarbonate and shock‑absorbent TPU for heavy‑duty protection.",15
"Title: Custom Replacement Infrared Remote  
Category: Electronics  
Brand: REDI REMOTE  
Description: A no‑programming required infrared remote designed to replace specific models of units.  
Details: Features 58 buttons, measures 7½""×2¼""×¾"", uses four AAA batteries, and includes a sliding cover for lower buttons.",19
"Title: KS K-STORM Silicone Mushroom EarTips  
Category: Accessories  
Brand: KS K-STORM  
Description: Replacement silicone ear tips for acoustic tube earpieces.  
Details: Made from durable silicone, fits standard tube earpieces for both left and right ears, and requires no modification.",9
"Title: Pioneer 2‑Handle Kitchen Faucet  
Category: Plumbing  
Brand: Pioneer  
Description: A deck‑mount two‑handle kitchen faucet with a 1.5 GPM flow rate and 360° swivel spout.  
Details: Features PVD brushed nickel finish, ceramic‑disc cartridges, side‑spray assembly, and ADA compliance.",75
"Title: Water‑Resistant USB Laptop Backpack for Teens  
Category: Accessories  
Brand: LSSAGOON  
Description: A stylish, waterproof daypack that fits a 15.4‑inch laptop and includes an external USB charging port.  
Details: Features breathable straps, adjustable waist belt, multiple pockets, and a cute Pompon keychain.",32
"Title: Grey Pneumatic 1311SD 8‑Point Impact Socket Set  
Category: Tools & Equipment  
Brand: Grey Pneumatic  
Description: A lightweight 11‑piece impact socket set featuring 1/2"" to 1‑1/8"" deep‑length 8‑point sockets.  
Details: Made from high‑strength chromoly alloy steel, the set includes a GP High Torque Drive design for enhanced durability and a lifetime warranty.",35
"Title: Aeromotive X1 Adjustable Fuel Regulator  
Category: Fuel System Components  
Brand: Aeromotive  
Description: Adjustable fuel regulator for carbureted or EFI systems, ranging 3‑15 psi.  
Details: Features dual 0.08″ inlet/outlet ports, 0.08″ return port, 0.313″ bypass, and NPT gauge/boost ports.",120
"Title: Walker Exhaust Ultra EPA 16478 Direct Fit Catalytic Converter  
Category: Automotive Parts  
Brand: Walker  
Description: Direct‑fit catalytic converter with integrated exhaust manifold for OBDII vehicles (1996+), meeting EPA emissions standards.  
Details: Features a durable OE‑style design, thick flanges, heat‑shielded manifold, and a 25,000‑mile/40,000‑km warranty.",220
```


---

<a id="file-week6-pricer-batch-py"></a>
## File: `week6/pricer/batch.py`

> **Path in repository:** `week6/pricer/batch.py`

```python
import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import json
import pickle
from functools import cache
from tqdm.notebook import tqdm

load_dotenv(override=True)


@cache
def groq():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))


MODEL = "openai/gpt-oss-20b"
BATCHES_FOLDER = "batches"
OUTPUT_FOLDER = "output"
state = Path("batches.pkl")

SYSTEM_PROMPT = """Create a concise description of a product. Respond only in this format. Do not include part numbers.
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features"""


class Batch:
    BATCH_SIZE = 1_000

    batches = []

    def __init__(self, items, start, end, lite):
        self.items = items
        self.start = start
        self.end = end
        self.filename = f"{start}_{end}.jsonl"
        self.file_id = None
        self.batch_id = None
        self.output_file_id = None
        self.done = False
        folder = Path("lite") if lite else Path("full")
        self.batches = folder / BATCHES_FOLDER
        self.output = folder / OUTPUT_FOLDER
        self.batches.mkdir(parents=True, exist_ok=True)
        self.output.mkdir(parents=True, exist_ok=True)

    def make_jsonl(self, item):
        body = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": item.full},
            ],
            "reasoning_effort": "low",
        }
        line = {
            "custom_id": str(item.id),
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": body,
        }
        return json.dumps(line)

    def make_file(self):
        batch_file = self.batches / self.filename
        with batch_file.open("w", encoding="utf-8") as f:
            for item in self.items[self.start : self.end]:
                f.write(self.make_jsonl(item))
                f.write("\n")

    def send_file(self):
        batch_file = self.batches / self.filename
        with batch_file.open("rb") as f:
            response = groq().files.create(file=f, purpose="batch")
        self.file_id = response.id

    def submit_batch(self):
        response = groq().batches.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id=self.file_id,
        )
        self.batch_id = response.id

    def is_ready(self):
        response = groq().batches.retrieve(self.batch_id)
        status = response.status
        if status == "completed":
            self.output_file_id = response.output_file_id
        return status == "completed"

    def fetch_output(self):
        output_file = str(self.output / self.filename)
        response = groq().files.content(self.output_file_id)
        response.write_to_file(output_file)

    def apply_output(self):
        output_file = str(self.output / self.filename)
        with open(output_file, "r", encoding="utf-8") as f:
            for line in f:
                json_line = json.loads(line)
                id = int(json_line["custom_id"])
                summary = json_line["response"]["body"]["choices"][0]["message"]["content"]
                self.items[id].summary = summary
        self.done = True

    @classmethod
    def create(cls, items, lite):
        for start in range(0, len(items), cls.BATCH_SIZE):
            end = min(start + cls.BATCH_SIZE, len(items))
            batch = Batch(items, start, end, lite)
            cls.batches.append(batch)
        print(f"Created {len(cls.batches)} batches")

    @classmethod
    def run(cls):
        for batch in tqdm(cls.batches):
            batch.make_file()
            batch.send_file()
            batch.submit_batch()
        print(f"Submitted {len(cls.batches)} batches")

    @classmethod
    def fetch(cls):
        for batch in tqdm(cls.batches):
            if not batch.done:
                if batch.is_ready():
                    batch.fetch_output()
                    batch.apply_output()
        finished = [batch for batch in cls.batches if batch.done]
        print(f"Finished {len(finished)} of {len(cls.batches)} batches")

    @classmethod
    def save(cls):
        items = cls.batches[0].items
        for batch in cls.batches:
            batch.items = None
        with state.open("wb") as f:
            pickle.dump(cls.batches, f)
        for batch in cls.batches:
            batch.items = items
        print(f"Saved {len(cls.batches)} batches")

    @classmethod
    def load(cls, items):
        with state.open("rb") as f:
            cls.batches = pickle.load(f)
        for batch in cls.batches:
            batch.items = items
        print(f"Loaded {len(cls.batches)} batches")
```


---

<a id="file-week6-pricer-deep-neural-network-py"></a>
## File: `week6/pricer/deep_neural_network.py`

> **Path in repository:** `week6/pricer/deep_neural_network.py`

```python
import numpy as np
from tqdm.notebook import tqdm
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from torch.optim.lr_scheduler import CosineAnnealingLR
from sklearn.feature_extraction.text import HashingVectorizer


class ResidualBlock(nn.Module):
    def __init__(self, hidden_size, dropout_prob):
        super(ResidualBlock, self).__init__()
        self.block = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.LayerNorm(hidden_size),
            nn.ReLU(),
            nn.Dropout(dropout_prob),
            nn.Linear(hidden_size, hidden_size),
            nn.LayerNorm(hidden_size),
        )
        self.relu = nn.ReLU()

    def forward(self, x):
        residual = x
        out = self.block(x)
        out += residual  # Skip connection
        return self.relu(out)


class DeepNeuralNetwork(nn.Module):
    def __init__(self, input_size, num_layers=10, hidden_size=4096, dropout_prob=0.2):
        super(DeepNeuralNetwork, self).__init__()

        # First layer
        self.input_layer = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.LayerNorm(hidden_size),
            nn.ReLU(),
            nn.Dropout(dropout_prob),
        )

        # Residual blocks
        self.residual_blocks = nn.ModuleList()
        for i in range(num_layers - 2):
            self.residual_blocks.append(ResidualBlock(hidden_size, dropout_prob))

        # Output layer
        self.output_layer = nn.Linear(hidden_size, 1)

    def forward(self, x):
        x = self.input_layer(x)

        for block in self.residual_blocks:
            x = block(x)

        return self.output_layer(x)


class DeepNeuralNetworkRunner:
    def __init__(self, train, val):
        self.train_data = train
        self.val_data = val
        self.vectorizer = None
        self.model = None
        self.device = None
        self.loss_function = None
        self.optimizer = None
        self.scheduler = None
        self.train_dataset = None
        self.train_loader = None
        self.y_mean = None
        self.y_std = None

        np.random.seed(42)
        torch.manual_seed(42)
        torch.cuda.manual_seed(42)

    def setup(self):
        self.vectorizer = HashingVectorizer(n_features=5000, stop_words="english", binary=True)

        train_documents = [item.summary for item in self.train_data]
        X_train_np = self.vectorizer.fit_transform(train_documents)
        self.X_train = torch.FloatTensor(X_train_np.toarray())
        y_train_np = np.array([float(item.price) for item in self.train_data])
        self.y_train = torch.FloatTensor(y_train_np).unsqueeze(1)

        val_documents = [item.summary for item in self.val_data]
        X_val_np = self.vectorizer.transform(val_documents)
        self.X_val = torch.FloatTensor(X_val_np.toarray())
        y_val_np = np.array([float(item.price) for item in self.val_data])
        self.y_val = torch.FloatTensor(y_val_np).unsqueeze(1)

        y_train_log = torch.log(self.y_train + 1)
        y_val_log = torch.log(self.y_val + 1)
        self.y_mean = y_train_log.mean()
        self.y_std = y_train_log.std()
        self.y_train_norm = (y_train_log - self.y_mean) / self.y_std
        self.y_val_norm = (y_val_log - self.y_mean) / self.y_std

        self.model = DeepNeuralNetwork(self.X_train.shape[1])
        total_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print(f"Deep Neural Network created with {total_params:,} parameters")

        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        print(f"Using {self.device}")

        self.model.to(self.device)
        self.loss_function = nn.L1Loss()
        self.optimizer = optim.AdamW(self.model.parameters(), lr=0.001, weight_decay=0.01)
        self.scheduler = CosineAnnealingLR(self.optimizer, T_max=10, eta_min=0)

        self.train_dataset = TensorDataset(self.X_train, self.y_train_norm)
        self.train_loader = DataLoader(self.train_dataset, batch_size=64, shuffle=True)

    def train(self, epochs=5):
        for epoch in range(1, epochs + 1):
            self.model.train()
            train_losses = []

            for batch_X, batch_y in tqdm(self.train_loader):
                batch_X = batch_X.to(self.device)
                batch_y = batch_y.to(self.device)

                self.optimizer.zero_grad()
                outputs = self.model(batch_X)
                loss = self.loss_function(outputs, batch_y)
                loss.backward()

                # Gradient clipping
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)

                self.optimizer.step()
                train_losses.append(loss.item())

            # Validation
            self.model.eval()
            with torch.no_grad():
                val_outputs = self.model(self.X_val.to(self.device))
                val_loss = self.loss_function(val_outputs, self.y_val_norm.to(self.device))

                # Convert back to original scale for meaningful metrics
                val_outputs_orig = torch.exp(val_outputs * self.y_std + self.y_mean) - 1
                mae = torch.abs(val_outputs_orig - self.y_val.to(self.device)).mean()

            avg_train_loss = np.mean(train_losses)
            print(f"Epoch [{epoch}/{epochs}]")
            print(f"Train Loss: {avg_train_loss:.4f}, Val Loss: {val_loss.item():.4f}")
            print(f"Val mean absolute error: ${mae.item():.2f}")
            print(f"Learning rate: {self.scheduler.get_last_lr()[0]:.6f}")

            self.scheduler.step()

    def save(self, path):
        torch.save(self.model.state_dict(), path)

    def load(self, path, device="mps"):
        self.model.load_state_dict(torch.load(path, map_location=device))
        self.model.to(self.device)

    def inference(self, item):
        self.model.eval()
        with torch.no_grad():
            vector = self.vectorizer.transform([item.summary])
            vector = torch.FloatTensor(vector.toarray()).to(self.device)
            pred = self.model(vector)[0]
            result = torch.exp(pred * self.y_std + self.y_mean) - 1
            result = result.item()
        return max(0, result)
```


---

<a id="file-week6-pricer-evaluator-py"></a>
## File: `week6/pricer/evaluator.py`

> **Path in repository:** `week6/pricer/evaluator.py`

```python
import re
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from itertools import accumulate
import math
from tqdm.notebook import tqdm
from concurrent.futures import ThreadPoolExecutor

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
COLOR_MAP = {"red": RED, "orange": YELLOW, "green": GREEN}

WORKERS = 5
DEFAULT_SIZE = 200


class Tester:
    def __init__(self, predictor, data, title=None, size=DEFAULT_SIZE, workers=WORKERS):
        self.predictor = predictor
        self.data = data
        self.title = title or self.make_title(predictor)
        self.size = size
        self.titles = []
        self.guesses = []
        self.truths = []
        self.errors = []
        self.colors = []
        self.workers = workers

    @staticmethod
    def make_title(predictor) -> str:
        return predictor.__name__.replace("__", ".").replace("_", " ").title().replace("Gpt", "GPT")

    @staticmethod
    def post_process(value):
        if isinstance(value, str):
            value = value.replace("$", "").replace(",", "")
            match = re.search(r"[-+]?\d*\.\d+|\d+", value)
            return float(match.group()) if match else 0
        else:
            return value

    def color_for(self, error, truth):
        if error < 40 or error / truth < 0.2:
            return "green"
        elif error < 80 or error / truth < 0.4:
            return "orange"
        else:
            return "red"

    def run_datapoint(self, i):
        datapoint = self.data[i]
        value = self.predictor(datapoint)
        guess = self.post_process(value)
        truth = datapoint.price
        error = abs(guess - truth)
        color = self.color_for(error, truth)
        title = datapoint.title if len(datapoint.title) <= 40 else datapoint.title[:40] + "..."
        return title, guess, truth, error, color

    def chart(self, title):
        df = pd.DataFrame(
            {
                "truth": self.truths,
                "guess": self.guesses,
                "title": self.titles,
                "error": self.errors,
                "color": self.colors,
            }
        )

        # Pre-format hover text
        df["hover"] = [
            f"{t}\nGuess=${g:,.2f} Actual=${y:,.2f}"
            for t, g, y in zip(df["title"], df["guess"], df["truth"])
        ]

        max_val = float(max(df["truth"].max(), df["guess"].max()))

        fig = px.scatter(
            df,
            x="truth",
            y="guess",
            color="color",
            color_discrete_map={"green": "green", "orange": "orange", "red": "red"},
            title=title,
            labels={"truth": "Actual Price", "guess": "Predicted Price"},
            width=1000,
            height=800,
        )

        # Assign customdata per trace (one color/category = one trace)
        for tr in fig.data:
            mask = df["color"] == tr.name
            tr.customdata = df.loc[mask, ["hover"]].to_numpy()
            tr.hovertemplate = "%{customdata[0]}<extra></extra>"
            tr.marker.update(size=6)

        # Reference line y=x
        fig.add_trace(
            go.Scatter(
                x=[0, max_val],
                y=[0, max_val],
                mode="lines",
                line=dict(width=2, dash="dash", color="deepskyblue"),
                name="y = x",
                hoverinfo="skip",
                showlegend=False,
            )
        )

        fig.update_xaxes(range=[0, max_val])
        fig.update_yaxes(range=[0, max_val])
        fig.update_layout(showlegend=False)
        fig.show()

    def error_trend_chart(self):
        n = len(self.errors)

        # Running mean and std (pure Python)
        running_sums = list(accumulate(self.errors))
        x = list(range(1, n + 1))
        running_means = [s / i for s, i in zip(running_sums, x)]

        running_squares = list(accumulate(e * e for e in self.errors))
        running_stds = [
            math.sqrt((sq_sum / i) - (mean**2)) if i > 1 else 0
            for i, sq_sum, mean in zip(x, running_squares, running_means)
        ]

        # 95% confidence interval for mean
        ci = [1.96 * (sd / math.sqrt(i)) if i > 1 else 0 for i, sd in zip(x, running_stds)]
        upper = [m + c for m, c in zip(running_means, ci)]
        lower = [m - c for m, c in zip(running_means, ci)]

        # Plot
        fig = go.Figure()

        # Shaded confidence interval band
        fig.add_trace(
            go.Scatter(
                x=x + x[::-1],
                y=upper + lower[::-1],
                fill="toself",
                fillcolor="rgba(128,128,128,0.2)",
                line=dict(color="rgba(255,255,255,0)"),
                hoverinfo="skip",
                showlegend=False,
                name="95% CI",
            )
        )

        # Main line with hover text showing CI
        fig.add_trace(
            go.Scatter(
                x=x,
                y=running_means,
                mode="lines",
                line=dict(width=3, color="firebrick"),
                name="Cumulative Avg Error",
                customdata=list(
                    zip(
                        ci,
                    )
                ),
                hovertemplate=(
                    "n=%{x}<br>"
                    "Avg Error=$%{y:,.2f}<br>"
                    "±95% CI=$%{customdata[0]:,.2f}<extra></extra>"
                ),
            )
        )

        # Title with final stats
        final_mean = running_means[-1]
        final_ci = ci[-1]
        title = f"{self.title} Error: ${final_mean:,.2f} ± ${final_ci:,.2f}"

        fig.update_layout(
            title=title,
            xaxis_title="Number of Datapoints",
            yaxis_title="Average Absolute Error ($)",
            width=1000,
            height=360,
            template="plotly_white",
            showlegend=False,
        )

        fig.show()

    def report(self):
        average_error = sum(self.errors) / self.size
        mse = mean_squared_error(self.truths, self.guesses)
        r2 = r2_score(self.truths, self.guesses) * 100
        title = f"{self.title} results<br><b>Error:</b> ${average_error:,.2f} <b>MSE:</b> {mse:,.0f} <b>r²:</b> {r2:.1f}%"
        self.error_trend_chart()
        self.chart(title)

    def run(self):
        with ThreadPoolExecutor(max_workers=self.workers) as ex:
            for title, guess, truth, error, color in tqdm(
                ex.map(self.run_datapoint, range(self.size)), total=self.size
            ):
                self.titles.append(title)
                self.guesses.append(guess)
                self.truths.append(truth)
                self.errors.append(error)
                self.colors.append(color)
                print(f"{COLOR_MAP[color]}${error:.0f} ", end="")
        self.report()


def evaluate(function, data, size=DEFAULT_SIZE, workers=WORKERS):
    Tester(function, data, size=size, workers=workers).run()
```


---

<a id="file-week6-pricer-items-py"></a>
## File: `week6/pricer/items.py`

> **Path in repository:** `week6/pricer/items.py`

```python
from pydantic import BaseModel
from datasets import Dataset, DatasetDict, load_dataset
from typing import Optional, Self


PREFIX = "Price is $"
QUESTION = "What does this cost to the nearest dollar?"


class Item(BaseModel):
    """
    An Item is a data-point of a Product with a Price
    """

    title: str
    category: str
    price: float
    full: Optional[str] = None
    weight: Optional[float] = None
    summary: Optional[str] = None
    prompt: Optional[str] = None
    id: Optional[int] = None

    def make_prompt(self, text: str):
        self.prompt = f"{QUESTION}\n\n{text}\n\n{PREFIX}{round(self.price)}.00"

    def test_prompt(self) -> str:
        return self.prompt.split(PREFIX)[0] + PREFIX

    def __repr__(self) -> str:
        return f"<{self.title} = ${self.price}>"

    @staticmethod
    def push_to_hub(dataset_name: str, train: list[Self], val: list[Self], test: list[Self]):
        """Push Item lists to HuggingFace Hub"""
        DatasetDict(
            {
                "train": Dataset.from_list([item.model_dump() for item in train]),
                "validation": Dataset.from_list([item.model_dump() for item in val]),
                "test": Dataset.from_list([item.model_dump() for item in test]),
            }
        ).push_to_hub(dataset_name)

    @classmethod
    def from_hub(cls, dataset_name: str) -> tuple[list[Self], list[Self], list[Self]]:
        """Load from HuggingFace Hub and reconstruct Items"""
        ds = load_dataset(dataset_name)
        return (
            [cls.model_validate(row) for row in ds["train"]],
            [cls.model_validate(row) for row in ds["validation"]],
            [cls.model_validate(row) for row in ds["test"]],
        )
```


---

<a id="file-week6-pricer-loaders-py"></a>
## File: `week6/pricer/loaders.py`

> **Path in repository:** `week6/pricer/loaders.py`

```python
from datetime import datetime
from tqdm import tqdm
from datasets import load_dataset
from concurrent.futures import ProcessPoolExecutor
from pricer.parser import parse
import os

CHUNK_SIZE = 1000

cpu_count = os.cpu_count()
WORKERS = max(cpu_count - 1, 1)


class ItemLoader:
    def __init__(self, category):
        self.category = category
        self.dataset = None

    def from_datapoint(self, datapoint):
        """
        Try to create an Item from this datapoint
        Return the Item if successful, or None if it shouldn't be included
        """
        return parse(datapoint, self.category)

    def from_chunk(self, chunk):
        """
        Create a list of Items from this chunk of elements from the Dataset
        """
        batch = [self.from_datapoint(datapoint) for datapoint in chunk]
        return [item for item in batch if item is not None]

    def chunk_generator(self):
        """
        Iterate over the Dataset, yielding chunks of datapoints at a time
        """
        size = len(self.dataset)
        for i in range(0, size, CHUNK_SIZE):
            yield self.dataset.select(range(i, min(i + CHUNK_SIZE, size)))

    def load_in_parallel(self, workers):
        """
        Use concurrent.futures to farm out the work to process chunks of datapoints -
        This speeds up processing significantly, but will tie up your computer while it's doing so!
        """
        results = []
        chunk_count = (len(self.dataset) // CHUNK_SIZE) + 1
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for batch in tqdm(pool.map(self.from_chunk, self.chunk_generator()), total=chunk_count):
                results.extend(batch)
        return results

    def load(self, workers=WORKERS):
        """
        Load in this dataset; the workers parameter specifies how many processes
        should work on loading and scrubbing the data
        """
        start = datetime.now()
        print(f"Loading dataset {self.category}", flush=True)
        self.dataset = load_dataset(
            "McAuley-Lab/Amazon-Reviews-2023",
            f"raw_meta_{self.category}",
            split="full",
            trust_remote_code=True,
        )
        results = self.load_in_parallel(workers)
        finish = datetime.now()
        print(
            f"Completed {self.category} with {len(results):,} datapoints in {(finish - start).total_seconds() / 60:.1f} mins",
            flush=True,
        )
        return results
```


---

<a id="file-week6-pricer-parser-py"></a>
## File: `week6/pricer/parser.py`

> **Path in repository:** `week6/pricer/parser.py`

```python
from pricer.items import Item
import json
import re

MIN_CHARS = 600
MIN_PRICE = 0.5
MAX_PRICE = 999.49
MAX_TEXT_EACH = 3000
MAX_TEXT_TOTAL = 4000

REMOVALS = [
    "Part Number",
    "Best Sellers Rank",
    "Batteries Included?",
    "Batteries Required?",
    "Item model number",
]


def simplify(text_list) -> str:
    """
    Return a simplified string without too much whitespace and limited to MAX_TEXT characters
    """
    return (
        str(text_list)
        .replace("\n", " ")
        .replace("\r", "")
        .replace("\t", "")
        .replace("  ", " ")
        .strip()[:MAX_TEXT_EACH]
    )


def scrub(title, description, features, details) -> str:
    """
    Return a cleansed full string with product numbers and unimportant details removed
    """
    for remove in REMOVALS:
        details.pop(remove, None)
    result = title + "\n"
    if description:
        result += simplify(description) + "\n"
    if features:
        result += simplify(features) + "\n"
    if details:
        result += json.dumps(details) + "\n"
    pattern = r"\b(?=[A-Z0-9]{7,}\b)(?=.*[A-Z])(?=.*\d)[A-Z0-9]+\b"
    return re.sub(pattern, "", result).strip()[:MAX_TEXT_TOTAL]


def get_weight(details):
    weight_str = details.get("Item Weight")
    if weight_str:
        parts = weight_str.split(" ")
        amount = float(parts[0])
        unit = parts[1].lower()
        if unit == "pounds":
            return amount
        elif unit == "ounces":
            return amount / 16
        elif unit == "grams":
            return amount / 453.592
        elif unit == "milligrams":
            return amount / 453592
        elif unit == "kilograms":
            return amount / 0.453592
        elif unit == "hundredths" and parts[2].lower() == "pounds":
            return amount / 100
    return 0


def parse(datapoint, category):
    try:
        price = float(datapoint["price"])
    except ValueError:
        return None
    if MIN_PRICE <= price <= MAX_PRICE:
        title = datapoint["title"]
        description = datapoint["description"]
        features = datapoint["features"]
        details = json.loads(datapoint["details"])
        weight = get_weight(details)
        full = scrub(title, description, features, details)
        if len(full) >= MIN_CHARS:
            return Item(
                title=title,
                category=category,
                price=price,
                full=full,
                weight=weight,
            )
```


---

<a id="file-week6-pricer-preprocessor-py"></a>
## File: `week6/pricer/preprocessor.py`

> **Path in repository:** `week6/pricer/preprocessor.py`

```python
from litellm import completion

DEFAULT_MODEL_NAME = "groq/openai/gpt-oss-20b"
DEFAULT_REASONING_EFFORT = "low"

SYSTEM_PROMPT = """Create a concise description of a product. Respond only in this format. Do not include part numbers.
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features"""


class Preprocessor:
    def __init__(self, model_name=DEFAULT_MODEL_NAME, reasoning_effort=DEFAULT_REASONING_EFFORT):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0
        self.model_name = model_name
        self.reasoning_effort = reasoning_effort

    def messages_for(self, text: str) -> list[dict]:
        return [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": text}]

    def preprocess(self, text: str) -> str:
        messages = self.messages_for(text)
        response = completion(
            messages=messages, model=self.model_name, reasoning_effort=self.reasoning_effort
        )
        self.total_input_tokens += response.usage.prompt_tokens
        self.total_output_tokens += response.usage.completion_tokens
        self.total_cost += response._hidden_params["response_cost"]
        return response.choices[0].message.content
```


---

<a id="file-week6-redemption-run-ipynb"></a>
## File: `week6/redemption_run.ipynb`

> **Path in repository:** `week6/redemption_run.ipynb`

# Week 6 Optional Extra - Deep Neural Network

Just to redeem ourselves from the disappointing result

I trained the Deep Neural Network in pricer/deep_neural_network.py and I've uploaded weights here. Download this file to the week6 directory:

The file `deep_neural_network.pth` here:

https://drive.google.com/drive/folders/1uq5C9edPIZ1973dArZiEO-VE13F7m8MK?usp=drive_link

```python
from dotenv import load_dotenv
import os
from huggingface_hub import login
from pricer.evaluator import evaluate
from pricer.deep_neural_network import DeepNeuralNetworkRunner
from pricer.items import Item
```

```python
# environment

LITE_MODE = False

load_dotenv(override=True)
hf_token = os.environ['HF_TOKEN']
login(hf_token, add_to_git_credential=True)
```

```python
username = "ed-donner"
dataset = f"{username}/items_lite" if LITE_MODE else f"{username}/items_full"

train, val, test = Item.from_hub(dataset)

print(f"Loaded {len(train):,} training items, {len(val):,} validation items, {len(test):,} test items")
```

```python
runner = DeepNeuralNetworkRunner(train, val[:1000])
runner.setup()
```

## If you want to train this yourself

Then run this - it takes about 4 hours on my M1 Mac hammering the GPU:

```python
runner.train(epochs=5)
runner.save('deep_neural_network.pth')
```

## Or just download the file `deep_neural_network.pth` here:

https://drive.google.com/drive/folders/1uq5C9edPIZ1973dArZiEO-VE13F7m8MK?usp=drive_link

And put it in this week6 directory.

```python
#runner.load('deep_neural_network.pth')                          # to load on a MAC
runner.load('deep_neural_network.pth', 'cpu')                   # use this one if want to load on a Win PC device --- if so comment out the line above
```

```python
def deep_neural_network(item):
    return runner.inference(item)

evaluate(deep_neural_network, test)
```


---

<a id="file-week6-redemption-train-ipynb"></a>
## File: `week6/redemption_train.ipynb`

> **Path in repository:** `week6/redemption_train.ipynb`

# Week 6 Optional Extra - Deep Neural Network

Just to redeem ourselves from the disappointing result

This is very optional to run yourself! Switch to the other notebook redemption_run to load the trained file and run it!

```python
from dotenv import load_dotenv
import os
from huggingface_hub import login
from pricer.evaluator import evaluate
from pricer.deep_neural_network import DeepNeuralNetworkRunner
from pricer.items import Item
```

```python
# environment

LITE_MODE = False

load_dotenv(override=True)
hf_token = os.environ['HF_TOKEN']
login(hf_token, add_to_git_credential=True)
```

**Cell Output:**
```text
Note: Environment variable`HF_TOKEN` is set and is the current active token independently from the token you've just configured.
```

```python
username = "ed-donner"
dataset = f"{username}/items_lite" if LITE_MODE else f"{username}/items_full"

train, val, test = Item.from_hub(dataset)

print(f"Loaded {len(train):,} training items, {len(val):,} validation items, {len(test):,} test items")
```

**Cell Output:**
```text
Loaded 800,000 training items, 10,000 validation items, 10,000 test items
```

```python
runner = DeepNeuralNetworkRunner(train, val[:1000])
runner.setup()
```

**Cell Output:**
```text
Deep Neural Network created with 289,128,449 parameters
Using mps
```

```python
runner.train(epochs=5)
```

**Cell Output:**
```text
0%|          | 0/12500 [00:00<?, ?it/s]
Epoch [1/5]
Train Loss: 0.5463, Val Loss: 0.4324
Val mean absolute error: $58.26
Learning rate: 0.001000
0%|          | 0/12500 [00:00<?, ?it/s]
Epoch [2/5]
Train Loss: 0.3823, Val Loss: 0.4100
Val mean absolute error: $56.25
Learning rate: 0.000976
0%|          | 0/12500 [00:00<?, ?it/s]
Epoch [3/5]
Train Loss: 0.3230, Val Loss: 0.4090
Val mean absolute error: $56.55
Learning rate: 0.000905
0%|          | 0/12500 [00:00<?, ?it/s]
Epoch [4/5]
Train Loss: 0.2806, Val Loss: 0.4037
Val mean absolute error: $55.70
Learning rate: 0.000794
0%|          | 0/12500 [00:00<?, ?it/s]
Epoch [5/5]
Train Loss: 0.2446, Val Loss: 0.3944
Val mean absolute error: $53.15
Learning rate: 0.000655
```

```python
def deep_neural_network(item):
    return runner.inference(item)

evaluate(deep_neural_network, test)
```

```python
runner.save('deep_neural_network.pth')
```


---

<a id="file-week6-results-ipynb"></a>
## File: `week6/results.ipynb`

> **Path in repository:** `week6/results.ipynb`

```python
import plotly.graph_objects as go

results = [
    ("Constant", "gray", 106.18),
    ("Linear Regression", "gray", 101.56),
    ("NLP + LR", "gray", 76.81),
    ("Random Forest", "gray", 72.28),
    ("XGBoost", "gray", 68.23),
    ("Human (Ed)", "black", 87.62),
    ("Neural Network", "orange", 63.97),
    ("GPT 4.1 Nano", "slateblue", 62.51),
    ("Grok 4.1 Fast", "slateblue", 57.62),
    ("Gemini 3 Pro", "slateblue", 50.54),
    ("Claude 4.5 Sonnet", "slateblue", 47.10),
    ("GPT 5.1", "green", 44.74),
    ("GPT 4.1 Nano (Fine-tuned)", "red", 75.91),
    ("Deep Neural Network", "orange", 46.49)
]

labels, colors, values = zip(*results)

fig = go.Figure(go.Bar(x=labels, y=values, marker_color=colors))

fig.update_layout(
    title="Week 6 model improvements - see the videos to reveal which triumphs!",
    yaxis=dict(range=[0, max(values)], title="Error"),
    xaxis=dict(tickangle=-45),
    width=1000,
    height=800
)

fig.show()
```


---
