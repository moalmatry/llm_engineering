# day4.ipynb

> **Original Path:** `week5/day4.ipynb`

---

# RAG Day 4

## Evaluation!

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Keep in mind how you would evaluate RAG for your business</h2>
            <span style="color:#181;">This is such an important part of building an accurate and reliable RAG pipeline. And it's applicable to many aspects of solving business problems with LLMs. People are often focused on RAG architecture and RAG frameworks for their business. But even more important: evaluations!</span>
        </td>
    </tr>
</table>

```python
from evaluation import test
```

```python
tests = test.load_tests()
```

```python
len(tests)
```

**Cell Output:**
```text
150
```

```python
example = tests[0]
print(example.question)
print(example.category)
print(example.reference_answer)
print(example.keywords)
```

**Cell Output:**
```text
Who won the prestigious IIOTY award in 2023?
direct_fact
Maxine Thompson won the prestigious Insurellm Innovator of the Year (IIOTY) award in 2023.
['Maxine', 'Thompson', 'IIOTY']
```

```python
from collections import Counter
count = Counter([t.category for t in tests])
count
```

**Cell Output:**
```text
Counter({'direct_fact': 70,
         'temporal': 20,
         'spanning': 20,
         'comparative': 10,
         'numerical': 10,
         'relationship': 10,
         'holistic': 10})
```

```python
from evaluation.eval import evaluate_retrieval, evaluate_answer
```

```python
evaluate_retrieval(example)
```

**Cell Output:**
```text
RetrievalEval(mrr=0.16666666666666666, ndcg=0.28711770538226206, keywords_found=2, total_keywords=3, keyword_coverage=66.66666666666666)
```

```python
eval, answer, chunks = evaluate_answer(example)
```

```python
eval
```

**Cell Output:**
```text
AnswerEval(feedback="The answer correctly identifies Maxine as the winner and mentions the IIOTY award in 2023, but it omits Thompson's full name, which is present in the reference. This affects completeness. The relevance is high, as it directly addresses the question about the award winner.", accuracy=5.0, completeness=4.0, relevance=5.0)
```

```python
print(eval.feedback)
print(eval.accuracy)
print(eval.completeness)
print(eval.relevance)
```

**Cell Output:**
```text
The answer correctly identifies Maxine as the winner and mentions the IIOTY award in 2023, but it omits Thompson's full name, which is present in the reference. This affects completeness. The relevance is high, as it directly addresses the question about the award winner.
5.0
4.0
5.0
```
