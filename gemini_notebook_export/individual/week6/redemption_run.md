# redemption_run.ipynb

> **Original Path:** `week6/redemption_run.ipynb`

---

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
