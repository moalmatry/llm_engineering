# Extras

This unified reference file consolidates **5 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [extras/community/prototype_signal.ipynb](#file-extras-community-prototype-signal-ipynb)
- [extras/trading/prototype_trader.ipynb](#file-extras-trading-prototype-trader-ipynb)
- [extras/trading/trades_claude.py](#file-extras-trading-trades-claude-py)
- [extras/trading/trades_gemini.py](#file-extras-trading-trades-gemini-py)
- [extras/trading/trades_gpt-4o.py](#file-extras-trading-trades-gpt-4o-py)

---

<a id="file-extras-community-prototype-signal-ipynb"></a>
## File: `extras/community/prototype_signal.ipynb`

> **Path in repository:** `extras/community/prototype_signal.ipynb`

## First step - generate training data from examples

```python
import requests
import pandas as pd
from datetime import datetime, timedelta,timezone
from datasets import load_dataset, Dataset
from dotenv import load_dotenv
import os
from openai import OpenAI
import json
import tiktoken
from IPython.display import display, Markdown
```

```python
# Load environment variables in a file called .env
load_dotenv()

# Replace with your CoinAPI key
API_KEY = os.getenv('YOUR_COINAPI_KEY')

# Define the base URL for CoinAPI
BASE_URL = 'https://rest.coinapi.io/v1/ohlcv/'
OLLAMA_URL = "http://localhost:11434/v1"

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
# URL to fetch the OHLCV data
```

```python
openai = OpenAI()

ollama = OpenAI(
    base_url=OLLAMA_URL,
    api_key='OLAMMA'
)
```

```python
# Define the symbol and timeframe
base_data = {
    'name': 'Cardano',
    'symbol': f'BINANCE_SPOT_ADA_USDT',
    'timeframe': '1DAY',
    'time_range': 365 * 2
}


# Calculate the start date for one year ago
end_date = datetime.now(tz=timezone.utc)

start_date = end_date - timedelta(days=base_data['time_range'])

# Format the dates in the required format (ISO 8601)
start_date_str = start_date.strftime('%Y-%m-%dT%H:%M:%S')
end_date_str = end_date.strftime('%Y-%m-%dT%H:%M:%S')

# Headers for authentication
headers = {
    'X-CoinAPI-Key': API_KEY
}

# URL to fetch the OHLCV base_data
url = f'{BASE_URL}{base_data['symbol']}/history'

# Request parameters
params = {
    'period_id': base_data['timeframe'],
    'time_start': start_date_str,
    'time_end': end_date_str,
    'limit': 1000  # Maximum number of records per request
}
```

```python
# Fetch the data
response = requests.get(url, headers=headers, params=params)     
len(response.json())
```

**Cell Output:**
```text
729
```

```python
# Check for successful response
if response.status_code == 200:
    data = response.json()

    if data:
        # Convert to DataFrame for better readability
        df = pd.DataFrame(data)

        df = df[["time_period_start", "price_open", "price_high", "price_low", "price_close"]]
        df.columns = ["Timestamp", "Open", "High", "Low", "Close"]

        # Convert timestamp to readable format
        df["Timestamp"] = pd.to_datetime(df["Timestamp"]).dt.strftime("%Y-%m-%d")

        # Display the first few rows of the data
        print(df.tail())
        
        # Convert last 365 days of data into JSON format
        price_history = df.to_dict(orient="records")
       
    else:
        print('No data found for the given period.')
else:
    print(f'Error fetching data: {response.status_code}, {response.text}')
```

**Cell Output:**
```text
Timestamp    Open    High     Low   Close
724  2025-02-06  0.7325  0.7660  0.6978  0.7052
725  2025-02-07  0.7052  0.7532  0.6902  0.7072
726  2025-02-08  0.7072  0.7180  0.6815  0.7005
727  2025-02-09  0.7006  0.7160  0.6503  0.6814
728  2025-02-10  0.6815  0.7177  0.6632  0.7037
```

```python
def count_tokens(text, model="gpt-4o"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))
```

```python
# Construct prompt 

prompt = f"""
  Given the last 365 days of ${base_data['name']} OHLC data:

  {json.dumps(price_history, indent=2)}

  Analyze this data and provide a trading signal (Buy, Sell, or Hold) for today based on the trend and the price action.
  Note that today is {end_date.strftime('%Y-%m-%d')}
  Also, provide short term ,mid term and long term signals.
  """
num_tokens = count_tokens(prompt)
print(f"Estimated Tokens: {num_tokens}")

print(prompt)
```

```python
def get_response(prompt):
    new_response = ollama.chat.completions.create(model="llama3.2",
    messages=[
        {"role": "system", "content": f"You are a trading analyst providing Buy/Sell/Hold signals based on ${base_data['name']} price history.Note that today is {end_date.strftime('%Y-%m-%d')}"},
        {"role": "user", "content": prompt}
    ],
    stream=True,
    max_tokens=5500
    )
    markdown_content = ""
    
    # Stream response and accumulate markdown content
    for chunk in new_response:
        content = chunk.choices[0].delta.content or ''
        markdown_content += content
        
        # Clear output and display updated markdown
        display(Markdown(markdown_content), clear=True)
        
        yield content

# Call the function and consume the generator to start streaming
for _ in get_response(prompt):
    pass
```

**Cell Output:**
```text
<IPython.core.display.Markdown object>
```

```python
def get_response(prompt):
    new_response = openai.chat.completions.create(model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"You are a trading analyst providing Buy/Sell/Hold signals based on ${base_data['name']} price history. Format your response in markdown.Note that today is {end_date.strftime('%Y-%m-%d')}"},
        {"role": "user", "content": prompt}
    ],
    stream=True,
    max_tokens=5500
    )
    
    # Initialize markdown cell output
    markdown_content = ""
    
    # Stream response and accumulate markdown content
    for chunk in new_response:
        content = chunk.choices[0].delta.content or ''
        markdown_content += content
        
        # Clear output and display updated markdown
        display(Markdown(markdown_content), clear=True)
        
        yield content

# Call the function and consume the generator to start streaming
for _ in get_response(prompt):
    pass
```

**Cell Output:**
```text
<IPython.core.display.Markdown object>
```


---

<a id="file-extras-trading-prototype-trader-ipynb"></a>
## File: `extras/trading/prototype_trader.ipynb`

> **Path in repository:** `extras/trading/prototype_trader.ipynb`

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


---

<a id="file-extras-trading-trades-claude-py"></a>
## File: `extras/trading/trades_claude.py`

> **Path in repository:** `extras/trading/trades_claude.py`

```python
# tickers is a list of stock tickers
import tickers

# prices is a dict; the key is a ticker and the value is a list of historic prices, today first
import prices

# Trade represents a decision to buy or sell a quantity of a ticker
import Trade

import random
import numpy as np

def trade2():
    # Buy if the current price is lower than the average of the last 5 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < np.mean(prices[ticker][1:6]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade3():
    # Sell if the current price is higher than the average of the last 10 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > np.mean(prices[ticker][1:11]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade4():
    # Buy if the current price is the lowest in the last 3 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] == min(prices[ticker][:3]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade5():
    # Sell if the current price is the highest in the last 3 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] == max(prices[ticker][:3]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade6():
    # Buy if the current price is higher than the previous day's price
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > prices[ticker][1]:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade7():
    # Sell if the current price is lower than the previous day's price
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < prices[ticker][1]:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade8():
    # Buy if the current price is higher than the average of the last 20 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > np.mean(prices[ticker][1:21]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade9():
    # Sell if the current price is lower than the average of the last 20 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < np.mean(prices[ticker][1:21]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade10():
    # Buy if the current price is higher than the highest price in the last 5 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > max(prices[ticker][1:6]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade11():
    # Sell if the current price is lower than the lowest price in the last 5 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < min(prices[ticker][1:6]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade12():
    # Long/Short: Buy the best-performing stock and sell the worst-performing stock in the last 10 days
    best_ticker = max(tickers, key=lambda x: (prices[x][0] - prices[x][9]) / prices[x][9])
    worst_ticker = min(tickers, key=lambda x: (prices[x][0] - prices[x][9]) / prices[x][9])
    return [Trade(best_ticker, 100), Trade(worst_ticker, -100)]

def trade13():
    # Buy if the 5-day moving average crosses above the 20-day moving average
    trades = []
    for ticker in tickers:
        if np.mean(prices[ticker][:5]) > np.mean(prices[ticker][:20]) and np.mean(prices[ticker][1:6]) <= np.mean(prices[ticker][1:21]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade14():
    # Sell if the 5-day moving average crosses below the 20-day moving average
    trades = []
    for ticker in tickers:
        if np.mean(prices[ticker][:5]) < np.mean(prices[ticker][:20]) and np.mean(prices[ticker][1:6]) >= np.mean(prices[ticker][1:21]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade15():
    # Buy if the current volume is higher than the average volume of the last 10 days
    trades = []
    for ticker in tickers:
        if volumes[ticker][0] > np.mean(volumes[ticker][1:11]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade16():
    # Sell if the current volume is lower than the average volume of the last 10 days
    trades = []
    for ticker in tickers:
        if volumes[ticker][0] < np.mean(volumes[ticker][1:11]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade17():
    # Long/Short: Buy the stock with the highest relative strength index (RSI) and sell the stock with the lowest RSI
    rsi = {}
    for ticker in tickers:
        gains = [max(prices[ticker][i] - prices[ticker][i+1], 0) for i in range(13)]
        losses = [max(prices[ticker][i+1] - prices[ticker][i], 0) for i in range(13)]
        avg_gain = sum(gains) / 14
        avg_loss = sum(losses) / 14
        rs = avg_gain / avg_loss if avg_loss > 0 else 100
        rsi[ticker] = 100 - (100 / (1 + rs))
    best_ticker = max(tickers, key=lambda x: rsi[x])
    worst_ticker = min(tickers, key=lambda x: rsi[x])
    return [Trade(best_ticker, 100), Trade(worst_ticker, -100)]

def trade18():
    # Buy if the current price is higher than the 50-day moving average and the 50-day moving average is higher than the 200-day moving average
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > np.mean(prices[ticker][:50]) > np.mean(prices[ticker][:200]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade19():
    # Sell if the current price is lower than the 50-day moving average and the 50-day moving average is lower than the 200-day moving average
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < np.mean(prices[ticker][:50]) < np.mean(prices[ticker][:200]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade20():
    # Long/Short: Buy the stock with the highest momentum and sell the stock with the lowest momentum
    momentums = {}
    for ticker in tickers:
        momentums[ticker] = prices[ticker][0] - prices[ticker][19]
    best_ticker = max(tickers, key=lambda x: momentums[x])
    worst_ticker = min(tickers, key=lambda x: momentums[x])
    return [Trade(best_ticker, 100), Trade(worst_ticker, -100)]

def trade21():
    # Buy if the current price is higher than the upper Bollinger Band
    trades = []
    for ticker in tickers:
        sma = np.mean(prices[ticker][:20])
        std = np.std(prices[ticker][:20])
        upper_band = sma + 2 * std
        if prices[ticker][0] > upper_band:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade22():
    # Sell if the current price is lower than the lower Bollinger Band
    trades = []
    for ticker in tickers:
        sma = np.mean(prices[ticker][:20])
        std = np.std(prices[ticker][:20])
        lower_band = sma - 2 * std
        if prices[ticker][0] < lower_band:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade23():
    # Buy if the current volatility is higher than the average volatility of the last 10 days
    trades = []
    for ticker in tickers:
        volatility = np.std(prices[ticker][:10])
        avg_volatility = np.mean([np.std(prices[ticker][i:i+10]) for i in range(10)])
        if volatility > avg_volatility:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade24():
    # Sell if the current volatility is lower than the average volatility of the last 10 days
    trades = []
    for ticker in tickers:
        volatility = np.std(prices[ticker][:10])
        avg_volatility = np.mean([np.std(prices[ticker][i:i+10]) for i in range(10)])
        if volatility < avg_volatility:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade25():
    # Long/Short: Buy the stock with the lowest volatility and sell the stock with the highest volatility
    volatilities = {}
    for ticker in tickers:
        volatilities[ticker] = np.std(prices[ticker][:10])
    best_ticker = min(tickers, key=lambda x: volatilities[x])
    worst_ticker = max(tickers, key=lambda x: volatilities[x])
    return [Trade(best_ticker, 100), Trade(worst_ticker, -100)]

def trade26():
    # Buy if the current price is higher than the 20-day exponential moving average (EMA)
    trades = []
    for ticker in tickers:
        ema = prices[ticker][0]
        multiplier = 2 / (20 + 1)
        for i in range(1, 20):
            ema = (prices[ticker][i] - ema) * multiplier + ema
        if prices[ticker][0] > ema:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade27():
    # Sell if the current price is lower than the 20-day exponential moving average (EMA)
    trades = []
    for ticker in tickers:
        ema = prices[ticker][0]
        multiplier = 2 / (20 + 1)
        for i in range(1, 20):
            ema = (prices[ticker][i] - ema) * multiplier + ema
        if prices[ticker][0] < ema:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade28():
    # Buy if the current price is higher than the upper Keltner Channel
    trades = []
    for ticker in tickers:
        ema = prices[ticker][0]
        multiplier = 2 / (20 + 1)
        for i in range(1, 20):
            ema = (prices[ticker][i] - ema) * multiplier + ema
        atr = np.mean([np.max(prices[ticker][i:i+10]) - np.min(prices[ticker][i:i+10]) for i in range(10)])
        upper_channel = ema + 2 * atr
        if prices[ticker][0] > upper_channel:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade29():
    # Sell if the current price is lower than the lower Keltner Channel
    trades = []
    for ticker in tickers:
        ema = prices[ticker][0]
        multiplier = 2 / (20 + 1)
        for i in range(1, 20):
            ema = (prices[ticker][i] - ema) * multiplier + ema
        atr = np.mean([np.max(prices[ticker][i:i+10]) - np.min(prices[ticker][i:i+10]) for i in range(10)])
        lower_channel = ema - 2 * atr
        if prices[ticker][0] < lower_channel:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade30():
    # Long/Short: Buy the stock with the highest Sharpe ratio and sell the stock with the lowest Sharpe ratio
    sharpe_ratios = {}
    for ticker in tickers:
        returns = [prices[ticker][i] / prices[ticker][i+1] - 1 for i in range(19)]
        sharpe_ratios[ticker] = np.mean(returns) / np.std(returns)
    best_ticker = max(tickers, key=lambda x: sharpe_ratios[x])
    worst_ticker = min(tickers, key=lambda x: sharpe_ratios[x])
    return [Trade(best_ticker, 100), Trade(worst_ticker, -100)]

def trade31():
    # Buy if the current price is higher than the Ichimoku Cloud conversion line
    trades = []
    for ticker in tickers:
        conversion_line = (np.max(prices[ticker][:9]) + np.min(prices[ticker][:9])) / 2
        if prices[ticker][0] > conversion_line:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade32():
    # Buy if the current price is higher than the price 5 days ago
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > prices[ticker][4]:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade33():
    # Sell if the current price is lower than the price 5 days ago
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < prices[ticker][4]:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade34():
    # Buy if the current price is the highest in the last 15 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] == max(prices[ticker][:15]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade35():
    # Sell if the current price is the lowest in the last 15 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] == min(prices[ticker][:15]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade36():
    # Buy if the current price is higher than the 10-day simple moving average (SMA)
    trades = []
    for ticker in tickers:
        sma = np.mean(prices[ticker][:10])
        if prices[ticker][0] > sma:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade37():
    # Sell if the current price is lower than the 10-day simple moving average (SMA)
    trades = []
    for ticker in tickers:
        sma = np.mean(prices[ticker][:10])
        if prices[ticker][0] < sma:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade38():
    # Buy if the current price is higher than the highest price in the last 20 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > max(prices[ticker][:20]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade39():
    # Sell if the current price is lower than the lowest price in the last 20 days
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < min(prices[ticker][:20]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade40():
    # Buy if the current price is higher than the 50-day SMA
    trades = []
    for ticker in tickers:
        sma = np.mean(prices[ticker][:50])
        if prices[ticker][0] > sma:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade41():
    # Sell if the current price is lower than the 50-day SMA
    trades = []
    for ticker in tickers:
        sma = np.mean(prices[ticker][:50])
        if prices[ticker][0] < sma:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade42():
    # Buy if the current price is higher than the previous 2 days (a simple uptrend)
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > prices[ticker][1] > prices[ticker][2]:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade43():
    # Sell if the current price is lower than the previous 2 days (a simple downtrend)
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < prices[ticker][1] < prices[ticker][2]:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade44():
    # Buy if the current price is higher than the previous day's high (a breakout)
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > max(prices[ticker][1:2]):
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade45():
    # Sell if the current price is lower than the previous day's low (a breakdown)
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < min(prices[ticker][1:2]):
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade46():
    # Buy if the current price is above the previous day's high and the previous day was a down day (a potential reversal)
    trades = []
    for ticker in tickers:
        if prices[ticker][0] > max(prices[ticker][1:2]) and prices[ticker][1] < prices[ticker][2]:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade47():
    # Sell if the current price is below the previous day's low and the previous day was an up day (a potential reversal)
    trades = []
    for ticker in tickers:
        if prices[ticker][0] < min(prices[ticker][1:2]) and prices[ticker][1] > prices[ticker][2]:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade48():
    # Buy if the current price is above the 5-day SMA and the 5-day SMA is above the 10-day SMA (a bullish crossover)
    trades = []
    for ticker in tickers:
        sma5 = np.mean(prices[ticker][:5])
        sma10 = np.mean(prices[ticker][:10])
        if prices[ticker][0] > sma5 > sma10:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade49():
    # Sell if the current price is below the 5-day SMA and the 5-day SMA is below the 10-day SMA (a bearish crossover)
    trades = []
    for ticker in tickers:
        sma5 = np.mean(prices[ticker][:5])
        sma10 = np.mean(prices[ticker][:10])
        if prices[ticker][0] < sma5 < sma10:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade50():
    # Buy if the current price is above the 50-day SMA and the previous price was below the 50-day SMA (a bullish breakthrough)
    trades = []
    for ticker in tickers:
        sma50 = np.mean(prices[ticker][:50])
        if prices[ticker][0] > sma50 and prices[ticker][1] < sma50:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade51():
    # Sell if the current price is below the 50-day SMA and the previous price was above the 50-day SMA (a bearish breakthrough)
    trades = []
    for ticker in tickers:
        sma50 = np.mean(prices[ticker][:50])
        if prices[ticker][0] < sma50 and prices[ticker][1] > sma50:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade52():
    # Buy if the current price is more than 2 standard deviations below the 20-day mean (a potential oversold condition)
    trades = []
    for ticker in tickers:
        mean20 = np.mean(prices[ticker][:20])
        std20 = np.std(prices[ticker][:20])
        if prices[ticker][0] < mean20 - 2 * std20:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade53():
    # Sell if the current price is more than 2 standard deviations above the 20-day mean (a potential overbought condition)
    trades = []
    for ticker in tickers:
        mean20 = np.mean(prices[ticker][:20])
        std20 = np.std(prices[ticker][:20])
        if prices[ticker][0] > mean20 + 2 * std20:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade54():
    # Buy if the current price is below the 50-day mean and the 50-day mean is increasing (a potential uptrend)
    trades = []
    for ticker in tickers:
        mean50 = np.mean(prices[ticker][:50])
        prev_mean50 = np.mean(prices[ticker][1:51])
        if prices[ticker][0] < mean50 and mean50 > prev_mean50:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade55():
    # Sell if the current price is above the 50-day mean and the 50-day mean is decreasing (a potential downtrend)
    trades = []
    for ticker in tickers:
        mean50 = np.mean(prices[ticker][:50])
        prev_mean50 = np.mean(prices[ticker][1:51])
        if prices[ticker][0] > mean50 and mean50 < prev_mean50:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade56():
    # Buy if the 5-day mean is above the 50-day mean and the 5-day mean was previously below the 50-day mean (a potential trend change)
    trades = []
    for ticker in tickers:
        mean5 = np.mean(prices[ticker][:5])
        mean50 = np.mean(prices[ticker][:50])
        prev_mean5 = np.mean(prices[ticker][1:6])
        if mean5 > mean50 and prev_mean5 < mean50:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade57():
    # Sell if the 5-day mean is below the 50-day mean and the 5-day mean was previously above the 50-day mean (a potential trend change)
    trades = []
    for ticker in tickers:
        mean5 = np.mean(prices[ticker][:5])
        mean50 = np.mean(prices[ticker][:50])
        prev_mean5 = np.mean(prices[ticker][1:6])
        if mean5 < mean50 and prev_mean5 > mean50:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade58():
    # Buy the ticker that has had the largest percent decrease over the last 10 days (a potential mean reversion play)
    percent_changes = {}
    for ticker in tickers:
        percent_changes[ticker] = (prices[ticker][0] - prices[ticker][9]) / prices[ticker][9] * 100
    worst_ticker = min(tickers, key=lambda x: percent_changes[x])
    return [Trade(worst_ticker, 100)]

def trade59():
    # Sell the ticker that has had the largest percent increase over the last 10 days (a potential mean reversion play)
    percent_changes = {}
    for ticker in tickers:
        percent_changes[ticker] = (prices[ticker][0] - prices[ticker][9]) / prices[ticker][9] * 100
    best_ticker = max(tickers, key=lambda x: percent_changes[x])
    return [Trade(best_ticker, -100)]

def trade60():
    # Buy if the current price is above the 200-day mean and the 200-day mean is increasing (a potential long-term uptrend)
    trades = []
    for ticker in tickers:
        mean200 = np.mean(prices[ticker][:200])
        prev_mean200 = np.mean(prices[ticker][1:201])
        if prices[ticker][0] > mean200 and mean200 > prev_mean200:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade61():
    # Sell if the current price is below the 200-day mean and the 200-day mean is decreasing (a potential long-term downtrend)
    trades = []
    for ticker in tickers:
        mean200 = np.mean(prices[ticker][:200])
        prev_mean200 = np.mean(prices[ticker][1:201])
        if prices[ticker][0] < mean200 and mean200 < prev_mean200:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade62():
    # Buy if the stock's return is greater than the market's return over the last 5 days
    trades = []
    for ticker in tickers:
        stock_return = (prices[ticker][0] - prices[ticker][4]) / prices[ticker][4]
        market_return = (sum(prices[t][0] for t in tickers) - sum(prices[t][4] for t in tickers)) / sum(prices[t][4] for t in tickers)
        if stock_return > market_return:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade63():
    # Sell if the stock's return is less than the market's return over the last 5 days
    trades = []
    for ticker in tickers:
        stock_return = (prices[ticker][0] - prices[ticker][4]) / prices[ticker][4]
        market_return = (sum(prices[t][0] for t in tickers) - sum(prices[t][4] for t in tickers)) / sum(prices[t][4] for t in tickers)
        if stock_return < market_return:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade64():
    # Buy the stock with the highest relative strength compared to the market over the last 10 days
    relative_strengths = {}
    for ticker in tickers:
        stock_return = prices[ticker][0] / prices[ticker][9]
        market_return = sum(prices[t][0] for t in tickers) / sum(prices[t][9] for t in tickers)
        relative_strengths[ticker] = stock_return / market_return
    best_ticker = max(tickers, key=lambda x: relative_strengths[x])
    return [Trade(best_ticker, 100)]

def trade65():
    # Sell the stock with the lowest relative strength compared to the market over the last 10 days
    relative_strengths = {}
    for ticker in tickers:
        stock_return = prices[ticker][0] / prices[ticker][9]
        market_return = sum(prices[t][0] for t in tickers) / sum(prices[t][9] for t in tickers)
        relative_strengths[ticker] = stock_return / market_return
    worst_ticker = min(tickers, key=lambda x: relative_strengths[x])
    return [Trade(worst_ticker, -100)]

def trade66():
    # Buy stocks that have a higher Sharpe ratio than the market over the last 20 days
    trades = []
    market_returns = [(sum(prices[t][i] for t in tickers) / sum(prices[t][i+1] for t in tickers)) - 1 for i in range(19)]
    market_sharpe = np.mean(market_returns) / np.std(market_returns)
    for ticker in tickers:
        stock_returns = [(prices[ticker][i] / prices[ticker][i+1]) - 1 for i in range(19)]
        stock_sharpe = np.mean(stock_returns) / np.std(stock_returns)
        if stock_sharpe > market_sharpe:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade67():
    # Sell stocks that have a lower Sharpe ratio than the market over the last 20 days
    trades = []
    market_returns = [(sum(prices[t][i] for t in tickers) / sum(prices[t][i+1] for t in tickers)) - 1 for i in range(19)]
    market_sharpe = np.mean(market_returns) / np.std(market_returns)
    for ticker in tickers:
        stock_returns = [(prices[ticker][i] / prices[ticker][i+1]) - 1 for i in range(19)]
        stock_sharpe = np.mean(stock_returns) / np.std(stock_returns)
        if stock_sharpe < market_sharpe:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade68():
    # Buy stocks that have a higher beta than 1 (they move more than the market)
    trades = []
    market_returns = [(sum(prices[t][i] for t in tickers) / sum(prices[t][i+1] for t in tickers)) - 1 for i in range(49)]
    for ticker in tickers:
        stock_returns = [(prices[ticker][i] / prices[ticker][i+1]) - 1 for i in range(49)]
        beta = np.cov(stock_returns, market_returns)[0, 1] / np.var(market_returns)
        if beta > 1:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade69():
    # Sell stocks that have a lower beta than 1 (they move less than the market)
    trades = []
    market_returns = [(sum(prices[t][i] for t in tickers) / sum(prices[t][i+1] for t in tickers)) - 1 for i in range(49)]
    for ticker in tickers:
        stock_returns = [(prices[ticker][i] / prices[ticker][i+1]) - 1 for i in range(49)]
        beta = np.cov(stock_returns, market_returns)[0, 1] / np.var(market_returns)
        if beta < 1:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades

def trade70():
    # Buy stocks that have a higher percentage of up days than the market over the last 50 days
    trades = []
    market_up_days = sum(sum(prices[t][i] for t in tickers) > sum(prices[t][i+1] for t in tickers) for i in range(49))
    for ticker in tickers:
        stock_up_days = sum(prices[ticker][i] > prices[ticker][i+1] for i in range(49))
        if stock_up_days > market_up_days:
            quantity = random.randrange(1, 100)
            trades.append(Trade(ticker, quantity))
    return trades

def trade71():
    # Sell stocks that have a lower percentage of up days than the market over the last 50 days
    trades = []
    market_up_days = sum(sum(prices[t][i] for t in tickers) > sum(prices[t][i+1] for t in tickers) for i in range(49))
    for ticker in tickers:
        stock_up_days = sum(prices[ticker][i] > prices[ticker][i+1] for i in range(49))
        if stock_up_days < market_up_days:
            quantity = random.randrange(-100, -1)
            trades.append(Trade(ticker, quantity))
    return trades
```


---

<a id="file-extras-trading-trades-gemini-py"></a>
## File: `extras/trading/trades_gemini.py`

> **Path in repository:** `extras/trading/trades_gemini.py`

```python
# tickers is a list of stock tickers
import tickers

# prices is a dict; the key is a ticker and the value is a list of historic prices, today first
import prices

# Trade represents a decision to buy or sell a quantity of a ticker
import Trade

import random
import numpy as np

def trade2():
    # Buy the stock with the highest price today
    ticker = max(prices, key=lambda t: prices[t][0])  # Find ticker with highest price
    return [Trade(ticker, random.randrange(1, 10))]   # Buy a small quantity

def trade3():
    # Sell the stock with the lowest price today
    ticker = min(prices, key=lambda t: prices[t][0])
    return [Trade(ticker, random.randrange(-10, -1))] 

def trade4():
    # Buy the stock with the largest percent increase today
    changes = {t: (prices[t][0] - prices[t][1]) / prices[t][1] for t in prices}
    ticker = max(changes, key=changes.get)
    return [Trade(ticker, random.randrange(1, 10))]

def trade5():
    # Sell the stock with the largest percent decrease today
    changes = {t: (prices[t][0] - prices[t][1]) / prices[t][1] for t in prices}
    ticker = min(changes, key=changes.get)
    return [Trade(ticker, random.randrange(-10, -1))]

def trade6():
    # Buy the 3 stocks with the highest moving average over the last 5 days
    mvgs = {t: np.mean(prices[t][:5]) for t in prices}
    top_tickers = sorted(mvgs, key=mvgs.get, reverse=True)[:3]
    return [Trade(t, random.randrange(1, 5)) for t in top_tickers]

def trade7():
    # Sell the 3 stocks with the lowest moving average over the last 5 days
    mvgs = {t: np.mean(prices[t][:5]) for t in prices}
    bottom_tickers = sorted(mvgs, key=mvgs.get)[:3]
    return [Trade(t, random.randrange(-5, -1)) for t in bottom_tickers]

def trade8():
    # Randomly buy or sell a single stock based on a coin flip
    ticker = random.choice(tickers)
    action = random.choice([-1, 1])  # -1 for sell, 1 for buy
    return [Trade(ticker, action * random.randrange(1, 10))]

def trade9():
    # Diversify: Buy a small amount of 5 random stocks
    chosen_tickers = random.sample(tickers, 5)
    return [Trade(t, random.randrange(1, 3)) for t in chosen_tickers]

def trade10():
    # Follow the trend: If the market is up today, buy, else sell
    market_change = (prices[tickers[0]][0] - prices[tickers[0]][1]) / prices[tickers[0]][1]
    action = 1 if market_change > 0 else -1
    ticker = random.choice(tickers)
    return [Trade(ticker, action * random.randrange(1, 10))]

def trade11():
    # Mean Reversion: Buy the 2 stocks that fell the most yesterday, hoping they rebound
    yesterday_changes = {t: (prices[t][1] - prices[t][2]) / prices[t][2] for t in prices}
    bottom_tickers = sorted(yesterday_changes, key=yesterday_changes.get)[:2]
    return [Trade(t, random.randrange(1, 5)) for t in bottom_tickers]

def trade12():
    # Momentum: Short the 2 stocks that rose the most yesterday, expecting a pullback
    yesterday_changes = {t: (prices[t][1] - prices[t][2]) / prices[t][2] for t in prices}
    top_tickers = sorted(yesterday_changes, key=yesterday_changes.get, reverse=True)[:2]
    return [Trade(t, random.randrange(-5, -1)) for t in top_tickers]

def trade13():
    # Pairs Trading: Long one stock, short another with a similar price history
    correlations = np.corrcoef([prices[t] for t in tickers])
    i, j = np.unravel_index(np.argmax(correlations), correlations.shape)
    return [Trade(tickers[i], 1), Trade(tickers[j], -1)] 

def trade14():
    # Relative Strength: Go long on the strongest stock, short the weakest
    performances = {t: (prices[t][0] - prices[t][-1]) / prices[t][-1] for t in prices}
    strongest = max(performances, key=performances.get)
    weakest = min(performances, key=performances.get)
    return [Trade(strongest, 1), Trade(weakest, -1)]

def trade15():
    # Calendar Spread: Buy this month's option, sell next month's (same strike
    # This is a simplified representation, as actual option trading is more complex
    ticker = random.choice(tickers)
    return [Trade(f"{ticker}_OPT_THIS_MONTH", 1), Trade(f"{ticker}_OPT_NEXT_MONTH", -1)]

def trade16():
    # Straddle: Buy both a call and put option on the same stock (same strike
    ticker = random.choice(tickers)
    strike = prices[ticker][0]  # Use the current price as a simple strike price
    return [Trade(f"{ticker}_CALL_{strike}", 1), Trade(f"{ticker}_PUT_{strike}", 1)]

def trade17():
    # Breakout: Buy if a stock breaks above its 52-week high
    ticker = random.choice(tickers)
    if prices[ticker][0] > max(prices[ticker]):
        return [Trade(ticker, random.randrange(1, 10))]
    else:
        return [] 

def trade18():
    # Volatility: If market volatility is high, sell (expecting it to decrease
    market_volatility = np.std([prices[t][0] / prices[t][1] for t in tickers])
    if market_volatility > 0.05:  # You'd adjust this threshold based on your risk tolerance
        ticker = random.choice(tickers)
        return [Trade(ticker, random.randrange(-10, -1))]
    else:
        return []

def trade19():
    # Golden Cross: Buy if the short-term moving average crosses above the long-term
    ticker = random.choice(tickers)
    short_ma = np.mean(prices[ticker][:5])
    long_ma = np.mean(prices[ticker][:20])
    if short_ma > long_ma and short_ma - long_ma < 0.01:  # Small margin to avoid false signals
        return [Trade(ticker, random.randrange(1, 10))]
    else:
        return []

def trade20():
    # Death Cross: Sell if the short-term moving average crosses below the long-term
    ticker = random.choice(tickers)
    short_ma = np.mean(prices[ticker][:5])
    long_ma = np.mean(prices[ticker][:20])
    if short_ma < long_ma and long_ma - short_ma < 0.01: 
        return [Trade(ticker, random.randrange(-10, -1))]
    else:
        return []

def trade21():
    # Correlated Pairs Buy: Buy a pair of stocks that have historically moved together
    correlations = np.corrcoef([prices[t] for t in tickers])
    i, j = np.unravel_index(np.argmax(correlations), correlations.shape)
    return [Trade(tickers[i], 1), Trade(tickers[j], 1)]

def trade22():
    # Correlated Pairs Sell: Sell a pair of stocks that have historically moved together
    correlations = np.corrcoef([prices[t] for t in tickers])
    i, j = np.unravel_index(np.argmax(correlations), correlations.shape)
    return [Trade(tickers[i], -1), Trade(tickers[j], -1)]

def trade23():
    # Contrarian Pairs Buy: Buy a stock that's down while its correlated pair is up
    correlations = np.corrcoef([prices[t] for t in tickers])
    i, j = np.unravel_index(np.argmax(correlations), correlations.shape)
    if prices[tickers[i]][0] < prices[tickers[i]][1] and prices[tickers[j]][0] > prices[tickers[j]][1]:
        return [Trade(tickers[i], 1)]
    else:
        return []

def trade24():
    # Contrarian Pairs Sell: Sell a stock that's up while its correlated pair is down
    correlations = np.corrcoef([prices[t] for t in tickers])
    i, j = np.unravel_index(np.argmax(correlations), correlations.shape)
    if prices[tickers[i]][0] > prices[tickers[i]][1] and prices[tickers[j]][0] < prices[tickers[j]][1]:
        return [Trade(tickers[i], -1)]
    else:
        return []

def trade25():
    # Correlation Reversal: Buy a stock that's recently become less correlated with the market
    # This is a simplified version, you'd likely use a rolling correlation window
    market_prices = [prices[t] for t in tickers]
    correlations_today = np.corrcoef(market_prices)
    correlations_yesterday = np.corrcoef([p[1:] for p in market_prices])
    diffs = correlations_today - correlations_yesterday
    i, j = np.unravel_index(np.argmin(diffs), diffs.shape)
    if i != j:  # Ensure we're not comparing a stock to itself
        return [Trade(tickers[i], 1)]
    else:
        return []

def trade26():
    # Sector Rotation: Buy the top 2 stocks from the sector that's most correlated with the market
    # Assuming you have sector data (e.g., 'sector_map' dict: ticker -> sector)
    sector_returns = {s: np.mean([(prices[t][0] - prices[t][1]) / prices[t][1] for t in tickers if sector_map[t] == s]) for s in set(sector_map.values())}
    top_sector = max(sector_returns, key=sector_returns.get)
    top_tickers_in_sector = sorted([(t, prices[t][0]) for t in tickers if sector_map[t] == top_sector], key=lambda x: x[1], reverse=True)[:2]
    return [Trade(t, 1) for t, _ in top_tickers_in_sector]

def trade27():
    # Beta-Weighted Portfolio: Allocate more to stocks with higher betas (more volatile
    # You'd need historical market data to calculate betas
    betas = {t: random.uniform(0.5, 2) for t in tickers}  # Placeholder for actual betas
    total_beta = sum(betas.values())
    allocations = {t: betas[t] / total_beta * 100 for t in tickers}
    return [Trade(t, int(allocations[t])) for t in tickers]

def trade28():
    # Diversified Portfolio: Buy a mix of stocks with low correlations to each other
    correlations = np.corrcoef([prices[t] for t in tickers])
    chosen_tickers = []
    while len(chosen_tickers) < 5 and len(tickers) > 0:
        t = random.choice(tickers)
        if all(correlations[tickers.index(t)][tickers.index(c)] < 0.5 for c in chosen_tickers):
            chosen_tickers.append(t)
            tickers.remove(t) 
    return [Trade(t, random.randrange(1, 3)) for t in chosen_tickers]

def trade29():
    # Cointegration: Find a pair of stocks that are cointegrated and trade their spread
    # This requires more complex analysis (e.g., using the Johansen test)
    # For simplicity, we'll just pick a random pair and assume cointegration
    i, j = random.sample(range(len(tickers)), 2)
    spread = prices[tickers[i]][0] - prices[tickers[j]][0]
    if spread > 0:
        return [Trade(tickers[i], -1), Trade(tickers[j], 1)] 
    else:
        return [Trade(tickers[i], 1), Trade(tickers[j], -1)]

def trade30():
    # Basket Trading: Buy or sell a basket of stocks based on their correlation to a benchmark
    # You'd need a benchmark ticker and its historical prices
    benchmark = "SPY"
    correlations = np.corrcoef([prices[t] for t in tickers + [benchmark]])[:-1, -1]  # Correlate each stock with the benchmark
    if np.mean(correlations) > 0.5:
        return [Trade(t, 1) for t in tickers]
    else:
        return [Trade(t, -1) for t in tickers]

def trade31():
    # Double Bottom: Buy when a stock forms a double bottom pattern
    ticker = random.choice(tickers)
    if prices[ticker][0] < prices[ticker][2] < prices[ticker][4] and prices[ticker][1] > prices[ticker][3]:
        return [Trade(ticker, 1)]
    else:
        return []

def trade32():
    # Double Top: Sell when a stock forms a double top pattern
    ticker = random.choice(tickers)
    if prices[ticker][0] > prices[ticker][2] > prices[ticker][4] and prices[ticker][1] < prices[ticker][3]:
        return [Trade(ticker, -1)]
    else:
        return []

def trade33():
    # Head and Shoulders: Sell when a stock forms a head and shoulders pattern
    ticker = random.choice(tickers)
    if prices[ticker][0] < prices[ticker][2] < prices[ticker][4] and prices[ticker][1] > prices[ticker][3] > prices[ticker][5]:
        return [Trade(ticker, -1)]
    else:
        return []

def trade34
    # Inverse Head and Shoulders: Buy when a stock forms an inverse head and shoulders pattern
    ticker = random.choice(tickers)
    if prices[ticker][0] > prices[ticker][2] > prices[ticker][4] and prices[ticker][1] < prices[ticker][3] < prices[ticker][5]:
        return [Trade(ticker, 1)]
    else:
        return []

def trade35():
    # Ascending Triangle: Buy when a stock forms an ascending triangle pattern
    ticker = random.choice(tickers)
    # Simplified logic: check for higher lows and flat highs
    if prices[ticker][0] > prices[ticker][2] > prices[ticker][4] and prices[ticker][1] == prices[ticker][3] == prices[ticker][5]:
        return [Trade(ticker, 1)]
    else:
        return []

def trade36():
    # Descending Triangle: Sell when a stock forms a descending triangle pattern
    ticker = random.choice(tickers)
    # Simplified logic: check for lower highs and flat lows
    if prices[ticker][0] < prices[ticker][2] < prices[ticker][4] and prices[ticker][1] == prices[ticker][3] == prices[ticker][5]:
        return [Trade(ticker, -1)]
    else:
        return []

def trade37():
    # Flag/Pennant: Buy or sell based on the direction of the flag/pennant pattern
    ticker = random.choice(tickers)
    # Simplified logic: check for a consolidation period after a strong move
    if abs(prices[ticker][0] - np.mean(prices[ticker][1:5])) < 0.05 and abs(prices[ticker][5] - prices[ticker][6]) > 0.1:
        # Buy if the prior move was up, sell if down
        return [Trade(ticker, 1 if prices[ticker][5] > prices[ticker][6] else -1)]
    else:
        return []

def trade38():
    # Gap Up: Buy when a stock opens significantly higher than its previous close
    ticker = random.choice(tickers)
    if prices[ticker][0] > prices[ticker][1] * 1.05:  # 5% gap up
        return [Trade(ticker, 1)]
    else:
        return []

def trade39():
    # Gap Down: Sell when a stock opens significantly lower than its previous close
    ticker = random.choice(tickers)
    if prices[ticker][0] < prices[ticker][1] * 0.95:  # 5% gap down
        return [Trade(ticker, -1)]
    else:
        return []

def trade40():
    # Rounding Bottom: Buy when a stock forms a rounding bottom pattern
    ticker = random.choice(tickers)
    # Simplified logic: check for a gradual price increase after a period of decline
    if prices[ticker][0] > prices[ticker][2] > prices[ticker][4] and prices[ticker][1] < prices[ticker][3] < prices[ticker][5]:
        return [Trade(ticker, 1)]
    else:
        return []

def trade41():
    # Overbought/Oversold (RSI): Sell if RSI is above 70, buy if below 30
    ticker = random.choice(tickers)
    rsi = calculate_rsi(prices[ticker], 14)  # Assuming you have an RSI calculation function
    if rsi > 70:
        return [Trade(ticker, -1)]
    elif rsi < 30:
        return [Trade(ticker, 1)]
    else:
        return []

def trade42():
    # Bollinger Bands Breakout: Buy if price breaks above the upper band, sell if below lower
    ticker = random.choice(tickers)
    upper, middle, lower = calculate_bollinger_bands(prices[ticker], 20, 2)  # Assuming you have a Bollinger Band calculation function
    if prices[ticker][0] > upper:
        return [Trade(ticker, 1)]
    elif prices[ticker][0] < lower:
        return [Trade(ticker, -1)]
    else:
        return []

def trade43():
    # Channel Breakout: Buy or sell when price breaks out of a recent price channel
    ticker = random.choice(tickers)
    highs = [max(prices[ticker][i:i+5]) for i in range(len(prices[ticker]) - 5)]
    lows = [min(prices[ticker][i:i+5]) for i in range(len(prices[ticker]) - 5)]
    if prices[ticker][0] > highs[-1]:
        return [Trade(ticker, 1)]
    elif prices[ticker][0] < lows[-1]:
        return [Trade(ticker, -1)]
    else:
        return []

def trade44():
    # Trend Following: Buy if the 20-day moving average is rising, sell if falling
    ticker = random.choice(tickers)
    ma20_today = np.mean(prices[ticker][:20])
    ma20_yesterday = np.mean(prices[ticker][1:21])
    if ma20_today > ma20_yesterday:
        return [Trade(ticker, 1)]
    elif ma20_today < ma20_yesterday:
        return [Trade(ticker, -1)]
    else:
        return []

def trade45():
    # MACD Crossover: Buy when MACD line crosses above signal line, sell when below
    ticker = random.choice(tickers)
    macd_line, signal_line = calculate_macd(prices[ticker])  # Assuming you have a MACD calculation function
    if macd_line[-1] > signal_line[-1] and macd_line[-2] <= signal_line[-2]:
        return [Trade(ticker, 1)]
    elif macd_line[-1] < signal_line[-1] and macd_line[-2] >= signal_line[-2]:
        return [Trade(ticker, -1)]
    else:
        return []

def trade46():
    # Stochastic Oscillator: Buy if %K crosses above %D in oversold zone, sell if opposite
    ticker = random.choice(tickers)
    k_line, d_line = calculate_stochastic(prices[ticker])  # Assuming you have a Stochastic calculation function
    if k_line[-1] > d_line[-1] and k_line[-1] < 20:
        return [Trade(ticker, 1)]
    elif k_line[-1] < d_line[-1] and k_line[-1] > 80:
        return [Trade(ticker, -1)]
    else:
        return []

def trade47():
    # Volume Spike: Buy if today's volume is much higher than the average
    # You'd need volume data for this strategy
    ticker = random.choice(tickers)
    avg_volume = np.mean(volumes[ticker][1:])  # Assuming you have 'volumes' data
    if volumes[ticker][0] > avg_volume * 2:
        return [Trade(ticker, 1)]
    else:
        return []

def trade48():
    # Price Spike: Buy if today's price increase is much higher than average daily change
    ticker = random.choice(tickers)
    daily_changes = [(prices[ticker][i] - prices[ticker][i + 1]) / prices[ticker][i + 1] for i in range(len(prices[ticker]) - 1)]
    avg_change = np.mean(daily_changes)
    today_change = (prices[ticker][0] - prices[ticker][1]) / prices[ticker][1]
    if today_change > avg_change * 2:
        return [Trade(ticker, 1)]
    else:
        return []

def trade49():
    # Mean Reversion (Long-term): Buy if the price is below its 200-day moving average
    ticker = random.choice(tickers)
    ma200 = np.mean(prices[ticker])
    if prices[ticker][0] < ma200:
        return [Trade(ticker, 1)]
    else:
        return []

def trade50():
    # Trend Reversal (Parabolic SAR): Buy or sell based on the Parabolic SAR indicator
    # Assuming you have a Parabolic SAR calculation function
    ticker = random.choice(tickers)
    sar = calculate_parabolic_sar(prices[ticker])
    if prices[ticker][0] > sar[-1]: 
        return [Trade(ticker, 1)]
    elif prices[ticker][0] < sar[-1]:
        return [Trade(ticker, -1)]
    else:
        return []

def trade51():
    # Market Outperformance: Buy stocks whose daily returns beat the market
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    market_return = (total_market_values[0] - total_market_values[1]) / total_market_values[1]
    outperformers = [t for t in tickers if (prices[t][0] - prices[t][1]) / prices[t][1] > market_return]
    if outperformers:
        ticker = random.choice(outperformers)
        return [Trade(ticker, 1)]
    else:
        return []

def trade52():
    # Market Underperformance: Short stocks whose daily returns lag the market
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    market_return = (total_market_values[0] - total_market_values[1]) / total_market_values[1]
    underperformers = [t for t in tickers if (prices[t][0] - prices[t][1]) / prices[t][1] < market_return]
    if underperformers:
        ticker = random.choice(underperformers)
        return [Trade(ticker, -1)]
    else:
        return []

def trade53():
    # Relative Strength to Market: Buy the stock with the highest relative strength to the market
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    market_return = (total_market_values[0] - total_market_values[1]) / total_market_values[1]
    relative_strengths = {t: ((prices[t][0] - prices[t][1]) / prices[t][1]) - market_return for t in tickers}
    ticker = max(relative_strengths, key=relative_strengths.get)
    return [Trade(ticker, 1)]

def trade54():
    # Relative Weakness to Market: Short the stock with the lowest relative strength to the market
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    market_return = (total_market_values[0] - total_market_values[1]) / total_market_values[1]
    relative_strengths = {t: ((prices[t][0] - prices[t][1]) / prices[t][1]) - market_return for t in tickers}
    ticker = min(relative_strengths, key=relative_strengths.get)
    return [Trade(ticker, -1)]

def trade55():
    # Sector vs. Market: Buy top stock from sector outperforming the market, short from underperforming
    # Assuming you have sector data (e.g., 'sector_map' dict: ticker -> sector)
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    market_return = (total_market_values[0] - total_market_values[1]) / total_market_values[1]
    sector_returns = {s: np.mean([(prices[t][0] - prices[t][1]) / prices[t][1] for t in tickers if sector_map[t] == s]) for s in set(sector_map.values())}
    outperforming_sectors = [s for s in sector_returns if sector_returns[s] > market_return]
    underperforming_sectors = [s for s in sector_returns if sector_returns[s] < market_return]
    trades = []
    if outperforming_sectors:
        top_ticker = max([(t, prices[t][0]) for t in tickers if sector_map[t] == random.choice(outperforming_sectors)], key=lambda x: x[1])[0]
        trades.append(Trade(top_ticker, 1))
    if underperforming_sectors:
        bottom_ticker = min([(t, prices[t][0]) for t in tickers if sector_map[t] == random.choice(underperforming_sectors)], key=lambda x: x[1])[0]
        trades.append(Trade(bottom_ticker, -1))
    return trades

def trade56():
    # Market-Neutral Pairs: Long/short pairs of stocks with similar market betas
    betas = {t: random.uniform(0.8, 1.2) for t in tickers}  # Placeholder, calculate actual betas
    pairs = [(t1, t2) for t1 in tickers for t2 in tickers if abs(betas[t1] - betas[t2]) < 0.1 and t1 != t2]
    if pairs:
        t1, t2 = random.choice(pairs)
        return [Trade(t1, 1), Trade(t2, -1)]
    else:
        return []

def trade57():
    # Beta Rotation: Buy high-beta stocks if the market is rising, low-beta if falling
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    market_return = (total_market_values[0] - total_market_values[1]) / total_market_values[1]
    betas = {t: random.uniform(0.5, 2) for t in tickers}  # Placeholder, calculate actual betas
    if market_return > 0:  # Market is rising
        target_beta = 1.5  # Example target for high-beta
    else:
        target_beta = 0.8   # Example target for low-beta
    closest_ticker = min(tickers, key=lambda t: abs(betas[t] - target_beta))
    return [Trade(closest_ticker, 1 if market_return > 0 else -1)]  # Buy if rising, short if falling

def trade58():
    # Market Timing with Relative Strength: Buy strong stocks in up markets, sell in down markets
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    market_return = (total_market_values[0] - total_market_values[1]) / total_market_values[1]
    relative_strengths = {t: ((prices[t][0] - prices[t][-1]) / prices[t][-1]) for t in tickers}  # Calculate over a longer period (e.g., 20 days)
    if market_return > 0:
        strongest = max(relative_strengths, key=relative_strengths.get)
        return [Trade(strongest, 1)]
    else:
        weakest = min(relative_strengths, key=relative_strengths.get)
        return [Trade(weakest, -1)]

def trade59():
    # Relative Value to Market: Buy stocks trading below their historical average relative to the market
    # Requires historical data to calculate averages
    total_market_values = [sum(prices[t][i] for t in tickers) for i in range(len(prices[tickers[0]]))]
    relative_values = {t: prices[t][0] / total_market_values[0] for t in tickers}  # Current relative value
    historical_averages = {t: 0.05 for t in tickers}  # Placeholder, calculate actual averages
    undervalued = [t for t in tickers if relative_values[t] < historical_averages[t] * 0.95]  # Allow some buffer
    if undervalued:
        ticker = random.choice(undervalued)
        return [Trade(ticker, 1)]
    else:
        return []

def trade60():
    # Market-Cap Weighted: Allocate trade amounts proportional to each stock's market cap relative to total market
    total_market_value = sum(prices[t][0] for t in tickers)
    market_caps = {t: prices[t][0] * 1000 for t in tickers}  # Assuming 1000 shares outstanding for each stock
    weights = {t: market_caps[t] / total_market_value for t in tickers}
    total_trade_amount = 100  # Example
    trades = [Trade(t, int(weights[t] * total_trade_amount)) for t in tickers]
    return trades
```


---

<a id="file-extras-trading-trades-gpt-4o-py"></a>
## File: `extras/trading/trades_gpt-4o.py`

> **Path in repository:** `extras/trading/trades_gpt-4o.py`

```python
# tickers is a list of stock tickers
import tickers

# prices is a dict; the key is a ticker and the value is a list of historic prices, today first
import prices

# Trade represents a decision to buy or sell a quantity of a ticker
import Trade

import random
import numpy as np

def trade2():
    # Buy top performing stock in the last 5 days
    avg_prices = {ticker: np.mean(prices[ticker][:5]) for ticker in tickers}
    best_ticker = max(avg_prices, key=avg_prices.get)
    trade = Trade(best_ticker, 100)
    return [trade]

def trade3():
    # Sell worst performing stock in the last 5 days
    avg_prices = {ticker: np.mean(prices[ticker][:5]) for ticker in tickers}
    worst_ticker = min(avg_prices, key=avg_prices.get)
    trade = Trade(worst_ticker, -100)
    return [trade]

def trade4():
    # Buy random stock from top 5 performing in the last 10 days
    avg_prices = {ticker: np.mean(prices[ticker][:10]) for ticker in tickers}
    top_5_tickers = sorted(avg_prices, key=avg_prices.get, reverse=True)[:5]
    ticker = random.choice(top_5_tickers)
    trade = Trade(ticker, 100)
    return [trade]

def trade5():
    # Sell random stock from bottom 5 performing in the last 10 days
    avg_prices = {ticker: np.mean(prices[ticker][:10]) for ticker in tickers}
    bottom_5_tickers = sorted(avg_prices, key=avg_prices.get)[:5]
    ticker = random.choice(bottom_5_tickers)
    trade = Trade(ticker, -100)
    return [trade]

def trade6():
    # Buy stocks with a positive trend over the last 7 days
    trending_up = [ticker for ticker in tickers if prices[ticker][0] > prices[ticker][6]]
    ticker = random.choice(trending_up)
    trade = Trade(ticker, 100)
    return [trade]

def trade7():
    # Sell stocks with a negative trend over the last 7 days
    trending_down = [ticker for ticker in tickers if prices[ticker][0] < prices[ticker][6]]
    ticker = random.choice(trending_down)
    trade = Trade(ticker, -100)
    return [trade]

def trade8():
    # Buy stocks with the lowest volatility over the last 20 days
    volatilities = {ticker: np.std(prices[ticker][:20]) for ticker in tickers}
    least_volatile = min(volatilities, key=volatilities.get)
    trade = Trade(least_volatile, 100)
    return [trade]

def trade9():
    # Sell stocks with the highest volatility over the last 20 days
    volatilities = {ticker: np.std(prices[ticker][:20]) for ticker in tickers}
    most_volatile = max(volatilities, key=volatilities.get)
    trade = Trade(most_volatile, -100)
    return [trade]

def trade10():
    # Random mixed strategy: randomly buy or sell a random stock
    ticker = random.choice(tickers)
    quantity = random.choice([-100, 100])
    trade = Trade(ticker, quantity)
    return [trade]

def trade11():
    # Buy the top 3 performing stocks in the last 15 days
    avg_prices = {ticker: np.mean(prices[ticker][:15]) for ticker in tickers}
    top_3_tickers = sorted(avg_prices, key=avg_prices.get, reverse=True)[:3]
    trades = [Trade(ticker, 100) for ticker in top_3_tickers]
    return trades

def trade12():
    # Sell the bottom 3 performing stocks in the last 15 days
    avg_prices = {ticker: np.mean(prices[ticker][:15]) for ticker in tickers}
    bottom_3_tickers = sorted(avg_prices, key=avg_prices.get)[:3]
    trades = [Trade(ticker, -100) for ticker in bottom_3_tickers]
    return trades

def trade13():
    # Buy 2 random stocks with the highest increase in price in the last 10 days
    price_increases = {ticker: prices[ticker][0] - prices[ticker][9] for ticker in tickers}
    top_2_increases = sorted(price_increases, key=price_increases.get, reverse=True)[:2]
    trades = [Trade(ticker, 100) for ticker in top_2_increases]
    return trades

def trade14():
    # Sell 2 random stocks with the highest decrease in price in the last 10 days
    price_decreases = {ticker: prices[ticker][0] - prices[ticker][9] for ticker in tickers}
    top_2_decreases = sorted(price_decreases, key=price_decreases.get)[:2]
    trades = [Trade(ticker, -100) for ticker in top_2_decreases]
    return trades

def trade15():
    # Buy stocks that have shown the highest volatility in the last 30 days
    volatilities = {ticker: np.std(prices[ticker][:30]) for ticker in tickers}
    high_volatility_tickers = sorted(volatilities, key=volatilities.get, reverse=True)[:3]
    trades = [Trade(ticker, 100) for ticker in high_volatility_tickers]
    return trades

def trade16():
    # Sell stocks that have shown the lowest volatility in the last 30 days
    volatilities = {ticker: np.std(prices[ticker][:30]) for ticker in tickers}
    low_volatility_tickers = sorted(volatilities, key=volatilities.get)[:3]
    trades = [Trade(ticker, -100) for ticker in low_volatility_tickers]
    return trades

def trade17():
    # Buy stocks with prices above their 50-day moving average
    ma_50 = {ticker: np.mean(prices[ticker][:50]) for ticker in tickers}
    above_ma_tickers = [ticker for ticker in tickers if prices[ticker][0] > ma_50[ticker]]
    trades = [Trade(ticker, 100) for ticker in random.sample(above_ma_tickers, min(3, len(above_ma_tickers)))]
    return trades

def trade18():
    # Sell stocks with prices below their 50-day moving average
    ma_50 = {ticker: np.mean(prices[ticker][:50]) for ticker in tickers}
    below_ma_tickers = [ticker for ticker in tickers if prices[ticker][0] < ma_50[ticker]]
    trades = [Trade(ticker, -100) for ticker in random.sample(below_ma_tickers, min(3, len(below_ma_tickers)))]
    return trades

def trade19():
    # Mixed strategy: buy 2 random stocks and sell 2 random stocks
    buy_tickers = random.sample(tickers, 2)
    sell_tickers = random.sample([ticker for ticker in tickers if ticker not in buy_tickers], 2)
    trades = [Trade(ticker, 100) for ticker in buy_tickers] + [Trade(ticker, -100) for ticker in sell_tickers]
    return trades

def trade20():
    # Buy stocks that have positive return in the last 20 days and sell those with negative return
    returns = {ticker: (prices[ticker][0] - prices[ticker][19]) / prices[ticker][19] for ticker in tickers}
    buy_tickers = [ticker for ticker in tickers if returns[ticker] > 0]
    sell_tickers = [ticker for ticker in tickers if returns[ticker] < 0]
    trades = [Trade(ticker, 100) for ticker in random.sample(buy_tickers, min(2, len(buy_tickers)))] + \
             [Trade(ticker, -100) for ticker in random.sample(sell_tickers, min(2, len(sell_tickers)))]
    return trades

def trade21():
    # Buy the top performing stock in the last 3 days
    avg_prices = {ticker: np.mean(prices[ticker][:3]) for ticker in tickers}
    best_ticker = max(avg_prices, key=avg_prices.get)
    trade = Trade(best_ticker, 100)
    return [trade]

def trade22():
    # Sell the worst performing stock in the last 3 days
    avg_prices = {ticker: np.mean(prices[ticker][:3]) for ticker in tickers}
    worst_ticker = min(avg_prices, key=avg_prices.get)
    trade = Trade(worst_ticker, -100)
    return [trade]

def trade23():
    # Buy stocks that have not changed price in the last 7 days
    stable_tickers = [ticker for ticker in tickers if prices[ticker][0] == prices[ticker][6]]
    trades = [Trade(ticker, 100) for ticker in random.sample(stable_tickers, min(3, len(stable_tickers)))]
    return trades

def trade24():
    # Sell stocks that have the smallest price change in the last 5 days
    smallest_changes = sorted(tickers, key=lambda t: abs(prices[t][0] - prices[t][4]))[:3]
    trades = [Trade(ticker, -100) for ticker in smallest_changes]
    return trades

def trade25():
    # Buy random stocks from the top 10 highest priced stocks
    highest_priced = sorted(tickers, key=lambda t: prices[t][0], reverse=True)[:10]
    ticker = random.choice(highest_priced)
    trade = Trade(ticker, 100)
    return [trade]

def trade26():
    # Sell random stocks from the bottom 10 lowest priced stocks
    lowest_priced = sorted(tickers, key=lambda t: prices[t][0])[:10]
    ticker = random.choice(lowest_priced)
    trade = Trade(ticker, -100)
    return [trade]

def trade27():
    # Buy 2 stocks with the highest momentum (last 5 days)
    momentums = {ticker: prices[ticker][0] - prices[ticker][4] for ticker in tickers}
    top_momentum_tickers = sorted(momentums, key=momentums.get, reverse=True)[:2]
    trades = [Trade(ticker, 100) for ticker in top_momentum_tickers]
    return trades

def trade28():
    # Sell 2 stocks with the lowest momentum (last 5 days)
    momentums = {ticker: prices[ticker][0] - prices[ticker][4] for ticker in tickers}
    lowest_momentum_tickers = sorted(momentums, key=momentums.get)[:2]
    trades = [Trade(ticker, -100) for ticker in lowest_momentum_tickers]
    return trades

def trade29():
    # Buy the stock with the highest daily price increase yesterday
    yesterday_increase = {ticker: prices[ticker][1] - prices[ticker][2] for ticker in tickers}
    best_yesterday_ticker = max(yesterday_increase, key=yesterday_increase.get)
    trade = Trade(best_yesterday_ticker, 100)
    return [trade]

def trade30():
    # Sell the stock with the highest daily price decrease yesterday
    yesterday_decrease = {ticker: prices[ticker][1] - prices[ticker][2] for ticker in tickers}
    worst_yesterday_ticker = min(yesterday_decrease, key=yesterday_decrease.get)
    trade = Trade(worst_yesterday_ticker, -100)
    return [trade]

def trade31():
    # Long/short strategy: Buy the top performing stock and sell the worst performing stock over the last 7 days
    avg_prices = {ticker: np.mean(prices[ticker][:7]) for ticker in tickers}
    best_ticker = max(avg_prices, key=avg_prices.get)
    worst_ticker = min(avg_prices, key=avg_prices.get)
    trades = [Trade(best_ticker, 100), Trade(worst_ticker, -100)]
    return trades

def trade32():
    # Buy stocks that have had a positive return in the last 5 days and sell those with a negative return
    returns = {ticker: (prices[ticker][0] - prices[ticker][4]) / prices[ticker][4] for ticker in tickers}
    buy_tickers = [ticker for ticker in tickers if returns[ticker] > 0]
    sell_tickers = [ticker for ticker in tickers if returns[ticker] < 0]
    trades = [Trade(ticker, 100) for ticker in random.sample(buy_tickers, min(2, len(buy_tickers)))] + \
             [Trade(ticker, -100) for ticker in random.sample(sell_tickers, min(2, len(sell_tickers)))]
    return trades

def trade33():
    # Buy 2 stocks with the highest price-to-earnings ratio and sell 2 with the lowest
    pe_ratios = {ticker: random.uniform(10, 30) for ticker in tickers}  # Mock P/E ratios
    top_pe_tickers = sorted(pe_ratios, key=pe_ratios.get, reverse=True)[:2]
    low_pe_tickers = sorted(pe_ratios, key=pe_ratios.get)[:2]
    trades = [Trade(ticker, 100) for ticker in top_pe_tickers] + [Trade(ticker, -100) for ticker in low_pe_tickers]
    return trades

def trade34():
    # Buy the stock with the highest volume and sell the one with the lowest volume
    volumes = {ticker: random.randint(1000, 10000) for ticker in tickers}  # Mock volumes
    high_volume_ticker = max(volumes, key=volumes.get)
    low_volume_ticker = min(volumes, key=volumes.get)
    trades = [Trade(high_volume_ticker, 100), Trade(low_volume_ticker, -100)]
    return trades

def trade35():
    # Buy 3 stocks with the highest recent momentum and sell 3 with the lowest recent momentum
    momentums = {ticker: prices[ticker][0] - prices[ticker][5] for ticker in tickers}
    top_momentum_tickers = sorted(momentums, key=momentums.get, reverse=True)[:3]
    low_momentum_tickers = sorted(momentums, key=momentums.get)[:3]
    trades = [Trade(ticker, 100) for ticker in top_momentum_tickers] + [Trade(ticker, -100) for ticker in low_momentum_tickers]
    return trades

def trade36():
    # Buy stocks in the technology sector and sell stocks in the energy sector
    tech_stocks = random.sample(tickers, 3)  # Mock tech stocks
    energy_stocks = random.sample(tickers, 3)  # Mock energy stocks
    trades = [Trade(ticker, 100) for ticker in tech_stocks] + [Trade(ticker, -100) for ticker in energy_stocks]
    return trades

def trade37():
    # Long/short strategy: Buy the top 2 stocks with the highest recent gains and sell the top 2 with the highest recent losses
    recent_gains = {ticker: prices[ticker][0] - prices[ticker][10] for ticker in tickers}
    top_gainers = sorted(recent_gains, key=recent_gains.get, reverse=True)[:2]
    top_losers = sorted(recent_gains, key=recent_gains.get)[:2]
    trades = [Trade(ticker, 100) for ticker in top_gainers] + [Trade(ticker, -100) for ticker in top_losers]
    return trades

def trade38():
    # Buy the stocks with the highest dividend yield and sell those with the lowest
    dividend_yields = {ticker: random.uniform(1, 5) for ticker in tickers}  # Mock dividend yields
    high_yield_tickers = sorted(dividend_yields, key=dividend_yields.get, reverse=True)[:2]
    low_yield_tickers = sorted(dividend_yields, key=dividend_yields.get)[:2]
    trades = [Trade(ticker, 100) for ticker in high_yield_tickers] + [Trade(ticker, -100) for ticker in low_yield_tickers]
    return trades

def trade39():
    # Buy stocks that are trading near their 52-week highs and sell those near their 52-week lows
    highs_52w = {ticker: max(prices[ticker]) for ticker in tickers}
    lows_52w = {ticker: min(prices[ticker]) for ticker in tickers}
    near_highs = [ticker for ticker in tickers if prices[ticker][0] >= 0.9 * highs_52w[ticker]]
    near_lows = [ticker for ticker in tickers if prices[ticker][0] <= 1.1 * lows_52w[ticker]]
    trades = [Trade(ticker, 100) for ticker in random.sample(near_highs, min(2, len(near_highs)))] + \
             [Trade(ticker, -100) for ticker in random.sample(near_lows, min(2, len(near_lows)))]
    return trades

def trade40():
    # Long/short strategy: Buy 2 random stocks from the top 10 performing sectors and sell 2 from the bottom 10
    sectors = {ticker: random.choice(['Tech', 'Energy', 'Health', 'Finance', 'Retail']) for ticker in tickers}
    sector_performance = {sector: random.uniform(-10, 10) for sector in set(sectors.values())}
    top_sectors = sorted(sector_performance, key=sector_performance.get, reverse=True)[:2]
    bottom_sectors = sorted(sector_performance, key=sector_performance.get)[:2]
    buy_tickers = [ticker for ticker in tickers if sectors[ticker] in top_sectors]
    sell_tickers = [ticker for ticker in tickers if sectors[ticker] in bottom_sectors]
    trades = [Trade(ticker, 100) for ticker in random.sample(buy_tickers, min(2, len(buy_tickers)))] + \
             [Trade(ticker, -100) for ticker in random.sample(sell_tickers, min(2, len(sell_tickers)))]
    return trades

def trade41():
    # Buy the stock with the highest price increase today
    price_increases = {ticker: prices[ticker][0] - prices[ticker][1] for ticker in tickers}
    best_ticker = max(price_increases, key=price_increases.get)
    trade = Trade(best_ticker, 100)
    return [trade]

def trade42():
    # Sell the stock with the highest price decrease today
    price_decreases = {ticker: prices[ticker][0] - prices[ticker][1] for ticker in tickers}
    worst_ticker = min(price_decreases, key=price_decreases.get)
    trade = Trade(worst_ticker, -100)
    return [trade]

def trade43():
    # Buy stocks that have had a positive return in the last 3 days
    returns = {ticker: (prices[ticker][0] - prices[ticker][2]) / prices[ticker][2] for ticker in tickers}
    buy_tickers = [ticker for ticker in tickers if returns[ticker] > 0]
    trades = [Trade(ticker, 100) for ticker in random.sample(buy_tickers, min(3, len(buy_tickers)))]
    return trades

def trade44():
    # Sell stocks that have had a negative return in the last 3 days
    returns = {ticker: (prices[ticker][0] - prices[ticker][2]) / prices[ticker][2] for ticker in tickers}
    sell_tickers = [ticker for ticker in tickers if returns[ticker] < 0]
    trades = [Trade(ticker, -100) for ticker in random.sample(sell_tickers, min(3, len(sell_tickers)))]
    return trades

def trade45():
    # Buy the stock with the highest average return over the last 10 days
    avg_returns = {ticker: np.mean([(prices[ticker][i] - prices[ticker][i+1]) / prices[ticker][i+1] for i in range(9)]) for ticker in tickers}
    best_ticker = max(avg_returns, key=avg_returns.get)
    trade = Trade(best_ticker, 100)
    return [trade]

def trade46():
    # Sell the stock with the lowest average return over the last 10 days
    avg_returns = {ticker: np.mean([(prices[ticker][i] - prices[ticker][i+1]) / prices[ticker][i+1] for i in range(9)]) for ticker in tickers}
    worst_ticker = min(avg_returns, key=avg_returns.get)
    trade = Trade(worst_ticker, -100)
    return [trade]

def trade47():
    # Buy stocks that are oversold based on RSI (Randomly assigned for simplicity)
    rsi = {ticker: random.uniform(0, 100) for ticker in tickers}
    oversold_tickers = [ticker for ticker in tickers if rsi[ticker] < 30]
    trades = [Trade(ticker, 100) for ticker in random.sample(oversold_tickers, min(3, len(oversold_tickers)))]
    return trades

def trade48():
    # Sell stocks that are overbought based on RSI (Randomly assigned for simplicity)
    rsi = {ticker: random.uniform(0, 100) for ticker in tickers}
    overbought_tickers = [ticker for ticker in tickers if rsi[ticker] > 70]
    trades = [Trade(ticker, -100) for ticker in random.sample(overbought_tickers, min(3, len(overbought_tickers)))]
    return trades

def trade49():
    # Buy stocks with positive momentum over the last 20 days
    momentums = {ticker: prices[ticker][0] - prices[ticker][19] for ticker in tickers}
    positive_momentum_tickers = [ticker for ticker in momentums if momentums[ticker] > 0]
    trades = [Trade(ticker, 100) for ticker in random.sample(positive_momentum_tickers, min(3, len(positive_momentum_tickers)))]
    return trades

def trade50():
    # Sell stocks with negative momentum over the last 20 days
    momentums = {ticker: prices[ticker][0] - prices[ticker][19] for ticker in tickers}
    negative_momentum_tickers = [ticker for ticker in momentums if momentums[ticker] < 0]
    trades = [Trade(ticker, -100) for ticker in random.sample(negative_momentum_tickers, min(3, len(negative_momentum_tickers)))]
    return trades

def trade51():
    # Buy stocks that have a high positive correlation with a randomly chosen strong performer
    import scipy.stats
    base_ticker = random.choice(tickers)
    base_prices = prices[base_ticker]
    correlations = {ticker: scipy.stats.pearsonr(base_prices, prices[ticker])[0] for ticker in tickers if ticker != base_ticker}
    high_corr_tickers = [ticker for ticker, corr in correlations.items() if corr > 0.8]
    trades = [Trade(ticker, 100) for ticker in random.sample(high_corr_tickers, min(3, len(high_corr_tickers)))]
    return trades

def trade52():
    # Sell stocks that have a high negative correlation with a randomly chosen weak performer
    import scipy.stats
    base_ticker = random.choice(tickers)
    base_prices = prices[base_ticker]
    correlations = {ticker: scipy.stats.pearsonr(base_prices, prices[ticker])[0] for ticker in tickers if ticker != base_ticker}
    low_corr_tickers = [ticker for ticker, corr in correlations.items() if corr < -0.8]
    trades = [Trade(ticker, -100) for ticker in random.sample(low_corr_tickers, min(3, len(low_corr_tickers)))]
    return trades

def trade53():
    # Long/short strategy: Buy stocks with high positive correlation and sell stocks with high negative correlation to a strong performer
    import scipy.stats
    base_ticker = random.choice(tickers)
    base_prices = prices[base_ticker]
    correlations = {ticker: scipy.stats.pearsonr(base_prices, prices[ticker])[0] for ticker in tickers if ticker != base_ticker}
    high_corr_tickers = [ticker for ticker, corr in correlations.items() if corr > 0.7]
    low_corr_tickers = [ticker for ticker, corr in correlations.items() if corr < -0.7]
    trades = [Trade(ticker, 100) for ticker in random.sample(high_corr_tickers, min(2, len(high_corr_tickers)))] + \
             [Trade(ticker, -100) for ticker in random.sample(low_corr_tickers, min(2, len(low_corr_tickers)))]
    return trades

def trade54():
    # Buy stocks that have a high correlation with an index (e.g., S&P 500)
    import scipy.stats
    index_prices = [random.uniform(1000, 5000) for _ in range(len(prices[tickers[0]]))]  # Mock index prices
    correlations = {ticker: scipy.stats.pearsonr(index_prices, prices[ticker])[0] for ticker in tickers}
    high_corr_tickers = [ticker for ticker, corr in correlations.items() if corr > 0.8]
    trades = [Trade(ticker, 100) for ticker in random.sample(high_corr_tickers, min(3, len(high_corr_tickers)))]
    return trades

def trade55():
    # Sell stocks that have a low correlation with an index (e.g., S&P 500)
    import scipy.stats
    index_prices = [random.uniform(1000, 5000) for _ in range(len(prices[tickers[0]]))]  # Mock index prices
    correlations = {ticker: scipy.stats.pearsonr(index_prices, prices[ticker])[0] for ticker in tickers}
    low_corr_tickers = [ticker for ticker, corr in correlations.items() if corr < 0.2]
    trades = [Trade(ticker, -100) for ticker in random.sample(low_corr_tickers, min(3, len(low_corr_tickers)))]
    return trades

def trade56():
    # Long/short strategy: Buy stocks with high correlation and sell stocks with low correlation to a randomly chosen strong performer
    import scipy.stats
    base_ticker = random.choice(tickers)
    base_prices = prices[base_ticker]
    correlations = {ticker: scipy.stats.pearsonr(base_prices, prices[ticker])[0] for ticker in tickers if ticker != base_ticker}
    high_corr_tickers = [ticker for ticker, corr in correlations.items() if corr > 0.7]
    low_corr_tickers = [ticker for ticker, corr in correlations.items() if corr < 0.2]
    trades = [Trade(ticker, 100) for ticker in random.sample(high_corr_tickers, min(2, len(high_corr_tickers)))] + \
             [Trade(ticker, -100) for ticker in random.sample(low_corr_tickers, min(2, len(low_corr_tickers)))]
    return trades

def trade57():
    # Buy stocks that are inversely correlated with a major sector ETF (mocked data)
    import scipy.stats
    sector_etf_prices = [random.uniform(50, 150) for _ in range(len(prices[tickers[0]]))]  # Mock sector ETF prices
    correlations = {ticker: scipy.stats.pearsonr(sector_etf_prices, prices[ticker])[0] for ticker in tickers}
    inverse_corr_tickers = [ticker for ticker, corr in correlations.items() if corr < -0.7]
    trades = [Trade(ticker, 100) for ticker in random.sample(inverse_corr_tickers, min(3, len(inverse_corr_tickers)))]
    return trades

def trade58():
    # Sell stocks that are highly correlated with a volatile index
    import scipy.stats
    volatile_index_prices = [random.uniform(1000, 2000) for _ in range(len(prices[tickers[0]]))]  # Mock volatile index prices
    correlations = {ticker: scipy.stats.pearsonr(volatile_index_prices, prices[ticker])[0] for ticker in tickers}
    high_corr_tickers = [ticker for ticker, corr in correlations.items() if corr > 0.8]
    trades = [Trade(ticker, -100) for ticker in random.sample(high_corr_tickers, min(3, len(high_corr_tickers)))]
    return trades

def trade59():
    # Buy stocks that are less correlated with the overall market (S&P 500)
    import scipy.stats
    market_prices = [random.uniform(1000, 5000) for _ in range(len(prices[tickers[0]]))]  # Mock market index prices
    correlations = {ticker: scipy.stats.pearsonr(market_prices, prices[ticker])[0] for ticker in tickers}
    low_corr_tickers = [ticker for ticker, corr in correlations.items() if corr < 0.3]
    trades = [Trade(ticker, 100) for ticker in random.sample(low_corr_tickers, min(3, len(low_corr_tickers)))]
    return trades

def trade60():
    # Sell stocks that are highly correlated with a specific commodity price (e.g., oil)
    import scipy.stats
    commodity_prices = [random.uniform(50, 100) for _ in range(len(prices[tickers[0]]))]  # Mock commodity prices
    correlations = {ticker: scipy.stats.pearsonr(commodity_prices, prices[ticker])[0] for ticker in tickers}
    high_corr_tickers = [ticker for ticker, corr in correlations.items() if corr > 0.7]
    trades = [Trade(ticker, -100) for ticker in random.sample(high_corr_tickers, min(3, len(high_corr_tickers)))]
    return trades

def trade61():
    # Buy stocks forming a "double bottom" pattern (last 5 days)
    double_bottom_tickers = [ticker for ticker in tickers if prices[ticker][4] < prices[ticker][2] == prices[ticker][0] < prices[ticker][1] and prices[ticker][3] > prices[ticker][2]]
    trades = [Trade(ticker, 100) for ticker in random.sample(double_bottom_tickers, min(3, len(double_bottom_tickers)))]
    return trades

def trade62():
    # Sell stocks forming a "double top" pattern (last 5 days)
    double_top_tickers = [ticker for ticker in tickers if prices[ticker][4] > prices[ticker][2] == prices[ticker][0] > prices[ticker][1] and prices[ticker][3] < prices[ticker][2]]
    trades = [Trade(ticker, -100) for ticker in random.sample(double_top_tickers, min(3, len(double_top_tickers)))]
    return trades

def trade63():
    # Buy stocks showing a "head and shoulders" bottom pattern (last 7 days)
    hs_bottom_tickers = [ticker for ticker in tickers if prices[ticker][6] > prices[ticker][5] < prices[ticker][4] > prices[ticker][3] < prices[ticker][2] and prices[ticker][1] < prices[ticker][0]]
    trades = [Trade(ticker, 100) for ticker in random.sample(hs_bottom_tickers, min(3, len(hs_bottom_tickers)))]
    return trades

def trade64():
    # Sell stocks showing a "head and shoulders" top pattern (last 7 days)
    hs_top_tickers = [ticker for ticker in tickers if prices[ticker][6] < prices[ticker][5] > prices[ticker][4] < prices[ticker][3] > prices[ticker][2] and prices[ticker][1] > prices[ticker][0]]
    trades = [Trade(ticker, -100) for ticker in random.sample(hs_top_tickers, min(3, len(hs_top_tickers)))]
    return trades

def trade65():
    # Buy stocks forming a "bullish flag" pattern (last 10 days)
    bullish_flag_tickers = [ticker for ticker in tickers if prices[ticker][9] < prices[ticker][8] and all(prices[ticker][i] < prices[ticker][i+1] for i in range(8, 4, -1)) and all(prices[ticker][i] > prices[ticker][i+1] for i in range(4, 0, -1))]
    trades = [Trade(ticker, 100) for ticker in random.sample(bullish_flag_tickers, min(3, len(bullish_flag_tickers)))]
    return trades

def trade66():
    # Sell stocks forming a "bearish flag" pattern (last 10 days)
    bearish_flag_tickers = [ticker for ticker in tickers if prices[ticker][9] > prices[ticker][8] and all(prices[ticker][i] > prices[ticker][i+1] for i in range(8, 4, -1)) and all(prices[ticker][i] < prices[ticker][i+1] for i in range(4, 0, -1))]
    trades = [Trade(ticker, -100) for ticker in random.sample(bearish_flag_tickers, min(3, len(bearish_flag_tickers)))]
    return trades

def trade67():
    # Buy stocks forming a "ascending triangle" pattern (last 15 days)
    ascending_triangle_tickers = [ticker for ticker in tickers if prices[ticker][14] < prices[ticker][13] and prices[ticker][0] > prices[ticker][7] and all(prices[ticker][i] <= prices[ticker][i+1] for i in range(13))]
    trades = [Trade(ticker, 100) for ticker in random.sample(ascending_triangle_tickers, min(3, len(ascending_triangle_tickers)))]
    return trades

def trade68():
    # Sell stocks forming a "descending triangle" pattern (last 15 days)
    descending_triangle_tickers = [ticker for ticker in tickers if prices[ticker][14] > prices[ticker][13] and prices[ticker][0] < prices[ticker][7] and all(prices[ticker][i] >= prices[ticker][i+1] for i in range(13))]
    trades = [Trade(ticker, -100) for ticker in random.sample(descending_triangle_tickers, min(3, len(descending_triangle_tickers)))]
    return trades

def trade69():
    # Buy stocks forming a "rounding bottom" pattern (last 20 days)
    rounding_bottom_tickers = [ticker for ticker in tickers if all(prices[ticker][i] >= prices[ticker][i+1] for i in range(10)) and all(prices[ticker][i] <= prices[ticker][i+1] for i in range(10, 19))]
    trades = [Trade(ticker, 100) for ticker in random.sample(rounding_bottom_tickers, min(3, len(rounding_bottom_tickers)))]
    return trades

def trade70():
    # Sell stocks forming a "rounding top" pattern (last 20 days)
    rounding_top_tickers = [ticker for ticker in tickers if all(prices[ticker][i] <= prices[ticker][i+1] for i in range(10)) and all(prices[ticker][i] >= prices[ticker][i+1] for i in range(10, 19))]
    trades = [Trade(ticker, -100) for ticker in random.sample(rounding_top_tickers, min(3, len(rounding_top_tickers)))]
    return trades

def trade71():
    # Buy stocks showing a strong upward trend over the last 10 days
    upward_trend_tickers = [ticker for ticker in tickers if prices[ticker][0] > prices[ticker][9] and all(prices[ticker][i] >= prices[ticker][i+1] for i in range(9))]
    trades = [Trade(ticker, 100) for ticker in random.sample(upward_trend_tickers, min(3, len(upward_trend_tickers)))]
    return trades

def trade72():
    # Sell stocks showing a strong downward trend over the last 10 days
    downward_trend_tickers = [ticker for ticker in tickers if prices[ticker][0] < prices[ticker][9] and all(prices[ticker][i] <= prices[ticker][i+1] for i in range(9))]
    trades = [Trade(ticker, -100) for ticker in random.sample(downward_trend_tickers, min(3, len(downward_trend_tickers)))]
    return trades

def trade73():
    # Buy stocks that have reverted to their mean price over the last 20 days
    mean_reversion_tickers = [ticker for ticker in tickers if abs(prices[ticker][0] - np.mean(prices[ticker][:20])) < np.std(prices[ticker][:20])]
    trades = [Trade(ticker, 100) for ticker in random.sample(mean_reversion_tickers, min(3, len(mean_reversion_tickers)))]
    return trades

def trade74():
    # Sell stocks that have deviated significantly from their mean price over the last 20 days
    mean_deviation_tickers = [ticker for ticker in tickers if abs(prices[ticker][0] - np.mean(prices[ticker][:20])) > 2 * np.std(prices[ticker][:20])]
    trades = [Trade(ticker, -100) for ticker in random.sample(mean_deviation_tickers, min(3, len(mean_deviation_tickers)))]
    return trades

def trade75():
    # Buy stocks that have shown increased volatility in the last 10 days compared to the previous 20 days
    increased_volatility_tickers = [ticker for ticker in tickers if np.std(prices[ticker][:10]) > 1.5 * np.std(prices[ticker][10:30])]
    trades = [Trade(ticker, 100) for ticker in random.sample(increased_volatility_tickers, min(3, len(increased_volatility_tickers)))]
    return trades

def trade76():
    # Sell stocks that have shown decreased volatility in the last 10 days compared to the previous 20 days
    decreased_volatility_tickers = [ticker for ticker in tickers if np.std(prices[ticker][:10]) < 0.5 * np.std(prices[ticker][10:30])]
    trades = [Trade(ticker, -100) for ticker in random.sample(decreased_volatility_tickers, min(3, len(decreased_volatility_tickers)))]
    return trades

def trade77():
    # Buy stocks that have broken above their previous 50-day high
    previous_50_day_highs = {ticker: max(prices[ticker][1:51]) for ticker in tickers}
    breakout_tickers = [ticker for ticker in tickers if prices[ticker][0] > previous_50_day_highs[ticker]]
    trades = [Trade(ticker, 100) for ticker in random.sample(breakout_tickers, min(3, len(breakout_tickers)))]
    return trades

def trade78():
    # Sell stocks that have broken below their previous 50-day low
    previous_50_day_lows = {ticker: min(prices[ticker][1:51]) for ticker in tickers}
    breakdown_tickers = [ticker for ticker in tickers if prices[ticker][0] < previous_50_day_lows[ticker]]
    trades = [Trade(ticker, -100) for ticker in random.sample(breakdown_tickers, min(3, len(breakdown_tickers)))]
    return trades

def trade79():
    # Buy stocks that have shown a significant upward price spike in the last 3 days
    price_spike_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][2]) / prices[ticker][2] > 0.1]
    trades = [Trade(ticker, 100) for ticker in random.sample(price_spike_tickers, min(3, len(price_spike_tickers)))]
    return trades

def trade80():
    # Sell stocks that have shown a significant downward price spike in the last 3 days
    price_drop_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][2]) / prices[ticker][2] < -0.1]
    trades = [Trade(ticker, -100) for ticker in random.sample(price_drop_tickers, min(3, len(price_drop_tickers)))]
    return trades

def trade81():
    # Buy stocks that have formed a "golden cross" (50-day MA crosses above 200-day MA)
    golden_cross_tickers = [ticker for ticker in tickers if np.mean(prices[ticker][:50]) > np.mean(prices[ticker][:200])]
    trades = [Trade(ticker, 100) for ticker in random.sample(golden_cross_tickers, min(3, len(golden_cross_tickers)))]
    return trades

def trade82():
    # Sell stocks that have formed a "death cross" (50-day MA crosses below 200-day MA)
    death_cross_tickers = [ticker for ticker in tickers if np.mean(prices[ticker][:50]) < np.mean(prices[ticker][:200])]
    trades = [Trade(ticker, -100) for ticker in random.sample(death_cross_tickers, min(3, len(death_cross_tickers)))]
    return trades

def trade83():
    # Buy stocks that have shown an increase in trading volume in the last 5 days
    volume_increase_tickers = [ticker for ticker in tickers if np.mean(prices[ticker][:5]) > 1.2 * np.mean(prices[ticker][5:10])]
    trades = [Trade(ticker, 100) for ticker in random.sample(volume_increase_tickers, min(3, len(volume_increase_tickers)))]
    return trades

def trade84():
    # Sell stocks that have shown a decrease in trading volume in the last 5 days
    volume_decrease_tickers = [ticker for ticker in tickers if np.mean(prices[ticker][:5]) < 0.8 * np.mean(prices[ticker][5:10])]
    trades = [Trade(ticker, -100) for ticker in random.sample(volume_decrease_tickers, min(3, len(volume_decrease_tickers)))]
    return trades

def trade85():
    # Buy stocks that have shown consistent daily gains for the last 5 days
    consistent_gainers = [ticker for ticker in tickers if all(prices[ticker][i] > prices[ticker][i+1] for i in range(5))]
    trades = [Trade(ticker, 100) for ticker in random.sample(consistent_gainers, min(3, len(consistent_gainers)))]
    return trades

def trade86():
    # Sell stocks that have shown consistent daily losses for the last 5 days
    consistent_losers = [ticker for ticker in tickers if all(prices[ticker][i] < prices[ticker][i+1] for i in range(5))]
    trades = [Trade(ticker, -100) for ticker in random.sample(consistent_losers, min(3, len(consistent_losers)))]
    return trades

def trade87():
    # Buy stocks that are trading near their all-time highs
    all_time_high_tickers = [ticker for ticker in tickers if prices[ticker][0] >= 0.95 * max(prices[ticker])]
    trades = [Trade(ticker, 100) for ticker in random.sample(all_time_high_tickers, min(3, len(all_time_high_tickers)))]
    return trades

def trade88():
    # Sell stocks that are trading near their all-time lows
    all_time_low_tickers = [ticker for ticker in tickers if prices[ticker][0] <= 1.05 * min(prices[ticker])]
    trades = [Trade(ticker, -100) for ticker in random.sample(all_time_low_tickers, min(3, len(all_time_low_tickers)))]
    return trades

def trade89():
    # Buy stocks that have gapped up at market open today
    gap_up_tickers = [ticker for ticker in tickers if prices[ticker][0] > 1.05 * prices[ticker][1]]
    trades = [Trade(ticker, 100) for ticker in random.sample(gap_up_tickers, min(3, len(gap_up_tickers)))]
    return trades

def trade90():
    # Sell stocks that have gapped down at market open today
    gap_down_tickers = [ticker for ticker in tickers if prices[ticker][0] < 0.95 * prices[ticker][1]]
    trades = [Trade(ticker, -100) for ticker in random.sample(gap_down_tickers, min(3, len(gap_down_tickers)))]
    return trades

def trade91():
    # Buy stocks that have shown a steady upward trend for the last 15 days
    steady_uptrend_tickers = [ticker for ticker in tickers if all(prices[ticker][i] >= prices[ticker][i+1] for i in range(15))]
    trades = [Trade(ticker, 100) for ticker in random.sample(steady_uptrend_tickers, min(3, len(steady_uptrend_tickers)))]
    return trades

def trade92():
    # Sell stocks that have shown a steady downward trend for the last 15 days
    steady_downtrend_tickers = [ticker for ticker in tickers if all(prices[ticker][i] <= prices[ticker][i+1] for i in range(15))]
    trades = [Trade(ticker, -100) for ticker in random.sample(steady_downtrend_tickers, min(3, len(steady_downtrend_tickers)))]
    return trades

def trade93():
    # Buy stocks that have outperformed the market index by 5% in the last 30 days
    market_index_return = random.uniform(-0.05, 0.05)  # Mock market index return
    outperforming_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][29]) / prices[ticker][29] > market_index_return + 0.05]
    trades = [Trade(ticker, 100) for ticker in random.sample(outperforming_tickers, min(3, len(outperforming_tickers)))]
    return trades

def trade94():
    # Sell stocks that have underperformed the market index by 5% in the last 30 days
    market_index_return = random.uniform(-0.05, 0.05)  # Mock market index return
    underperforming_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][29]) / prices[ticker][29] < market_index_return - 0.05]
    trades = [Trade(ticker, -100) for ticker in random.sample(underperforming_tickers, min(3, len(underperforming_tickers)))]
    return trades

def trade95():
    # Buy stocks that have broken above their previous 10-day high
    previous_10_day_highs = {ticker: max(prices[ticker][1:11]) for ticker in tickers}
    breakout_tickers = [ticker for ticker in tickers if prices[ticker][0] > previous_10_day_highs[ticker]]
    trades = [Trade(ticker, 100) for ticker in random.sample(breakout_tickers, min(3, len(breakout_tickers)))]
    return trades

def trade96():
    # Sell stocks that have broken below their previous 10-day low
    previous_10_day_lows = {ticker: min(prices[ticker][1:11]) for ticker in tickers}
    breakdown_tickers = [ticker for ticker in tickers if prices[ticker][0] < previous_10_day_lows[ticker]]
    trades = [Trade(ticker, -100) for ticker in random.sample(breakdown_tickers, min(3, len(breakdown_tickers)))]
    return trades

def trade97():
    # Buy stocks with a relative strength index (RSI) below 30 (oversold)
    rsi = {ticker: random.uniform(0, 100) for ticker in tickers}  # Mock RSI values
    oversold_tickers = [ticker for ticker in tickers if rsi[ticker] < 30]
    trades = [Trade(ticker, 100) for ticker in random.sample(oversold_tickers, min(3, len(oversold_tickers)))]
    return trades

def trade98():
    # Sell stocks with a relative strength index (RSI) above 70 (overbought)
    rsi = {ticker: random.uniform(0, 100) for ticker in tickers}  # Mock RSI values
    overbought_tickers = [ticker for ticker in tickers if rsi[ticker] > 70]
    trades = [Trade(ticker, -100) for ticker in random.sample(overbought_tickers, min(3, len(overbought_tickers)))]
    return trades

def trade99():
    # Buy stocks with a price-to-earnings ratio (P/E) below the industry average (mocked data)
    pe_ratios = {ticker: random.uniform(10, 30) for ticker in tickers}  # Mock P/E ratios
    industry_average_pe = 20  # Mock industry average P/E
    undervalued_tickers = [ticker for ticker in tickers if pe_ratios[ticker] < industry_average_pe]
    trades = [Trade(ticker, 100) for ticker in random.sample(undervalued_tickers, min(3, len(undervalued_tickers)))]
    return trades

def trade100():
    # Sell stocks with a price-to-earnings ratio (P/E) above the industry average (mocked data)
    pe_ratios = {ticker: random.uniform(10, 30) for ticker in tickers}  # Mock P/E ratios
    industry_average_pe = 20  # Mock industry average P/E
    overvalued_tickers = [ticker for ticker in tickers if pe_ratios[ticker] > industry_average_pe]
    trades = [Trade(ticker, -100) for ticker in random.sample(overvalued_tickers, min(3, len(overvalued_tickers)))]
    return trades

def trade101():
    # Buy stocks that have outperformed the market by more than 5% in the last 10 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(10)]
    market_return = (market_total[0] - market_total[-1]) / market_total[-1]
    outperforming_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][9]) / prices[ticker][9] > market_return + 0.05]
    trades = [Trade(ticker, 100) for ticker in random.sample(outperforming_tickers, min(3, len(outperforming_tickers)))]
    return trades

def trade102():
    # Sell stocks that have underperformed the market by more than 5% in the last 10 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(10)]
    market_return = (market_total[0] - market_total[-1]) / market_total[-1]
    underperforming_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][9]) / prices[ticker][9] < market_return - 0.05]
    trades = [Trade(ticker, -100) for ticker in random.sample(underperforming_tickers, min(3, len(underperforming_tickers)))]
    return trades

def trade103():
    # Buy stocks that have shown a positive return while the market showed a negative return over the last 5 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(5)]
    market_return = (market_total[0] - market_total[-1]) / market_total[-1]
    positive_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][4]) / prices[ticker][4] > 0 and market_return < 0]
    trades = [Trade(ticker, 100) for ticker in random.sample(positive_tickers, min(3, len(positive_tickers)))]
    return trades

def trade104():
    # Sell stocks that have shown a negative return while the market showed a positive return over the last 5 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(5)]
    market_return = (market_total[0] - market_total[-1]) / market_total[-1]
    negative_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][4]) / prices[ticker][4] < 0 and market_return > 0]
    trades = [Trade(ticker, -100) for ticker in random.sample(negative_tickers, min(3, len(negative_tickers)))]
    return trades

def trade105():
    # Buy stocks that have shown less volatility compared to the market over the last 20 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(20)]
    market_volatility = np.std(market_total)
    low_volatility_tickers = [ticker for ticker in tickers if np.std(prices[ticker][:20]) < market_volatility]
    trades = [Trade(ticker, 100) for ticker in random.sample(low_volatility_tickers, min(3, len(low_volatility_tickers)))]
    return trades

def trade106():
    # Sell stocks that have shown more volatility compared to the market over the last 20 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(20)]
    market_volatility = np.std(market_total)
    high_volatility_tickers = [ticker for ticker in tickers if np.std(prices[ticker][:20]) > market_volatility]
    trades = [Trade(ticker, -100) for ticker in random.sample(high_volatility_tickers, min(3, len(high_volatility_tickers)))]
    return trades

def trade107():
    # Buy stocks that have shown an increasing trend while the market showed a decreasing trend over the last 15 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(15)]
    market_trend = market_total[0] > market_total[-1]
    increasing_tickers = [ticker for ticker in tickers if prices[ticker][0] > prices[ticker][14] and not market_trend]
    trades = [Trade(ticker, 100) for ticker in random.sample(increasing_tickers, min(3, len(increasing_tickers)))]
    return trades

def trade108():
    # Sell stocks that have shown a decreasing trend while the market showed an increasing trend over the last 15 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(15)]
    market_trend = market_total[0] < market_total[-1]
    decreasing_tickers = [ticker for ticker in tickers if prices[ticker][0] < prices[ticker][14] and market_trend]
    trades = [Trade(ticker, -100) for ticker in random.sample(decreasing_tickers, min(3, len(decreasing_tickers)))]
    return trades

def trade109():
    # Buy stocks that have broken above their previous 10-day high while the market is flat
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(10)]
    market_flat = abs((market_total[0] - market_total[-1]) / market_total[-1]) < 0.01
    previous_10_day_highs = {ticker: max(prices[ticker][1:11]) for ticker in tickers}
    breakout_tickers = [ticker for ticker in tickers if prices[ticker][0] > previous_10_day_highs[ticker] and market_flat]
    trades = [Trade(ticker, 100) for ticker in random.sample(breakout_tickers, min(3, len(breakout_tickers)))]
    return trades

def trade110():
    # Sell stocks that have broken below their previous 10-day low while the market is flat
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(10)]
    market_flat = abs((market_total[0] - market_total[-1]) / market_total[-1]) < 0.01
    previous_10_day_lows = {ticker: min(prices[ticker][1:11]) for ticker in tickers}
    breakdown_tickers = [ticker for ticker in tickers if prices[ticker][0] < previous_10_day_lows[ticker] and market_flat]
    trades = [Trade(ticker, -100) for ticker in random.sample(breakdown_tickers, min(3, len(breakdown_tickers)))]
    return trades

def trade111():
    # Buy stocks that have shown a higher positive return compared to the market over the last 20 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(20)]
    market_return = (market_total[0] - market_total[-1]) / market_total[-1]
    higher_positive_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][19]) / prices[ticker][19] > market_return]
    trades = [Trade(ticker, 100) for ticker in random.sample(higher_positive_tickers, min(3, len(higher_positive_tickers)))]
    return trades

def trade112():
    # Sell stocks that have shown a higher negative return compared to the market over the last 20 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(20)]
    market_return = (market_total[0] - market_total[-1]) / market_total[-1]
    higher_negative_tickers = [ticker for ticker in tickers if (prices[ticker][0] - prices[ticker][19]) / prices[ticker][19] < market_return]
    trades = [Trade(ticker, -100) for ticker in random.sample(higher_negative_tickers, min(3, len(higher_negative_tickers)))]
    return trades

def trade113():
    # Buy stocks that have shown less drawdown compared to the market over the last 30 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(30)]
    market_drawdown = min(market_total) / max(market_total)
    less_drawdown_tickers = [ticker for ticker in tickers if min(prices[ticker][:30]) / max(prices[ticker][:30]) > market_drawdown]
    trades = [Trade(ticker, 100) for ticker in random.sample(less_drawdown_tickers, min(3, len(less_drawdown_tickers)))]
    return trades

def trade114():
    # Sell stocks that have shown more drawdown compared to the market over the last 30 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(30)]
    market_drawdown = min(market_total) / max(market_total)
    more_drawdown_tickers = [ticker for ticker in tickers if min(prices[ticker][:30]) / max(prices[ticker][:30]) < market_drawdown]
    trades = [Trade(ticker, -100) for ticker in random.sample(more_drawdown_tickers, min(3, len(more_drawdown_tickers)))]
    return trades

def trade115():
    # Buy stocks that have had a smaller price range compared to the market over the last 15 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(15)]
    market_range = max(market_total) - min(market_total)
    small_range_tickers = [ticker for ticker in tickers if max(prices[ticker][:15]) - min(prices[ticker][:15]) < market_range]
    trades = [Trade(ticker, 100) for ticker in random.sample(small_range_tickers, min(3, len(small_range_tickers)))]
    return trades

def trade116():
    # Sell stocks that have had a larger price range compared to the market over the last 15 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(15)]
    market_range = max(market_total) - min(market_total)
    large_range_tickers = [ticker for ticker in tickers if max(prices[ticker][:15]) - min(prices[ticker][:15]) > market_range]
    trades = [Trade(ticker, -100) for ticker in random.sample(large_range_tickers, min(3, len(large_range_tickers)))]
    return trades

def trade117():
    # Buy stocks that have consistently stayed above their market-relative average price in the last 10 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(10)]
    market_avg = sum(market_total) / len(market_total)
    consistent_above_avg_tickers = [ticker for ticker in tickers if all(prices[ticker][i] > market_avg for i in range(10))]
    trades = [Trade(ticker, 100) for ticker in random.sample(consistent_above_avg_tickers, min(3, len(consistent_above_avg_tickers)))]
    return trades

def trade118():
    # Sell stocks that have consistently stayed below their market-relative average price in the last 10 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(10)]
    market_avg = sum(market_total) / len(market_total)
    consistent_below_avg_tickers = [ticker for ticker in tickers if all(prices[ticker][i] < market_avg for i in range(10))]
    trades = [Trade(ticker, -100) for ticker in random.sample(consistent_below_avg_tickers, min(3, len(consistent_below_avg_tickers)))]
    return trades

def trade119():
    # Buy stocks that have shown a positive correlation with the market trend over the last 20 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(20)]
    market_trend = scipy.stats.linregress(range(20), market_total).slope
    positive_corr_tickers = [ticker for ticker in tickers if scipy.stats.pearsonr(prices[ticker][:20], market_total)[0] > 0.5]
    trades = [Trade(ticker, 100) for ticker in random.sample(positive_corr_tickers, min(3, len(positive_corr_tickers)))]
    return trades

def trade120():
    # Sell stocks that have shown a negative correlation with the market trend over the last 20 days
    market_total = [sum(prices[ticker][i] for ticker in tickers) for i in range(20)]
    market_trend = scipy.stats.linregress(range(20), market_total).slope
    negative_corr_tickers = [ticker for ticker in tickers if scipy.stats.pearsonr(prices[ticker][:20], market_total)[0] < -0.5]
    trades = [Trade(ticker, -100) for ticker in random.sample(negative_corr_tickers, min(3, len(negative_corr_tickers)))]
    return trades
```


---
