# Week3 Visualizer and Tools

This unified reference file consolidates **6 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [week3/day1.ipynb](#file-week3-day1-ipynb)
- [week3/day2.ipynb](#file-week3-day2-ipynb)
- [week3/day3.ipynb](#file-week3-day3-ipynb)
- [week3/day4.ipynb](#file-week3-day4-ipynb)
- [week3/day5.ipynb](#file-week3-day5-ipynb)
- [week3/visualizer.py](#file-week3-visualizer-py)

---

<a id="file-week3-day1-ipynb"></a>
## File: `week3/day1.ipynb`

> **Path in repository:** `week3/day1.ipynb`

# Introducing Colab

Learn about Google Colab and set up a Google account (if you don't already have one) [here](https://colab.research.google.com/)

You should be able to use the free tier or minimal spend to complete all the projects in the class. I personally signed up for Colab Pro+ and I'm loving it - but it's not required.

To see some of what Colab can do, please follow the link below!

https://colab.research.google.com/drive/1DjcrYDZldAXKJ08x1uYIVCtItoLPk1Wr?usp=sharing


---

<a id="file-week3-day2-ipynb"></a>
## File: `week3/day2.ipynb`

> **Path in repository:** `week3/day2.ipynb`

# HuggingFace pipelines

For this session we head to Google Colab and use this Notebook to explore the HuggingFace High Level API, pipelines.

https://colab.research.google.com/drive/1aMaEw8A56xs0bRM4lu8z7ou18jqyybGm?usp=sharing

You can use a low cost (or free) T4 GPU runtime for this notebook - and the results look great!

There are instructions in the notebook for setting up your HuggingFace Token and including it as a secret in the notebook.


---

<a id="file-week3-day3-ipynb"></a>
## File: `week3/day3.ipynb`

> **Path in repository:** `week3/day3.ipynb`

# Tokenizers

Please can I bring you back to the wonderful Google Colab where we'll look at different Tokenizers:

https://colab.research.google.com/drive/1WD6Y2N7ctQi1X9wa6rpkg8UfyA4iSVuz?usp=sharing


---

<a id="file-week3-day4-ipynb"></a>
## File: `week3/day4.ipynb`

> **Path in repository:** `week3/day4.ipynb`

# Models

And now - this colab unveils the heart (or the brains?) of the transformers library - the models:

https://colab.research.google.com/drive/1hhR9Z-yiqjUe7pJjVQw4c74z_V3VchLy?usp=sharing

This should run nicely on a low-cost or free T4 box.


---

<a id="file-week3-day5-ipynb"></a>
## File: `week3/day5.ipynb`

> **Path in repository:** `week3/day5.ipynb`

# Meeting minutes creator

In this colab, we make a meeting minutes program.

It includes useful code to connect your Google Drive to your colab.

Upload your own audio to make this work!!

https://colab.research.google.com/drive/1KSMxOCprsl1QRpt_Rq0UqCAyMtPqDQYx?usp=sharing

This should run nicely on a low-cost or free T4 box.

### BUT FIRST - Something cool - really showing you how "model inference" works via OpenAI

```python
from visualizer import TokenPredictor, create_token_graph, visualize_predictions

message = "In one sentence, describe the color orange to someone who has never been able to see"
model_name = "gpt-6-luna"

predictor = TokenPredictor(model_name)
predictions = predictor.predict_tokens(message)
G = create_token_graph(model_name, predictions)
plt = visualize_predictions(G)
plt.show()
```


---

<a id="file-week3-visualizer-py"></a>
## File: `week3/visualizer.py`

> **Path in repository:** `week3/visualizer.py`

```python
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict
import math
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)


class TokenPredictor:
    def __init__(self, model_name: str):
        self.client = OpenAI()
        self.messages = []
        self.predictions = []
        self.model_name = model_name

    def predict_tokens(self, prompt: str, max_tokens: int = 100) -> List[Dict]:
        """
        Generate text token by token and track prediction probabilities.
        Returns list of predictions with top token and alternatives.
        """
        response = self.client.chat.completions.create(
            model=self.model_name,
            reasoning_effort="none",
            messages=[{"role": "user", "content": prompt}],
            max_completion_tokens=max_tokens,
            temperature=0,  # Use temperature 0 for deterministic output
            logprobs=True,
            seed=42,
            top_logprobs=3,  # Get top 3 token predictions
            stream=True,  # Stream the response
        )

        predictions = []
        for chunk in response:
            if chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                logprobs = chunk.choices[0].logprobs.content[0].top_logprobs
                logprob_dict = {item.token: item.logprob for item in logprobs}

                # Get top predicted token and probability
                top_token = token
                top_prob = logprob_dict[token]

                # Get alternative predictions
                alternatives = []
                for alt_token, alt_prob in logprob_dict.items():
                    if alt_token != token:
                        alternatives.append((alt_token, math.exp(alt_prob)))
                alternatives.sort(key=lambda x: x[1], reverse=True)

                prediction = {
                    "token": top_token,
                    "probability": math.exp(top_prob),
                    "alternatives": alternatives[:2],  # Keep top 2 alternatives
                }
                predictions.append(prediction)

        return predictions


def create_token_graph(model_name: str, predictions: List[Dict]) -> nx.DiGraph:
    """
    Create a directed graph showing token predictions and alternatives.
    """
    G = nx.DiGraph()

    G.add_node("START", token=model_name, prob="START", color="lightgreen", size=4000)

    # First, create all main token nodes in sequence
    for i, pred in enumerate(predictions):
        token_id = f"t{i}"
        G.add_node(
            token_id,
            token=pred["token"],
            prob=f"{pred['probability'] * 100:.1f}%",
            color="lightblue",
            size=6000,
        )

        if i == 0:
            G.add_edge("START", token_id)
        else:
            G.add_edge(f"t{i - 1}", token_id)

    # Then add alternative nodes with a different y-position
    last_id = None
    for i, pred in enumerate(predictions):
        parent_token = "START" if i == 0 else f"t{i - 1}"

        # Add alternative token nodes slightly below main sequence
        for j, (alt_token, alt_prob) in enumerate(pred["alternatives"]):
            alt_id = f"t{i}_alt{j}"
            G.add_node(
                alt_id, token=alt_token, prob=f"{alt_prob * 100:.1f}%", color="lightgray", size=6000
            )

            # Add edge from main token to its alternatives only
            G.add_edge(parent_token, alt_id)
            last_id = parent_token

    last_id = f"t{len(predictions) - 1}" if predictions else "START"
    G.add_node("END", token="END", prob="100%", color="red", size=6000)
    G.add_edge(last_id, "END")

    return G


def visualize_predictions(G: nx.DiGraph, figsize=(14, 80)):
    """
    Visualize the token prediction graph with vertical layout and alternating alternatives.
    """
    plt.figure(figsize=figsize)

    # Create custom positioning for nodes
    pos = {}
    spacing_y = 5  # Vertical spacing between main tokens
    spacing_x = 5  # Horizontal spacing for alternatives

    # Position main token nodes in a vertical line
    main_nodes = [n for n in G.nodes() if "_alt" not in n]
    for i, node in enumerate(main_nodes):
        pos[node] = (0, -i * spacing_y)  # Center main tokens vertically

    # Position alternative nodes to left and right of main tokens
    for node in G.nodes():
        if "_alt" in node:
            main_token = node.split("_")[0]
            alt_num = int(node.split("_alt")[1])
            if main_token in pos:
                # Place first alternative to left, second to right
                x_offset = -spacing_x if alt_num == 0 else spacing_x
                pos[node] = (x_offset, pos[main_token][1] + 0.05)

    # Draw nodes
    node_colors = [G.nodes[node]["color"] for node in G.nodes()]
    node_sizes = [G.nodes[node]["size"] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)

    # Draw all edges as straight lines
    nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True, arrowsize=20, alpha=0.7)

    # Add labels with token and probability
    labels = {node: f"{G.nodes[node]['token']}\n{G.nodes[node]['prob']}" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=14)

    plt.title("Token prediction.")
    plt.axis("off")

    # Adjust plot limits to ensure all nodes are visible
    margin = 8
    x_values = [x for x, y in pos.values()]
    y_values = [y for x, y in pos.values()]
    plt.xlim(min(x_values) - margin, max(x_values) + margin)
    plt.ylim(min(y_values) - margin, max(y_values) + margin)

    # plt.tight_layout()
    return plt
```


---
