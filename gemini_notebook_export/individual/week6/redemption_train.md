# redemption_train.ipynb

> **Original Path:** `week6/redemption_train.ipynb`

---

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
