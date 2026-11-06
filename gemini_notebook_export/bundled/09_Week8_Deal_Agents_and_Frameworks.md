# Week8 Deal Agents and Frameworks

This unified reference file consolidates **29 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [week8/agents/agent.py](#file-week8-agents-agent-py)
- [week8/agents/autonomous_planning_agent.py](#file-week8-agents-autonomous-planning-agent-py)
- [week8/agents/deals.py](#file-week8-agents-deals-py)
- [week8/agents/deep_neural_network.py](#file-week8-agents-deep-neural-network-py)
- [week8/agents/ensemble_agent.py](#file-week8-agents-ensemble-agent-py)
- [week8/agents/evaluator.py](#file-week8-agents-evaluator-py)
- [week8/agents/frontier_agent.py](#file-week8-agents-frontier-agent-py)
- [week8/agents/items.py](#file-week8-agents-items-py)
- [week8/agents/messaging_agent.py](#file-week8-agents-messaging-agent-py)
- [week8/agents/neural_network_agent.py](#file-week8-agents-neural-network-agent-py)
- [week8/agents/planning_agent.py](#file-week8-agents-planning-agent-py)
- [week8/agents/preprocessor.py](#file-week8-agents-preprocessor-py)
- [week8/agents/scanner_agent.py](#file-week8-agents-scanner-agent-py)
- [week8/agents/specialist_agent.py](#file-week8-agents-specialist-agent-py)
- [week8/day1.ipynb](#file-week8-day1-ipynb)
- [week8/day2.ipynb](#file-week8-day2-ipynb)
- [week8/day3.ipynb](#file-week8-day3-ipynb)
- [week8/day4.ipynb](#file-week8-day4-ipynb)
- [week8/day5.ipynb](#file-week8-day5-ipynb)
- [week8/deal_agent_framework.py](#file-week8-deal-agent-framework-py)
- [week8/hello.py](#file-week8-hello-py)
- [week8/llama.py](#file-week8-llama-py)
- [week8/log_utils.py](#file-week8-log-utils-py)
- [week8/memory.json](#file-week8-memory-json)
- [week8/price_is_right.py](#file-week8-price-is-right-py)
- [week8/pricer_ephemeral.py](#file-week8-pricer-ephemeral-py)
- [week8/pricer_service.py](#file-week8-pricer-service-py)
- [week8/pricer_service2.py](#file-week8-pricer-service2-py)
- [week8/results.ipynb](#file-week8-results-ipynb)

---

<a id="file-week8-agents-agent-py"></a>
## File: `week8/agents/agent.py`

> **Path in repository:** `week8/agents/agent.py`

```python
import logging

class Agent:
    """
    An abstract superclass for Agents
    Used to log messages in a way that can identify each Agent
    """

    # Foreground colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Background color
    BG_BLACK = '\033[40m'
    
    # Reset code to return to default color
    RESET = '\033[0m'

    name: str = ""
    color: str = '\033[37m'

    def log(self, message):
        """
        Log this as an info message, identifying the agent
        """
        color_code = self.BG_BLACK + self.color
        message = f"[{self.name}] {message}"
        logging.info(color_code + message + self.RESET)
```


---

<a id="file-week8-agents-autonomous-planning-agent-py"></a>
## File: `week8/agents/autonomous_planning_agent.py`

> **Path in repository:** `week8/agents/autonomous_planning_agent.py`

```python
from typing import Optional, List, Dict
from agents.agent import Agent
from agents.deals import Deal, Opportunity
from agents.scanner_agent import ScannerAgent
from agents.ensemble_agent import EnsembleAgent
from agents.messaging_agent import MessagingAgent
from openai import OpenAI
import json


class AutonomousPlanningAgent(Agent):
    name = "Autonomous Planning Agent"
    color = Agent.GREEN
    MODEL = "gpt-5.1"

    def __init__(self, collection):
        """
        Create instances of the 3 Agents that this planner coordinates across
        """
        self.log("Autonomous Planning Agent is initializing")
        self.scanner = ScannerAgent()
        self.ensemble = EnsembleAgent(collection)
        self.messenger = MessagingAgent()
        self.openai = OpenAI()
        self.memory = None
        self.opportunity = None
        self.log("Autonomous Planning Agent is ready")

    def scan_the_internet_for_bargains(self) -> str:
        """
        Run the tool to scan
        """
        self.log("Autonomous Planning agent is calling scanner")
        results = self.scanner.scan(memory=self.memory)
        return results.model_dump_json() if results else "No deals found"

    def estimate_true_value(self, description: str) -> str:
        """
        Run the tool to estimate true value
        """
        self.log("Autonomous Planning agent is estimating value via Ensemble Agent")
        estimate = self.ensemble.price(description)
        return f"The estimated true value of {description} is {estimate}"

    def notify_user_of_deal(
        self, description: str, deal_price: float, estimated_true_value: float, url: str
    ) -> Dict:
        """
        Run the tool to notify the user
        """
        if self.opportunity:
            self.log("Autonomous Planning agent is trying to notify the user a 2nd time; ignoring")
        else:
            self.log("Autonomous Planning agent is notifying user")
            self.messenger.notify(description, deal_price, estimated_true_value, url)
            deal = Deal(product_description=description, price=deal_price, url=url)
            discount = estimated_true_value - deal_price
            self.opportunity = Opportunity(
                deal=deal, estimate=estimated_true_value, discount=discount
            )
        return "Notification sent ok"

    scan_function = {
        "name": "scan_the_internet_for_bargains",
        "description": "Returns top bargains scraped from the internet along with the price each item is being offered for",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    }

    estimate_function = {
        "name": "estimate_true_value",
        "description": "Given the description of an item, estimate how much it is actually worth",
        "parameters": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string",
                    "description": "The description of the item to be estimated",
                },
            },
            "required": ["description"],
            "additionalProperties": False,
        },
    }

    notify_function = {
        "name": "notify_user_of_deal",
        "description": "Send the user a push notification about the single most compelling deal; only call this one time",
        "parameters": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string",
                    "description": "The description of the item itself scraped from the internet",
                },
                "deal_price": {
                    "type": "number",
                    "description": "The price offered by this deal scraped from the internet",
                },
                "estimated_true_value": {
                    "type": "number",
                    "description": "The estimated actual value that this is worth",
                },
                "url": {
                    "type": "string",
                    "description": "The URL of this deal as scraped from the internet",
                },
            },
            "required": ["description", "deal_price", "estimated_true_value", "url"],
            "additionalProperties": False,
        },
    }

    def get_tools(self):
        """
        Return the json for the tools to be used
        """
        return [
            {"type": "function", "function": self.scan_function},
            {"type": "function", "function": self.estimate_function},
            {"type": "function", "function": self.notify_function},
        ]

    def handle_tool_call(self, message):
        """
        Actually call the tools associated with this message
        """
        mapping = {
            "scan_the_internet_for_bargains": self.scan_the_internet_for_bargains,
            "estimate_true_value": self.estimate_true_value,
            "notify_user_of_deal": self.notify_user_of_deal,
        }
        results = []
        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            tool = mapping.get(tool_name)
            result = tool(**arguments) if tool else ""
            results.append({"role": "tool", "content": result, "tool_call_id": tool_call.id})
        return results

    system_message = "You find great deals on bargain products using your tools, and notify the user of the best bargain."
    user_message = """
    First, use your tool to scan the internet for bargain deals. Then for each deal, use your tool to estimate its true value.
    Then pick the single most compelling deal where the price is much lower than the estimated true value, and use your tool to notify the user.
    Then just reply OK to indicate success.
    """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    def plan(self, memory: List[str] = []) -> Optional[Opportunity]:
        """
        Run the full workflow, providing the LLM with tools to surface scraped deals to the user
        :param memory: a list of URLs that have been surfaced in the past
        :return: an Opportunity if one was surfaced, otherwise None
        """
        self.log("Autonomous Planning Agent is kicking off a run")
        self.memory = memory
        self.opportunity = None
        messages = self.messages[:]
        done = False
        while not done:
            response = self.openai.chat.completions.create(
                model=self.MODEL, messages=messages, tools=self.get_tools()
            )
            if response.choices[0].finish_reason == "tool_calls":
                message = response.choices[0].message
                results = self.handle_tool_call(message)
                messages.append(message)
                messages.extend(results)
            else:
                done = True
        reply = response.choices[0].message.content
        self.log(f"Autonomous Planning Agent completed with: {reply}")
        return self.opportunity
```


---

<a id="file-week8-agents-deals-py"></a>
## File: `week8/agents/deals.py`

> **Path in repository:** `week8/agents/deals.py`

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Self
from bs4 import BeautifulSoup
import re
import feedparser
from tqdm import tqdm
import requests
import time

feeds = [
    "https://www.dealnews.com/c142/Electronics/?rss=1",
    "https://www.dealnews.com/c39/Computers/?rss=1",
    "https://www.dealnews.com/f1912/Smart-Home/?rss=1",
]

# You could also add: "https://www.dealnews.com/c238/Automotive/?rss=1"
# "https://www.dealnews.com/c196/Home-Garden/?rss=1"


def extract(html_snippet: str) -> str:
    """
    Use Beautiful Soup to clean up this HTML snippet and extract useful text
    """
    soup = BeautifulSoup(html_snippet, "html.parser")
    snippet_div = soup.find("div", class_="snippet summary")

    if snippet_div:
        description = snippet_div.get_text(strip=True)
        description = BeautifulSoup(description, "html.parser").get_text()
        description = re.sub("<[^<]+?>", "", description)
        result = description.strip()
    else:
        result = html_snippet
    return result.replace("\n", " ")


class ScrapedDeal:
    """
    A class to represent a Deal retrieved from an RSS feed
    """

    category: str
    title: str
    summary: str
    url: str
    details: str
    features: str

    def __init__(self, entry: Dict[str, str]):
        """
        Populate this instance based on the provided dict
        """
        self.title = entry["title"]
        self.summary = extract(entry["summary"])
        self.url = entry["links"][0]["href"]
        stuff = requests.get(self.url).content
        soup = BeautifulSoup(stuff, "html.parser")
        content = soup.find("div", class_="content-section").get_text()
        content = content.replace("\nmore", "").replace("\n", " ")
        if "Features" in content:
            self.details, self.features = content.split("Features", 1)
        else:
            self.details = content
            self.features = ""
        self.truncate()

    def truncate(self):
        """
        Limit the fields to a sensible length to avoid sending too much info to the model
        """
        self.title = self.title[:100]
        self.details = self.details[:500]
        self.features = self.features[:500]

    def __repr__(self):
        """
        Return a string to describe this deal
        """
        return f"<{self.title}>"

    def describe(self):
        """
        Return a longer string to describe this deal for use in calling a model
        """
        return f"Title: {self.title}\nDetails: {self.details.strip()}\nFeatures: {self.features.strip()}\nURL: {self.url}"

    @classmethod
    def fetch(cls, show_progress: bool = False) -> List[Self]:
        """
        Retrieve all deals from the selected RSS feeds
        """
        deals = []
        feed_iter = tqdm(feeds) if show_progress else feeds
        for feed_url in feed_iter:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:10]:
                deals.append(cls(entry))
                time.sleep(0.05)
        return deals


class Deal(BaseModel):
    """
    A class to Represent a Deal with a summary description
    """

    product_description: str = Field(
        description="Your clearly expressed summary of the product in 3-4 sentences. Details of the item are much more important than why it's a good deal. Avoid mentioning discounts and coupons; focus on the item itself. There should be a short paragraph of text for each item you choose."
    )
    price: float = Field(
        description="The actual price of this product, as advertised in the deal. Be sure to give the actual price; for example, if a deal is described as $100 off the usual $300 price, you should respond with $200"
    )
    url: str = Field(description="The URL of the deal, as provided in the input")


class DealSelection(BaseModel):
    """
    A class to Represent a list of Deals
    """

    deals: List[Deal] = Field(
        description="Your selection of the 5 deals that have the most detailed, high quality description and the most clear price. You should be confident that the price reflects the deal, that it is a good deal, with a clear description"
    )


class Opportunity(BaseModel):
    """
    A class to represent a possible opportunity: a Deal where we estimate
    it should cost more than it's being offered
    """

    deal: Deal
    estimate: float
    discount: float
```


---

<a id="file-week8-agents-deep-neural-network-py"></a>
## File: `week8/agents/deep_neural_network.py`

> **Path in repository:** `week8/agents/deep_neural_network.py`

```python
import numpy as np
from tqdm.notebook import tqdm
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from torch.optim.lr_scheduler import CosineAnnealingLR
from sklearn.feature_extraction.text import HashingVectorizer
import logging


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


Y_STD = 1.0328539609909058
Y_MEAN = 4.434937953948975


class DeepNeuralNetworkInference:
    def __init__(self):
        self.vectorizer = None
        self.model = None
        self.device = None

        np.random.seed(42)
        torch.manual_seed(42)
        torch.cuda.manual_seed(42)

    def setup(self):
        self.vectorizer = HashingVectorizer(n_features=5000, stop_words="english", binary=True)
        self.model = DeepNeuralNetwork(5000)
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        logging.info(f"Neural Network is using {self.device}")

        self.model.to(self.device)

    def load(self, path):
        self.model.load_state_dict(torch.load(path, map_location=self.device))
        self.model.to(self.device)

    def inference(self, text):
        self.model.eval()
        with torch.no_grad():
            vector = self.vectorizer.transform([text])
            vector = torch.FloatTensor(vector.toarray()).to(self.device)
            pred = self.model(vector)[0]
            result = torch.exp(pred * Y_STD + Y_MEAN) - 1
            result = result.item()
        return max(0, result)
```


---

<a id="file-week8-agents-ensemble-agent-py"></a>
## File: `week8/agents/ensemble_agent.py`

> **Path in repository:** `week8/agents/ensemble_agent.py`

```python
from agents.agent import Agent
from agents.specialist_agent import SpecialistAgent
from agents.frontier_agent import FrontierAgent
from agents.neural_network_agent import NeuralNetworkAgent
from agents.preprocessor import Preprocessor


class EnsembleAgent(Agent):
    name = "Ensemble Agent"
    color = Agent.YELLOW

    def __init__(self, collection):
        """
        Create an instance of Ensemble, by creating each of the models
        And loading the weights of the Ensemble
        """
        self.log("Initializing Ensemble Agent")
        self.specialist = SpecialistAgent()
        self.frontier = FrontierAgent(collection)
        self.neural_network = NeuralNetworkAgent()
        self.preprocessor = Preprocessor()
        self.log("Ensemble Agent is ready")

    def price(self, description: str) -> float:
        """
        Run this ensemble model
        Ask each of the models to price the product
        Then use the Linear Regression model to return the weighted price
        :param description: the description of a product
        :return: an estimate of its price
        """
        self.log("Running Ensemble Agent - preprocessing text")
        rewrite = self.preprocessor.preprocess(description)
        self.log(f"Pre-processed text using {self.preprocessor.model_name}")
        specialist = self.specialist.price(rewrite)
        frontier = self.frontier.price(rewrite)
        neural_network = self.neural_network.price(rewrite)
        combined = frontier * 0.8 + specialist * 0.1 + neural_network * 0.1
        self.log(f"Ensemble Agent complete - returning ${combined:.2f}")
        return combined
```


---

<a id="file-week8-agents-evaluator-py"></a>
## File: `week8/agents/evaluator.py`

> **Path in repository:** `week8/agents/evaluator.py`

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

<a id="file-week8-agents-frontier-agent-py"></a>
## File: `week8/agents/frontier_agent.py`

> **Path in repository:** `week8/agents/frontier_agent.py`

```python
import re
from typing import List, Dict
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from agents.agent import Agent


class FrontierAgent(Agent):
    name = "Frontier Agent"
    color = Agent.BLUE

    MODEL = "gpt-4o-mini"

    def __init__(self, collection):
        """
        Set up this instance by connecting to OpenAI or DeepSeek, to the Chroma Datastore,
        And setting up the vector encoding model
        """
        self.log("Initializing Frontier Agent")
        self.client = OpenAI()
        self.MODEL = "gpt-5.1"
        self.log("Frontier Agent is setting up with OpenAI")
        self.collection = collection
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.log("Frontier Agent is ready")

    def make_context(self, similars: List[str], prices: List[float]) -> str:
        """
        Create context that can be inserted into the prompt
        :param similars: similar products to the one being estimated
        :param prices: prices of the similar products
        :return: text to insert in the prompt that provides context
        """
        message = "To provide some context, here are some other items that might be similar to the item you need to estimate.\n\n"
        for similar, price in zip(similars, prices):
            message += f"Potentially related product:\n{similar}\nPrice is ${price:.2f}\n\n"
        return message

    def messages_for(
        self, description: str, similars: List[str], prices: List[float]
    ) -> List[Dict[str, str]]:
        """
        Create the message list to be included in a call to OpenAI
        With the system and user prompt
        :param description: a description of the product
        :param similars: similar products to this one
        :param prices: prices of similar products
        :return: the list of messages in the format expected by OpenAI
        """
        message = f"Estimate the price of this product. Respond with the price, no explanation\n\n{description}\n\n"
        message += self.make_context(similars, prices)
        return [{"role": "user", "content": message}]

    def find_similars(self, description: str):
        """
        Return a list of items similar to the given one by looking in the Chroma datastore
        """
        self.log(
            "Frontier Agent is performing a RAG search of the Chroma datastore to find 5 similar products"
        )
        vector = self.model.encode([description])
        results = self.collection.query(query_embeddings=vector.astype(float).tolist(), n_results=5)
        documents = results["documents"][0][:]
        prices = [m["price"] for m in results["metadatas"][0][:]]
        self.log("Frontier Agent has found similar products")
        return documents, prices

    def get_price(self, s) -> float:
        """
        A utility that plucks a floating point number out of a string
        """
        s = s.replace("$", "").replace(",", "")
        match = re.search(r"[-+]?\d*\.\d+|\d+", s)
        return float(match.group()) if match else 0.0

    def price(self, description: str) -> float:
        """
        Make a call to OpenAI or DeepSeek to estimate the price of the described product,
        by looking up 5 similar products and including them in the prompt to give context
        :param description: a description of the product
        :return: an estimate of the price
        """
        documents, prices = self.find_similars(description)
        self.log(
            f"Frontier Agent is about to call {self.MODEL} with context including 5 similar products"
        )
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=self.messages_for(description, documents, prices),
            seed=42,
            reasoning_effort="none",
        )
        reply = response.choices[0].message.content
        result = self.get_price(reply)
        self.log(f"Frontier Agent completed - predicting ${result:.2f}")
        return result
```


---

<a id="file-week8-agents-items-py"></a>
## File: `week8/agents/items.py`

> **Path in repository:** `week8/agents/items.py`

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

<a id="file-week8-agents-messaging-agent-py"></a>
## File: `week8/agents/messaging_agent.py`

> **Path in repository:** `week8/agents/messaging_agent.py`

```python
import os
from agents.deals import Opportunity
from agents.agent import Agent
from litellm import completion
import requests

pushover_url = "https://api.pushover.net/1/messages.json"


class MessagingAgent(Agent):
    name = "Messaging Agent"
    color = Agent.WHITE
    MODEL = "anthropic/claude-haiku-5-5"

    def __init__(self):
        """
        Set up this object to either do push notifications via Pushover,
        or SMS via Twilio,
        whichever is specified in the constants
        """
        self.log("Messaging Agent is initializing")
        self.pushover_user = os.getenv("PUSHOVER_USER", "your-pushover-user-if-not-using-env")
        self.pushover_token = os.getenv("PUSHOVER_TOKEN", "your-pushover-user-if-not-using-env")
        self.log("Messaging Agent has initialized Pushover and Claude")

    def push(self, text):
        """
        Send a Push Notification using the Pushover API
        """
        self.log("Messaging Agent is sending a push notification")
        payload = {
            "user": self.pushover_user,
            "token": self.pushover_token,
            "message": text,
            "sound": "cashregister",
        }
        requests.post(pushover_url, data=payload)

    def alert(self, opportunity: Opportunity):
        """
        Make an alert about the specified Opportunity
        """
        text = f"Deal Alert! Price=${opportunity.deal.price:.2f}, "
        text += f"Estimate=${opportunity.estimate:.2f}, "
        text += f"Discount=${opportunity.discount:.2f} :"
        text += opportunity.deal.product_description[:10] + "... "
        text += opportunity.deal.url
        self.push(text)
        self.log("Messaging Agent has completed")

    def craft_message(
        self, description: str, deal_price: float, estimated_true_value: float
    ) -> str:
        user_prompt = "Please summarize this great deal in 2-3 sentences to be sent as an exciting push notification alerting the user about this deal.\n"
        user_prompt += f"Item Description: {description}\nOffered Price: {deal_price}\nEstimated true value: {estimated_true_value}"
        user_prompt += "\n\nRespond only with the 2-3 sentence message which will be used to alert & excite the user about this deal"
        response = completion(
            model=self.MODEL,
            messages=[
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content

    def notify(self, description: str, deal_price: float, estimated_true_value: float, url: str):
        """
        Make an alert about the specified details
        """
        self.log("Messaging Agent is using Claude to craft the message")
        text = self.craft_message(description, deal_price, estimated_true_value)
        self.push(text[:200] + "... " + url)
        self.log("Messaging Agent has completed")
```


---

<a id="file-week8-agents-neural-network-agent-py"></a>
## File: `week8/agents/neural_network_agent.py`

> **Path in repository:** `week8/agents/neural_network_agent.py`

```python
from agents.agent import Agent
from agents.deep_neural_network import DeepNeuralNetworkInference


class NeuralNetworkAgent(Agent):
    name = "Neural Network Agent"
    color = Agent.MAGENTA

    def __init__(self):
        """
        Initialize this object by loading in the saved model weights
        and the SentenceTransformer vector encoding model
        """
        self.log("Neural Network Agent is initializing")
        self.neural_network = DeepNeuralNetworkInference()
        self.neural_network.setup()
        self.neural_network.load("deep_neural_network.pth")
        self.log("Neural Network Agent is ready and weights are loaded")

    def price(self, description: str) -> float:
        """
        Use the Deep Neural Network to estimate the price of the described item
        :param description: the product to be estimated
        :return: the price as a float
        """
        self.log("Neural Network Agent is starting a prediction")
        result = self.neural_network.inference(description)
        self.log(f"Neural Network Agent completed - predicting ${result:.2f}")
        return result
```


---

<a id="file-week8-agents-planning-agent-py"></a>
## File: `week8/agents/planning_agent.py`

> **Path in repository:** `week8/agents/planning_agent.py`

```python
from typing import Optional, List
from agents.agent import Agent
from agents.deals import ScrapedDeal, DealSelection, Deal, Opportunity
from agents.scanner_agent import ScannerAgent
from agents.ensemble_agent import EnsembleAgent
from agents.messaging_agent import MessagingAgent


class PlanningAgent(Agent):

    name = "Planning Agent"
    color = Agent.GREEN
    DEAL_THRESHOLD = 50

    def __init__(self, collection):
        """
        Create instances of the 3 Agents that this planner coordinates across
        """
        self.log("Planning Agent is initializing")
        self.scanner = ScannerAgent()
        self.ensemble = EnsembleAgent(collection)
        self.messenger = MessagingAgent()
        self.log("Planning Agent is ready")

    def run(self, deal: Deal) -> Opportunity:
        """
        Run the workflow for a particular deal
        :param deal: the deal, summarized from an RSS scrape
        :returns: an opportunity including the discount
        """
        self.log("Planning Agent is pricing up a potential deal")
        estimate = self.ensemble.price(deal.product_description)
        discount = estimate - deal.price
        self.log(f"Planning Agent has processed a deal with discount ${discount:.2f}")
        return Opportunity(deal=deal, estimate=estimate, discount=discount)

    def plan(self, memory: List[str] = []) -> Optional[Opportunity]:
        """
        Run the full workflow:
        1. Use the ScannerAgent to find deals from RSS feeds
        2. Use the EnsembleAgent to estimate them
        3. Use the MessagingAgent to send a notification of deals
        :param memory: a list of URLs that have been surfaced in the past
        :return: an Opportunity if one was surfaced, otherwise None
        """
        self.log("Planning Agent is kicking off a run")
        selection = self.scanner.scan(memory=memory)
        if selection:
            opportunities = [self.run(deal) for deal in selection.deals[:5]]
            opportunities.sort(key=lambda opp: opp.discount, reverse=True)
            best = opportunities[0]
            self.log(f"Planning Agent has identified the best deal has discount ${best.discount:.2f}")
            if best.discount > self.DEAL_THRESHOLD:
                self.messenger.alert(best)
            self.log("Planning Agent has completed a run")
            return best if best.discount > self.DEAL_THRESHOLD else None
        return None
```


---

<a id="file-week8-agents-preprocessor-py"></a>
## File: `week8/agents/preprocessor.py`

> **Path in repository:** `week8/agents/preprocessor.py`

```python
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DEFAULT_MODEL_NAME = os.getenv("PRICER_PREPROCESSOR_MODEL", "ollama/llama3.2")
DEFAULT_REASONING_EFFORT = "low" if "gpt-oss" in DEFAULT_MODEL_NAME else None

SYSTEM_PROMPT = """Create a concise description of a product. Respond only in this format. Do not include part numbers.
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features"""


class Preprocessor:
    def __init__(
        self,
        model_name=DEFAULT_MODEL_NAME,
        reasoning_effort=DEFAULT_REASONING_EFFORT,
        base_url=None,
    ):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0
        self.model_name = model_name
        self.reasoning_effort = reasoning_effort
        self.base_url = base_url
        if "ollama" in model_name and not base_url:
            self.base_url = "http://localhost:11434"

    def messages_for(self, text: str) -> list[dict]:
        return [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": text}]

    def preprocess(self, text: str) -> str:
        messages = self.messages_for(text)
        response = completion(
            messages=messages,
            model=self.model_name,
            reasoning_effort=self.reasoning_effort,
            api_base=self.base_url,
        )
        self.total_input_tokens += response.usage.prompt_tokens
        self.total_output_tokens += response.usage.completion_tokens
        self.total_cost += response._hidden_params["response_cost"]
        return response.choices[0].message.content
```


---

<a id="file-week8-agents-scanner-agent-py"></a>
## File: `week8/agents/scanner_agent.py`

> **Path in repository:** `week8/agents/scanner_agent.py`

```python
from typing import Optional, List
from openai import OpenAI
from agents.deals import ScrapedDeal, DealSelection
from agents.agent import Agent


class ScannerAgent(Agent):
    MODEL = "gpt-6-luna"

    SYSTEM_PROMPT = """You identify and summarize the 5 most detailed deals from a list, by selecting deals that have the most detailed, high quality description and the most clear price.
    Respond strictly in JSON with no explanation, using this format. You should provide the price as a number derived from the description. If the price of a deal isn't clear, do not include that deal in your response.
    Most important is that you respond with the 5 deals that have the most detailed product description with price. It's not important to mention the terms of the deal; most important is a thorough description of the product.
    Be careful with products that are described as "$XXX off" or "reduced by $XXX" - this isn't the actual price of the product. Only respond with products when you are highly confident about the price. 
    """

    USER_PROMPT_PREFIX = """Respond with the most promising 5 deals from this list, selecting those which have the most detailed, high quality product description and a clear price that is greater than 0.
    You should rephrase the description to be a summary of the product itself, not the terms of the deal.
    Remember to respond with a short paragraph of text in the product_description field for each of the 5 items that you select.
    Be careful with products that are described as "$XXX off" or "reduced by $XXX" - this isn't the actual price of the product. Only respond with products when you are highly confident about the price. 
    
    Deals:
    
    """

    USER_PROMPT_SUFFIX = "\n\nInclude exactly 5 deals, no more."

    name = "Scanner Agent"
    color = Agent.CYAN

    def __init__(self):
        """
        Set up this instance by initializing OpenAI
        """
        self.log("Scanner Agent is initializing")
        self.openai = OpenAI()
        self.log("Scanner Agent is ready")

    def fetch_deals(self, memory) -> List[ScrapedDeal]:
        """
        Look up deals published on RSS feeds
        Return any new deals that are not already in the memory provided
        """
        self.log("Scanner Agent is about to fetch deals from RSS feed")
        urls = [opp.deal.url for opp in memory]
        scraped = ScrapedDeal.fetch()
        result = [scrape for scrape in scraped if scrape.url not in urls]
        self.log(f"Scanner Agent received {len(result)} deals not already scraped")
        return result

    def make_user_prompt(self, scraped) -> str:
        """
        Create a user prompt for OpenAI based on the scraped deals provided
        """
        user_prompt = self.USER_PROMPT_PREFIX
        user_prompt += "\n\n".join([scrape.describe() for scrape in scraped])
        user_prompt += self.USER_PROMPT_SUFFIX
        return user_prompt

    def scan(self, memory: List[str] = []) -> Optional[DealSelection]:
        """
        Call OpenAI to provide a high potential list of deals with good descriptions and prices
        Use StructuredOutputs to ensure it conforms to our specifications
        :param memory: a list of URLs representing deals already raised
        :return: a selection of good deals, or None if there aren't any
        """
        scraped = self.fetch_deals(memory)
        if scraped:
            user_prompt = self.make_user_prompt(scraped)
            self.log("Scanner Agent is calling OpenAI using Structured Outputs")
            result = self.openai.chat.completions.parse(
                model=self.MODEL,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                response_format=DealSelection,
                reasoning_effort="none",
            )
            result = result.choices[0].message.parsed
            result.deals = [deal for deal in result.deals if deal.price > 0]
            self.log(
                f"Scanner Agent received {len(result.deals)} selected deals with price>0 from OpenAI"
            )
            return result
        return None

    def test_scan(self, memory: List[str] = []) -> Optional[DealSelection]:
        """
        Return a test DealSelection, to be used during testing
        """
        results = {
            "deals": [
                {
                    "product_description": "The Hisense R6 Series 55R6030N is a 55-inch 4K UHD Roku Smart TV that offers stunning picture quality with 3840x2160 resolution. It features Dolby Vision HDR and HDR10 compatibility, ensuring a vibrant and dynamic viewing experience. The TV runs on Roku's operating system, allowing easy access to streaming services and voice control compatibility with Google Assistant and Alexa. With three HDMI ports available, connecting multiple devices is simple and efficient.",
                    "price": 178,
                    "url": "https://www.dealnews.com/products/Hisense/Hisense-R6-Series-55-R6030-N-55-4-K-UHD-Roku-Smart-TV/484824.html?iref=rss-c142",
                },
                {
                    "product_description": "The Poly Studio P21 is a 21.5-inch LED personal meeting display designed specifically for remote work and video conferencing. With a native resolution of 1080p, it provides crystal-clear video quality, featuring a privacy shutter and stereo speakers. This display includes a 1080p webcam with manual pan, tilt, and zoom control, along with an ambient light sensor to adjust the vanity lighting as needed. It also supports 5W wireless charging for mobile devices, making it an all-in-one solution for home offices.",
                    "price": 30,
                    "url": "https://www.dealnews.com/products/Poly-Studio-P21-21-5-1080-p-LED-Personal-Meeting-Display/378335.html?iref=rss-c39",
                },
                {
                    "product_description": "The Lenovo IdeaPad Slim 5 laptop is powered by a 7th generation AMD Ryzen 5 8645HS 6-core CPU, offering efficient performance for multitasking and demanding applications. It features a 16-inch touch display with a resolution of 1920x1080, ensuring bright and vivid visuals. Accompanied by 16GB of RAM and a 512GB SSD, the laptop provides ample speed and storage for all your files. This model is designed to handle everyday tasks with ease while delivering an enjoyable user experience.",
                    "price": 446,
                    "url": "https://www.dealnews.com/products/Lenovo/Lenovo-Idea-Pad-Slim-5-7-th-Gen-Ryzen-5-16-Touch-Laptop/485068.html?iref=rss-c39",
                },
                {
                    "product_description": "The Dell G15 gaming laptop is equipped with a 6th-generation AMD Ryzen 5 7640HS 6-Core CPU, providing powerful performance for gaming and content creation. It features a 15.6-inch 1080p display with a 120Hz refresh rate, allowing for smooth and responsive gameplay. With 16GB of RAM and a substantial 1TB NVMe M.2 SSD, this laptop ensures speedy performance and plenty of storage for games and applications. Additionally, it includes the Nvidia GeForce RTX 3050 GPU for enhanced graphics and gaming experiences.",
                    "price": 650,
                    "url": "https://www.dealnews.com/products/Dell/Dell-G15-Ryzen-5-15-6-Gaming-Laptop-w-Nvidia-RTX-3050/485067.html?iref=rss-c39",
                },
            ]
        }
        return DealSelection(**results)
```


---

<a id="file-week8-agents-specialist-agent-py"></a>
## File: `week8/agents/specialist_agent.py`

> **Path in repository:** `week8/agents/specialist_agent.py`

```python
import modal
from agents.agent import Agent


class SpecialistAgent(Agent):
    """
    An Agent that runs our fine-tuned LLM that's running remotely on Modal
    """

    name = "Specialist Agent"
    color = Agent.RED

    def __init__(self):
        """
        Set up this Agent by creating an instance of the modal class
        """
        self.log("Specialist Agent is initializing - connecting to modal")
        Pricer = modal.Cls.from_name("pricer-service", "Pricer")
        self.pricer = Pricer()

    def price(self, description: str) -> float:
        """
        Make a remote call to return the estimate of the price of this item
        """
        self.log("Specialist Agent is calling remote fine-tuned model")
        result = self.pricer.price.remote(description)
        self.log(f"Specialist Agent completed - predicting ${result:.2f}")
        return result
```


---

<a id="file-week8-day1-ipynb"></a>
## File: `week8/day1.ipynb`

> **Path in repository:** `week8/day1.ipynb`

# Welcome to a very busy Week 8 folder

## We have lots to do this week!

We'll move at a faster pace than usual, particularly as you're becoming proficient LLM engineers.

# The Price is Right

## Week 8 Order of Play

Day 1: Modal.com and SpecialistAgent  
Day 2: RAG, FrontierAgent, Ensemble Agent  
Day 3: ScannerAgent, MessengerAgent  
Day 4: AutonomousPlannerAgent and DealAgentFramework  
Day 5: The Price Is Right Finale

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#b22;">Especially important this week: pull the latest</h2>
            <span style="color:#b22;">I'm continually improving these labs, adding more examples and exercises.
            At the start of each week, it's worth checking you have the latest code.<br/>
            Please see Guide 3 in the Guides folder if you're not sure how to do a <code>git pull</code>
            </span>
        </td>
    </tr>
</table>

```python
import os
import locale
import modal
from agents.preprocessor import Preprocessor
from dotenv import load_dotenv
load_dotenv(override=True)
```

```python
# To check that your computer can output special characters, make sure this outputs UTF-8 

print(locale.getpreferredencoding())  # Should print 'UTF-8'
```

```python
os.environ["PYTHONIOENCODING"] = "utf-8"
```

# Setting up the modal tokens

## IMPORTANT - please do read and follow these instructions!

First please visit: https://modal.com

And sign up for an account. Then click the Avatar menu on the top right and select "Settings"

Then click "API Tokens" in the left sidebar, then click "New Token".

You will be given something like this to run:

`modal token set --token-id ak-somethinghere --token-secret as-somethinghere`

But because we're using uv, the real thing to run is this:

`uv run modal token set --token-id ak-somethinghere --token-secret as-somethinghere`

### Troubleshooting

If you have problems, 3 things to try:

1. Try running `uv run modal token new` before the `uv run modal token set..`  

2. Suggestion from student David S. on Windows:

> In case anyone else using Windows hits this problem: Along with having to run `modal token new` from a command prompt, you have to move the generated token file. It will deploy the token file (.modal.toml) to your Windows profile folder. The virtual environment couldn't see that location (strangely, it couldn't even after I set environment variables for it and rebooted). I moved that token file to the folder I'm operating out of for the lab and it stopped throwing auth errors.

3. Doing in the manual way:

It might be totally fine to simply add the 2 keys directly to your .env file:

```
MODAL_TOKEN_ID=ak-...
MODAL_TOKEN_SECRET=as-...
```

Then rerun `load_dotenv(override=True)` to load these environment variables.

```python
from hello import app, hello, hello_europe
```

```python
with app.run():
    reply=hello.local()
reply
```

```python
with app.run():
    reply=hello.remote()
reply
```

## Added thanks to student Tue H.

If you look in hello.py, I've added a simple function hello_europe

That uses the decorator:  
`@app.function(image=image, region="eu")`

See the result below! More region specific settings are [here](https://modal.com/docs/guide/region-selection)

Note that it does consume marginally more credits to specify a region.

```python
with app.run():
    reply=hello_europe.remote()
reply
```

# Before we move on -

## We need to set your HuggingFace Token as a secret in Modal

## Super important - please read - this confuses a lot of people!

Secrets in Modal are given a **name** that describes the secret.  
Then the secret itself has a KEY and a VALUE.  
We will be setting up a secret with:  

Name: huggingface-secret  
Key: HF_TOKEN  
Value: hf_...  

## The bulletproof recipe:

1. Go to modal.com, sign in and go to your dashboard  
2. Click on Secrets in the nav bar  
3. Create new secret, click on Hugging Face, this new secret needs to be called **huggingface-secret** because that's how we refer to it in the code  
4. Fill in your key as HF_TOKEN and the value as your actual token hf_...  
5. Click done

### And now back to business: time to work with Llama

```python
# This import may give a deprecation warning about adding local Python modules to the Image
# That warning can be safely ignored. You may get the same warning in other places, too..

from llama import app, generate
```

```python
with modal.enable_output():
    with app.run():
        result=generate.remote("Never gonna give you up, never gonna")
result

# Or it you object to being rickrolled, try this: "Hey Jude, don't make it"
```

```python
from pricer_ephemeral import app, price
```

```python
with modal.enable_output():
    with app.run():
        result=price.remote("Quadcast HyperX condenser mic, connects via usb-c to your computer for crystal clear audio")
result
```

```python
preprocessor = Preprocessor()
text = preprocessor.preprocess("Quadcast HyperX condenser mic, connects via usb-c to your computer for crystal clear audio")
print(text)
```

```python
preprocessor = Preprocessor(model_name="groq/openai/gpt-oss-20b")
text = preprocessor.preprocess("Quadcast HyperX condenser mic, connects via usb-c to your computer for crystal clear audio")
print(text)
```

### Add this to your .env if you want the Preprocessor to use a different model by default:

`PRICER_PREPROCESSOR_MODEL=groq/openai/gpt-oss-20b`

```python
with modal.enable_output():
    with app.run():
        result = price.remote(text)
print(result)
```

```python
print(text)
```

## Transitioning From Ephemeral Apps to Deployed Apps

From a command line, `uv run modal deploy xxx` will deploy your code as a Deployed App

This is how you could package your AI service behind an API to be used in a Production System.

You can also build REST endpoints easily, although we won't cover that as we'll be calling direct from Python.

## Important note about secrets

In both the files `pricer_service.py` and `pricer_service2.py` you will find code like this near the top:  
`secrets = [modal.Secret.from_name("hf-secret")]`  
You may need to change from `hf-secret` to `huggingface-secret` depending on how the Secret is configured in modal.  
To check, visit this page and look in the first column:  
https://modal.com/secrets/

## Important note for Windows people:

On the next line, I call `uv run modal deploy` from within Jupyter lab; I've heard that on some versions of Windows this gives a strange unicode error because modal prints emojis to the output which can't be displayed. If that happens to you, open a Terminal and run `uv run modal deploy..`

```python
# You can also run "uv run modal deploy -m pricer_service" in the Terminal

!uv run modal deploy -m pricer_service
```

```python
pricer = modal.Function.from_name("pricer-service", "price")
```

Watch it happening:

https://modal.com

```python
# This can take a while! We'll use faster approaches shortly

pricer.remote(text)
```

```python
# You can also run "modal deploy -m pricer_service2" at the command line in an activated environment

!modal deploy -m pricer_service2
```

```python
Pricer = modal.Cls.from_name("pricer-service", "Pricer")
pricer = Pricer()
reply = pricer.price.remote(text)
print(reply)
```

```python
reply = pricer.price.remote(text)
print(reply)
```

# Optional: Keeping Modal warm

## A way to improve the speed of the Modal pricer service

The first time you run this modal class, it might take as much as 10 minutes to build.  
Subsequently it should be much faster.. 30 seconds if it needs to wake up, otherwise 2 seconds.  
If you want it to always be 2 seconds, you can keep the container from going to sleep by editing this constant in pricer_service2.py:

`MIN_CONTAINERS = 0`



Make it 1 to keep a container alive.  
But please note: this will eat up credits! Only do this if you are comfortable to have a process running continually.

Alternatively, you can run this code and it will stay warm for 20 mins rather than 2 mins.

### Code to keep warm for 20 mins before cooling down:

```python
import modal
Pricer = modal.Cls.from_name("pricer-service", "Pricer")
pricer = Pricer()
pricer.update_autoscaler(scaledown_window=1200)
```

### Code to revert to keeping warm for only 2 mins

```python
import modal
Pricer = modal.Cls.from_name("pricer-service", "Pricer")
pricer = Pricer()
pricer.update_autoscaler(scaledown_window=120)
```

## And now introducing our Agent class

By default this will preprocess using Llama3.2

If you'd prefer to use Groq, then add this env variable like:

```
PRICER_PREPROCESSOR_MODEL=groq/openai/gpt-oss-20b
```

```python
import logging
root = logging.getLogger()
root.setLevel(logging.INFO)
```

```python
from agents.specialist_agent import SpecialistAgent
```

```python
agent = SpecialistAgent()
```

```python
agent.price("iPhone 10")
```


---

<a id="file-week8-day2-ipynb"></a>
## File: `week8/day2.ipynb`

> **Path in repository:** `week8/day2.ipynb`

# The Price is Right

## Week 8 Order of Play

Day 1: Modal.com and SpecialistAgent  
Day 2: RAG, FrontierAgent, Ensemble Agent  
Day 3: ScannerAgent, MessengerAgent  
Day 4: AutonomousPlannerAgent and DealAgentFramework  
Day 5: The Price Is Right Finale

## RAG (Retrieval Augmented Generation) based on a dataset of 800,000 scraped Amazon products

#### For our 2nd agent, we will be asking OpenAI to estimate the price of one of our deals - and we will give it a hand.

We discovered that LLMs are really good at this, out of the box.

And we discovered that we can beat a frontier LLM by fine-tuning an open-source LLM.

Now we are going to try **inference time** techniques instead of training -- by using RAG!

```python
# imports

import os
import logging
from dotenv import load_dotenv
from huggingface_hub import login
import numpy as np
import re
from sentence_transformers import SentenceTransformer
import chromadb
from sklearn.manifold import TSNE
import plotly.graph_objects as go
from litellm import completion
from tqdm.notebook import tqdm
from agents.evaluator import evaluate
from agents.items import Item
```

```python
# environment

load_dotenv(override=True)
DB = "products_vectorstore"
```

```python
# Log in to HuggingFace
# If you don't have a HuggingFace account, you can set one up for free at www.huggingface.co
# And then add the HF_TOKEN to your .env file as explained in the project README

hf_token = os.environ['HF_TOKEN']
login(token=hf_token, add_to_git_credential=False)
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

# Now create a Chroma Datastore

Now we will use the free, open-source Vector database Chroma.  
We will create a Chroma datastore with 400,000 products from our training dataset.

```python
client = chromadb.PersistentClient(path=DB)
```

# Introducing the SentenceTransformer Encoding LLM

The all-MiniLM is a very useful model from HuggingFace that maps sentences & paragraphs to 384 dimensional vectors and is ideal for tasks like semantic search.

https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

It can run pretty quickly locally.

As an alternative, OpenAI provides a closed-source Embeddings model. Benefits compared to OpenAI embeddings:
1. It's free and fast!
3. We can run it locally, so the data never leaves our box - might be useful if you're building a personal RAG

```python
encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
```

```python
# Pass in a list of texts, get back a numpy array of vectors

vector = encoder.encode(["A proficient AI engineer who has almost reached the finale of AI Engineering Core Track!"])[0]
print(vector.shape)
vector
```

## With that background, let's populate our Chroma database

### By calculating vectors for 800,000 scraped products

This takes 30 minutes on my machine on my GPU - it might take longer for you - feel free to use the Lite dataset!

```python
# Check if the collection exists; if not, create it

collection_name = "products"
existing_collection_names = [collection.name for collection in client.list_collections()]

if collection_name not in existing_collection_names:
    collection = client.create_collection(collection_name)
    for i in tqdm(range(0, len(train), 1000)):
        documents = [item.summary for item in train[i: i+1000]]
        vectors = encoder.encode(documents).astype(float).tolist()
        metadatas = [{"category": item.category, "price": item.price} for item in train[i: i+1000]]
        ids = [f"doc_{j}" for j in range(i, i+1000)]
        ids = ids[:len(documents)]
        collection.add(ids=ids, documents=documents, embeddings=vectors, metadatas=metadatas)

collection = client.get_or_create_collection(collection_name)
```

# Let's visualize the vectorized data

```python
# It is very fun turning this up to 800_000 and seeing the full dataset visualized,
# but it almost crashes my box every time so do that at your own risk!! 10_000 is safe!

MAXIMUM_DATAPOINTS = 10_000
```

```python
CATEGORIES = ['Appliances', 'Automotive', 'Cell_Phones_and_Accessories', 'Electronics','Musical_Instruments', 'Office_Products', 'Tools_and_Home_Improvement', 'Toys_and_Games']
COLORS = ['cyan', 'blue', 'brown', 'orange', 'yellow', 'green' , 'purple', 'red']
```

```python
# Prework
result = collection.get(include=['embeddings', 'documents', 'metadatas'], limit=MAXIMUM_DATAPOINTS)
vectors = np.array(result['embeddings'])
documents = result['documents']
categories = [metadata['category'] for metadata in result['metadatas']]
colors = [COLORS[CATEGORIES.index(c)] for c in categories]
```

```python
# Let's try a 2D chart
# TSNE stands for t-distributed Stochastic Neighbor Embedding - it's a common technique for reducing dimensionality of data

tsne = TSNE(n_components=2, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)
```

```python
# Create the 2D scatter plot
fig = go.Figure(data=[go.Scatter(
    x=reduced_vectors[:, 0],
    y=reduced_vectors[:, 1],
    mode='markers',
    marker=dict(size=4, color=colors, opacity=0.7),
    text=[f"Category: {c}<br>Text: {d[:50]}..." for c, d in zip(categories, documents)],
    hoverinfo='text'
)])

fig.update_layout(
    title='2D Chroma Vectorstore Visualization',
    scene=dict(xaxis_title='x', yaxis_title='y'),
    width=1200,
    height=800,
    margin=dict(r=20, b=10, l=10, t=40)
)

fig.show()
```

```python
# Let's try 3D!

tsne = TSNE(n_components=3, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)
```

```python
# Create the 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=reduced_vectors[:, 0],
    y=reduced_vectors[:, 1],
    z=reduced_vectors[:, 2],
    mode='markers',
    marker=dict(size=2, color=colors, opacity=0.7),
    text=[f"Category: {c}<br>Text: {d[:50]}..." for c, d in zip(categories, documents)],
    hoverinfo='text'
)])

fig.update_layout(
    title='3D Chroma Vector Store Visualization',
    scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
    width=1200,
    height=800,
    margin=dict(r=20, b=10, l=10, t=40)
)

fig.show()
```

```python
test[0]
```

```python
def vector(item):
    return encoder.encode(item.summary)
```

```python
def find_similars(item):
    vec = vector(item)
    results = collection.query(query_embeddings=vec.astype(float).tolist(), n_results=5)
    documents = results['documents'][0][:]
    prices = [m['price'] for m in results['metadatas'][0][:]]
    return documents, prices
```

```python
find_similars(test[0])
```

```python
# We need to give some context to GPT-5.1 by selecting 5 products with similar descriptions

def make_context(similars, prices):
    message = "For context, here are some other items that might be similar to the item you need to estimate.\n\n"
    for similar, price in zip(similars, prices):
        message += f"Potentially related product:\n{similar}\nPrice is ${price:.2f}\n\n"
    return message
```

```python
documents, prices = find_similars(test[0])
print(make_context(documents, prices))
```

```python
def messages_for(item, similars, prices):
    message = f"Estimate the price of this product. Respond with the price, no explanation\n\n{item.summary}\n\n"
    message += make_context(similars, prices)
    return [{"role": "user", "content": message}]
```

```python
documents, prices = find_similars(test[0])
print(messages_for(test[0], documents, prices)[0]['content'])
```

```python
# The function for gpt-5.1

def gpt_5__1_rag(item):
    documents, prices = find_similars(item)
    response = completion(model="gpt-5.1", messages=messages_for(item, documents, prices), reasoning_effort="none", seed=42)
    return response.choices[0].message.content
```

```python
# How much does our favorite distortion pedal cost?

test[0].price
```

```python
# Let's do this!!

gpt_5__1_rag(test[0])
```

```python
evaluate(gpt_5__1_rag, test)
```

```python
import modal
Pricer = modal.Cls.from_name("pricer-service", "Pricer")
pricer = Pricer()
```

```python
def specialist(item):
    return pricer.price.remote(item.summary)
```

```python
def get_price(reply):
    reply = reply.replace("$", "").replace(",", "")
    match = re.search(r"[-+]?\d*\.\d+|\d+", reply)
    return float(match.group()) if match else 0
```

## Download the Neural Network weights from Week 6 into this directory

The file `deep_neural_network.pth` here:

https://drive.google.com/drive/folders/1uq5C9edPIZ1973dArZiEO-VE13F7m8MK?usp=drive_link

```python
from agents.deep_neural_network import DeepNeuralNetworkInference

runner = DeepNeuralNetworkInference()
runner.setup()
runner.load("deep_neural_network.pth")

def deep_neural_network(item):
    return runner.inference(item.summary)
```

```python
def ensemble(item):
    price1 = get_price(gpt_5__1_rag(item))
    price2 = specialist(item)
    price3 = deep_neural_network(item)
    return price1 * 0.8 + price2 * 0.1 + price3 * 0.1
```

```python
evaluate(ensemble, test)
```

```python
root = logging.getLogger()
root.setLevel(logging.INFO)
```

```python
from agents.frontier_agent import FrontierAgent

agent = FrontierAgent(collection)
agent.price("Quadcast HyperX condenser mic, connects via usb-c to your computer for crystal clear audio")
```

```python
agent.price("Shure MV7+ professional podcaster microphone with usb-c and XLR outputs")
```

```python
from agents.neural_network_agent import NeuralNetworkAgent
agent = NeuralNetworkAgent()
```

```python
agent.price("Shure MV7+ professional podcaster microphone with usb-c and XLR outputs")
```

```python
from agents.ensemble_agent import EnsembleAgent
agent = EnsembleAgent(collection)
```

```python
agent.price("Shure MV7+ professional podcaster microphone with usb-c and XLR outputs")
```


---

<a id="file-week8-day3-ipynb"></a>
## File: `week8/day3.ipynb`

> **Path in repository:** `week8/day3.ipynb`

# The Price is Right

## Week 8 Order of Play

Day 1: Modal.com and SpecialistAgent  
Day 2: RAG, FrontierAgent, Ensemble Agent  
Day 3: ScannerAgent, MessengerAgent  
Day 4: AutonomousPlannerAgent and DealAgentFramework  
Day 5: The Price Is Right Finale


Today we'll build another piece of the puzzle: a ScanningAgent that looks for promising deals by subscribing to RSS feeds.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI
from agents.deals import ScrapedDeal, DealSelection
import logging
import requests
load_dotenv(override=True)
openai = OpenAI()
MODEL = 'gpt-6-luna'
```

```python
deals = ScrapedDeal.fetch(show_progress=True)
```

```python
len(deals)
```

```python
deals[10].describe()
```

### We are going to ask GPT-6 Luna to summarize deals and identify their price

```python
SYSTEM_PROMPT = """You identify and summarize the 5 most detailed deals from a list, by selecting deals that have the most detailed, high quality description and the most clear price.
Respond strictly in JSON with no explanation, using this format. You should provide the price as a number derived from the description. If the price of a deal isn't clear, do not include that deal in your response.
Most important is that you respond with the 5 deals that have the most detailed product description with price. It's not important to mention the terms of the deal; most important is a thorough description of the product.
Be careful with products that are described as "$XXX off" or "reduced by $XXX" - this isn't the actual price of the product. Only respond with products when you are highly confident about the price. 
"""

USER_PROMPT_PREFIX = """Respond with the most promising 5 deals from this list, selecting those which have the most detailed, high quality product description and a clear price that is greater than 0.
You should rephrase the description to be a summary of the product itself, not the terms of the deal.
Remember to respond with a short paragraph of text in the product_description field for each of the 5 items that you select.
Be careful with products that are described as "$XXX off" or "reduced by $XXX" - this isn't the actual price of the product. Only respond with products when you are highly confident about the price. 

Deals:

"""

USER_PROMPT_SUFFIX = "\n\nInclude exactly 5 deals, no more."
```

```python
# this makes a suitable user prompt given scraped deals

def make_user_prompt(scraped):
    user_prompt = USER_PROMPT_PREFIX
    user_prompt += '\n\n'.join([scrape.describe() for scrape in scraped])
    user_prompt += USER_PROMPT_SUFFIX
    return user_prompt
```

```python
# Let's create a user prompt for the deals we just scraped, and look at how it begins

user_prompt = make_user_prompt(deals)
print(user_prompt[:2000])
messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_prompt}]
```

```python
response = openai.chat.completions.parse(model=MODEL, messages=messages, response_format=DealSelection, reasoning_effort="none")
results = response.choices[0].message.parsed
results
```

```python
for deal in results.deals:
    print(deal.product_description)
    print(deal.price)
    print(deal.url)
    print()
```

```python
root = logging.getLogger()
root.setLevel(logging.INFO)
```

```python
from agents.scanner_agent import ScannerAgent
```

```python
agent = ScannerAgent()
result = agent.scan()
```

```python
result
```

### Introducing Pushover

Pushover is a nifty tool for sending Push Notifications to your phone.

It's super easy to set up and install!

Simply visit https://pushover.net/ and click 'Login or Signup' on the top right to sign up for a free account, and create your API keys.

Once you've signed up, on the home screen, click "Create an Application/API Token", and give it any name (like AIEngineer) and click Create Application.

Then add 2 lines to your `.env` file:

PUSHOVER_USER=_put the key that's on the top right of your Pushover home screen and probably starts with a u_  
PUSHOVER_TOKEN=_put the key when you click into your new application called Agents (or whatever) and probably starts with an a_

Remember to save your `.env` file, and run `load_dotenv(override=True)` after saving, to set your environment variables.

Finally, click "Add Phone, Tablet or Desktop" to install on your phone.

```python
load_dotenv(override=True)
```

```python
pushover_user = os.getenv('PUSHOVER_USER')
pushover_token = os.getenv('PUSHOVER_TOKEN')
pushover_url = "https://api.pushover.net/1/messages.json"
```

```python
if pushover_user:
    print(f"Pushover user found and starts with {pushover_user[0]}")
else:
    print("Pushover user not found")

if pushover_token:
    print(f"Pushover token found and starts with {pushover_token[0]}")
else:
    print("Pushover token not found")
```

```python
def push(message):
    print(f"Push: {message}")
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    requests.post(pushover_url, data=payload)
```

```python
push("MASSIVE DEAL!!")
```

```python
from agents.messaging_agent import MessagingAgent

agent = MessagingAgent()
agent.push("SUCH A MASSIVE DEAL!!")
```

```python
agent.notify("A special deal on Sumsung 60 inch LED TV going at a great bargain", 300, 1000, "www.samsung.com")
```


---

<a id="file-week8-day4-ipynb"></a>
## File: `week8/day4.ipynb`

> **Path in repository:** `week8/day4.ipynb`

# The Price is Right

## Week 8 Order of Play

Day 1: Modal.com and SpecialistAgent  
Day 2: RAG, FrontierAgent, Ensemble Agent  
Day 3: ScannerAgent, MessengerAgent   
Day 4: AutonomousPlannerAgent  
Day 5: The Price Is Right Finale


Now it's time for the Planning Agent

```python
import json
from openai import OpenAI
from dotenv import load_dotenv
from agents.scanner_agent import ScannerAgent
import chromadb
import logging
load_dotenv(override=True)
openai = OpenAI()
MODEL = "gpt-5.1"
```

## Start with some test data

```python
test_results = ScannerAgent().test_scan()
test_results
```

## Now let's create 3 pretend functions..

```python
def scan_the_internet_for_bargains() -> str:
    """ This tool scans the internet for great deals and gets a curated list of promising deals """
    print("Fake function to scan the internet - this returns a hardcoded set of deals")
    return test_results.model_dump_json()
```

```python
def estimate_true_value(description: str) -> str:
    """
    This tool estimates the true value of a product based on a text description of it
    """
    print(f"Fake function to estimating true value of {description[:20]}... - this always returns $300")
    return f"Product {description} has an estimated true value of $300"
```

```python
def notify_user_of_deal(description: str, deal_price: float, estimated_true_value: float, url: str) -> str:
    """
    This tool notifies the user of a great deal, given a description of it, the price of the deal, and the estimated true value
    """
    print(f"Fake function to notify user of {description} which costs {deal_price} and estimate is {estimated_true_value}")
    return "notification sent ok"
```

### Let's try them out

```python
notify_user_of_deal("a new iphone", 100, 1000, "https://www.apple.com/iphone")
```

### OK now a big block of JSON

```python
scan_function = {
        "name": "scan_the_internet_for_bargains",
        "description": "Returns top bargains scraped from the internet along with the price each item is being offered for",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    }

estimate_function = {
    "name": "estimate_true_value",
    "description": "Given the description of an item, estimate how much it is actually worth",
    "parameters": {
        "type": "object",
        "properties": {
            "description": {
                "type": "string",
                "description": "The description of the item to be estimated"
            },
        },
        "required": ["description"],
        "additionalProperties": False
    }
}

notify_function = {
    "name": "notify_user_of_deal",
    "description": "Send the user a push notification about the single most compelling deal; only call this one time",
    "parameters": {
        "type": "object",
        "properties": {
            "description": {
                "type": "string",
                "description": "The description of the item itself scraped from the internet"
            },
            "deal_price": {
                "type": "number",
                "description": "The price offered by this deal scraped from the internet"
            }
            ,
            "estimated_true_value": {
                "type": "number",
                "description": "The estimated actual value that this is worth"
            }
            ,
            "url": {
                "type": "string",
                "description": "The URL of this deal as scraped from the internet"
            }
        },
        "required": ["description", "deal_price", "estimated_true_value", "url"],
        "additionalProperties": False
    }
}
```

```python
tools = [{"type": "function", "function": scan_function},
 {"type": "function", "function": estimate_function},
 {"type": "function", "function": notify_function}
 ]
```

```python
tools
```

```python
def handle_tool_call(message):
    """
    Actually call the tools associated with this message
    """
    results = []
    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        tool = globals().get(tool_name)
        result = tool(**arguments) if tool else {}
        results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
    return results
```

```python
system_message = "You find great deals on bargain products using your tools, and notify the user of the best bargain."
user_message = """
First, use your tool to scan the internet for bargain deals. Then for each deal, use your tool to estimate its true value.
Then pick the single most compelling deal where the price is much lower than the estimated true value, and use your tool to notify the user.
Then just reply OK to indicate success.
"""
messages = [{"role": "system", "content": system_message},{"role": "user", "content": user_message}]
```

```python
messages
```

```python
done = False
while not done:
    response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        results = handle_tool_call(message)
        messages.append(message)
        messages.extend(results)
    else:
        done = True
response.choices[0].message.content
```

## And now.. into an Autonomous Planning Agent

And switching the fake functions for REAL functions!

```python
root = logging.getLogger()
root.setLevel(logging.INFO)
```

```python
DB = "products_vectorstore"
client = chromadb.PersistentClient(path=DB)
collection = client.get_or_create_collection('products')
```

```python
from agents.autonomous_planning_agent import AutonomousPlanningAgent
agent = AutonomousPlanningAgent(collection)
```

```python
agent.plan()
```


---

<a id="file-week8-day5-ipynb"></a>
## File: `week8/day5.ipynb`

> **Path in repository:** `week8/day5.ipynb`

# The Price is Right

The final step is to build a User Interface

We will use more advanced aspects of Gradio - building piece by piece.

```python
import gradio as gr
from deal_agent_framework import DealAgentFramework
from agents.deals import Opportunity, Deal
```

```python
with gr.Blocks(title="The Price is Right", fill_width=True) as ui:

    with gr.Row():
        gr.Markdown('<div style="text-align: center;font-size:24px">The Price is Right - Deal Hunting Agentic AI</div>')
    with gr.Row():
        gr.Markdown('<div style="text-align: center;font-size:14px">Autonomous agent framework that finds online deals, collaborating with a proprietary fine-tuned LLM deployed on Modal, and a RAG pipeline with a frontier model and Chroma.</div>')
        

ui.launch(inbrowser=True)
```

```python
# Updated to change from height to max_height due to change in Gradio v5
# With much thanks to student Ed B. for raising this

with gr.Blocks(title="The Price is Right", fill_width=True) as ui:

    initial_deal = Deal(product_description="Example description", price=100.0, url="https://cnn.com")
    initial_opportunity = Opportunity(deal=initial_deal, estimate=200.0, discount=100.0)
    opportunities = gr.State([initial_opportunity])

    def get_table(opps):
        return [[opp.deal.product_description, opp.deal.price, opp.estimate, opp.discount, opp.deal.url] for opp in opps]

    with gr.Row():
        gr.Markdown('<div style="text-align: center;font-size:24px">"The Price is Right" - Deal Hunting Agentic AI</div>')
    with gr.Row():
        gr.Markdown('<div style="text-align: center;font-size:14px">Deals surfaced so far:</div>')
    with gr.Row():
        opportunities_dataframe = gr.Dataframe(
            headers=["Description", "Price", "Estimate", "Discount", "URL"],
            wrap=True,
            column_widths=[4, 1, 1, 1, 2],
            row_count=10,
            col_count=5,
            max_height=400,
        )

    ui.load(get_table, inputs=[opportunities], outputs=[opportunities_dataframe])

ui.launch(inbrowser=True)
```

```python
agent_framework = DealAgentFramework()
agent_framework.init_agents_as_needed()

with gr.Blocks(title="The Price is Right", fill_width=True) as ui:

    initial_deal = Deal(product_description="Example description", price=100.0, url="https://cnn.com")
    initial_opportunity = Opportunity(deal=initial_deal, estimate=200.0, discount=100.0)
    opportunities = gr.State([initial_opportunity])

    def get_table(opps):
        return [[opp.deal.product_description, opp.deal.price, opp.estimate, opp.discount, opp.deal.url] for opp in opps]

    def do_select(opportunities, selected_index: gr.SelectData):
        row = selected_index.index[0]
        opportunity = opportunities[row]
        agent_framework.planner.messenger.alert(opportunity)

    with gr.Row():
        gr.Markdown('<div style="text-align: center;font-size:24px">"The Price is Right" - Deal Hunting Agentic AI</div>')
    with gr.Row():
        gr.Markdown('<div style="text-align: center;font-size:14px">Deals surfaced so far:</div>')
    with gr.Row():
        opportunities_dataframe = gr.Dataframe(
            headers=["Description", "Price", "Estimate", "Discount", "URL"],
            wrap=True,
            column_widths=[4, 1, 1, 1, 2],
            row_count=10,
            col_count=5,
            max_height=400,
        )

    ui.load(get_table, inputs=[opportunities], outputs=[opportunities_dataframe])
    opportunities_dataframe.select(do_select, inputs=[opportunities], outputs=[])

ui.launch(inbrowser=True)
```

# Time for the code

And now we'll move to the price_is_right.py code

```python
# Reset memory back to 2 deals discovered in the past

from deal_agent_framework import DealAgentFramework
DealAgentFramework.reset_memory()
```

```python
import logging
root = logging.getLogger()
root.setLevel(logging.INFO)
```

# Running the final product

## Just hit shift + enter in the next cell, and let the deals flow in!!

```python
!uv run price_is_right.py
```

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/important.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#a22;">But wait!! There's more..</h2>
            <span style="color:#a22;">If you're not fed up of product prices yet 😂 I've built this out some more!<br/>
            If you look in my repo <a href="https://github.com/ed-donner/tech2ai">tech2ai</a>, in segment4 is a version that uses OpenAI Agents SDK for the AutonomousPlanningAgent, and makes use of MCP servers.  If you're intrigued by Agents and MCP, and would like to learn more, then I also have a companion course on this. This, along with my 2 other companion courses, are laid out in my <a href="https://edwarddonner.com/2025/05/28/connecting-my-courses-become-an-llm-expert-and-leader/">complete AI curriculum</a>.
            </span>
        </td>
    </tr>
</table>

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/thankyou.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#090;">CONGRATULATIONS AND THANK YOU!!!</h2>
            <span style="color:#090;">
                It's so fabulous that you've made it to the very end! My heartiest congratulations. Please stay in touch! I'm <a href="https://www.linkedin.com/in/eddonner/">here on LinkedIn</a> if we're not already connected and I'm on X at <a href="https://x.com/edwarddonner">@edwarddonner</a>. And my editor would be cross with me if I didn't mention one more time: it makes a HUGE difference when students rate this course on Udemy - it's one of the main ways that Udemy decides whether to show it to others. <br/><br/>Massive thanks again for putting up with me for 8 weeks and getting all the way to the final cell! I'm excited to hear all about your career as an LLM Engineer. If you post on LinkedIn about completing the course and tag me, then I'll weigh in to amplify your achievement. <br/><b>You could not have picked a better time to be in this field.</b>
            </span>
        </td>
    </tr>
</table>


---

<a id="file-week8-deal-agent-framework-py"></a>
## File: `week8/deal_agent_framework.py`

> **Path in repository:** `week8/deal_agent_framework.py`

```python
import os
import sys
import logging
import json
from typing import List
from dotenv import load_dotenv
import chromadb
from agents.planning_agent import PlanningAgent
from agents.deals import Opportunity
from sklearn.manifold import TSNE
import numpy as np

load_dotenv(override=True)

# Colors for logging
BG_BLUE = "\033[44m"
WHITE = "\033[37m"
RESET = "\033[0m"

# Colors for plot
CATEGORIES = [
    "Appliances",
    "Automotive",
    "Cell_Phones_and_Accessories",
    "Electronics",
    "Musical_Instruments",
    "Office_Products",
    "Tools_and_Home_Improvement",
    "Toys_and_Games",
]
COLORS = ["red", "blue", "brown", "orange", "yellow", "green", "purple", "cyan"]


def init_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "[%(asctime)s] [Agents] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %z",
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)


class DealAgentFramework:
    DB = "products_vectorstore"
    MEMORY_FILENAME = "memory.json"

    def __init__(self):
        init_logging()
        client = chromadb.PersistentClient(path=self.DB)
        self.memory = self.read_memory()
        self.collection = client.get_or_create_collection("products")
        self.planner = None

    def init_agents_as_needed(self):
        if not self.planner:
            self.log("Initializing Agent Framework")
            self.planner = PlanningAgent(self.collection)
            self.log("Agent Framework is ready")

    def read_memory(self) -> List[Opportunity]:
        if os.path.exists(self.MEMORY_FILENAME):
            with open(self.MEMORY_FILENAME, "r") as file:
                data = json.load(file)
            opportunities = [Opportunity(**item) for item in data]
            return opportunities
        return []

    def write_memory(self) -> None:
        data = [opportunity.model_dump() for opportunity in self.memory]
        with open(self.MEMORY_FILENAME, "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def reset_memory(cls) -> None:
        data = []
        if os.path.exists(cls.MEMORY_FILENAME):
            with open(cls.MEMORY_FILENAME, "r") as file:
                data = json.load(file)
        truncated = data[:2]
        with open(cls.MEMORY_FILENAME, "w") as file:
            json.dump(truncated, file, indent=2)

    def log(self, message: str):
        text = BG_BLUE + WHITE + "[Agent Framework] " + message + RESET
        logging.info(text)

    def run(self) -> List[Opportunity]:
        self.init_agents_as_needed()
        logging.info("Kicking off Planning Agent")
        result = self.planner.plan(memory=self.memory)
        logging.info(f"Planning Agent has completed and returned: {result}")
        if result:
            self.memory.append(result)
            self.write_memory()
        return self.memory

    @classmethod
    def get_plot_data(cls, max_datapoints=2000):
        client = chromadb.PersistentClient(path=cls.DB)
        collection = client.get_or_create_collection("products")
        result = collection.get(
            include=["embeddings", "documents", "metadatas"], limit=max_datapoints
        )
        vectors = np.array(result["embeddings"])
        documents = result["documents"]
        categories = [metadata["category"] for metadata in result["metadatas"]]
        colors = [COLORS[CATEGORIES.index(c)] for c in categories]
        tsne = TSNE(n_components=3, random_state=42, n_jobs=-1)
        reduced_vectors = tsne.fit_transform(vectors)
        return documents, reduced_vectors, colors


if __name__ == "__main__":
    DealAgentFramework().run()
```


---

<a id="file-week8-hello-py"></a>
## File: `week8/hello.py`

> **Path in repository:** `week8/hello.py`

```python
import modal
from modal import Image

# Setup

app = modal.App("hello")
image = Image.debian_slim().pip_install("requests")

# Hello!


@app.function(image=image)
def hello() -> str:
    import requests

    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    city, region, country = data["city"], data["region"], data["country"]
    return f"Hello from {city}, {region}, {country}!!"


# New - added thanks to student Tue H.!


@app.function(image=image, region="eu")
def hello_europe() -> str:
    import requests

    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    city, region, country = data["city"], data["region"], data["country"]
    return f"Hello from {city}, {region}, {country}!!"
```


---

<a id="file-week8-llama-py"></a>
## File: `week8/llama.py`

> **Path in repository:** `week8/llama.py`

```python
import modal
from modal import Image

# Setup

app = modal.App("llama")
image = Image.debian_slim().pip_install("torch", "transformers", "accelerate")
secrets = [modal.Secret.from_name("huggingface-secret")]
GPU = "T4"
MODEL_NAME = "meta-llama/Llama-3.2-3B"


@app.function(image=image, secrets=secrets, gpu=GPU, timeout=1800)
def generate(prompt: str) -> str:
    from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")

    set_seed(42)
    inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs, max_new_tokens=5)
    return tokenizer.decode(outputs[0])
```


---

<a id="file-week8-log-utils-py"></a>
## File: `week8/log_utils.py`

> **Path in repository:** `week8/log_utils.py`

```python
# Foreground colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Background color
BG_BLACK = '\033[40m'
BG_BLUE = '\033[44m'

# Reset code to return to default color
RESET = '\033[0m'

mapper = {
    BG_BLACK+RED: "#dd0000",
    BG_BLACK+GREEN: "#00dd00",
    BG_BLACK+YELLOW: "#dddd00",
    BG_BLACK+BLUE: "#0000ee",
    BG_BLACK+MAGENTA: "#aa00dd",
    BG_BLACK+CYAN: "#00dddd",
    BG_BLACK+WHITE: "#87CEEB",
    BG_BLUE+WHITE: "#ff7800"
}


def reformat(message):
    for key, value in mapper.items():
        message = message.replace(key, f'<span style="color: {value}">')
    message = message.replace(RESET, '</span>')
    return message
```


---

<a id="file-week8-memory-json"></a>
## File: `week8/memory.json`

> **Path in repository:** `week8/memory.json`

```json
[
  {
    "deal": {
      "product_description": "The Samsung Galaxy Watch Ultra is a premium 47mm LTE Titanium smartwatch designed for both style and functionality. It features a circular display made with durable materials suitable for outdoor activities, providing GPS tracking, health monitoring, and custom apps for various needs. The robust design integrates a range of smart features including notifications, music control, and heart rate tracking, making it an ideal companion for fitness enthusiasts and tech-savvy users alike.",
      "price": 350.0,
      "url": "https://www.dealnews.com/Samsung-Galaxy-Watch-Ultra-47-mm-LTE-Titanium-Smartwatch-up-to-350-off-w-Trade-in-free-shipping/21663266.html?iref=rss-c142"
    },
    "estimate": 773.8138460593241,
    "discount": 423.8138460593241
  },
  {
    "deal": {
      "product_description": "The Refurbished Unlocked Apple iPhone 14 Pro Max offers an impressive 256GB storage and a huge display, perfect for both media consumption and productivity. Enjoy advanced camera technology for stunning photos. This model is designed to provide a seamless user experience with 5G capabilities for faster downloads and streaming. Refurbished to high standards, it comes in various colors and can support all the latest apps from the App Store, accommodating any Apple enthusiast's needs.",
      "price": 705.0,
      "url": "https://www.dealnews.com/products/Apple/Unlocked-Apple-iPhone-14-Pro-Max-256-GB-Smartphone/462808.html?iref=rss-c142"
    },
    "estimate": 930.8824204895075,
    "discount": 225.88242048950747
  }
]
```


---

<a id="file-week8-price-is-right-py"></a>
## File: `week8/price_is_right.py`

> **Path in repository:** `week8/price_is_right.py`

```python
import logging
import queue
import threading
import time
import gradio as gr
from deal_agent_framework import DealAgentFramework
from log_utils import reformat
import plotly.graph_objects as go
from dotenv import load_dotenv

load_dotenv(override=True)


class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(self.format(record))


def html_for(log_data):
    output = "<br>".join(log_data[-18:])
    return f"""
    <div id="scrollContent" style="height: 400px; overflow-y: auto; border: 1px solid #ccc; background-color: #222229; padding: 10px;">
    {output}
    </div>
    """


def setup_logging(log_queue):
    handler = QueueHandler(log_queue)
    formatter = logging.Formatter(
        "[%(asctime)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %z",
    )
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class App:
    def __init__(self):
        self.agent_framework = None

    def get_agent_framework(self):
        if not self.agent_framework:
            self.agent_framework = DealAgentFramework()
        return self.agent_framework

    def run(self):
        with gr.Blocks(title="The Price is Right", fill_width=True) as ui:
            log_data = gr.State([])

            def table_for(opps):
                return [
                    [
                        opp.deal.product_description,
                        f"${opp.deal.price:.2f}",
                        f"${opp.estimate:.2f}",
                        f"${opp.discount:.2f}",
                        opp.deal.url,
                    ]
                    for opp in opps
                ]

            def update_output(log_data, log_queue, result_queue):
                initial_result = table_for(self.get_agent_framework().memory)
                final_result = None
                while True:
                    try:
                        message = log_queue.get_nowait()
                        log_data.append(reformat(message))
                        yield log_data, html_for(log_data), final_result or initial_result
                    except queue.Empty:
                        try:
                            final_result = result_queue.get_nowait()
                            yield log_data, html_for(log_data), final_result or initial_result
                        except queue.Empty:
                            if final_result is not None:
                                break
                            time.sleep(0.1)

            def get_initial_plot():
                fig = go.Figure()
                fig.update_layout(
                    title="Loading vector DB...",
                    height=400,
                )
                return fig

            def get_plot():
                documents, vectors, colors = DealAgentFramework.get_plot_data(max_datapoints=800)
                # Create the 3D scatter plot
                fig = go.Figure(
                    data=[
                        go.Scatter3d(
                            x=vectors[:, 0],
                            y=vectors[:, 1],
                            z=vectors[:, 2],
                            mode="markers",
                            marker=dict(size=2, color=colors, opacity=0.7),
                        )
                    ]
                )

                fig.update_layout(
                    scene=dict(
                        xaxis_title="x",
                        yaxis_title="y",
                        zaxis_title="z",
                        aspectmode="manual",
                        aspectratio=dict(x=2.2, y=2.2, z=1),  # Make x-axis twice as long
                        camera=dict(
                            eye=dict(x=1.6, y=1.6, z=0.8)  # Adjust camera position
                        ),
                    ),
                    height=400,
                    margin=dict(r=5, b=1, l=5, t=2),
                )

                return fig

            def do_run():
                new_opportunities = self.get_agent_framework().run()
                table = table_for(new_opportunities)
                return table

            def run_with_logging(initial_log_data):
                log_queue = queue.Queue()
                result_queue = queue.Queue()
                setup_logging(log_queue)

                def worker():
                    result = do_run()
                    result_queue.put(result)

                thread = threading.Thread(target=worker)
                thread.start()

                for log_data, output, final_result in update_output(
                    initial_log_data, log_queue, result_queue
                ):
                    yield log_data, output, final_result

            def do_select(selected_index: gr.SelectData):
                opportunities = self.get_agent_framework().memory
                row = selected_index.index[0]
                opportunity = opportunities[row]
                self.get_agent_framework().planner.messenger.alert(opportunity)

            with gr.Row():
                gr.Markdown(
                    '<div style="text-align: center;font-size:24px"><strong>The Price is Right</strong> - Autonomous Agent Framework that hunts for deals</div>'
                )
            with gr.Row():
                gr.Markdown(
                    '<div style="text-align: center;font-size:14px">A proprietary fine-tuned LLM deployed on Modal and a RAG pipeline with a frontier model collaborate to send push notifications with great online deals.</div>'
                )
            with gr.Row():
                opportunities_dataframe = gr.Dataframe(
                    headers=["Deals found so far", "Price", "Estimate", "Discount", "URL"],
                    wrap=True,
                    column_widths=[6, 1, 1, 1, 3],
                    row_count=10,
                    col_count=5,
                    max_height=400,
                )
            with gr.Row():
                with gr.Column(scale=1):
                    logs = gr.HTML()
                with gr.Column(scale=1):
                    plot = gr.Plot(value=get_plot(), show_label=False)

            ui.load(
                run_with_logging,
                inputs=[log_data],
                outputs=[log_data, logs, opportunities_dataframe],
            )

            timer = gr.Timer(value=300, active=True)
            timer.tick(
                run_with_logging,
                inputs=[log_data],
                outputs=[log_data, logs, opportunities_dataframe],
            )

            opportunities_dataframe.select(do_select)

        ui.launch(share=False, inbrowser=True)


if __name__ == "__main__":
    App().run()
```


---

<a id="file-week8-pricer-ephemeral-py"></a>
## File: `week8/pricer_ephemeral.py`

> **Path in repository:** `week8/pricer_ephemeral.py`

```python
import modal
from modal import Image

# Setup

app = modal.App("pricer")
image = Image.debian_slim().pip_install(
    "torch", "transformers", "bitsandbytes", "accelerate", "peft"
)
secrets = [modal.Secret.from_name("huggingface-secret")]

# Constants

GPU = "T4"
BASE_MODEL = "meta-llama/Llama-3.2-3B"
PROJECT_NAME = "price"
HF_USER = "ed-donner"  # your HF name here! Or use mine if you just want to reproduce my results.
RUN_NAME = "2025-11-28_18.47.07"
PROJECT_RUN_NAME = f"{PROJECT_NAME}-{RUN_NAME}"
REVISION = "b19c8bfea3b6ff62237fbb0a8da9779fc12cefbd"
FINETUNED_MODEL = f"{HF_USER}/{PROJECT_RUN_NAME}"


@app.function(image=image, secrets=secrets, gpu=GPU, timeout=1800)
def price(description: str) -> float:
    import re
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, set_seed
    from peft import PeftModel

    PREFIX = "Price is $"
    QUESTION = "What does this cost to the nearest dollar?"

    prompt = f"{QUESTION}\n\n{description}\n\n{PREFIX}"

    # Quant Config
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
    )

    # Load model and tokenizer

    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL, quantization_config=quant_config, device_map="auto"
    )

    fine_tuned_model = PeftModel.from_pretrained(base_model, FINETUNED_MODEL, revision=REVISION)

    set_seed(42)
    inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    with torch.no_grad():
        outputs = fine_tuned_model.generate(inputs, max_new_tokens=5)
    result = tokenizer.decode(outputs[0])
    contents = result.split("Price is $")[1]
    contents = contents.replace(",", "")
    match = re.search(r"[-+]?\d*\.\d+|\d+", contents)
    return float(match.group()) if match else 0
```


---

<a id="file-week8-pricer-service-py"></a>
## File: `week8/pricer_service.py`

> **Path in repository:** `week8/pricer_service.py`

```python
import modal
from modal import Image

# Setup - define our infrastructure with code!

app = modal.App("pricer-service")
image = Image.debian_slim().pip_install(
    "torch", "transformers", "bitsandbytes", "accelerate", "peft"
)

# This collects the secret from Modal.
# Depending on your Modal configuration, you may need to replace "huggingface-secret" with "hf-secret"
secrets = [modal.Secret.from_name("huggingface-secret")]

# Constants

GPU = "T4"
BASE_MODEL = "meta-llama/Llama-3.2-3B"
PROJECT_NAME = "price"
HF_USER = "ed-donner"  # your HF name here! Or use mine if you just want to reproduce my results.
RUN_NAME = "2025-11-28_18.47.07"
PROJECT_RUN_NAME = f"{PROJECT_NAME}-{RUN_NAME}"
REVISION = "b19c8bfea3b6ff62237fbb0a8da9779fc12cefbd"
FINETUNED_MODEL = f"{HF_USER}/{PROJECT_RUN_NAME}"


@app.function(image=image, secrets=secrets, gpu=GPU, timeout=1800)
def price(description: str) -> float:
    import re
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, set_seed
    from peft import PeftModel

    PREFIX = "Price is $"
    QUESTION = "What does this cost to the nearest dollar?"

    prompt = f"{QUESTION}\n\n{description}\n\n{PREFIX}"

    # Quant Config
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
    )

    # Load model and tokenizer

    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL, quantization_config=quant_config, device_map="auto"
    )

    fine_tuned_model = PeftModel.from_pretrained(base_model, FINETUNED_MODEL, revision=REVISION)

    set_seed(42)
    inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    with torch.no_grad():
        outputs = fine_tuned_model.generate(inputs, max_new_tokens=5)
    result = tokenizer.decode(outputs[0])
    contents = result.split("Price is $")[1]
    contents = contents.replace(",", "")
    match = re.search(r"[-+]?\d*\.\d+|\d+", contents)
    return float(match.group()) if match else 0
```


---

<a id="file-week8-pricer-service2-py"></a>
## File: `week8/pricer_service2.py`

> **Path in repository:** `week8/pricer_service2.py`

```python
import modal
from modal import Volume, Image
# Setup - define our infrastructure with code!

app = modal.App("pricer-service")
image = Image.debian_slim().pip_install(
    "huggingface", "torch", "transformers", "bitsandbytes", "accelerate", "peft"
)

# This collects the secret from Modal.
# Depending on your Modal configuration, you may need to replace "huggingface-secret" with "hf-secret"
secrets = [modal.Secret.from_name("huggingface-secret")]

GPU = "T4"
BASE_MODEL = "meta-llama/Llama-3.2-3B"
PROJECT_NAME = "price"
HF_USER = "ed-donner"  # your HF name here! Or use mine if you just want to reproduce my results.
RUN_NAME = "2025-11-28_18.47.07"
PROJECT_RUN_NAME = f"{PROJECT_NAME}-{RUN_NAME}"
REVISION = "b19c8bfea3b6ff62237fbb0a8da9779fc12cefbd"
FINETUNED_MODEL = f"{HF_USER}/{PROJECT_RUN_NAME}"
CACHE_DIR = "/cache"

# Change this to 1 if you want Modal to be always running, otherwise it will go cold after 2 mins
MIN_CONTAINERS = 0

PREFIX = "Price is $"
QUESTION = "What does this cost to the nearest dollar?"

hf_cache_volume = Volume.from_name("hf-hub-cache", create_if_missing=True)


@app.cls(
    image=image.env({"HF_HUB_CACHE": CACHE_DIR}),
    secrets=secrets,
    gpu=GPU,
    timeout=1800,
    min_containers=MIN_CONTAINERS,
    volumes={CACHE_DIR: hf_cache_volume},
)
class Pricer:
    @modal.enter()
    def setup(self):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
        from peft import PeftModel

        # Quant Config
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
        )

        # Load model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"
        self.base_model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL, quantization_config=quant_config, device_map="auto"
        )
        self.fine_tuned_model = PeftModel.from_pretrained(
            self.base_model, FINETUNED_MODEL, revision=REVISION
        )

    @modal.method()
    def price(self, description: str) -> float:
        import re
        import torch
        from transformers import set_seed

        set_seed(42)
        prompt = f"{QUESTION}\n\n{description}\n\n{PREFIX}"

        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = self.fine_tuned_model.generate(inputs, max_new_tokens=5)
        result = self.tokenizer.decode(outputs[0])
        contents = result.split("Price is $")[1]
        contents = contents.replace(",", "")
        match = re.search(r"[-+]?\d*\.\d+|\d+", contents)
        return float(match.group()) if match else 0
```


---

<a id="file-week8-results-ipynb"></a>
## File: `week8/results.ipynb`

> **Path in repository:** `week8/results.ipynb`

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
    ("GPT 5.1", "slateblue", 44.74),
    ("GPT 4.1 Nano (Fine-tuned)", "skyblue", 75.91),
    ("Deep Neural Network", "orange", 46.49),
    ("Base Llama 3.2 4 bit", "darkred", 110.72),
    ("Fine-tuned Lite", "red", 65.40),
    ("Fine-tuned Full", "red", 39.85),
    ("GPT 5.1 RAG", "green", 30.19),
    ("Ensemble", "purple", 29.9)
]

labels, colors, values = zip(*results)

fig = go.Figure(go.Bar(x=labels, y=values, marker_color=colors))

fig.update_layout(
    title="Prediction error from each model",
    yaxis=dict(range=[0, max(values)], title="Error"),
    xaxis=dict(tickangle=-45),
    width=1000,
    height=800
)

fig.show()
```


---
