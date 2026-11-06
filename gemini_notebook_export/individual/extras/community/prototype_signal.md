# prototype_signal.ipynb

> **Original Path:** `extras/community/prototype_signal.ipynb`

---

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
