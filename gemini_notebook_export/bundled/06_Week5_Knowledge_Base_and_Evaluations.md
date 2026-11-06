# Week5 Knowledge Base and Evaluations

This unified reference file consolidates **90 source files** from the LLM Engineering course repository.
Optimized for **Google NotebookLM** and **Gemini Context Windows**.

## Table of Contents

- [week5/app.py](#file-week5-app-py)
- [week5/day1.ipynb](#file-week5-day1-ipynb)
- [week5/day2.ipynb](#file-week5-day2-ipynb)
- [week5/day3.ipynb](#file-week5-day3-ipynb)
- [week5/day4.ipynb](#file-week5-day4-ipynb)
- [week5/day5.ipynb](#file-week5-day5-ipynb)
- [week5/evaluation/eval.py](#file-week5-evaluation-eval-py)
- [week5/evaluation/test.py](#file-week5-evaluation-test-py)
- [week5/evaluation/tests.jsonl](#file-week5-evaluation-tests-jsonl)
- [week5/evaluator.py](#file-week5-evaluator-py)
- [week5/implementation/answer.py](#file-week5-implementation-answer-py)
- [week5/implementation/ingest.py](#file-week5-implementation-ingest-py)
- [week5/knowledge-base/company/about.md](#file-week5-knowledge-base-company-about-md)
- [week5/knowledge-base/company/careers.md](#file-week5-knowledge-base-company-careers-md)
- [week5/knowledge-base/company/culture.md](#file-week5-knowledge-base-company-culture-md)
- [week5/knowledge-base/company/overview.md](#file-week5-knowledge-base-company-overview-md)
- [week5/knowledge-base/contracts/Contract with Advantage Medical Coverage for Healthllm.md](#file-week5-knowledge-base-contracts-contract-with-advantage-medical-coverage-for-healthllm-md)
- [week5/knowledge-base/contracts/Contract with Apex Reinsurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md](#file-week5-knowledge-base-contracts-contract-with-apex-reinsurance-for-rellm---ai-powered-enterprise-reinsurance-solution-md)
- [week5/knowledge-base/contracts/Contract with Atlantic Risk Solutions for Bizllm.md](#file-week5-knowledge-base-contracts-contract-with-atlantic-risk-solutions-for-bizllm-md)
- [week5/knowledge-base/contracts/Contract with Belvedere Insurance for Markellm.md](#file-week5-knowledge-base-contracts-contract-with-belvedere-insurance-for-markellm-md)
- [week5/knowledge-base/contracts/Contract with BrightWay Solutions for Markellm.md](#file-week5-knowledge-base-contracts-contract-with-brightway-solutions-for-markellm-md)
- [week5/knowledge-base/contracts/Contract with ConnectInsure Agency for Markellm.md](#file-week5-knowledge-base-contracts-contract-with-connectinsure-agency-for-markellm-md)
- [week5/knowledge-base/contracts/Contract with Continental Commercial Group for Bizllm.md](#file-week5-knowledge-base-contracts-contract-with-continental-commercial-group-for-bizllm-md)
- [week5/knowledge-base/contracts/Contract with DriveSmart Insurance for Carllm.md](#file-week5-knowledge-base-contracts-contract-with-drivesmart-insurance-for-carllm-md)
- [week5/knowledge-base/contracts/Contract with EverGuard Insurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md](#file-week5-knowledge-base-contracts-contract-with-everguard-insurance-for-rellm---ai-powered-enterprise-reinsurance-solution-md)
- [week5/knowledge-base/contracts/Contract with Evergreen Life Insurance for Lifellm.md](#file-week5-knowledge-base-contracts-contract-with-evergreen-life-insurance-for-lifellm-md)
- [week5/knowledge-base/contracts/Contract with FastTrack Insurance Services for Claimllm.md](#file-week5-knowledge-base-contracts-contract-with-fasttrack-insurance-services-for-claimllm-md)
- [week5/knowledge-base/contracts/Contract with Fortress Business Underwriters for Bizllm.md](#file-week5-knowledge-base-contracts-contract-with-fortress-business-underwriters-for-bizllm-md)
- [week5/knowledge-base/contracts/Contract with GlobalRe Partners for Rellm.md](#file-week5-knowledge-base-contracts-contract-with-globalre-partners-for-rellm-md)
- [week5/knowledge-base/contracts/Contract with GreenField Holdings for Markellm.md](#file-week5-knowledge-base-contracts-contract-with-greenfield-holdings-for-markellm-md)
- [week5/knowledge-base/contracts/Contract with GreenValley Insurance for Homellm.md](#file-week5-knowledge-base-contracts-contract-with-greenvalley-insurance-for-homellm-md)
- [week5/knowledge-base/contracts/Contract with Greenstone Insurance for Homellm.md](#file-week5-knowledge-base-contracts-contract-with-greenstone-insurance-for-homellm-md)
- [week5/knowledge-base/contracts/Contract with Guardian Life Partners for Lifellm.md](#file-week5-knowledge-base-contracts-contract-with-guardian-life-partners-for-lifellm-md)
- [week5/knowledge-base/contracts/Contract with Harmony Health Plans for Healthllm.md](#file-week5-knowledge-base-contracts-contract-with-harmony-health-plans-for-healthllm-md)
- [week5/knowledge-base/contracts/Contract with Heritage Life Assurance for Lifellm.md](#file-week5-knowledge-base-contracts-contract-with-heritage-life-assurance-for-lifellm-md)
- [week5/knowledge-base/contracts/Contract with Metropolitan Life Group for Lifellm.md](#file-week5-knowledge-base-contracts-contract-with-metropolitan-life-group-for-lifellm-md)
- [week5/knowledge-base/contracts/Contract with National Claims Network for Claimllm.md](#file-week5-knowledge-base-contracts-contract-with-national-claims-network-for-claimllm-md)
- [week5/knowledge-base/contracts/Contract with Pinnacle Insurance Co. for Homellm.md](#file-week5-knowledge-base-contracts-contract-with-pinnacle-insurance-co--for-homellm-md)
- [week5/knowledge-base/contracts/Contract with Premier Adjusters Inc. for Claimllm.md](#file-week5-knowledge-base-contracts-contract-with-premier-adjusters-inc--for-claimllm-md)
- [week5/knowledge-base/contracts/Contract with Rapid Claims Associates for Claimllm.md](#file-week5-knowledge-base-contracts-contract-with-rapid-claims-associates-for-claimllm-md)
- [week5/knowledge-base/contracts/Contract with Roadway Insurance Inc. for Carllm.md](#file-week5-knowledge-base-contracts-contract-with-roadway-insurance-inc--for-carllm-md)
- [week5/knowledge-base/contracts/Contract with SafeHaven Property Insurance for Homellm.md](#file-week5-knowledge-base-contracts-contract-with-safehaven-property-insurance-for-homellm-md)
- [week5/knowledge-base/contracts/Contract with Stellar Insurance Co. for Rellm.md](#file-week5-knowledge-base-contracts-contract-with-stellar-insurance-co--for-rellm-md)
- [week5/knowledge-base/contracts/Contract with Summit Commercial Insurance for Bizllm.md](#file-week5-knowledge-base-contracts-contract-with-summit-commercial-insurance-for-bizllm-md)
- [week5/knowledge-base/contracts/Contract with TechDrive Insurance for Carllm.md](#file-week5-knowledge-base-contracts-contract-with-techdrive-insurance-for-carllm-md)
- [week5/knowledge-base/contracts/Contract with United Healthcare Alliance for Healthllm.md](#file-week5-knowledge-base-contracts-contract-with-united-healthcare-alliance-for-healthllm-md)
- [week5/knowledge-base/contracts/Contract with Velocity Auto Solutions for Carllm.md](#file-week5-knowledge-base-contracts-contract-with-velocity-auto-solutions-for-carllm-md)
- [week5/knowledge-base/contracts/Contract with WellCare Insurance Co. for Healthllm.md](#file-week5-knowledge-base-contracts-contract-with-wellcare-insurance-co--for-healthllm-md)
- [week5/knowledge-base/employees/Alex Chen.md](#file-week5-knowledge-base-employees-alex-chen-md)
- [week5/knowledge-base/employees/Alex Harper.md](#file-week5-knowledge-base-employees-alex-harper-md)
- [week5/knowledge-base/employees/Alex Thomson.md](#file-week5-knowledge-base-employees-alex-thomson-md)
- [week5/knowledge-base/employees/Amanda Foster.md](#file-week5-knowledge-base-employees-amanda-foster-md)
- [week5/knowledge-base/employees/Avery Lancaster.md](#file-week5-knowledge-base-employees-avery-lancaster-md)
- [week5/knowledge-base/employees/Brandon Walker.md](#file-week5-knowledge-base-employees-brandon-walker-md)
- [week5/knowledge-base/employees/Carlos Rodriguez.md](#file-week5-knowledge-base-employees-carlos-rodriguez-md)
- [week5/knowledge-base/employees/Daniel Park.md](#file-week5-knowledge-base-employees-daniel-park-md)
- [week5/knowledge-base/employees/David Kim.md](#file-week5-knowledge-base-employees-david-kim-md)
- [week5/knowledge-base/employees/Emily Carter.md](#file-week5-knowledge-base-employees-emily-carter-md)
- [week5/knowledge-base/employees/Emily Tran.md](#file-week5-knowledge-base-employees-emily-tran-md)
- [week5/knowledge-base/employees/James Wilson.md](#file-week5-knowledge-base-employees-james-wilson-md)
- [week5/knowledge-base/employees/Jennifer Adams.md](#file-week5-knowledge-base-employees-jennifer-adams-md)
- [week5/knowledge-base/employees/Jessica Liu.md](#file-week5-knowledge-base-employees-jessica-liu-md)
- [week5/knowledge-base/employees/Jordan Blake.md](#file-week5-knowledge-base-employees-jordan-blake-md)
- [week5/knowledge-base/employees/Jordan K. Bishop.md](#file-week5-knowledge-base-employees-jordan-k--bishop-md)
- [week5/knowledge-base/employees/Kevin Zhang.md](#file-week5-knowledge-base-employees-kevin-zhang-md)
- [week5/knowledge-base/employees/Lisa Anderson.md](#file-week5-knowledge-base-employees-lisa-anderson-md)
- [week5/knowledge-base/employees/Marcus Johnson.md](#file-week5-knowledge-base-employees-marcus-johnson-md)
- [week5/knowledge-base/employees/Maxine Thompson.md](#file-week5-knowledge-base-employees-maxine-thompson-md)
- [week5/knowledge-base/employees/Maya Thompson.md](#file-week5-knowledge-base-employees-maya-thompson-md)
- [week5/knowledge-base/employees/Michael O'Brien.md](#file-week5-knowledge-base-employees-michael-o'brien-md)
- [week5/knowledge-base/employees/Michelle Rivera.md](#file-week5-knowledge-base-employees-michelle-rivera-md)
- [week5/knowledge-base/employees/Nina Patel.md](#file-week5-knowledge-base-employees-nina-patel-md)
- [week5/knowledge-base/employees/Oliver Spencer.md](#file-week5-knowledge-base-employees-oliver-spencer-md)
- [week5/knowledge-base/employees/Priya Sharma.md](#file-week5-knowledge-base-employees-priya-sharma-md)
- [week5/knowledge-base/employees/Rachel Martinez.md](#file-week5-knowledge-base-employees-rachel-martinez-md)
- [week5/knowledge-base/employees/Robert Chen.md](#file-week5-knowledge-base-employees-robert-chen-md)
- [week5/knowledge-base/employees/Samantha Greene.md](#file-week5-knowledge-base-employees-samantha-greene-md)
- [week5/knowledge-base/employees/Samuel Trenton.md](#file-week5-knowledge-base-employees-samuel-trenton-md)
- [week5/knowledge-base/employees/Sarah Williams.md](#file-week5-knowledge-base-employees-sarah-williams-md)
- [week5/knowledge-base/employees/Tyler Brooks.md](#file-week5-knowledge-base-employees-tyler-brooks-md)
- [week5/knowledge-base/products/Bizllm.md](#file-week5-knowledge-base-products-bizllm-md)
- [week5/knowledge-base/products/Carllm.md](#file-week5-knowledge-base-products-carllm-md)
- [week5/knowledge-base/products/Claimllm.md](#file-week5-knowledge-base-products-claimllm-md)
- [week5/knowledge-base/products/Healthllm.md](#file-week5-knowledge-base-products-healthllm-md)
- [week5/knowledge-base/products/Homellm.md](#file-week5-knowledge-base-products-homellm-md)
- [week5/knowledge-base/products/Lifellm.md](#file-week5-knowledge-base-products-lifellm-md)
- [week5/knowledge-base/products/Markellm.md](#file-week5-knowledge-base-products-markellm-md)
- [week5/knowledge-base/products/Rellm.md](#file-week5-knowledge-base-products-rellm-md)
- [week5/pro_implementation/answer.py](#file-week5-pro-implementation-answer-py)
- [week5/pro_implementation/ingest.py](#file-week5-pro-implementation-ingest-py)

---

<a id="file-week5-app-py"></a>
## File: `week5/app.py`

> **Path in repository:** `week5/app.py`

```python
import gradio as gr
from dotenv import load_dotenv

from implementation.answer import answer_question

load_dotenv(override=True)


def format_context(context):
    result = "<h2 style='color: #ff7800;'>Relevant Context</h2>\n\n"
    for doc in context:
        result += f"<span style='color: #ff7800;'>Source: {doc.metadata['source']}</span>\n\n"
        result += doc.page_content + "\n\n"
    return result


def chat(history):
    last_message = history[-1]["content"]
    prior = history[:-1]
    answer, context = answer_question(last_message, prior)
    history.append({"role": "assistant", "content": answer})
    return history, format_context(context)


def main():
    def put_message_in_chatbot(message, history):
        return "", history + [{"role": "user", "content": message}]

    theme = gr.themes.Soft(font=["Inter", "system-ui", "sans-serif"])

    with gr.Blocks(title="Insurellm Expert Assistant", theme=theme) as ui:
        gr.Markdown("# 🏢 Insurellm Expert Assistant\nAsk me anything about Insurellm!")

        with gr.Row():
            with gr.Column(scale=1):
                chatbot = gr.Chatbot(
                    label="💬 Conversation", height=600, type="messages", show_copy_button=True
                )
                message = gr.Textbox(
                    label="Your Question",
                    placeholder="Ask anything about Insurellm...",
                    show_label=False,
                )

            with gr.Column(scale=1):
                context_markdown = gr.Markdown(
                    label="📚 Retrieved Context",
                    value="*Retrieved context will appear here*",
                    container=True,
                    height=600,
                )

        message.submit(
            put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]
        ).then(chat, inputs=chatbot, outputs=[chatbot, context_markdown])

    ui.launch(inbrowser=True)


if __name__ == "__main__":
    main()
```


---

<a id="file-week5-day1-ipynb"></a>
## File: `week5/day1.ipynb`

> **Path in repository:** `week5/day1.ipynb`

# Welcome to RAG week!!

## Expert Knowledge Worker

### A question answering Assistant that is an expert knowledge worker
### To be used by employees of Insurellm, an Insurance Tech company
### The AI assistant needs to be accurate and the solution should be low cost.

This project will use RAG (Retrieval Augmented Generation) to ensure our question/answering assistant has high accuracy.

This first implementation will use a simplistic, brute-force type of RAG..

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="../assets/business.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#181;">Business applications of this week's projects</h2>
            <span style="color:#181;">RAG is perhaps the most immediately applicable technique of anything that we cover in the course! In fact, there are commercial products that do precisely what we build this week: nuanced querying across large databases of information, such as company contracts or product specs. RAG gives you a quick-to-market, low cost mechanism for adapting an LLM to your business area.</span>
        </td>
    </tr>
</table>

```python
import os
import glob
from dotenv import load_dotenv
from pathlib import Path
import gradio as gr
from openai import OpenAI
```

```python
# Setting up

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

MODEL = "gpt-6-luna"
openai = OpenAI()
```

### Let's read in all employee data into a dictionary

```python
knowledge = {}

filenames = glob.glob("knowledge-base/employees/*")

for filename in filenames:
    name = Path(filename).stem.split(' ')[-1]
    with open(filename, "r", encoding="utf-8") as f:
        knowledge[name.lower()] = f.read()
```

```python
knowledge
```

```python
knowledge["lancaster"]
```

```python
filenames = glob.glob("knowledge-base/products/*")

for filename in filenames:
    name = Path(filename).stem
    with open(filename, "r", encoding="utf-8") as f:
        knowledge[name.lower()] = f.read()
```

```python
knowledge.keys()
```

```python
SYSTEM_PREFIX = """
You represent Insurellm, the Insurance Tech company.
You are an expert in answering questions about Insurellm; its employees and its products.
You are provided with additional context that might be relevant to the user's question.
Give brief, accurate answers. If you don't know the answer, say so.

Relevant context:
"""
```

```python
def get_relevant_context_simple(message):
    text = ''.join(ch for ch in message if ch.isalpha() or ch.isspace())
    words = text.lower().split()
    relevant_context = []
    for word in words:
        if word in knowledge:
            relevant_context.append(knowledge[word])
    return relevant_context
```

## But a more pythonic way:

```python
def get_relevant_context(message):
    text = ''.join(ch for ch in message if ch.isalpha() or ch.isspace())
    words = text.lower().split()
    return [knowledge[word] for word in words if word in knowledge]
```

```python
get_relevant_context("Who is lancaster?")
```

```python
get_relevant_context("Who is Lancaster and what is carllm?")
```

```python
def additional_context(message):
    relevant_context = get_relevant_context(message)
    if not relevant_context:
        result = "There is no additional context relevant to the user's question."
    else:
        result = "The following additional context might be relevant in answering the user's question:\n\n"
        result += "\n\n".join(relevant_context)
    return result
```

```python
print(additional_context("Who is Alex Lancaster?"))
```

```python
def chat(message, history):
    system_message = SYSTEM_PREFIX + additional_context(message)
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL, reasoning_effort="none", messages=messages)
    return response.choices[0].message.content
```

## Now we will bring this up in Gradio using the Chat interface -

A quick and easy way to prototype a chat with an LLM

```python
view = gr.ChatInterface(chat, type="messages").launch(inbrowser=True)
```


---

<a id="file-week5-day2-ipynb"></a>
## File: `week5/day2.ipynb`

> **Path in repository:** `week5/day2.ipynb`

## Expert Knowledge Worker

### A question answering agent that is an expert knowledge worker
### To be used by employees of Insurellm, an Insurance Tech company
### The agent needs to be accurate and the solution should be low cost.

This project will use RAG (Retrieval Augmented Generation) to ensure our question/answering assistant has high accuracy.

## TODAY:

- Part A: We will divide our documents into CHUNKS
- Part B: We will encode our CHUNKS into VECTORS and put in Chroma
- Part C: We will visualize our vectors

### PART A: Divide our documents into chunks

```python
import os
import glob
import tiktoken
import numpy as np
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sklearn.manifold import TSNE
import plotly.graph_objects as go
```

```python
# price is a factor for our company, so we're going to use a low cost model

MODEL = "gpt-6-luna"
db_name = "vector_db"
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
```

```python
# How many characters in all the documents?

knowledge_base_path = "knowledge-base/**/*.md"
files = glob.glob(knowledge_base_path, recursive=True)
print(f"Found {len(files)} files in the knowledge base")

entire_knowledge_base = ""

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        entire_knowledge_base += f.read()
        entire_knowledge_base += "\n\n"

print(f"Total characters in knowledge base: {len(entire_knowledge_base):,}")
```

```python
# How many tokens in all the documents?

# gpt-6-luna isn't in tiktoken yet, so we use the encoding of recent OpenAI models
encoding = tiktoken.get_encoding("o200k_base")
tokens = encoding.encode(entire_knowledge_base)
token_count = len(tokens)
print(f"Total tokens for {MODEL}: {token_count:,}")
```

```python
# Load in everything in the knowledgebase using LangChain's loaders

folders = glob.glob("knowledge-base/*")

documents = []
for folder in folders:
    doc_type = os.path.basename(folder)
    loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
    folder_docs = loader.load()
    for doc in folder_docs:
        doc.metadata["doc_type"] = doc_type
        documents.append(doc)

print(f"Loaded {len(documents)} documents")
```

```python
documents[1]
```

```python
# Divide into chunks using the RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

print(f"Divided into {len(chunks)} chunks")
print(f"First chunk:\n\n{chunks[0]}")
```

```python
chunks[100]
```

### PART B: Make vectors and store in Chroma

In Week 3, you set up a Hugging Face account and got an HF_TOKEN

At this point, you might want to add it to your `.env` file and run `load_dotenv(override=True)`

(This actually shouldn't be required).

```python
# Pick an embedding model

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

if os.path.exists(db_name):
    Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_name)
print(f"Vectorstore created with {vectorstore._collection.count()} documents")
```

```python
# Let's investigate the vectors

collection = vectorstore._collection
count = collection.count()

sample_embedding = collection.get(limit=1, include=["embeddings"])["embeddings"][0]
dimensions = len(sample_embedding)
print(f"There are {count:,} vectors with {dimensions:,} dimensions in the vector store")
```

### Part C: Visualize!

```python
# Prework

result = collection.get(include=['embeddings', 'documents', 'metadatas'])
vectors = np.array(result['embeddings'])
documents = result['documents']
metadatas = result['metadatas']
doc_types = [metadata['doc_type'] for metadata in metadatas]
colors = [['blue', 'green', 'red', 'orange'][['products', 'employees', 'contracts', 'company'].index(t)] for t in doc_types]
```

```python
# We humans find it easier to visalize things in 2D!
# Reduce the dimensionality of the vectors to 2D using t-SNE
# (t-distributed stochastic neighbor embedding)

tsne = TSNE(n_components=2, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)

# Create the 2D scatter plot
fig = go.Figure(data=[go.Scatter(
    x=reduced_vectors[:, 0],
    y=reduced_vectors[:, 1],
    mode='markers',
    marker=dict(size=5, color=colors, opacity=0.8),
    text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
    hoverinfo='text'
)])

fig.update_layout(title='2D Chroma Vector Store Visualization',
    scene=dict(xaxis_title='x',yaxis_title='y'),
    width=800,
    height=600,
    margin=dict(r=20, b=10, l=10, t=40)
)

fig.show()
```

```python
# Let's try 3D!

tsne = TSNE(n_components=3, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)

# Create the 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=reduced_vectors[:, 0],
    y=reduced_vectors[:, 1],
    z=reduced_vectors[:, 2],
    mode='markers',
    marker=dict(size=5, color=colors, opacity=0.8),
    text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
    hoverinfo='text'
)])

fig.update_layout(
    title='3D Chroma Vector Store Visualization',
    scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
    width=900,
    height=700,
    margin=dict(r=10, b=10, l=10, t=40)
)

fig.show()
```


---

<a id="file-week5-day3-ipynb"></a>
## File: `week5/day3.ipynb`

> **Path in repository:** `week5/day3.ipynb`

## RAG Day 3

### Expert Question Answerer for InsureLLM

LangChain 1.0 implementation of a RAG pipeline.

Using the VectorStore we created last time (with HuggingFace `all-MiniLM-L6-v2`)

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_chroma import Chroma
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_huggingface import HuggingFaceEmbeddings
import gradio as gr
```

```python
MODEL = "gpt-6-luna"
DB_NAME = "vector_db"
load_dotenv(override=True)
```

### Connect to Chroma; use Hugging Face all-MiniLM-L6-v2

```python
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory=DB_NAME, embedding_function=embeddings)
```

### Set up the 2 key LangChain objects: retriever and llm

#### A sidebar on "temperature":
- Controls how diverse the output is
- A temperature of 0 means that the output should be predictable
- Higher temperature for more variety in answers

Some people describe temperature as being like 'creativity' but that's not quite right
- It actually controls which tokens get selected during inference
- temperature=0 means: always select the token with highest probability
- temperature=1 usually means: a token with 10% probability should be picked 10% of the time

Note: a temperature of 0 doesn't mean outputs will always be reproducible. You also need to set a random seed. We will do that in weeks 6-8. (Even then, it's not always reproducible.)

Note 2: if you want creativity, use the System Prompt!

```python
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(temperature=0, model_name=MODEL, reasoning_effort="none")
```

### These LangChain objects implement the method `invoke()`

```python
retriever.invoke("Who is Avery?")
```

```python
llm.invoke("Who is Avery?")
```

## Time to put this together!

```python
SYSTEM_PROMPT_TEMPLATE = """
You are a knowledgeable, friendly assistant representing the company Insurellm.
You are chatting with a user about Insurellm.
If relevant, use the given context to answer any question.
If you don't know the answer, say so.
Context:
{context}
"""
```

```python
def answer_question(question: str, history):
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context)
    response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=question)])
    return response.content
```

```python
answer_question("Who is Averi Lancaster?", [])
```

## What could possibly come next? 😂

```python
gr.ChatInterface(answer_question).launch()
```

## Admit it - you thought RAG would be more complicated than that!!


---

<a id="file-week5-day4-ipynb"></a>
## File: `week5/day4.ipynb`

> **Path in repository:** `week5/day4.ipynb`

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


---

<a id="file-week5-day5-ipynb"></a>
## File: `week5/day5.ipynb`

> **Path in repository:** `week5/day5.ipynb`

# Let's go PRO!

Advanced RAG Techniques!

Let's start by digging into ingest:

1. No LangChain! Just native for maximum flexibility
2. Let's use an LLM to divide up chunks in a sensible way
3. Let's use the best chunk size and encoder from yesterday
4. Let's also have the LLM rewrite chunks in a way that's most useful ("document pre-processing")

```python
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from chromadb import PersistentClient
from tqdm import tqdm
from litellm import completion
import numpy as np
from sklearn.manifold import TSNE
import plotly.graph_objects as go


load_dotenv(override=True)

MODEL = "openai/gpt-6-luna"

DB_NAME = "preprocessed_db"
collection_name = "docs"
embedding_model = "text-embedding-3-large"
KNOWLEDGE_BASE_PATH = Path("knowledge-base")
AVERAGE_CHUNK_SIZE = 500

openai = OpenAI()
```

```python
# Inspired by LangChain's Document - let's have something similar

class Result(BaseModel):
    page_content: str
    metadata: dict
```

```python
# A class to perfectly represent a chunk

class Chunk(BaseModel):
    headline: str = Field(description="A brief heading for this chunk, typically a few words, that is most likely to be surfaced in a query")
    summary: str = Field(description="A few sentences summarizing the content of this chunk to answer common questions")
    original_text: str = Field(description="The original text of this chunk from the provided document, exactly as is, not changed in any way")

    def as_result(self, document):
        metadata = {"source": document["source"], "type": document["type"]}
        return Result(page_content=self.headline + "\n\n" + self.summary + "\n\n" + self.original_text,metadata=metadata)


class Chunks(BaseModel):
    chunks: list[Chunk]
```

## Three steps:

1. Fetch documents from the knowledge base, like LangChain did
2. Call an LLM to turn documents into Chunks
3. Store the Chunks in Chroma

That's it!

### Let's start with Step 1

```python
def fetch_documents():
    """A homemade version of the LangChain DirectoryLoader"""

    documents = []

    for folder in KNOWLEDGE_BASE_PATH.iterdir():
        doc_type = folder.name
        for file in folder.rglob("*.md"):
            with open(file, "r", encoding="utf-8") as f:
                documents.append({"type": doc_type, "source": file.as_posix(), "text": f.read()})

    print(f"Loaded {len(documents)} documents")
    return documents
```

```python
documents = fetch_documents()
```

### Donezo! On to Step 2 - make the chunks

```python
def make_prompt(document):
    how_many = (len(document["text"]) // AVERAGE_CHUNK_SIZE) + 1
    return f"""
You take a document and you split the document into overlapping chunks for a KnowledgeBase.

The document is from the shared drive of a company called Insurellm.
The document is of type: {document["type"]}
The document has been retrieved from: {document["source"]}

A chatbot will use these chunks to answer questions about the company.
You should divide up the document as you see fit, being sure that the entire document is returned in the chunks - don't leave anything out.
This document should probably be split into {how_many} chunks, but you can have more or less as appropriate.
There should be overlap between the chunks as appropriate; typically about 25% overlap or about 50 words, so you have the same text in multiple chunks for best retrieval results.

For each chunk, you should provide a headline, a summary, and the original text of the chunk.
Together your chunks should represent the entire document with overlap.

Here is the document:

{document["text"]}

Respond with the chunks.
"""
```

```python
print(make_prompt(documents[0]))
```

```python
def make_messages(document):
    return [
        {"role": "user", "content": make_prompt(document)},
    ]
```

```python
make_messages(documents[0])
```

```python
def process_document(document):
    messages = make_messages(document)
    response = completion(model=MODEL, extra_body={"reasoning_effort": "none"}, messages=messages, response_format=Chunks)
    reply = response.choices[0].message.content
    doc_as_chunks = Chunks.model_validate_json(reply).chunks
    return [chunk.as_result(document) for chunk in doc_as_chunks]
```

```python
process_document(documents[0])
```

```python
def create_chunks(documents):
    chunks = []
    for doc in tqdm(documents):
        chunks.extend(process_document(doc))
    return chunks
```

```python
chunks = create_chunks(documents)
```

```python
print(len(chunks))
```

### Well that was easy! If a bit slow.

In the python module version, I sneakily use the multi-processing Pool to run this in parallel,
but if you get a Rate Limit Error you can turn this off in the code.

### Finally, Step 3 - save the embeddings

```python
def create_embeddings(chunks):
    chroma = PersistentClient(path=DB_NAME)
    if collection_name in [c.name for c in chroma.list_collections()]:
        chroma.delete_collection(collection_name)

    texts = [chunk.page_content for chunk in chunks]
    emb = openai.embeddings.create(model=embedding_model, input=texts).data
    vectors = [e.embedding for e in emb]

    collection = chroma.get_or_create_collection(collection_name)

    ids = [str(i) for i in range(len(chunks))]
    metas = [chunk.metadata for chunk in chunks]

    collection.add(ids=ids, embeddings=vectors, documents=texts, metadatas=metas)
    print(f"Vectorstore created with {collection.count()} documents")
```

```python
create_embeddings(chunks)
```

# Nothing more to do here... right?

Wait! Didja think I'd forget??

```python
chroma = PersistentClient(path=DB_NAME)
collection = chroma.get_or_create_collection(collection_name)
result = collection.get(include=['embeddings', 'documents', 'metadatas'])
vectors = np.array(result['embeddings'])
documents = result['documents']
metadatas = result['metadatas']
doc_types = [metadata['type'] for metadata in metadatas]
colors = [['blue', 'green', 'red', 'orange'][['products', 'employees', 'contracts', 'company'].index(t)] for t in doc_types]
```

```python
tsne = TSNE(n_components=2, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)

# Create the 2D scatter plot
fig = go.Figure(data=[go.Scatter(
    x=reduced_vectors[:, 0],
    y=reduced_vectors[:, 1],
    mode='markers',
    marker=dict(size=5, color=colors, opacity=0.8),
    text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
    hoverinfo='text'
)])

fig.update_layout(title='2D Chroma Vector Store Visualization',
    scene=dict(xaxis_title='x',yaxis_title='y'),
    width=800,
    height=600,
    margin=dict(r=20, b=10, l=10, t=40)
)

fig.show()
```

```python
tsne = TSNE(n_components=3, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)

# Create the 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=reduced_vectors[:, 0],
    y=reduced_vectors[:, 1],
    z=reduced_vectors[:, 2],
    mode='markers',
    marker=dict(size=5, color=colors, opacity=0.8),
    text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
    hoverinfo='text'
)])

fig.update_layout(
    title='3D Chroma Vector Store Visualization',
    scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
    width=900,
    height=700,
    margin=dict(r=10, b=10, l=10, t=40)
)

fig.show()
```

## And now - let's build an Advanced RAG!

We will use these techniques:

1. Reranking - reorder the rank results
2. Query re-writing

```python
class RankOrder(BaseModel):
    order: list[int] = Field(
        description="The order of relevance of chunks, from most relevant to least relevant, by chunk id number"
    )
```

```python
def rerank(question, chunks):
    system_prompt = """
You are a document re-ranker.
You are provided with a question and a list of relevant chunks of text from a query of a knowledge base.
The chunks are provided in the order they were retrieved; this should be approximately ordered by relevance, but you may be able to improve on that.
You must rank order the provided chunks by relevance to the question, with the most relevant chunk first.
Reply only with the list of ranked chunk ids, nothing else. Include all the chunk ids you are provided with, reranked.
"""
    user_prompt = f"The user has asked the following question:\n\n{question}\n\nOrder all the chunks of text by relevance to the question, from most relevant to least relevant. Include all the chunk ids you are provided with, reranked.\n\n"
    user_prompt += "Here are the chunks:\n\n"
    for index, chunk in enumerate(chunks):
        user_prompt += f"# CHUNK ID: {index + 1}:\n\n{chunk.page_content}\n\n"
    user_prompt += "Reply only with the list of ranked chunk ids, nothing else."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = completion(model=MODEL, extra_body={"reasoning_effort": "none"}, messages=messages, response_format=RankOrder)
    reply = response.choices[0].message.content
    order = RankOrder.model_validate_json(reply).order
    print(order)
    return [chunks[i - 1] for i in order]
```

```python
RETRIEVAL_K = 10

def fetch_context_unranked(question):
    query = openai.embeddings.create(model=embedding_model, input=[question]).data[0].embedding
    results = collection.query(query_embeddings=[query], n_results=RETRIEVAL_K)
    chunks = []
    for result in zip(results["documents"][0], results["metadatas"][0]):
        chunks.append(Result(page_content=result[0], metadata=result[1]))
    return chunks
```

```python
question = "Who won the IIOTY award?"
chunks = fetch_context_unranked(question)
```

```python
for chunk in chunks:
    print(chunk.page_content[:15]+"...")
```

```python
reranked = rerank(question, chunks)
```

```python
for chunk in reranked:
    print(chunk.page_content[:15]+"...")
```

```python
question = "Who went to Manchester University?"
RETRIEVAL_K = 20
chunks = fetch_context_unranked(question)
for index, c in enumerate(chunks):
    if "manchester" in c.page_content.lower():
        print(index)
```

```python
reranked = rerank(question, chunks)
```

```python
for index, c in enumerate(reranked):
    if "manchester" in c.page_content.lower():
        print(index)
```

```python
reranked[0].page_content
```

```python
def fetch_context(question):
    chunks = fetch_context_unranked(question)
    return rerank(question, chunks)
```

```python
SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing the company Insurellm.
You are chatting with a user about Insurellm.
Your answer will be evaluated for accuracy, relevance and completeness, so make sure it only answers the question and fully answers it.
If you don't know the answer, say so.
For context, here are specific extracts from the Knowledge Base that might be directly relevant to the user's question:
{context}

With this context, please answer the user's question. Be accurate, relevant and complete.
"""
```

```python
# In the context, include the source of the chunk

def make_rag_messages(question, history, chunks):
    context = "\n\n".join(f"Extract from {chunk.metadata['source']}:\n{chunk.page_content}" for chunk in chunks)
    system_prompt = SYSTEM_PROMPT.format(context=context)
    return [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": question}]
```

```python
def rewrite_query(question, history=[]):
    """Rewrite the user's question to be a more specific question that is more likely to surface relevant content in the Knowledge Base."""
    message = f"""
You are in a conversation with a user, answering questions about the company Insurellm.
You are about to look up information in a Knowledge Base to answer the user's question.

This is the history of your conversation so far with the user:
{history}

And this is the user's current question:
{question}

Respond only with a single, refined question that you will use to search the Knowledge Base.
It should be a VERY short specific question most likely to surface content. Focus on the question details.
Don't mention the company name unless it's a general question about the company.
IMPORTANT: Respond ONLY with the knowledgebase query, nothing else.
"""
    response = completion(model=MODEL, extra_body={"reasoning_effort": "none"}, messages=[{"role": "system", "content": message}])
    return response.choices[0].message.content
```

```python
rewrite_query("Who won the IIOTY award?", [])
```

```python
def answer_question(question: str, history: list[dict] = []) -> tuple[str, list]:
    """
    Answer a question using RAG and return the answer and the retrieved context
    """
    query = rewrite_query(question, history)
    print(query)
    chunks = fetch_context(query)
    messages = make_rag_messages(question, history, chunks)
    response = completion(model=MODEL, extra_body={"reasoning_effort": "none"}, messages=messages)
    return response.choices[0].message.content, chunks
```

```python
answer_question("Who won the IIOTY award?", [])
```

```python
answer_question("Who went to Manchester University?", [])
```


---

<a id="file-week5-evaluation-eval-py"></a>
## File: `week5/evaluation/eval.py`

> **Path in repository:** `week5/evaluation/eval.py`

```python
import sys
import math
from pydantic import BaseModel, Field
from litellm import completion
from dotenv import load_dotenv

from evaluation.test import TestQuestion, load_tests
from implementation.answer import answer_question, fetch_context


load_dotenv(override=True)

MODEL = "openai/gpt-6-luna"
db_name = "vector_db"


class RetrievalEval(BaseModel):
    """Evaluation metrics for retrieval performance."""

    mrr: float = Field(description="Mean Reciprocal Rank - average across all keywords")
    ndcg: float = Field(description="Normalized Discounted Cumulative Gain (binary relevance)")
    keywords_found: int = Field(description="Number of keywords found in top-k results")
    total_keywords: int = Field(description="Total number of keywords to find")
    keyword_coverage: float = Field(description="Percentage of keywords found")


class AnswerEval(BaseModel):
    """LLM-as-a-judge evaluation of answer quality."""

    feedback: str = Field(
        description="Concise feedback on the answer quality, comparing it to the reference answer and evaluating based on the retrieved context"
    )
    accuracy: float = Field(
        description="How factually correct is the answer compared to the reference answer? 1 (wrong. any wrong answer must score 1) to 5 (ideal - perfectly accurate). An acceptable answer would score 3."
    )
    completeness: float = Field(
        description="How complete is the answer in addressing all aspects of the question? 1 (very poor - missing key information) to 5 (ideal - all the information from the reference answer is provided completely). Only answer 5 if ALL information from the reference answer is included."
    )
    relevance: float = Field(
        description="How relevant is the answer to the specific question asked? 1 (very poor - off-topic) to 5 (ideal - directly addresses question and gives no additional information). Only answer 5 if the answer is completely relevant to the question and gives no additional information."
    )


def calculate_mrr(keyword: str, retrieved_docs: list) -> float:
    """Calculate reciprocal rank for a single keyword (case-insensitive)."""
    keyword_lower = keyword.lower()
    for rank, doc in enumerate(retrieved_docs, start=1):
        if keyword_lower in doc.page_content.lower():
            return 1.0 / rank
    return 0.0


def calculate_dcg(relevances: list[int], k: int) -> float:
    """Calculate Discounted Cumulative Gain."""
    dcg = 0.0
    for i in range(min(k, len(relevances))):
        dcg += relevances[i] / math.log2(i + 2)  # i+2 because rank starts at 1
    return dcg


def calculate_ndcg(keyword: str, retrieved_docs: list, k: int = 10) -> float:
    """Calculate nDCG for a single keyword (binary relevance, case-insensitive)."""
    keyword_lower = keyword.lower()

    # Binary relevance: 1 if keyword found, 0 otherwise
    relevances = [
        1 if keyword_lower in doc.page_content.lower() else 0 for doc in retrieved_docs[:k]
    ]

    # DCG
    dcg = calculate_dcg(relevances, k)

    # Ideal DCG (best case: keyword in first position)
    ideal_relevances = sorted(relevances, reverse=True)
    idcg = calculate_dcg(ideal_relevances, k)

    return dcg / idcg if idcg > 0 else 0.0


def evaluate_retrieval(test: TestQuestion, k: int = 10) -> RetrievalEval:
    """
    Evaluate retrieval performance for a test question.

    Args:
        test: TestQuestion object containing question and keywords
        k: Number of top documents to retrieve (default 10)

    Returns:
        RetrievalEval object with MRR, nDCG, and keyword coverage metrics
    """
    # Retrieve documents using shared answer module
    retrieved_docs = fetch_context(test.question)

    # Calculate MRR (average across all keywords)
    mrr_scores = [calculate_mrr(keyword, retrieved_docs) for keyword in test.keywords]
    avg_mrr = sum(mrr_scores) / len(mrr_scores) if mrr_scores else 0.0

    # Calculate nDCG (average across all keywords)
    ndcg_scores = [calculate_ndcg(keyword, retrieved_docs, k) for keyword in test.keywords]
    avg_ndcg = sum(ndcg_scores) / len(ndcg_scores) if ndcg_scores else 0.0

    # Calculate keyword coverage
    keywords_found = sum(1 for score in mrr_scores if score > 0)
    total_keywords = len(test.keywords)
    keyword_coverage = (keywords_found / total_keywords * 100) if total_keywords > 0 else 0.0

    return RetrievalEval(
        mrr=avg_mrr,
        ndcg=avg_ndcg,
        keywords_found=keywords_found,
        total_keywords=total_keywords,
        keyword_coverage=keyword_coverage,
    )


def evaluate_answer(test: TestQuestion) -> tuple[AnswerEval, str, list]:
    """
    Evaluate answer quality using LLM-as-a-judge (async).

    Args:
        test: TestQuestion object containing question and reference answer

    Returns:
        Tuple of (AnswerEval object, generated_answer string, retrieved_docs list)
    """
    # Get RAG response using shared answer module
    generated_answer, retrieved_docs = answer_question(test.question)

    # LLM judge prompt
    judge_messages = [
        {
            "role": "system",
            "content": "You are an expert evaluator assessing the quality of answers. Evaluate the generated answer by comparing it to the reference answer. Only give 5/5 scores for perfect answers.",
        },
        {
            "role": "user",
            "content": f"""Question:
{test.question}

Generated Answer:
{generated_answer}

Reference Answer:
{test.reference_answer}

Please evaluate the generated answer on three dimensions:
1. Accuracy: How factually correct is it compared to the reference answer? Only give 5/5 scores for perfect answers.
2. Completeness: How thoroughly does it address all aspects of the question, covering all the information from the reference answer?
3. Relevance: How well does it directly answer the specific question asked, giving no additional information?

Provide detailed feedback and scores from 1 (very poor) to 5 (ideal) for each dimension. If the answer is wrong, then the accuracy score must be 1.""",
        },
    ]

    # Call LLM judge with structured outputs (async)
    judge_response = completion(model=MODEL, extra_body={"reasoning_effort": "none"}, messages=judge_messages, response_format=AnswerEval)

    answer_eval = AnswerEval.model_validate_json(judge_response.choices[0].message.content)

    return answer_eval, generated_answer, retrieved_docs


def evaluate_all_retrieval():
    """Evaluate all retrieval tests."""
    tests = load_tests()
    total_tests = len(tests)
    for index, test in enumerate(tests):
        result = evaluate_retrieval(test)
        progress = (index + 1) / total_tests
        yield test, result, progress


def evaluate_all_answers():
    """Evaluate all answers to tests using batched async execution."""
    tests = load_tests()
    total_tests = len(tests)
    for index, test in enumerate(tests):
        result = evaluate_answer(test)[0]
        progress = (index + 1) / total_tests
        yield test, result, progress


def run_cli_evaluation(test_number: int):
    """Run evaluation for a specific test (async helper for CLI)."""
    # Load tests
    tests = load_tests("tests.jsonl")

    if test_number < 0 or test_number >= len(tests):
        print(f"Error: test_row_number must be between 0 and {len(tests) - 1}")
        sys.exit(1)

    # Get the test
    test = tests[test_number]

    # Print test info
    print(f"\n{'=' * 80}")
    print(f"Test #{test_number}")
    print(f"{'=' * 80}")
    print(f"Question: {test.question}")
    print(f"Keywords: {test.keywords}")
    print(f"Category: {test.category}")
    print(f"Reference Answer: {test.reference_answer}")

    # Retrieval Evaluation
    print(f"\n{'=' * 80}")
    print("Retrieval Evaluation")
    print(f"{'=' * 80}")

    retrieval_result = evaluate_retrieval(test)

    print(f"MRR: {retrieval_result.mrr:.4f}")
    print(f"nDCG: {retrieval_result.ndcg:.4f}")
    print(f"Keywords Found: {retrieval_result.keywords_found}/{retrieval_result.total_keywords}")
    print(f"Keyword Coverage: {retrieval_result.keyword_coverage:.1f}%")

    # Answer Evaluation
    print(f"\n{'=' * 80}")
    print("Answer Evaluation")
    print(f"{'=' * 80}")

    answer_result, generated_answer, retrieved_docs = evaluate_answer(test)

    print(f"\nGenerated Answer:\n{generated_answer}")
    print(f"\nFeedback:\n{answer_result.feedback}")
    print("\nScores:")
    print(f"  Accuracy: {answer_result.accuracy:.2f}/5")
    print(f"  Completeness: {answer_result.completeness:.2f}/5")
    print(f"  Relevance: {answer_result.relevance:.2f}/5")
    print(f"\n{'=' * 80}\n")


def main():
    """CLI to evaluate a specific test by row number."""
    if len(sys.argv) != 2:
        print("Usage: uv run eval.py <test_row_number>")
        sys.exit(1)

    try:
        test_number = int(sys.argv[1])
    except ValueError:
        print("Error: test_row_number must be an integer")
        sys.exit(1)

    run_cli_evaluation(test_number)


if __name__ == "__main__":
    main()
```


---

<a id="file-week5-evaluation-test-py"></a>
## File: `week5/evaluation/test.py`

> **Path in repository:** `week5/evaluation/test.py`

```python
import json
from pathlib import Path
from pydantic import BaseModel, Field

TEST_FILE = str(Path(__file__).parent / "tests.jsonl")


class TestQuestion(BaseModel):
    """A test question with expected keywords and reference answer."""

    question: str = Field(description="The question to ask the RAG system")
    keywords: list[str] = Field(description="Keywords that must appear in retrieved context")
    reference_answer: str = Field(description="The reference answer for this question")
    category: str = Field(description="Question category (e.g., direct_fact, spanning, temporal)")


def load_tests() -> list[TestQuestion]:
    """Load test questions from JSONL file."""
    tests = []
    with open(TEST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            tests.append(TestQuestion(**data))
    return tests
```


---

<a id="file-week5-evaluation-tests-jsonl"></a>
## File: `week5/evaluation/tests.jsonl`

> **Path in repository:** `week5/evaluation/tests.jsonl`

```json
{"question": "Who won the prestigious IIOTY award in 2023?", "keywords": ["Maxine", "Thompson", "IIOTY"], "reference_answer": "Maxine Thompson won the prestigious Insurellm Innovator of the Year (IIOTY) award in 2023.", "category": "direct_fact"}
{"question": "When was Insurellm founded?", "keywords": ["2015", "founded"], "reference_answer": "Insurellm was founded in 2015.", "category": "direct_fact"}
{"question": "Who founded Insurellm?", "keywords": ["Avery", "Lancaster"], "reference_answer": "Avery Lancaster founded Insurellm in 2015.", "category": "direct_fact"}
{"question": "How many employees does Insurellm currently have?", "keywords": ["32", "employees"], "reference_answer": "Insurellm currently operates with 32 employees as of 2025.", "category": "direct_fact"}
{"question": "What was Insurellm's first product?", "keywords": ["Markellm", "first"], "reference_answer": "Insurellm's first product was Markellm, the marketplace connecting consumers with insurance providers.", "category": "direct_fact"}
{"question": "How many active contracts does Insurellm manage?", "keywords": ["32", "contracts"], "reference_answer": "Insurellm manages 32 active contracts spanning all eight product lines.", "category": "direct_fact"}
{"question": "Where is Insurellm's headquarters located?", "keywords": ["San Francisco", "headquarters"], "reference_answer": "Insurellm's headquarters is located in San Francisco.", "category": "direct_fact"}
{"question": "How many office locations does Insurellm maintain?", "keywords": ["offices in", "5"], "reference_answer": "Insurellm maintains 5 office locations: San Francisco, New York, Austin, Chicago, and Denver.", "category": "direct_fact"}
{"question": "What is Insurellm's vision statement?", "keywords": ["revolutionize", "insurance", "technology"], "reference_answer": "Insurellm's vision is to revolutionize the insurance industry through innovative technology that makes insurance accessible, transparent, and effortless.", "category": "direct_fact"}
{"question": "How many Bizllm contracts has Insurellm secured?", "keywords": ["7", "Bizllm"], "reference_answer": "Insurellm has secured 7 commercial insurance contracts for Bizllm.", "category": "direct_fact"}
{"question": "How many Claimllm contracts does Insurellm have?", "keywords": ["7", "Claimllm"], "reference_answer": "Insurellm has 7 contracts for Claimllm, ranging from independent adjusting firms to enterprise claims networks.", "category": "direct_fact"}
{"question": "How many life insurance contracts has Lifellm secured?", "keywords": ["6", "Lifellm"], "reference_answer": "Lifellm has secured 6 life insurance contracts serving carriers from small regional providers to major national groups.", "category": "direct_fact"}
{"question": "How many health insurance contracts does Healthllm have?", "keywords": ["6", "Healthllm"], "reference_answer": "Healthllm has 6 health insurance contracts with plans from regional insurers to multi-state healthcare alliances.", "category": "direct_fact"}
{"question": "What is the monthly cost of Carllm's Basic Tier?", "keywords": ["$1,000", "Basic", "Carllm"], "reference_answer": "Carllm's Basic Tier costs $1,000 per month.", "category": "direct_fact"}
{"question": "What is the monthly cost of Carllm's Enterprise Tier?", "keywords": ["$5,000", "Enterprise", "Carllm"], "reference_answer": "Carllm's Enterprise Tier costs $5,000 per month.", "category": "direct_fact"}
{"question": "What is the monthly cost of Homellm's Standard Tier?", "keywords": ["$10,000", "Standard", "Homellm"], "reference_answer": "Homellm's Standard Tier costs $10,000 per month for medium-sized insurers.", "category": "direct_fact"}
{"question": "What is the monthly cost of Bizllm's Professional Tier?", "keywords": ["$12,000", "Professional", "Bizllm"], "reference_answer": "Bizllm's Professional Tier costs $12,000 per month for multi-line carriers.", "category": "direct_fact"}
{"question": "What is the monthly cost of Claimllm's Core Tier?", "keywords": ["$4,500", "Core", "Claimllm"], "reference_answer": "Claimllm's Core Tier costs $4,500 per month for smaller insurers processing up to 5,000 claims annually.", "category": "direct_fact"}
{"question": "What is the monthly cost of Healthllm's Essential Tier?", "keywords": ["$8,000", "Essential", "Healthllm"], "reference_answer": "Healthllm's Essential Tier costs $8,000 per month for regional health plans.", "category": "direct_fact"}
{"question": "What is the monthly cost of Lifellm's Starter Tier?", "keywords": ["$3,500", "Starter", "Lifellm"], "reference_answer": "Lifellm's Starter Tier costs $3,500 per month for small insurers.", "category": "direct_fact"}
{"question": "What is the monthly cost of Rellm's Basic Plan?", "keywords": ["$5,000", "Basic", "Rellm"], "reference_answer": "Rellm's Basic Plan costs $5,000 per month.", "category": "direct_fact"}
{"question": "What is Maxine Thompson's current job title?", "keywords": ["Senior Data Engineer", "Maxine"], "reference_answer": "Maxine Thompson's current job title is Senior Data Engineer.", "category": "direct_fact"}
{"question": "What is Maxine Thompson's current salary?", "keywords": ["$120,000", "Maxine"], "reference_answer": "Maxine Thompson's current salary is $120,000.", "category": "direct_fact"}
{"question": "Where is Maxine Thompson located?", "keywords": ["Austin", "Texas", "Maxine"], "reference_answer": "Maxine Thompson is located in Austin, Texas.", "category": "direct_fact"}
{"question": "What is Avery Lancaster's job title?", "keywords": ["CEO", "Avery", "Lancaster"], "reference_answer": "Avery Lancaster is the Co-Founder and Chief Executive Officer (CEO) of Insurellm.", "category": "direct_fact"}
{"question": "What is Avery Lancaster's current salary?", "keywords": ["$225,000", "Avery"], "reference_answer": "Avery Lancaster's current salary is $225,000.", "category": "direct_fact"}
{"question": "What is James Wilson's job title?", "keywords": ["CTO", "James", "Wilson"], "reference_answer": "James Wilson is the Chief Technology Officer (CTO) of Insurellm.", "category": "direct_fact"}
{"question": "What is James Wilson's current salary?", "keywords": ["$285,000", "James", "Wilson"], "reference_answer": "James Wilson's current salary is $285,000.", "category": "direct_fact"}
{"question": "What is Priya Sharma's job title?", "keywords": ["Senior Data Scientist", "Priya"], "reference_answer": "Priya Sharma is a Senior Data Scientist at Insurellm.", "category": "direct_fact"}
{"question": "What is Priya Sharma's current salary?", "keywords": ["$145,000", "Priya"], "reference_answer": "Priya Sharma's current salary is $145,000.", "category": "direct_fact"}
{"question": "What is Robert Chen's job title?", "keywords": ["Senior Full Stack Engineer", "Robert"], "reference_answer": "Robert Chen is a Senior Full Stack Engineer at Insurellm.", "category": "direct_fact"}
{"question": "What is Robert Chen's current salary?", "keywords": ["$152,000", "Robert"], "reference_answer": "Robert Chen's current salary is $152,000.", "category": "direct_fact"}
{"question": "Which product does Robert Chen serve as technical lead for?", "keywords": ["Homellm", "Robert", "Chen"], "reference_answer": "Robert Chen is the technical lead for Homellm home insurance portal.", "category": "direct_fact"}
{"question": "What is David Kim's job title?", "keywords": ["DevOps Engineer", "David", "Kim"], "reference_answer": "David Kim is a DevOps Engineer at Insurellm.", "category": "direct_fact"}
{"question": "What is Sarah Williams's job title?", "keywords": ["UX Designer", "Sarah"], "reference_answer": "Sarah Williams is a UX Designer at Insurellm.", "category": "direct_fact"}
{"question": "Which product does Sarah Williams lead design for?", "keywords": ["Homellm", "Sarah"], "reference_answer": "Sarah Williams leads design for the Homellm home insurance portal.", "category": "direct_fact"}
{"question": "What is Marcus Johnson's job title?", "keywords": ["Customer Success Manager", "Marcus"], "reference_answer": "Marcus Johnson is a Customer Success Manager at Insurellm.", "category": "direct_fact"}
{"question": "What is Marcus Johnson's client retention rate?", "keywords": ["95%", "retention", "Marcus"], "reference_answer": "Marcus Johnson achieved a 95% client retention rate over the past three years.", "category": "direct_fact"}
{"question": "What is Lisa Anderson's job title?", "keywords": ["Marketing Manager", "Lisa"], "reference_answer": "Lisa Anderson is a Marketing Manager at Insurellm.", "category": "direct_fact"}
{"question": "What is the size of Lisa Anderson's annual marketing budget?", "keywords": ["$2M", "Lisa"], "reference_answer": "Lisa Anderson manages a $2M annual marketing budget.", "category": "direct_fact"}
{"question": "What is Emily Carter's job title?", "keywords": ["Account Executive", "Emily"], "reference_answer": "Emily Carter is an Account Executive at Insurellm.", "category": "direct_fact"}
{"question": "What is the contract number for DriveSmart Insurance's Carllm agreement?", "keywords": ["CR-2025-E-0078", "DriveSmart"], "reference_answer": "The contract number for DriveSmart Insurance's Carllm agreement is CR-2025-E-0078.", "category": "direct_fact"}
{"question": "What is the duration of the DriveSmart Insurance Carllm contract?", "keywords": ["36 months", "DriveSmart"], "reference_answer": "The DriveSmart Insurance Carllm contract is effective for a period of 36 months.", "category": "direct_fact"}
{"question": "What is the total contract value for DriveSmart Insurance's Carllm agreement?", "keywords": ["$702,000", "DriveSmart"], "reference_answer": "The total contract value for DriveSmart Insurance's Carllm agreement is $702,000 over the 36-month term.", "category": "direct_fact"}
{"question": "How many active auto policies does DriveSmart Insurance have?", "keywords": ["85,000", "DriveSmart", "policies"], "reference_answer": "DriveSmart Insurance currently has 85,000 active auto policies across 8 states.", "category": "direct_fact"}
{"question": "What is the uptime SLA guarantee for DriveSmart Insurance?", "keywords": ["99.9%", "uptime", "DriveSmart"], "reference_answer": "Insurellm guarantees 99.9% platform uptime measured monthly for DriveSmart Insurance.", "category": "direct_fact"}
{"question": "Who signed the DriveSmart Insurance contract on behalf of Insurellm?", "keywords": ["Jennifer Rodriguez", "DriveSmart"], "reference_answer": "Jennifer Rodriguez, CEO of Insurellm, signed the DriveSmart Insurance contract.", "category": "direct_fact"}
{"question": "What is the monthly payment for Greenstone Insurance's Homellm contract?", "keywords": ["$10,000", "Greenstone"], "reference_answer": "Greenstone Insurance pays $10,000 per month for the Standard Tier of the Homellm service.", "category": "direct_fact"}
{"question": "What tier did Harmony Health Plans subscribe to for Healthllm?", "keywords": ["Professional", "Harmony"], "reference_answer": "Harmony Health Plans subscribed to the Professional Tier of Healthllm.", "category": "direct_fact"}
{"question": "What is the monthly cost for Harmony Health Plans' Healthllm subscription?", "keywords": ["$15,000", "Harmony"], "reference_answer": "Harmony Health Plans pays $15,000 per month for the Professional Tier of Healthllm.", "category": "direct_fact"}
{"question": "How many covered members does Harmony Health Plans have?", "keywords": ["38,000", "Harmony"], "reference_answer": "Harmony Health Plans currently covers 38,000 members across 3 states.", "category": "direct_fact"}
{"question": "Who signed the Harmony Health Plans contract on behalf of Insurellm?", "keywords": ["Sarah Chen", "Harmony"], "reference_answer": "Sarah Chen, Vice President of Sales at Insurellm, signed the Harmony Health Plans contract.", "category": "direct_fact"}
{"question": "What is the contract number for Metropolitan Life Group's Lifellm agreement?", "keywords": ["LF-2025-E-0087", "Metropolitan"], "reference_answer": "The contract number for Metropolitan Life Group's Lifellm agreement is LF-2025-E-0087.", "category": "direct_fact"}
{"question": "What is the total contract value for Metropolitan Life Group's Lifellm agreement?", "keywords": ["$1,098,000", "Metropolitan"], "reference_answer": "The total contract value for Metropolitan Life Group's Lifellm agreement is $1,098,000 over the 36-month term.", "category": "direct_fact"}
{"question": "How many active policies does Metropolitan Life Group manage?", "keywords": ["50,000", "Metropolitan"], "reference_answer": "Metropolitan Life Group manages 50,000+ active policies.", "category": "direct_fact"}
{"question": "Who signed the Metropolitan Life Group contract on behalf of the client?", "keywords": ["Richard Thompson", "Metropolitan"], "reference_answer": "Richard Thompson, Chairman & Chief Executive Officer, signed the contract on behalf of Metropolitan Life Group.", "category": "direct_fact"}
{"question": "What tier did FastTrack Insurance Services subscribe to for Claimllm?", "keywords": ["Advanced", "FastTrack"], "reference_answer": "FastTrack Insurance Services subscribed to the Advanced Tier of Claimllm.", "category": "direct_fact"}
{"question": "What is the monthly payment for FastTrack Insurance Services' Claimllm contract?", "keywords": ["$9,500", "FastTrack"], "reference_answer": "FastTrack Insurance Services pays $9,500 per month for Claimllm Advanced Tier.", "category": "direct_fact"}
{"question": "What is the duration of the FastTrack Insurance Services contract?", "keywords": ["18 months", "FastTrack"], "reference_answer": "The FastTrack Insurance Services contract has a duration of 18 months.", "category": "direct_fact"}
{"question": "Who signed the FastTrack Insurance Services contract on behalf of Insurellm?", "keywords": ["Sarah Chen", "FastTrack"], "reference_answer": "Sarah Chen, VP of Sales, signed the FastTrack Insurance Services contract on behalf of Insurellm.", "category": "direct_fact"}
{"question": "What tier did Atlantic Risk Solutions subscribe to for Bizllm?", "keywords": ["Professional", "Atlantic"], "reference_answer": "Atlantic Risk Solutions subscribed to the Professional Tier of Bizllm.", "category": "direct_fact"}
{"question": "What is the monthly cost for Atlantic Risk Solutions' Bizllm subscription?", "keywords": ["$12,000", "Atlantic"], "reference_answer": "Atlantic Risk Solutions pays $12,000 per month for Bizllm Professional Tier.", "category": "direct_fact"}
{"question": "How many user licenses are included in Atlantic Risk Solutions' contract?", "keywords": ["35", "Atlantic"], "reference_answer": "Atlantic Risk Solutions' contract includes 35 named user licenses.", "category": "direct_fact"}
{"question": "Who signed the Atlantic Risk Solutions contract on behalf of Insurellm?", "keywords": ["Michael Torres", "Atlantic"], "reference_answer": "Michael Torres, Chief Revenue Officer, signed the Atlantic Risk Solutions contract on behalf of Insurellm.", "category": "direct_fact"}
{"question": "What is the monthly fee for Belvedere Insurance's Markellm listing?", "keywords": ["$199", "Belvedere"], "reference_answer": "Belvedere Insurance pays a Basic Listing Fee of $199 per month for accessing the Markellm platform.", "category": "direct_fact"}
{"question": "When did Maxine Thompson join Insurellm?", "keywords": ["January 2017", "Maxine"], "reference_answer": "Maxine Thompson joined Insurellm in January 2017 as a Junior Data Engineer.", "category": "temporal"}
{"question": "When did James Wilson join Insurellm?", "keywords": ["January 2017", "James", "Wilson"], "reference_answer": "James Wilson joined Insurellm as Chief Technology Officer in January 2017.", "category": "temporal"}
{"question": "When did Insurellm reach its peak of 200 employees?", "keywords": ["2020", "200"], "reference_answer": "Insurellm reached a peak of 200 employees in 2020.", "category": "temporal"}
{"question": "When did Insurellm undergo strategic restructuring?", "keywords": ["2022-2023", "restructuring"], "reference_answer": "Insurellm underwent strategic restructuring in 2022-2023 to focus on profitability and sustainable growth.", "category": "temporal"}
{"question": "When is Carllm's telematics-based pricing feature scheduled to launch?", "keywords": ["Q2 2025", "telematics"], "reference_answer": "Carllm's telematics-based pricing is scheduled to launch in Q2 2025.", "category": "temporal"}
{"question": "When is Homellm version 2.0 scheduled for release?", "keywords": ["Q1 2025", "Homellm"], "reference_answer": "Homellm version 2.0 is scheduled for release in Q1 2025.", "category": "temporal"}
{"question": "When is Bizllm version 1.0 scheduled to launch?", "keywords": ["Q2 2025", "Bizllm"], "reference_answer": "Bizllm version 1.0 is scheduled to launch in Q2 2025 with core multi-line underwriting, quoting, and policy administration.", "category": "temporal"}
{"question": "When is Claimllm version 1.0 scheduled to launch?", "keywords": ["Q1 2025", "Claimllm"], "reference_answer": "Claimllm version 1.0 is scheduled to launch in Q1 2025 with core claims processing automation, FNOL capture, and basic fraud detection.", "category": "temporal"}
{"question": "When is Lifellm version 1.0 scheduled to launch?", "keywords": ["Q2 2025", "Lifellm"], "reference_answer": "Lifellm version 1.0 is scheduled to launch in Q2 2025 with core AI underwriting and policy management capabilities.", "category": "temporal"}
{"question": "When is Healthllm version 1.0 scheduled to launch?", "keywords": ["Q1 2025", "Healthllm"], "reference_answer": "Healthllm version 1.0 is scheduled to launch in Q1 2025 featuring core claims processing, eligibility verification, and member portal.", "category": "temporal"}
{"question": "When was the DriveSmart Insurance contract for Carllm signed?", "keywords": ["March 20, 2025", "DriveSmart"], "reference_answer": "The DriveSmart Insurance contract for Carllm was signed on March 20, 2025.", "category": "temporal"}
{"question": "When was the Harmony Health Plans Healthllm contract effective?", "keywords": ["January 25, 2025", "Harmony"], "reference_answer": "The Harmony Health Plans Healthllm contract became effective on January 25, 2025.", "category": "temporal"}
{"question": "When was the Metropolitan Life Group Lifellm contract signed?", "keywords": ["April 5, 2025", "Metropolitan"], "reference_answer": "The Metropolitan Life Group Lifellm contract was signed on April 5, 2025.", "category": "temporal"}
{"question": "When was the FastTrack Insurance Services Claimllm contract signed?", "keywords": ["May 10, 2025", "FastTrack"], "reference_answer": "The FastTrack Insurance Services Claimllm contract was signed on May 10, 2025.", "category": "temporal"}
{"question": "When was the Atlantic Risk Solutions Bizllm contract effective?", "keywords": ["January 15, 2025", "Atlantic"], "reference_answer": "The Atlantic Risk Solutions Bizllm contract became effective on January 15, 2025.", "category": "temporal"}
{"question": "How much did Priya Sharma's recommendation engine increase conversion by for Marketllm?", "keywords": ["28%", "Priya", "Marketllm"], "reference_answer": "Priya Sharma built a recommendation engine for Marketllm that increased conversion by 28%.", "category": "comparative"}
{"question": "By what percentage did David Kim reduce deployment time with CI/CD pipelines?", "keywords": ["60%", "David", "Kim"], "reference_answer": "David Kim implemented CI/CD pipelines that reduced deployment time by 60%.", "category": "comparative"}
{"question": "By what percentage did Sarah Williams improve user satisfaction scores?", "keywords": ["35%", "Sarah"], "reference_answer": "Sarah Williams conducted comprehensive user research that resulted in a 35% improvement in user satisfaction scores.", "category": "comparative"}
{"question": "By what percentage has Lisa Anderson increased qualified leads since 2021?", "keywords": ["65%", "Lisa"], "reference_answer": "Lisa Anderson increased qualified leads by 65% since 2021.", "category": "comparative"}
{"question": "By what percentage did Emily Carter exceed her annual sales target in 2022?", "keywords": ["30%", "Emily", "Carter"], "reference_answer": "Emily Carter exceeded her annual sales target by 30% in 2022.", "category": "comparative"}
{"question": "What is the performance-based pricing for Belvedere Insurance's Markellm contract?", "keywords": ["$25", "Belvedere"], "reference_answer": "Belvedere Insurance pays $25 per lead generated through Markellm on a performance-based pricing model.", "category": "comparative"}
{"question": "What is the monthly cost for Stellar Insurance Co.'s Rellm subscription?", "keywords": ["$10,000", "Stellar"], "reference_answer": "Stellar Insurance Co. pays $10,000 per month for the Professional Plan of Rellm.", "category": "comparative"}
{"question": "What are Insurellm's four core values?", "keywords": ["Innovation First", "Customer Obsession", "Collaborative Excellence"], "reference_answer": "Insurellm's four core values are Innovation First, Customer Obsession, Integrity & Transparency, and Collaborative Excellence.", "category": "comparative"}
{"question": "What award did Alex Harper win in 2022?", "keywords": ["SDR of the Year", "Alex", "Harper"], "reference_answer": "Alex Harper was awarded SDR of the Year in 2022 for outstanding contributions.", "category": "comparative"}
{"question": "When was the Stellar Insurance Co. Rellm contract effective?", "keywords": ["January 1, 2024", "Stellar"], "reference_answer": "The Stellar Insurance Co. Rellm contract became effective on January 1, 2024.", "category": "comparative"}
{"question": "How many claims does FastTrack Insurance Services project for year 1?", "keywords": ["22,000", "FastTrack"], "reference_answer": "FastTrack Insurance Services projects 22,000 claims in year 1.", "category": "numerical"}
{"question": "How much annual revenue does Marcus Johnson's portfolio generate?", "keywords": ["$5M", "Marcus"], "reference_answer": "Marcus Johnson manages a portfolio of 25 enterprise clients generating $5M in annual revenue.", "category": "numerical"}
{"question": "What percentage of quota did Jennifer Adams achieve in 2023?", "keywords": ["78%", "Jennifer"], "reference_answer": "Jennifer Adams achieved 78% of her lead generation quota in 2023.", "category": "numerical"}
{"question": "How many products does Insurellm offer?", "keywords": ["8", "products"], "reference_answer": "Insurellm offers 8 insurance software products across multiple insurance lines.", "category": "numerical"}
{"question": "What is the monthly cost of Carllm's Professional Tier?", "keywords": ["$2,500", "Professional", "Carllm"], "reference_answer": "Carllm's Professional Tier costs $2,500 per month.", "category": "numerical"}
{"question": "What are the core insurance portals offered by Insurellm?", "keywords": ["Core Insurance Portals", "Carllm"], "reference_answer": "Insurellm's core insurance portals are Carllm (auto), Homellm (home), Lifellm (life), Healthllm (health), and Bizllm (commercial).", "category": "relationship"}
{"question": "What are the marketplace and infrastructure products offered by Insurellm?", "keywords": ["Marketplace & Infrastructure", "Markellm"], "reference_answer": "Insurellm's marketplace and infrastructure products are Markellm (marketplace), Claimllm (claims processing), and Rellm (reinsurance).", "category": "relationship"}
{"question": "Which product does Jessica Liu develop for?", "keywords": ["Rellm", "Jessica"], "reference_answer": "Jessica Liu develops user interfaces for the Rellm reinsurance platform using React.", "category": "relationship"}
{"question": "What is Tyler Brooks's job title?", "keywords": ["Junior Backend Developer", "Tyler"], "reference_answer": "Tyler Brooks is a Junior Backend Developer at Insurellm.", "category": "relationship"}
{"question": "Which product does Tyler Brooks work on?", "keywords": ["Carllm", "Tyler"], "reference_answer": "Tyler Brooks develops backend services for the Carllm auto insurance portal.", "category": "relationship"}
{"question": "What is the job title of the IIOTY award winner?", "keywords": ["Maxine", "Thompson", "Senior Data Engineer", "IIOTY"], "reference_answer": "Maxine Thompson, who won the IIOTY award in 2023, works as a Senior Data Engineer.", "category": "spanning"}
{"question": "Who is the technical lead for the product that costs $10,000/month for Standard Tier?", "keywords": ["Robert", "Chen", "Homellm", "$10,000"], "reference_answer": "Robert Chen is the technical lead for Homellm, which costs $10,000/month for the Standard Tier.", "category": "spanning"}
{"question": "What is the salary of the CTO who joined in January 2017?", "keywords": ["James", "Wilson", "$285,000", "January 2017"], "reference_answer": "James Wilson, who joined as CTO in January 2017, has a current salary of $285,000.", "category": "spanning"}
{"question": "What is the current salary of the founder of Insurellm?", "keywords": ["Avery", "Lancaster", "$225,000", "founder"], "reference_answer": "Avery Lancaster, the founder of Insurellm, has a current salary of $225,000.", "category": "spanning"}
{"question": "Which product did the Senior Data Scientist build a recommendation engine for that increased conversion by 28%?", "keywords": ["Priya", "Sharma", "Marketllm", "28%"], "reference_answer": "Priya Sharma built a recommendation engine for Marketllm that increased conversion by 28%.", "category": "spanning"}
{"question": "Which product does the UX Designer who improved user satisfaction by 35% lead design for?", "keywords": ["Sarah", "Williams", "Homellm", "35%"], "reference_answer": "Sarah Williams, who improved user satisfaction by 35%, leads design for Homellm.", "category": "spanning"}
{"question": "What is the annual marketing budget managed by the Marketing Manager in Austin?", "keywords": ["Lisa", "Anderson", "$2M", "Austin"], "reference_answer": "Lisa Anderson, the Marketing Manager in Austin, manages a $2M annual marketing budget.", "category": "spanning"}
{"question": "Who signed the contract on behalf of Insurellm for the client that pays $18,000 per month for Carllm?", "keywords": ["Jennifer", "Rodriguez", "DriveSmart", "$18,000"], "reference_answer": "Jennifer Rodriguez, CEO of Insurellm, signed the contract for DriveSmart Insurance which pays $18,000 per month for Carllm.", "category": "spanning"}
{"question": "What tier did the client with 35 user licenses subscribe to for Bizllm?", "keywords": ["Atlantic", "Risk", "Solutions", "Professional", "35"], "reference_answer": "Atlantic Risk Solutions, which has 35 named user licenses, subscribed to the Professional Tier of Bizllm.", "category": "spanning"}
{"question": "How many covered members does the client who subscribed to Healthllm Professional Tier for $15,000/month have?", "keywords": ["Harmony", "Health", "Plans", "38,000", "$15,000"], "reference_answer": "Harmony Health Plans, which subscribed to Healthllm Professional Tier for $15,000/month, has 38,000 covered members.", "category": "spanning"}
{"question": "Who signed the Metropolitan Life Group contract that totals $1,098,000?", "keywords": ["Jennifer", "Rodriguez", "Richard", "Thompson", "$1,098,000"], "reference_answer": "Jennifer Rodriguez signed for Insurellm and Richard Thompson signed for Metropolitan Life Group on the contract totaling $1,098,000.", "category": "spanning"}
{"question": "What is the total contract value for the client paying $12,000 per month for Bizllm Professional Tier?", "keywords": ["Atlantic", "$144,000", "12 months", "$12,000"], "reference_answer": "Atlantic Risk Solutions pays $12,000/month for 12 months, totaling $144,000 for Bizllm Professional Tier.", "category": "spanning"}
{"question": "By what percentage did the DevOps Engineer in New York reduce deployment time?", "keywords": ["David", "Kim", "60%", "New York"], "reference_answer": "David Kim, the DevOps Engineer in New York, reduced deployment time by 60% with CI/CD pipelines.", "category": "spanning"}
{"question": "What is the annual revenue generated by the portfolio managed by the Customer Success Manager in New York?", "keywords": ["Marcus", "Johnson", "$5M", "New York"], "reference_answer": "Marcus Johnson, the Customer Success Manager in New York, manages a portfolio generating $5M in annual revenue.", "category": "spanning"}
{"question": "By what percentage did the Account Executive in Austin exceed their annual sales target in 2022?", "keywords": ["Emily", "Carter", "30%", "Austin", "2022"], "reference_answer": "Emily Carter, the Account Executive in Austin, exceeded her annual sales target by 30% in 2022.", "category": "spanning"}
{"question": "When is the telematics-based pricing feature scheduled to launch for the product that costs $1,000/month for Basic Tier?", "keywords": ["Carllm", "Q2 2025", "telematics", "$1,000"], "reference_answer": "Carllm, which costs $1,000/month for Basic Tier, has telematics-based pricing scheduled to launch in Q2 2025.", "category": "spanning"}
{"question": "What is the monthly cost for the Basic Listing Fee on the marketplace that was Insurellm's first product?", "keywords": ["Markellm", "$199", "first product"], "reference_answer": "Markellm, Insurellm's first product, has a Basic Listing Fee of $199/month.", "category": "spanning"}
{"question": "How many core values does the company founded by Avery Lancaster have?", "keywords": ["four", "core values", "Avery", "Lancaster", "founded"], "reference_answer": "Insurellm, founded by Avery Lancaster, has four core values: Innovation First, Customer Obsession, Integrity & Transparency, and Collaborative Excellence.", "category": "spanning"}
{"question": "What tier of Healthllm costs $15,000 per month and includes Advanced Medication Management?", "keywords": ["Professional", "Healthllm", "$15,000", "Advanced Medication Management"], "reference_answer": "The Professional Tier of Healthllm costs $15,000 per month and includes Advanced Medication Management features.", "category": "spanning"}
{"question": "How many active policies does the client who pays $28,000 per month for Lifellm manage?", "keywords": ["Metropolitan", "Life", "Group", "50,000", "$28,000"], "reference_answer": "Metropolitan Life Group, which pays $28,000 per month for Lifellm, manages 50,000+ active policies.", "category": "spanning"}
{"question": "What is Alex Chen's current job title?", "keywords": ["Backend Software Engineer", "Alex Chen"], "reference_answer": "Alex Chen is a Backend Software Engineer at Insurellm.", "category": "direct_fact"}
{"question": "What is Carlos Rodriguez's current salary?", "keywords": ["$125,000", "Carlos"], "reference_answer": "Carlos Rodriguez's current salary is $125,000.", "category": "direct_fact"}
{"question": "What is the monthly cost of the Bizllm Business Tier?", "keywords": ["$6,000", "Business", "Bizllm"], "reference_answer": "The Bizllm Business Tier costs $6,000 per month.", "category": "direct_fact"}
{"question": "What is Nina Patel's job title?", "keywords": ["Business Intelligence Analyst", "Nina"], "reference_answer": "Nina Patel is a Business Intelligence Analyst at Insurellm.", "category": "direct_fact"}
{"question": "What is the contract number for the GreenValley Insurance Homellm agreement?", "keywords": ["HV-2023-0458", "GreenValley"], "reference_answer": "The contract number for the GreenValley Insurance Homellm agreement is HV-2023-0458.", "category": "direct_fact"}
{"question": "When did Alex Chen join Insurellm?", "keywords": ["April 2020", "Alex Chen"], "reference_answer": "Alex Chen joined Insurellm in April 2020 as a Junior Backend Developer.", "category": "temporal"}
{"question": "When was the GreenValley Insurance Homellm contract signed?", "keywords": ["October 6, 2023", "GreenValley"], "reference_answer": "The GreenValley Insurance Homellm contract was signed on October 6, 2023.", "category": "temporal"}
{"question": "When was the Summit Commercial Insurance Bizllm contract effective?", "keywords": ["March 15, 2025", "Summit"], "reference_answer": "The Summit Commercial Insurance Bizllm contract became effective on March 15, 2025.", "category": "temporal"}
{"question": "When was the Roadway Insurance Carllm contract effective?", "keywords": ["January 1, 2025", "Roadway"], "reference_answer": "The Roadway Insurance Carllm contract became effective on January 1, 2025.", "category": "temporal"}
{"question": "When was the Evergreen Life Insurance Lifellm contract signed?", "keywords": ["January 20, 2025", "Evergreen"], "reference_answer": "The Evergreen Life Insurance Lifellm contract was signed on January 20, 2025.", "category": "temporal"}
{"question": "How many employees did Insurellm have at its peak in 2020?", "keywords": ["200", "2020", "peak"], "reference_answer": "Insurellm reached a peak of 200 employees in 2020.", "category": "numerical"}
{"question": "What is the monthly cost for Apex Reinsurance's Rellm subscription?", "keywords": ["$10,000", "Apex"], "reference_answer": "Apex Reinsurance pays $10,000 per month for the Rellm solution.", "category": "numerical"}
{"question": "How many active policies does Evergreen Life Insurance currently manage?", "keywords": ["1,400", "Evergreen"], "reference_answer": "Evergreen Life Insurance currently manages 1,400 active policies.", "category": "numerical"}
{"question": "How many user licenses are provided for onboarding training in the Summit Commercial Insurance contract?", "keywords": ["15", "Summit"], "reference_answer": "Summit Commercial Insurance receives onboarding training for up to 15 staff members.", "category": "numerical"}
{"question": "How much new business did Michael O'Brien generate over the past 3 years?", "keywords": ["$8.2M", "Michael", "O'Brien"], "reference_answer": "Michael O'Brien generated $8.2M in new business over the past 3 years.", "category": "numerical"}
{"question": "Which product does Rachel Martinez lead product strategy for?", "keywords": ["Carllm", "Rachel", "Martinez"], "reference_answer": "Rachel Martinez leads product strategy for Carllm, the auto insurance portal.", "category": "relationship"}
{"question": "Which mobile app does Kevin Zhang lead iOS development for?", "keywords": ["Marketllm", "Kevin", "Zhang"], "reference_answer": "Kevin Zhang leads iOS development for the Marketllm consumer mobile app.", "category": "relationship"}
{"question": "Which tier of Bizllm did Summit Commercial Insurance subscribe to?", "keywords": ["Business", "Summit"], "reference_answer": "Summit Commercial Insurance subscribed to the Business Tier of Bizllm.", "category": "relationship"}
{"question": "What award did Carlos Rodriguez win in 2023?", "keywords": ["Solutions Engineer of the Year", "Carlos"], "reference_answer": "Carlos Rodriguez won Solutions Engineer of the Year 2023.", "category": "relationship"}
{"question": "Who signed the Summit Commercial Insurance contract on behalf of Insurellm?", "keywords": ["Michael Torres", "Summit"], "reference_answer": "Michael Torres, Chief Revenue Officer, signed the Summit Commercial Insurance contract on behalf of Insurellm.", "category": "relationship"}
{"question": "How many employees at Insurellm have a current salary under $80,000?", "keywords": ["salary", "employees"], "reference_answer": "Based on the employee records, there are several employees with salaries under $80,000, including Tyler Brooks ($75,000) and Alex Harper ($75,000).", "category": "holistic"}
{"question": "What is the total contract value of all Healthllm contracts combined?", "keywords": ["Healthllm", "contract value"], "reference_answer": "The total contract value of all Healthllm contracts is $3,510,000, combining United Healthcare Alliance ($2,784,000), Harmony Health Plans ($360,000), Advanced Medical Coverage ($270,000), and WellCare Insurance Co. ($96,000).", "category": "holistic"}
{"question": "Which product line has the most active contracts according to the company overview?", "keywords": ["contracts", "products"], "reference_answer": "According to the company overview, both Bizllm and Claimllm are tied with the most active contracts at 7 contracts each.", "category": "holistic"}
{"question": "How many total employees work at Insurellm across all locations?", "keywords": ["employees", "total"], "reference_answer": "Insurellm has 32 employees operating primarily remotely across the US, with offices in San Francisco, New York, Austin, Chicago, and Denver.", "category": "holistic"}
{"question": "What is the average monthly subscription cost across all Carllm contracts?", "keywords": ["Carllm", "monthly cost"], "reference_answer": "The average monthly subscription cost across Carllm contracts varies, with examples including Roadway Insurance at $2,500/month for Professional Tier, though specific averages require aggregating all Carllm contract data.", "category": "holistic"}
{"question": "How many different insurance product lines does Insurellm offer in total?", "keywords": ["products", "insurance lines"], "reference_answer": "Insurellm offers 8 different insurance software products: Carllm, Homellm, Lifellm, Healthllm, Bizllm, Markellm, Claimllm, and Rellm.", "category": "holistic"}
{"question": "Which product has the fewest active contracts according to the portfolio breakdown?", "keywords": ["contracts", "fewest"], "reference_answer": "According to the portfolio breakdown, both Markellm and Rellm are tied with the fewest active contracts at 2 contracts each.", "category": "holistic"}
{"question": "What is the total number of active contracts across all Insurellm products?", "keywords": ["contracts", "total"], "reference_answer": "Insurellm has 32 active contracts across all product lines, serving clients ranging from regional insurers to national carriers and global reinsurance partners.", "category": "holistic"}
{"question": "How many states does United Healthcare Alliance operate in according to their contract?", "keywords": ["United Healthcare", "states"], "reference_answer": "United Healthcare Alliance operates across 12 states according to their Healthllm contract, supporting 250,000+ members.", "category": "holistic"}
{"question": "What is the longest contract duration among all Insurellm contracts?", "keywords": ["contract", "duration"], "reference_answer": "The longest contract duration is 48 months (4 years) for the United Healthcare Alliance Healthllm contract, representing Insurellm's most strategic long-term healthcare partnership.", "category": "holistic"}
```


---

<a id="file-week5-evaluator-py"></a>
## File: `week5/evaluator.py`

> **Path in repository:** `week5/evaluator.py`

```python
import gradio as gr
import pandas as pd
from collections import defaultdict
from dotenv import load_dotenv

from evaluation.eval import evaluate_all_retrieval, evaluate_all_answers

load_dotenv(override=True)

# Color coding thresholds - Retrieval
MRR_GREEN = 0.9
MRR_AMBER = 0.75
NDCG_GREEN = 0.9
NDCG_AMBER = 0.75
COVERAGE_GREEN = 90.0
COVERAGE_AMBER = 75.0

# Color coding thresholds - Answer (1-5 scale)
ANSWER_GREEN = 4.5
ANSWER_AMBER = 4.0


def get_color(value: float, metric_type: str) -> str:
    """Get color based on metric value and type."""
    if metric_type == "mrr":
        if value >= MRR_GREEN:
            return "green"
        elif value >= MRR_AMBER:
            return "orange"
        else:
            return "red"
    elif metric_type == "ndcg":
        if value >= NDCG_GREEN:
            return "green"
        elif value >= NDCG_AMBER:
            return "orange"
        else:
            return "red"
    elif metric_type == "coverage":
        if value >= COVERAGE_GREEN:
            return "green"
        elif value >= COVERAGE_AMBER:
            return "orange"
        else:
            return "red"
    elif metric_type in ["accuracy", "completeness", "relevance"]:
        if value >= ANSWER_GREEN:
            return "green"
        elif value >= ANSWER_AMBER:
            return "orange"
        else:
            return "red"
    return "black"


def format_metric_html(
    label: str,
    value: float,
    metric_type: str,
    is_percentage: bool = False,
    score_format: bool = False,
) -> str:
    """Format a metric with color coding."""
    color = get_color(value, metric_type)
    if is_percentage:
        value_str = f"{value:.1f}%"
    elif score_format:
        value_str = f"{value:.2f}/5"
    else:
        value_str = f"{value:.4f}"
    return f"""
    <div style="margin: 10px 0; padding: 15px; background-color: #f5f5f5; border-radius: 8px; border-left: 5px solid {color};">
        <div style="font-size: 14px; color: #666; margin-bottom: 5px;">{label}</div>
        <div style="font-size: 28px; font-weight: bold; color: {color};">{value_str}</div>
    </div>
    """


def run_retrieval_evaluation(progress=gr.Progress()):
    """Run retrieval evaluation and yield updates."""
    total_mrr = 0.0
    total_ndcg = 0.0
    total_coverage = 0.0
    category_mrr = defaultdict(list)
    count = 0

    for test, result, prog_value in evaluate_all_retrieval():
        count += 1
        total_mrr += result.mrr
        total_ndcg += result.ndcg
        total_coverage += result.keyword_coverage

        category_mrr[test.category].append(result.mrr)

        # Update progress bar only
        progress(prog_value, desc=f"Evaluating test {count}...")

    # Calculate final averages
    avg_mrr = total_mrr / count
    avg_ndcg = total_ndcg / count
    avg_coverage = total_coverage / count

    # Create final summary metrics HTML
    final_html = f"""
    <div style="padding: 0;">
        {format_metric_html("Mean Reciprocal Rank (MRR)", avg_mrr, "mrr")}
        {format_metric_html("Normalized DCG (nDCG)", avg_ndcg, "ndcg")}
        {format_metric_html("Keyword Coverage", avg_coverage, "coverage", is_percentage=True)}
        <div style="margin-top: 20px; padding: 10px; background-color: #d4edda; border-radius: 5px; text-align: center; border: 1px solid #c3e6cb;">
            <span style="font-size: 14px; color: #155724; font-weight: bold;">✓ Evaluation Complete: {count} tests</span>
        </div>
    </div>
    """

    # Create final bar chart data
    category_data = []
    for category, mrr_scores in category_mrr.items():
        avg_cat_mrr = sum(mrr_scores) / len(mrr_scores)
        category_data.append({"Category": category, "Average MRR": avg_cat_mrr})

    df = pd.DataFrame(category_data)

    return final_html, df


def run_answer_evaluation(progress=gr.Progress()):
    """Run answer evaluation and yield updates (async)."""
    total_accuracy = 0.0
    total_completeness = 0.0
    total_relevance = 0.0
    category_accuracy = defaultdict(list)
    count = 0

    for test, result, prog_value in evaluate_all_answers():
        count += 1
        total_accuracy += result.accuracy
        total_completeness += result.completeness
        total_relevance += result.relevance

        category_accuracy[test.category].append(result.accuracy)

        # Update progress bar only
        progress(prog_value, desc=f"Evaluating test {count}...")

    # Calculate final averages
    avg_accuracy = total_accuracy / count
    avg_completeness = total_completeness / count
    avg_relevance = total_relevance / count

    # Create final summary metrics HTML
    final_html = f"""
    <div style="padding: 0;">
        {format_metric_html("Accuracy", avg_accuracy, "accuracy", score_format=True)}
        {format_metric_html("Completeness", avg_completeness, "completeness", score_format=True)}
        {format_metric_html("Relevance", avg_relevance, "relevance", score_format=True)}
        <div style="margin-top: 20px; padding: 10px; background-color: #d4edda; border-radius: 5px; text-align: center; border: 1px solid #c3e6cb;">
            <span style="font-size: 14px; color: #155724; font-weight: bold;">✓ Evaluation Complete: {count} tests</span>
        </div>
    </div>
    """

    # Create final bar chart data
    category_data = []
    for category, accuracy_scores in category_accuracy.items():
        avg_cat_accuracy = sum(accuracy_scores) / len(accuracy_scores)
        category_data.append({"Category": category, "Average Accuracy": avg_cat_accuracy})

    df = pd.DataFrame(category_data)

    return final_html, df


def main():
    """Launch the Gradio evaluation app."""
    theme = gr.themes.Soft(font=["Inter", "system-ui", "sans-serif"])

    with gr.Blocks(title="RAG Evaluation Dashboard", theme=theme) as app:
        gr.Markdown("# 📊 RAG Evaluation Dashboard")
        gr.Markdown("Evaluate retrieval and answer quality for the Insurellm RAG system")

        # RETRIEVAL SECTION
        gr.Markdown("## 🔍 Retrieval Evaluation")

        retrieval_button = gr.Button("Run Evaluation", variant="primary", size="lg")

        with gr.Row():
            with gr.Column(scale=1):
                retrieval_metrics = gr.HTML(
                    "<div style='padding: 20px; text-align: center; color: #999;'>Click 'Run Evaluation' to start</div>"
                )

            with gr.Column(scale=1):
                retrieval_chart = gr.BarPlot(
                    x="Category",
                    y="Average MRR",
                    title="Average MRR by Category",
                    y_lim=[0, 1],
                    height=400,
                )

        # ANSWERING SECTION
        gr.Markdown("## 💬 Answer Evaluation")

        answer_button = gr.Button("Run Evaluation", variant="primary", size="lg")

        with gr.Row():
            with gr.Column(scale=1):
                answer_metrics = gr.HTML(
                    "<div style='padding: 20px; text-align: center; color: #999;'>Click 'Run Evaluation' to start</div>"
                )

            with gr.Column(scale=1):
                answer_chart = gr.BarPlot(
                    x="Category",
                    y="Average Accuracy",
                    title="Average Accuracy by Category",
                    y_lim=[1, 5],
                    height=400,
                )

        # Wire up the evaluations
        retrieval_button.click(
            fn=run_retrieval_evaluation,
            outputs=[retrieval_metrics, retrieval_chart],
        )

        answer_button.click(
            fn=run_answer_evaluation,
            outputs=[answer_metrics, answer_chart],
        )

    app.launch(inbrowser=True)


if __name__ == "__main__":
    main()
```


---

<a id="file-week5-implementation-answer-py"></a>
## File: `week5/implementation/answer.py`

> **Path in repository:** `week5/implementation/answer.py`

```python
from pathlib import Path
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, convert_to_messages
from langchain_core.documents import Document

from dotenv import load_dotenv


load_dotenv(override=True)

MODEL = "gpt-6-luna"
DB_NAME = str(Path(__file__).parent.parent / "vector_db")

# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
RETRIEVAL_K = 10

SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing the company Insurellm.
You are chatting with a user about Insurellm.
If relevant, use the given context to answer any question.
If you don't know the answer, say so.
Context:
{context}
"""

vectorstore = Chroma(persist_directory=DB_NAME, embedding_function=embeddings)
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(temperature=0, model_name=MODEL, reasoning_effort="none")


def fetch_context(question: str) -> list[Document]:
    """
    Retrieve relevant context documents for a question.
    """
    return retriever.invoke(question, k=RETRIEVAL_K)


def combined_question(question: str, history: list[dict] = []) -> str:
    """
    Combine all the user's messages into a single string.
    """
    prior = "\n".join(m["content"] for m in history if m["role"] == "user")
    return prior + "\n" + question


def answer_question(question: str, history: list[dict] = []) -> tuple[str, list[Document]]:
    """
    Answer the given question with RAG; return the answer and the context documents.
    """
    combined = combined_question(question, history)
    docs = fetch_context(combined)
    context = "\n\n".join(doc.page_content for doc in docs)
    system_prompt = SYSTEM_PROMPT.format(context=context)
    messages = [SystemMessage(content=system_prompt)]
    messages.extend(convert_to_messages(history))
    messages.append(HumanMessage(content=question))
    response = llm.invoke(messages)
    return response.content, docs
```


---

<a id="file-week5-implementation-ingest-py"></a>
## File: `week5/implementation/ingest.py`

> **Path in repository:** `week5/implementation/ingest.py`

```python
import os
import glob
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings


from dotenv import load_dotenv

MODEL = "gpt-6-luna"

DB_NAME = str(Path(__file__).parent.parent / "vector_db")
KNOWLEDGE_BASE = str(Path(__file__).parent.parent / "knowledge-base")

# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

load_dotenv(override=True)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


def fetch_documents():
    folders = glob.glob(str(Path(KNOWLEDGE_BASE) / "*"))
    documents = []
    for folder in folders:
        doc_type = os.path.basename(folder)
        loader = DirectoryLoader(
            folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"}
        )
        folder_docs = loader.load()
        for doc in folder_docs:
            doc.metadata["doc_type"] = doc_type
            documents.append(doc)
    return documents


def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    return chunks


def create_embeddings(chunks):
    if os.path.exists(DB_NAME):
        Chroma(persist_directory=DB_NAME, embedding_function=embeddings).delete_collection()

    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=DB_NAME
    )

    collection = vectorstore._collection
    count = collection.count()

    sample_embedding = collection.get(limit=1, include=["embeddings"])["embeddings"][0]
    dimensions = len(sample_embedding)
    print(f"There are {count:,} vectors with {dimensions:,} dimensions in the vector store")
    return vectorstore


if __name__ == "__main__":
    documents = fetch_documents()
    chunks = create_chunks(documents)
    create_embeddings(chunks)
    print("Ingestion complete")
```


---

<a id="file-week5-knowledge-base-company-about-md"></a>
## File: `week5/knowledge-base/company/about.md`

> **Path in repository:** `week5/knowledge-base/company/about.md`

# About Insurellm

Insurellm was founded by Avery Lancaster in 2015 as an insurance tech startup designed to disrupt an industry in need of innovative products. Its first product was Markellm, the marketplace connecting consumers with insurance providers.

The company experienced rapid growth in its first five years, expanding its product portfolio to include Carllm (auto insurance portal), Homellm (home insurance portal), and Rellm (enterprise reinsurance platform). By 2020, Insurellm had reached a peak of 200 employees with 12 offices across the US.

However, the company underwent a strategic restructuring in 2022-2023 to focus on profitability and sustainable growth. This included consolidating office locations, implementing a remote-first strategy, and streamlining operations. As of 2025, Insurellm operates with a lean, highly efficient team of 32 employees who have built a portfolio of 32 active contracts spanning all eight product lines. The company maintains its San Francisco headquarters along with small satellite offices in key markets including New York, Austin, Chicago, and Denver.

Since the restructuring, Insurellm has continued to innovate, expanding its product suite to eight comprehensive platforms. The company added Lifellm (life insurance), Healthllm (health insurance), Bizllm (commercial insurance), and Claimllm (claims processing) to serve the full spectrum of insurance needs. This strategic expansion has been highly successful, with strong adoption across all new products:

- **Bizllm** quickly gained traction with 7 commercial insurance contracts, including regional carriers and national commercial groups
- **Claimllm** signed 7 contracts ranging from independent adjusting firms to enterprise claims networks
- **Lifellm** secured 6 life insurance clients from small regional providers to major national carriers
- **Healthllm** won 6 health plan contracts including regional insurers and multi-state healthcare alliances

Combined with continued growth in the original product lines (Carllm, Homellm, Markellm, and Rellm), Insurellm now serves clients ranging from regional insurers to global reinsurance partners, demonstrating the company's ability to compete across the entire insurance value chain.


---

<a id="file-week5-knowledge-base-company-careers-md"></a>
## File: `week5/knowledge-base/company/careers.md`

> **Path in repository:** `week5/knowledge-base/company/careers.md`

# Careers at Insurellm

## Why Join Insurellm?

At Insurellm, we're not just building software—we're revolutionizing an entire industry. Since our founding in 2015, we've evolved from a high-growth startup to a lean, profitable company with 32 highly talented employees managing 32 active contracts across all eight of our product lines.

After reaching 200 employees in 2020, we strategically restructured in 2022-2023 to focus on sustainable growth, operational excellence, and building a world-class remote-first culture. Today, we're a tight-knit team of exceptional professionals who deliver outsized impact through automation, AI, and strategic focus on high-value enterprise clients—from regional insurers to global reinsurance partners.

### Our Culture

We live by our core values every day:
- **Innovation First**: We encourage experimentation and creative problem-solving
- **Customer Obsession**: Your work directly impacts 32 active client operations spanning the entire insurance value chain
- **Integrity & Transparency**: We build trust through ethical behavior and open communication
- **Collaborative Excellence**: Diverse perspectives and teamwork drive our success

### What We Offer

- Competitive compensation with equity participation
- Comprehensive health, dental, and vision insurance
- Flexible working arrangements and generous PTO
- Professional development programs and mentorship
- Clear career progression paths
- Latest technologies and tools
- Inclusive, diverse work environment

## Current Opportunities

### Engineering

**Senior Full Stack Engineer** - San Francisco, CA
- Lead development of next-generation insurance platform features
- Work with React, Node.js, Python, and cloud technologies
- Mentor junior engineers and drive technical decisions
- 5+ years experience required

**Backend Software Engineer** - San Francisco, CA / Austin, TX
- Build scalable microservices and APIs
- Optimize system performance and reliability
- Collaborate with product and design teams
- 3+ years experience with Java, Python, or Go

**Frontend Developer** - Remote
- Create intuitive user interfaces for our insurance platforms
- Work with modern frameworks (React, Vue, or Angular)
- Ensure accessibility and responsive design
- 2+ years experience required

**DevOps Engineer** - New York, NY
- Manage cloud infrastructure (AWS/GCP)
- Implement CI/CD pipelines and automation
- Monitor system performance and security
- 3+ years experience in DevOps/SRE

**Mobile Developer (iOS/Android)** - San Francisco, CA
- Build native mobile applications for our marketplace
- Create seamless user experiences
- Integrate with backend APIs
- 3+ years mobile development experience

### Data & Analytics

**Senior Data Scientist** - San Francisco, CA / New York, NY
- Develop predictive models for insurance risk assessment
- Build recommendation systems for our marketplace
- Lead data-driven product initiatives
- PhD or MS in related field preferred, 4+ years experience

**Data Engineer** - Austin, TX
- Design and maintain data pipelines
- Build data warehousing solutions
- Optimize data infrastructure for scale
- 3+ years experience with SQL, Python, and ETL tools

**Business Intelligence Analyst** - Chicago, IL
- Create dashboards and reports for stakeholders
- Analyze business metrics and trends
- Support data-driven decision making
- 2+ years experience with BI tools (Tableau, Looker, etc.)

### Product & Design

**Product Manager** - San Francisco, CA
- Define product roadmap and strategy
- Work closely with engineering and design teams
- Gather customer insights and market research
- 3+ years product management experience in B2B SaaS

**UX/UI Designer** - Remote
- Design user experiences for our insurance platforms
- Conduct user research and usability testing
- Create design systems and prototypes
- 3+ years design experience, insurance/fintech preferred

### Sales & Customer Success

**Account Executive** - New York, NY / Chicago, IL / Austin, TX
- Manage B2B sales cycle for enterprise clients
- Build relationships with insurance companies
- Exceed revenue targets and grow territory
- 3+ years B2B sales experience, SaaS preferred

**Sales Development Representative** - Austin, TX / Remote
- Generate qualified leads for sales team
- Conduct outreach to prospective clients
- Research and identify target accounts
- 1+ years SDR/BDR experience preferred

**Customer Success Manager** - San Francisco, CA / New York, NY
- Ensure client satisfaction and retention
- Drive product adoption and expansion
- Serve as trusted advisor to clients
- 2+ years customer success experience in SaaS

**Solutions Engineer** - Remote
- Provide technical expertise during sales process
- Conduct product demonstrations and POCs
- Support implementation and integration
- 3+ years technical pre-sales experience

### Operations & Support

**Technical Support Specialist** - Remote
- Provide tier 2/3 technical support to clients
- Troubleshoot platform issues
- Create documentation and knowledge base articles
- 2+ years technical support experience

**HR Business Partner** - San Francisco, CA
- Partner with leadership on people strategy
- Support talent development and retention
- Drive culture and engagement initiatives
- 4+ years HR experience, tech industry preferred

## How to Apply

Visit our careers portal at careers.insurellm.com or send your resume to jobs@insurellm.com. Please include the position title in your subject line.

Insurellm is an equal opportunity employer. We celebrate diversity and are committed to creating an inclusive environment for all employees.


---

<a id="file-week5-knowledge-base-company-culture-md"></a>
## File: `week5/knowledge-base/company/culture.md`

> **Path in repository:** `week5/knowledge-base/company/culture.md`

# Insurellm Culture

## Vision Statement
To revolutionize the insurance industry through innovative technology that makes insurance accessible, transparent, and effortless for everyone.

## Mission Statement
We empower insurance providers and consumers with cutting-edge software solutions that streamline processes, enhance customer experiences, and drive meaningful connections in the insurance marketplace. By combining deep industry expertise with technological innovation, we're building the future of insurance.

## Core Values

### Innovation First
We challenge the status quo and embrace creative problem-solving. Our team is encouraged to experiment, take calculated risks, and push the boundaries of what's possible in insurance technology. We believe that breakthrough solutions come from curiosity, collaboration, and a willingness to learn from both successes and failures.

### Customer Obsession
Our clients' success is our success. We deeply understand our customers' needs and work tirelessly to exceed their expectations. Every product decision, every feature, and every interaction is guided by a commitment to delivering exceptional value and building lasting partnerships.

### Integrity & Transparency
We operate with honesty and openness in everything we do. From our products to our internal operations, we believe that trust is earned through consistent ethical behavior, clear communication, and accountability at all levels of the organization.

### Collaborative Excellence
We achieve more together. We foster a culture where diverse perspectives are valued, knowledge is shared freely, and every team member is empowered to contribute their unique talents. We celebrate collective wins and support each other through challenges.

## Employer Value Proposition

**Build the Future of Insurance Technology with Elite Talent**

At Insurellm, you'll join an elite team of 32 exceptional professionals transforming a traditional industry with cutting-edge technology. After our strategic restructuring in 2022-2023, we evolved from a 200-person startup to a lean, high-performing organization where every person makes a significant impact. With 32 active contracts across all eight product lines—from regional insurers to global reinsurance partners—each team member directly influences technology used by thousands of insurance professionals and millions of consumers. We offer:

- **Meaningful Impact**: Your work directly shapes products powering 32 active insurance operations, from commercial carriers to health plans to global reinsurance firms
- **Growth & Development**: Comprehensive professional development programs, mentorship opportunities, and clear career progression paths
- **Innovation Freedom**: Access to the latest technologies and the autonomy to experiment with new ideas
- **Work-Life Harmony**: Flexible working arrangements, generous PTO, and a culture that respects personal time
- **Competitive Rewards**: Market-leading compensation, equity participation, comprehensive benefits, and performance bonuses
- **Inclusive Environment**: A diverse team where every voice matters and different perspectives drive better solutions
- **Purpose-Driven Mission**: Be part of making insurance more accessible and fair for everyone

Join us in disrupting an industry and building technology that matters.


---

<a id="file-week5-knowledge-base-company-overview-md"></a>
## File: `week5/knowledge-base/company/overview.md`

> **Path in repository:** `week5/knowledge-base/company/overview.md`

# Overview of Insurellm

Insurellm is an innovative insurance tech firm with 32 employees operating primarily remotely across the US, with offices in San Francisco (HQ), New York, Austin, Chicago, and Denver.

Founded in 2015, the company has evolved from a high-growth startup to a lean, profitable operation focused on sustainable growth and operational excellence.

## Products

Insurellm offers 8 insurance software products across multiple insurance lines:

### Core Insurance Portals
- **Carllm** - Auto insurance platform for insurers
- **Homellm** - Home insurance platform for insurers
- **Lifellm** - Life insurance platform with AI-powered underwriting
- **Healthllm** - Comprehensive health insurance platform
- **Bizllm** - Commercial insurance platform for business coverage

### Marketplace & Infrastructure
- **Markellm** - Marketplace connecting consumers with insurance providers (original flagship product)
- **Claimllm** - AI-powered claims processing platform across all insurance lines
- **Rellm** - Enterprise platform for the reinsurance sector

## Scale & Impact

Despite its compact team size, Insurellm has built an impressive client portfolio with 32 active contracts across all product lines, serving clients ranging from regional insurers to national carriers and global reinsurance partners. The company demonstrates exceptional productivity and leverage through:
- Highly automated systems and processes
- Strategic use of AI and machine learning
- Remote-first culture enabling access to top talent
- Focus on high-value enterprise clients in multiple insurance verticals

## Client Portfolio Breakdown

Insurellm's 32 active contracts span the full spectrum of insurance technology:

**Commercial Insurance (Bizllm)**: 7 contracts including regional carriers, multi-line insurers, and national commercial insurance groups

**Claims Processing (Claimllm)**: 7 contracts ranging from independent adjusting firms to enterprise claims networks

**Life Insurance (Lifellm)**: 6 contracts serving life insurance carriers from small regional providers to major national groups

**Health Insurance (Healthllm)**: 6 contracts with health plans from regional insurers to multi-state healthcare alliances

**Auto Insurance (Carllm)**: 3 contracts with personal and commercial auto insurers

**Home Insurance (Homellm)**: 4 contracts including property insurers with advanced IoT and catastrophe management needs

**Insurance Marketplace (Markellm)**: 2 contracts with agencies and brokers leveraging the consumer-insurer matching platform

**Reinsurance (Rellm)**: 2 contracts with reinsurance companies including global treaty and facultative operations

This diversified portfolio demonstrates Insurellm's ability to serve the entire insurance value chain, from consumer-facing marketplaces to complex reinsurance operations.


---

<a id="file-week5-knowledge-base-contracts-contract-with-advantage-medical-coverage-for-healthllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Advantage Medical Coverage for Healthllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Advantage Medical Coverage for Healthllm.md`

# Contract with Advantage Medical Coverage for Healthllm

**Contract Date:** April 18, 2025
**Contract Number:** HL-2025-0124

---

## Terms

1. **Parties Involved**: This contract is entered into between Insurellm, Inc. ("Provider") and Advantage Medical Coverage ("Client").

2. **License Grant**: Insurellm grants Advantage Medical Coverage a non-exclusive, non-transferable license to use the Healthllm Professional Tier platform.

3. **Payment Terms**: Advantage Medical Coverage agrees to make monthly payments of $15,000 for the duration of this 18-month contract, totaling $270,000. Payments due on the 10th of each month via wire transfer.

4. **Member Coverage**: Professional Tier supports up to 50,000 covered members. Advantage currently covers 32,000 members in 2 states.

5. **Confidentiality**: Both parties shall maintain confidentiality regarding proprietary information, member PHI, and business strategies throughout the contract duration and for 7 years post-termination, in compliance with HIPAA retention requirements.

## Renewal

1. **Automatic Renewal**: This contract automatically renews for successive 18-month terms unless either party provides written notice of non-renewal at least 60 days prior to expiration.

2. **Pricing Review**: Renewal pricing will be discussed 75 days prior to term end and mutually agreed upon in writing. Price increases limited to 7% annually.

## Features

1. **Included Features**: Advantage Medical Coverage will have access to Healthllm Professional Tier features:
   - Intelligent Plan Design with competitive benchmarking
   - Real-Time Eligibility Verification with provider integration
   - AI-Driven Claims Adjudication with auto-processing
   - Predictive Healthcare Analytics for population health
   - Provider Network Management with 8,000+ providers
   - Member Engagement Platform with mobile app
   - Advanced Medication Management with PBM integration
   - Regulatory Compliance Engine (ACA, state mandates, HIPAA)
   - Enhanced Analytics and predictive modeling
   - Care management tools and workflows

2. **Value-Based Care Support:**
   - ACO performance tracking and shared savings calculation
   - HEDIS measure calculation for quality reporting
   - Provider pay-for-performance scorecards
   - Risk adjustment and HCC coding support
   - Medicare STAR ratings optimization

3. **Telehealth Integration**: Built-in telehealth platform supporting:
   - Video visits with in-network providers
   - E-consults and asynchronous care
   - Behavioral health virtual visits
   - Member scheduling and appointment management

## Support

1. **Customer Support**: Insurellm will provide priority support to Advantage Medical Coverage:
   - Dedicated support team Monday-Friday 6 AM - 9 PM EST
   - Emergency support 24/7 for critical system issues
   - Response time: 6 hours for critical, 12 hours for high priority, 24 hours for standard
   - Private support portal with ticket tracking

2. **Training**: Comprehensive training program:
   - 5-week implementation with project manager
   - Training for up to 30 staff members (45 hours total)
   - Role-specific training tracks
   - Quarterly webinars on new features
   - Online training library with 75+ courses

3. **System Updates**: Monthly platform enhancements and bi-weekly security patches. Maintenance windows on Saturday 11 PM - Sunday 2 AM EST with 72-hour advance notice.

4. **Account Management**: Named senior customer success manager with quarterly business reviews and annual strategic planning session.

5. **Integration Support**: Technical assistance for integrating with:
   - Advantage's HealthRules policy admin system
   - Optum PBM
   - Availity clearinghouse
   - Provider credentialing platforms
   - Member portal and mobile apps

---

**Signatures:**

**Insurellm, Inc.**
Sarah Chen, VP of Sales
Date: April 18, 2025

**Advantage Medical Coverage**
Dr. Michael Ramirez, Chief Medical Officer
Date: April 18, 2025

---

This contract enables Advantage Medical Coverage to leverage advanced AI and predictive analytics for improved member health outcomes and operational efficiency.


---

<a id="file-week5-knowledge-base-contracts-contract-with-apex-reinsurance-for-rellm---ai-powered-enterprise-reinsurance-solution-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Apex Reinsurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Apex Reinsurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md`

# Contract with Apex Reinsurance for Rellm: AI-Powered Enterprise Reinsurance Solution

## Terms

1. **Parties Involved**: This contract (“Agreement”) is entered into between Insurellm, Inc. (“Provider”) and Apex Reinsurance (“Client”) on this [Date].

2. **Scope of Services**: Provider agrees to deliver the Rellm solution, which includes AI-driven analytics, seamless integrations, risk assessment modules, customizable dashboards, regulatory compliance tools, and client and broker portals as described in the product summary.

3. **Payment Terms**: Client shall pay the Provider the sum of $10,000 per month for the duration of this agreement. Payments are due on the first day of each month and will be processed via electronic funds transfer.

4. **Contract Duration**: This Agreement shall commence on [Start Date] and shall remain in effect for a period of twelve (12) months unless terminated earlier in accordance with the terms set forth herein.

## Renewal

1. **Automatic Renewal**: This Agreement will automatically renew for successive one-year terms unless either party provides a written notice of intent to terminate at least thirty (30) days prior to the expiration of the current term.

2. **Renewal Pricing**: Upon renewal, the pricing may be subject to adjustment by the Provider. The Provider will give a minimum of sixty (60) days’ notice of any changes in pricing.

## Features

1. **AI-Driven Analytics**: The Rellm platform will utilize AI algorithms to provide predictive insights into risk exposures, allowing the Client to make informed decisions with real-time data analysis.

2. **Seamless Integrations**: The architecture of Rellm allows for easy integration with existing systems used by the Client, including policy management and claims processing.

3. **Customizable Dashboard**: The dashboard will be tailored to display metrics specific to the Client's operational needs, enhancing productivity and facilitating more efficient data access.

4. **Regulatory Compliance**: The solution will include compliance tracking features to assist the Client in maintaining adherence to relevant regulations.

5. **Dedicated Client Portal**: A portal for the Client will facilitate real-time communication and document sharing, ensuring seamless collaboration throughout the partnership.

## Support

1. **Technical Support**: Provider shall offer dedicated technical support to the Client via phone, email, and a ticketing system during business hours (Monday to Friday, 9 AM to 5 PM EST).

2. **Training and Onboarding**: Provider will deliver comprehensive onboarding training for up to ten (10) members of the Client's staff to ensure effective use of the Rellm solution.

3. **Updates and Maintenance**: Provider is responsible for providing updates to the Rellm platform to improve functionality and security, at no additional cost to the Client.

4. **Escalation Protocol**: Issues that cannot be resolved at the first level of support will be escalated to the senior support team, ensuring that critical concerns are addressed promptly.

---

**Acceptance of Terms**: By signing below, both parties agree to the Terms, Renewal, Features, and Support outlined in this Agreement.

**Insurellm, Inc.**  
_____________________________  
Authorized Signature   
Date: ___________________  

**Apex Reinsurance**  
_____________________________  
Authorized Signature  
Date: ___________________


---

<a id="file-week5-knowledge-base-contracts-contract-with-atlantic-risk-solutions-for-bizllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Atlantic Risk Solutions for Bizllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Atlantic Risk Solutions for Bizllm.md`

# Contract with Atlantic Risk Solutions for Bizllm

---

## Terms

1. **Agreement Effective Date**: This contract is effective as of January 15, 2025.
2. **Duration**: This agreement will remain in effect for a term of 12 months, concluding on January 14, 2026.
3. **Subscription Type**: Atlantic Risk Solutions agrees to subscribe to the **Professional Tier** of Bizllm, at a cost of $12,000/month, totaling $144,000 for the duration of this contract.
4. **Payment Terms**: Payments are due on the 10th of each month via ACH transfer. Late payments will incur a penalty of 1.5% per month and may result in service suspension after 15 days delinquency.
5. **User Licenses**: Contract includes 35 named user licenses. Additional users may be added at $180/month per license.
6. **Termination Clause**: Either party may terminate this agreement with 45 days' written notice. Early termination requires payment of 50% of remaining contract value.

---

## Renewal

1. **Automatic Renewal**: This agreement will automatically renew for an additional 12-month term unless either party provides written notice of non-renewal at least 45 days before the expiration date.
2. **Price Protection**: Pricing increases capped at 8% annually for the first two renewal periods, providing Atlantic Risk Solutions with budget predictability.
3. **Volume Discounts**: If Atlantic Risk Solutions expands to Enterprise tier during renewal, they receive a 15% discount on the difference for the first renewal year.

---

## Features

1. **Access to Professional Tier Features**: Atlantic Risk Solutions will have access to all Professional Tier features, including:
   - Multi-Line Underwriting Engine supporting general liability, professional liability, property, workers' compensation, and cyber insurance
   - Business Intelligence Integration with automated data gathering from 50+ data sources
   - Cyber Risk Assessment module with security posture evaluation
   - Workers' Compensation Optimization with payroll integration and class code analysis
   - Commercial Property Evaluation with catastrophe modeling
   - Professional Liability Specialization for E&O coverage
   - Portfolio Management Dashboard with loss ratio tracking and geographic analysis
   - Agent and Broker Portal supporting up to 500 distribution partners
   - Claims Management Integration with reserve recommendation engine

2. **Industry-Specific Templates**: Pre-configured underwriting templates for:
   - Technology companies and software-as-a-service (SaaS) businesses
   - Professional services firms (consulting, accounting, legal)
   - Healthcare providers and medical practices
   - Contractors and construction trades
   - Restaurants and hospitality businesses

3. **Advanced Reporting**: Monthly automated reports including:
   - New business pipeline and conversion rates
   - Renewal retention analysis
   - Loss ratio trending by line of business
   - Agent performance scorecards
   - Competitive market positioning insights

---

## Support

1. **Technical Support**: Atlantic Risk Solutions will receive priority technical support from Insurellm for any issues arising from the Bizllm product:
   - Dedicated support phone line and email
   - Response time: 4 hours for critical issues, 12 hours for standard requests
   - Access to technical support Monday-Friday 7 AM - 8 PM EST

2. **Training**: Insurellm will provide comprehensive training program:
   - Initial onboarding for up to 15 staff members (20 hours total training)
   - Bi-monthly webinars on platform updates and best practices
   - Access to on-demand video library and knowledge base
   - Annual refresher training session

3. **Updates and Maintenance**:
   - Quarterly platform updates with new features and security enhancements
   - Monthly minor updates and bug fixes
   - Maintenance windows: Sunday 1 AM - 5 AM EST
   - 48-hour advance notice for all scheduled maintenance

4. **Account Management**:
   - Assigned account manager with quarterly business review meetings
   - Annual strategic planning session to align platform usage with business goals
   - Priority access to new beta features

5. **Integration Support**: Technical assistance for integrating Bizllm with:
   - Atlantic's existing agency management system (Applied Epic)
   - Commercial lines rating platforms
   - Third-party data providers (Dun & Bradstreet, Experian, Verisk)
   - Email marketing platforms for agent communications

---

**Signatures:**

_________________________________
**Michael Torres**
**Title**: Chief Revenue Officer
**Insurellm, Inc.**
**Date**: January 15, 2025

_________________________________
**Diana Marquez**
**Title**: Senior Vice President, Commercial Lines
**Atlantic Risk Solutions**
**Date**: January 15, 2025

---

*This contract establishes a professional partnership between Insurellm and Atlantic Risk Solutions, enabling Atlantic to leverage cutting-edge AI technology for commercial insurance underwriting and administration.*


---

<a id="file-week5-knowledge-base-contracts-contract-with-belvedere-insurance-for-markellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Belvedere Insurance for Markellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Belvedere Insurance for Markellm.md`

# Contract with Belvedere Insurance for Markellm

## Terms
This Contract ("Agreement") is made and entered into as of [Date] by and between Insurellm, Inc., a corporation registered in the United States, ("Provider") and Belvedere Insurance, ("Client"). 

1. **Service Commencement**: The services described herein will commence on [Start Date].
2. **Contract Duration**: This Agreement shall remain in effect for a period of 1 year from the Commencement Date, unless terminated earlier in accordance with the termination clause of this Agreement.
3. **Fees**: Client agrees to pay a Basic Listing Fee of $199/month for accessing the Markellm platform along with a performance-based pricing of $25 per lead generated.
4. **Payment Terms**: Payments shall be made monthly, in advance, with invoices issued on the 1st of each month, payable within 15 days of receipt.

## Renewal
1. **Renewal Terms**: This Agreement may be renewed for additional one-year terms upon mutual written consent of both parties no later than 30 days before the end of the current term.
2. **Fee Adjustments**: Any changes to the fees or terms will be communicated in writing at least 60 days prior to the renewal date.

## Features
1. **AI-Powered Matching**: Belvedere Insurance will benefit from Markellm's AI-powered matching, ensuring the best-fit customers are identified and connected.
2. **Real-Time Quotes**: Access to real-time quotes will enhance the customer acquisition process, facilitating timely and informed decision-making.
3. **Data Insights**: Client shall have access to Markellm's analytics dashboard, allowing insights into consumer behavior and market trends.
4. **Customization Options**: Belvedere Insurance can leverage optional premium features and analytics upon payment of an additional $9.99/month.
5. **Customer Support**: Insurellm will provide dedicated support to Belvedere Insurance, ensuring any issues or queries are promptly addressed.

## Support
1. **Technical Support**: Technical support will be available from 9 AM to 7 PM EST, Monday through Friday via email and phone.
2. **Response Times**: Insurellm agrees to respond to all support queries within 24 business hours. Emergency support will be prioritized throughout the contract period.
3. **Training**: Insurellm will offer a comprehensive training session for the Client’s staff upon beginning the service to ensure effective utilization of the features.

## Acceptance
By signing below, the parties agree to the terms of this Agreement.

**Insurellm, Inc.**  
Signature: ______________________  
Name: [Authorized Signatory]  
Title: [Title]  
Date: ______________________  

**Belvedere Insurance**  
Signature: ______________________  
Name: [Authorized Signatory]  
Title: [Title]  
Date: ______________________  

--- 
This synthetic contract document outlines a fictional agreement between Insurellm and a fictional insurance client, Belvedere Insurance, which engages with the Markellm platform. The contract contains creative yet realistic terms for potential use in training and development in insurance technology scenarios.


---

<a id="file-week5-knowledge-base-contracts-contract-with-brightway-solutions-for-markellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with BrightWay Solutions for Markellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with BrightWay Solutions for Markellm.md`

# Contract with BrightWay Solutions for Markellm

**Contract Date:** October 5, 2023  
**Contract ID:** INS-2023-0092

### Terms
This contract (“Contract”) is made between Insurellm, a company incorporated in the United States, and BrightWay Solutions, a technology provider specializing in insurance services.

1. **Scope of Services:**  
   Insurellm shall provide BrightWay Solutions access to the Markellm platform under the agreed pricing structure for a duration of one year from the effective date.

2. **Payment Terms:**  
   BrightWay Solutions agrees to pay an initial setup fee of $1,000 for integration services, followed by the Basic Listing Fee of $199 per month for featured listing on Markellm. Payment shall be made within 30 days of invoice.

3. **Service Level Agreement (SLA):**  
   Insurellm commits to a 99.9% uptime for the platform with dedicated support response times not exceeding 4 business hours.

### Renewal
1. **Automatic Renewal:**  
   This Contract will automatically renew for additional one-year terms unless either party provides a written notice of intent to terminate at least 30 days prior to the renewal date.

2. **Review Period:**  
   Both parties will enter a review period each year, during which they will discuss potential amendments to the pricing or contract terms based on market conditions and performance metrics.

### Features
1. **Access to AI-Powered Matching:**  
   BrightWay Solutions will benefit from the AI algorithms for optimal customer matches, helping them connect with consumers looking for their specific insurance offerings.

2. **Real-Time Quote Availability:**  
   Consumers sourced via BrightWay Solutions will receive real-time quotes, allowing for a seamless customer experience.

3. **Analytics Dashboard:**  
   Access to Markellm’s analytics dashboard will provide BrightWay Solutions with insights into consumer behavior and market trends, assisting them in refining their insurance offerings.

4. **Customization Options:**  
   BrightWay Solutions may request customizations to their listing page on Markellm, within the capabilities of the platform.

### Support
1. **Dedicated Customer Support:**  
   BrightWay Solutions will have access to a dedicated support team from Insurellm during standard business hours (9 AM - 7 PM EST).

2. **Additional Support Services:**  
   Technical support for integration and maintenance will be available. An optional premium support package can be purchased for $49.99/month, which includes 24/7 support and advanced troubleshooting.

3. **Training and Onboarding:**  
   Insurellm agrees to provide one free training session on how to utilize the Markellm platform effectively for BrightWay Solutions’ team upon contract signing.

### Signatures
By signing below, both parties agree to the terms and conditions outlined in this Contract.

__________________________  
**[Name], [Title]**  
**Insurellm**  
Date: ______________________

__________________________  
**[Name], [Title]**  
**BrightWay Solutions**  
Date: ______________________

---

This document serves as a formal agreement between Insurellm and BrightWay Solutions, ensuring a successful partnership focused on enhancing the insurance shopping experience for consumers.


---

<a id="file-week5-knowledge-base-contracts-contract-with-connectinsure-agency-for-markellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with ConnectInsure Agency for Markellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with ConnectInsure Agency for Markellm.md`

# Contract with ConnectInsure Agency for Markellm

**Contract Date:** February 28, 2025
**Contract Number:** MK-2025-0056

---

## Terms

1. **Parties Involved**: This contract is entered into between Insurellm, Inc. ("Provider") and ConnectInsure Agency ("Client").

2. **Service Commencement**: Services will commence on March 1, 2025.

3. **Contract Duration**: This Agreement shall remain in effect for 18 months from the commencement date, ending August 31, 2026.

4. **Fee Structure**: ConnectInsure Agency agrees to a hybrid pricing model:
   - Basic Listing Fee: $199/month for featured placement on the Markellm platform
   - Performance-Based Pricing: $25 per qualified lead generated through Markellm
   - Premium Analytics Package (optional): $99/month for enhanced data insights and reporting

5. **Lead Volume Expectations**: Based on ConnectInsure's profile, Markellm projects 80-120 qualified leads per month, resulting in estimated monthly costs of $2,199-$3,199.

6. **Payment Terms**:
   - Monthly listing fee due on the 1st of each month
   - Performance-based fees invoiced monthly on the 5th for prior month activity
   - Payment due within 15 days of invoice via ACH or credit card

7. **Lead Quality Standards**: Qualified leads meet the following criteria:
   - Valid contact information (verified phone and email)
   - Active insurance shopping intent (quote request within 7 days)
   - Geographic coverage within ConnectInsure's operating territories
   - Products matching ConnectInsure's offerings

8. **Dispute Resolution**: Lead quality disputes must be submitted within 5 business days with documentation. Insurellm will credit for validated low-quality leads.

## Renewal

1. **Automatic Renewal**: This agreement automatically renews for successive 6-month terms unless either party provides written notice of non-renewal at least 30 days before expiration.

2. **Fee Adjustments**: Listing fees and performance fees may be adjusted annually with 60 days' written notice. Historical average: 5-8% annual adjustment.

## Features

1. **AI-Powered Matching**: ConnectInsure Agency will benefit from Markellm's sophisticated matching:
   - Consumer needs analysis with ML algorithms
   - Product-to-need matching across auto, home, life, health insurance
   - Geographic and specialty matching
   - Price range and coverage preference alignment
   - Consumer demographic matching to ConnectInsure's sweet spot

2. **Featured Listing**: Premium marketplace placement including:
   - Enhanced agency profile with logo, photos, testimonials
   - Badges for specializations (e.g., "High-Risk Auto Specialist", "Multi-Policy Expert")
   - Priority positioning in search results
   - Featured placement in relevant consumer matches
   - Up to 10 agent profiles within agency listing

3. **Real-Time Quote Integration**: Technology enabling:
   - API integration with ConnectInsure's quoting systems
   - Real-time rate display to consumers
   - Competitive positioning insights
   - Quote abandonment recovery campaigns

4. **Lead Management Portal**: Comprehensive tools for:
   - Real-time lead notifications (SMS, email, push)
   - Lead routing to specific agents based on specialty
   - Follow-up task management and CRM integration
   - Lead status tracking (contacted, quoted, sold, declined)
   - Performance analytics by agent and product line

5. **Data Insights**: Analytics dashboard providing:
   - Lead volume trends and forecasting
   - Conversion rate analysis
   - Cost per acquisition metrics
   - Competitive benchmarking (anonymized)
   - Consumer behavior insights
   - Product mix recommendations

6. **Consumer Reviews**: Reputation management:
   - Consumer rating and review collection
   - Response management for reviews
   - Review showcase on agency profile
   - Negative review mediation support

7. **Marketing Support**: Platform-provided marketing:
   - Co-branded marketing materials
   - Email drip campaigns to warm leads
   - Social media content suggestions
   - Seasonal campaign participation
   - Referral program integration

## Support

1. **Technical Support**: ConnectInsure Agency will receive:
   - Email and phone support Monday-Friday 8 AM - 6 PM EST
   - Response time: 24 hours for standard inquiries
   - Online help center and FAQ
   - Video tutorials for platform features

2. **Onboarding**: Implementation includes:
   - 2-week onboarding process
   - Platform training for up to 5 agency staff (3 hours total)
   - Profile optimization consultation
   - Quote integration setup (if applicable)
   - CRM integration assistance

3. **Account Management**:
   - Named account manager with monthly check-ins
   - Quarterly performance reviews
   - Lead quality monitoring and optimization
   - Competitive positioning recommendations
   - Best practices sharing from top-performing agencies

4. **Platform Updates**:
   - Regular feature enhancements
   - Mobile app updates
   - Consumer experience improvements
   - New product line additions
   - Advance notice of major changes (minimum 14 days)

5. **Marketing Assistance**:
   - Quarterly marketing strategy consultations
   - Campaign performance analysis
   - Consumer trend reports
   - Co-marketing opportunity identification

---

**Signatures:**

**Insurellm, Inc.**
Michael Torres, Chief Revenue Officer
Date: February 28, 2025

**ConnectInsure Agency**
Brian Foster, Agency Principal
Date: February 28, 2025

---

This contract enables ConnectInsure Agency to leverage Markellm's AI-powered marketplace to connect with qualified insurance shoppers and grow their business through data-driven lead generation.


---

<a id="file-week5-knowledge-base-contracts-contract-with-continental-commercial-group-for-bizllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Continental Commercial Group for Bizllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Continental Commercial Group for Bizllm.md`

# Contract with Continental Commercial Group for Bizllm

**Contract Date:** April 12, 2025
**Contract Number:** BZ-2025-E-0147
**Parties:**
- Insurellm, Inc.
- Continental Commercial Group, Inc.

---

## Terms

1. **Coverage:** Insurellm agrees to provide Continental Commercial Group with comprehensive access to the Bizllm Enterprise platform, including white-label capabilities, dedicated infrastructure, and full API access for commercial insurance operations across all 50 US states.

2. **Duration:** This agreement is effective for a period of 36 months from the contract date, with provisions for early renewal discussions at the 24-month mark.

3. **Payment:** Continental Commercial Group shall pay custom Enterprise pricing of $42,000 per month for the first 12 months, with pricing review and adjustment for years 2-3 based on usage metrics and expanded feature adoption.

4. **Confidentiality:** Both parties agree to maintain the highest level of confidentiality regarding proprietary algorithms, trade secrets, customer data, and business strategies disclosed during this partnership.

5. **Liability:** Insurellm's liability is limited to direct damages not exceeding the annual contract value. Continental Commercial Group maintains $25 million in cybersecurity insurance covering data breaches.

6. **Service Level Agreement (SLA):** Insurellm guarantees 99.9% platform uptime, measured monthly. For each 0.1% below target, Continental receives a 5% monthly fee credit, up to a maximum of 25% monthly credit.

7. **Exclusivity:** Continental Commercial Group receives exclusive use of Bizllm in the specialty construction insurance vertical for the contract duration within North America.

---

## Renewal

This agreement includes a mutual 90-day renewal notice period. Continental Commercial Group receives right of first refusal on any new Bizllm features or modules developed for the commercial insurance sector. Renewal terms will be negotiated based on platform evolution, competitive landscape, and business performance metrics.

---

## Features

Continental Commercial Group will receive the complete Bizllm Enterprise suite:

1. **White-Label Customization:** Full platform branding with Continental's logos, color schemes, and custom domain names for client-facing portals.

2. **Dedicated Cloud Infrastructure:** Private cloud deployment with dedicated servers, ensuring data isolation and optimized performance for Continental's 200+ concurrent users.

3. **Unlimited API Access:** Full API integration capabilities with no call volume limits, enabling seamless connection to Continental's existing tech stack including:
   - Duck Creek policy administration system
   - Guidewire ClaimCenter
   - Custom data warehouse and business intelligence platforms
   - Third-party data providers (Verisk, ISO, Dun & Bradstreet)

4. **Advanced Cyber Risk Module:** Comprehensive cyber insurance underwriting tools including:
   - Automated security posture assessment
   - Breach history analysis and dark web monitoring
   - IT infrastructure vulnerability scanning
   - Ransomware risk scoring

5. **Custom Product Configuration:** Ability to configure and deploy unlimited custom commercial insurance products, including specialty lines such as:
   - Construction surety and wrap-up programs
   - Environmental liability
   - Directors and officers (D&O) coverage
   - Employment practices liability (EPLI)

6. **Predictive Analytics Engine:** Machine learning models for:
   - Loss forecasting and reserve adequacy
   - Optimal pricing recommendations
   - Renewal probability scoring
   - Cross-sell and upsell opportunity identification

7. **Agent Network Management:** Enterprise-grade agent portal supporting Continental's 3,500+ independent agents with hierarchical permissions, customizable commission structures, and real-time policy binding.

8. **Regulatory Compliance Suite:** Automated compliance monitoring for all 50 states including form filing, rate approval tracking, and surplus lines requirements.

---

## Support

Insurellm commits to comprehensive Enterprise-level support:

1. **Dedicated Success Team:**
   - Named Chief Customer Officer oversight
   - Dedicated Technical Account Manager (TAM)
   - Solutions architect for ongoing optimization
   - Quarterly executive business reviews with C-suite participation

2. **24/7/365 Support:**
   - Guaranteed 15-minute response time for critical issues
   - 1-hour response for high-priority issues
   - Dedicated Slack channel for real-time communication
   - Monthly system health reports and optimization recommendations

3. **Implementation and Onboarding:**
   - 6-month implementation program with dedicated project manager
   - Comprehensive training for up to 150 Continental staff members
   - Custom training materials and certification program
   - On-site support during first 90 days of production operation

4. **Development and Customization:**
   - 500 hours annually of custom development included
   - Priority feature requests with guaranteed evaluation
   - Beta access to all new features 60 days before general release
   - Input into product roadmap and strategic direction

5. **Data Services:**
   - Quarterly data quality audits
   - Annual data migration support for system upgrades
   - Dedicated data warehouse with 7-year retention
   - Custom reporting and analytics dashboard development

6. **Performance Optimization:**
   - Monthly platform performance reviews
   - Proactive capacity planning and scaling recommendations
   - Load testing before major product launches
   - Dedicated infrastructure monitoring with real-time alerts

---

**Signatures:**

_________________________________
**Jennifer Rodriguez**
**Title**: Chief Executive Officer
**Insurellm, Inc.**
**Date**: April 12, 2025

_________________________________
**Thomas Wellington**
**Title**: President & Chief Operating Officer
**Continental Commercial Group, Inc.**
**Date**: April 12, 2025

---

This agreement represents a strategic partnership between Insurellm and Continental Commercial Group to transform commercial insurance operations through cutting-edge technology and innovation. This contract supersedes all prior agreements and represents the complete understanding between both parties.


---

<a id="file-week5-knowledge-base-contracts-contract-with-drivesmart-insurance-for-carllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with DriveSmart Insurance for Carllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with DriveSmart Insurance for Carllm.md`

# Contract with DriveSmart Insurance for Carllm

**Contract Date:** March 20, 2025
**Contract Number:** CR-2025-E-0078
**Parties:**
- Insurellm, Inc.
- DriveSmart Insurance Corp.

---

## Terms

1. **Coverage:** Insurellm agrees to provide DriveSmart Insurance with enterprise access to the Carllm platform, including white-label capabilities, unlimited user licenses, dedicated infrastructure, and full API access for their multi-state auto insurance operations.

2. **Duration:** This agreement is effective for a period of 36 months from the contract date.

3. **Payment:** DriveSmart Insurance shall pay custom Enterprise Tier pricing of $18,000 per month for the first 12 months, $19,500 per month for months 13-24, and $21,000 per month for months 25-36, totaling $702,000 over the contract term.

4. **Policy Volume**: Enterprise Tier supports unlimited policies. DriveSmart currently has 85,000 active auto policies across 8 states.

5. **Service Level Agreement:** Insurellm guarantees 99.9% platform uptime measured monthly, with 8% monthly credit for each 0.1% below target, maximum 40% monthly credit.

6. **Confidentiality:** Both parties agree to maintain strict confidentiality of proprietary algorithms, driver data, pricing models, and business strategies.

7. **Data Security:** Insurellm maintains SOC 2 Type II compliance, annual penetration testing, and comprehensive cyber insurance coverage.

---

## Renewal

This agreement includes a 90-day mutual renewal notice period. DriveSmart receives most-favored-customer pricing guarantees ensuring competitive rates at renewal. Contract may be extended in 12 or 24-month increments.

---

## Features

DriveSmart Insurance will receive the complete Carllm Enterprise suite:

1. **Unlimited Policy Administration:** Full support for DriveSmart's 85,000+ policies with scalability to 500,000+ policies.

2. **White-Label Platform:** Complete customization:
   - Custom domains (quote.drivesmartinsurance.com, portal.drivesmartinsurance.com)
   - Branded mobile apps for iOS and Android
   - Customized marketing materials and quote tools
   - Co-branded agent portals

3. **Advanced AI Risk Assessment:** Enterprise-grade risk analysis:
   - Real-time driver behavior analysis from telematics devices
   - Vehicle condition assessment from VIN decoding and maintenance records
   - Claims history analysis across all carriers (LexisNexis, CLUE)
   - Credit-based insurance scoring
   - Geographic risk modeling with granular loss costs
   - Multi-car and multi-driver household optimization
   - Commercial auto risk assessment capabilities

4. **Instant Quoting Engine:** High-performance quoting:
   - Sub-3-second quote generation
   - Real-time rate optimization across 50+ rating factors
   - Competitive intelligence with market positioning
   - Dynamic pricing based on demand and capacity
   - Multi-product bundling discounts (auto + home)
   - A/B testing capabilities for pricing strategies

5. **Customizable Coverage Plans:** Flexible product configuration:
   - State-specific coverage options (all 8 operating states)
   - Usage-based insurance (UBI) programs
   - Pay-per-mile options
   - Rideshare and delivery driver coverage
   - Classic and collector car programs
   - SR-22 and high-risk driver programs

6. **Advanced Fraud Detection:** Comprehensive fraud prevention:
   - Application fraud detection (identity verification, address validation)
   - Claims fraud analytics with pattern recognition
   - Agent fraud monitoring
   - Staged accident detection
   - Social network analysis for fraud rings
   - Integration with NICB and SIU databases

7. **Customer Insights Dashboard:** Deep analytics:
   - Real-time policy metrics and KPIs
   - Retention and churn analysis
   - Loss ratio tracking by segment
   - Agent performance analytics
   - Marketing campaign ROI measurement
   - Customer lifetime value prediction

8. **Telematics Integration:** Complete telematics platform:
   - Device-agnostic integration (OBD-II dongles, smartphone apps, embedded)
   - Real-time driver behavior scoring
   - Trip-level data analysis (hard braking, acceleration, cornering, speeding)
   - Mileage verification for low-mileage discounts
   - Accident detection and emergency response
   - Driver coaching and feedback programs
   - Gamification and safe driving rewards

9. **Complete API Access:** Unlimited API calls:
   - Integration with DriveSmart's core systems
   - Agent management system connectivity
   - Third-party data providers (LexisNexis, Verisk, Experian)
   - DMV and MVR integrations
   - Payment processing systems
   - Document management platforms
   - Marketing automation tools

10. **Multi-State Operations:** Comprehensive state support:
    - State-specific forms and endorsements
    - Regulatory compliance monitoring
    - Rate filing management
    - Multi-state agent licensing tracking
    - Surplus lines support where needed

---

## Support

Insurellm commits to comprehensive Enterprise-level support for DriveSmart Insurance:

1. **Dedicated Success Team:**
   - Named VP-level executive sponsor with quarterly reviews
   - Senior Customer Success Manager with weekly check-ins
   - Technical Account Manager for optimization
   - Solutions Architect for strategic initiatives
   - Quarterly executive business reviews with ROI analysis

2. **24/7/365 Support:**
   - 30-minute response time for P1 critical issues
   - 2-hour response for P2 high-priority issues
   - 4-hour response for P3 standard issues
   - Dedicated support hotline with no phone tree
   - Private Slack channel with engineering team
   - Quarterly on-site visits (minimum 4 per year)

3. **Implementation:**
   - 6-month phased implementation
   - Dedicated project manager
   - Migration of 85,000 policies from legacy system
   - Training for 75+ staff and 200+ agents
   - Parallel processing for 60 days
   - Go-live support (4 weeks on-site)

4. **Training and Enablement:**
   - Role-based training for all users
   - Train-the-trainer program
   - Annual user conference attendance (5 attendees)
   - Monthly training webinars
   - Unlimited online learning access
   - Custom training materials

5. **Custom Development:**
   - 800 hours annually of custom development
   - Priority feature requests on product roadmap
   - Beta access to new features 60 days early
   - Co-development opportunities

6. **Integration Services:**
   - Integration with DriveSmart's systems:
     - Duck Creek policy administration
     - Applied Epic agency management
     - Guidewire ClaimCenter
     - Telematics providers (Arity, Cambridge Mobile Telematics)
     - Payment processors
     - Salesforce CRM
   - Dedicated integration specialist
   - Quarterly integration reviews

7. **Analytics and Reporting:**
   - Custom dashboard development (up to 15 dashboards)
   - Automated daily, weekly, monthly reporting
   - Ad-hoc analytics support (20 requests/month)
   - Industry benchmarking
   - Predictive modeling consultation

8. **Continuous Improvement:**
   - Quarterly optimization workshops
   - Annual efficiency audits
   - Best practice sharing
   - Innovation lab for emerging tech (AI, IoT, connected cars)

---

**Signatures:**

_________________________________
**Jennifer Rodriguez**
**Title**: Chief Executive Officer
**Insurellm, Inc.**
**Date**: March 20, 2025

_________________________________
**Steven Brooks**
**Title**: President & Chief Operating Officer
**DriveSmart Insurance Corp.**
**Date**: March 20, 2025

---

This agreement establishes DriveSmart Insurance as a premier enterprise partner leveraging Carllm's advanced AI and telematics capabilities to transform auto insurance operations. This contract supersedes all prior agreements.


---

<a id="file-week5-knowledge-base-contracts-contract-with-everguard-insurance-for-rellm---ai-powered-enterprise-reinsurance-solution-md"></a>
## File: `week5/knowledge-base/contracts/Contract with EverGuard Insurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with EverGuard Insurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md`

# Contract with EverGuard Insurance for Rellm: AI-Powered Enterprise Reinsurance Solution

**Contract Number:** IG-2023-EG  
**Effective Date:** January 1, 2024  
**Expiration Date:** December 31, 2026  

## Terms

1. **Parties**: This agreement is made between Insurellm, located at 123 Innovation Drive, Tech City, USA, and EverGuard Insurance, located at 456 Safety Lane, Protectville, USA.
   
2. **Product Description**: This contract pertains to the use of the Rellm platform, an AI-powered enterprise reinsurance solution provided by Insurellm. EverGuard Insurance will implement Rellm to enhance its reinsurance operations.

3. **Payment Terms**: EverGuard Insurance agrees to pay Insurellm a monthly fee of $10,000 for the duration of this contract, covering the Professional Plan features of Rellm, which includes all advanced integrations and priority customer support.

4. **Usage Rights**: EverGuard Insurance is granted a non-exclusive, non-transferable license to access and use Rellm for the duration of this contract. Unauthorized sharing or distribution is strictly prohibited.

## Renewal

1. **Automatic Renewal**: This contract will automatically renew for successive one-year terms unless either party provides written notice of termination at least 60 days prior to the expiration date.

2. **Price Adjustment**: In the event of a renewal, Insurellm reserves the right to adjust the monthly fee based on market conditions and the value of services offered, with a minimum notice of 30 days.

## Features

1. **Core Functionality**: Rellm provides EverGuard Insurance with advanced AI-driven analytics, seamless integrations, and a comprehensive risk assessment module designed to optimize risk management.

2. **Customizable Dashboard**: Users at EverGuard Insurance will have access to a customizable dashboard that allows them to tailor their experience based on their specific operational metrics.

3. **Compliance Tools**: The built-in regulatory compliance tools will ensure that EverGuard Insurance meets industry standards while managing its reinsurance practices.

4. **Client Portal Access**: EverGuard Insurance will have access to both client and broker portals, enhancing communication and collaboration with its partners.

## Support

1. **Customer Support**: Insurellm will provide EverGuard Insurance with 24/7 customer support, including live chat, email, and phone assistance for any technical issues or inquiries regarding Rellm.

2. **Training Services**: Insurellm will provide initial training for EverGuard Insurance staff to ensure proper utilization of Rellm features. Additional training sessions can be scheduled upon request at an agreed fee.

3. **Updates and Upgrades**: EverGuard Insurance will receive all platform updates and upgrades at no additional cost during the contract term, including enhancements outlined in Insurellm’s 2025-2026 roadmap.

4. **Feedback Mechanisms**: EverGuard Insurance is encouraged to provide feedback regarding Rellm’s functionalities and any desired features, which will be considered for future updates.

---

**Signatures**  
**For Insurellm**: __________________________  
**Name**: John Smith  
**Title**: Chief Operating Officer  
**Date**: _________________  

**For EverGuard Insurance**: __________________________  
**Name**: Sarah Johnson  
**Title**: Chief Executive Officer  
**Date**: _________________  

--- 

This contract seeks to foster a strong partnership between Insurellm and EverGuard Insurance, leveraging Rellm to innovate and enhance reinsurance capabilities while ensuring mutual growth and compliance in the ever-evolving insurance landscape.


---

<a id="file-week5-knowledge-base-contracts-contract-with-evergreen-life-insurance-for-lifellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Evergreen Life Insurance for Lifellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Evergreen Life Insurance for Lifellm.md`

# Contract with Evergreen Life Insurance for Lifellm

**Contract Date:** January 20, 2025
**Contract Number:** LF-2025-0012
**Parties:**
- Insurellm, Inc.
- Evergreen Life Insurance Company

---

## Terms

1. **Coverage:** Insurellm agrees to provide Evergreen Life Insurance with access to the Lifellm platform, enabling AI-powered life insurance underwriting, policy administration, and risk assessment for individual and group life policies.

2. **Duration:** This agreement is effective for a period of 12 months from the contract date, with automatic renewal provisions unless terminated with 30-day written notice.

3. **Payment:** Evergreen Life Insurance shall pay a monthly fee of $3,500, due by the 5th of every month for the Starter Tier package.

4. **Policy Volume:** Starter Tier supports underwriting and administration for up to 2,000 active policies. Current baseline: 1,400 policies.

5. **Confidentiality:** Both parties agree to maintain strict confidentiality of proprietary underwriting models, policyholder health information (PHI), and business strategies.

6. **HIPAA Compliance:** Insurellm maintains full HIPAA compliance for all health data processed through the Lifellm platform.

7. **Liability:** Insurellm's liability is limited to direct damages not exceeding the total fees paid in the preceding 6 months.

---

## Renewal

Unless either party provides written notice of termination at least 30 days prior to contract expiration, this agreement automatically renews for successive 12-month terms under the same terms, subject to pricing adjustments with 60 days' advance notice (capped at 10% annual increase).

---

## Features

Evergreen Life Insurance will receive the following Starter Tier features:

1. **AI-Powered Underwriting:** Accelerated underwriting process analyzing:
   - Medical histories and prescription databases (Milliman IntelliScript)
   - Motor vehicle records (MVRs)
   - Credit-based insurance scores
   - Lifestyle and occupation risk factors
   - Automated underwriting decisions for standard risks

2. **Risk Assessment:** AI-driven mortality risk modeling considering:
   - Age, gender, and family medical history
   - Current health conditions and lab values
   - Tobacco and alcohol use
   - High-risk activities and occupations

3. **Automated Policy Management:**
   - Digital policy issuance and delivery
   - Beneficiary management and updates
   - Premium calculation and billing integration
   - Coverage adjustments and conversions
   - Policy reinstatement processing

4. **Smart Document Processing:** OCR and NLP extraction from:
   - Medical records and attending physician statements (APS)
   - Lab results and paramedical exams
   - Application forms
   - Financial documentation

5. **Customer Portal:** Policyholder self-service portal featuring:
   - Policy document access
   - Beneficiary updates
   - Premium payment processing
   - Coverage summary and statements
   - Digital insurance cards

6. **Regulatory Compliance:** Built-in compliance monitoring for:
   - State insurance regulations
   - NAIC model laws and regulations
   - Anti-money laundering (AML) requirements
   - Policy form approvals

7. **Basic Analytics:** Standard dashboards tracking:
   - Application submission and approval rates
   - Average underwriting cycle time
   - Policy persistency and lapse rates
   - Face amount in force

---

## Support

Insurellm commits to providing comprehensive support to Evergreen Life Insurance:

1. **Onboarding:** 2-week implementation program including:
   - System configuration and setup
   - Training for up to 8 underwriters and administrators
   - Integration with Evergreen's policy administration system
   - Data migration from legacy system (up to 1,400 policies)

2. **Technical Support:**
   - Email and phone support Monday-Friday 8 AM - 6 PM EST
   - Response time: 12 hours for critical issues, 24 hours for standard
   - Online ticketing system for issue tracking
   - Knowledge base and FAQ access

3. **Platform Updates:**
   - Quarterly feature releases
   - Monthly security patches and improvements
   - Advance notice of updates (minimum 14 days)
   - Release notes and user documentation

4. **Account Management:**
   - Named customer success manager
   - Semi-annual business review meetings
   - Usage analytics and optimization recommendations
   - Assistance with tier upgrade when volume grows

5. **Compliance Support:**
   - Annual compliance review and audit support
   - Regulatory update notifications
   - State insurance department filing assistance

---

**Signatures:**

_________________________________
**Michael Torres**
**Title**: Chief Revenue Officer
**Insurellm, Inc.**
**Date**: January 20, 2025

_________________________________
**Catherine Wu**
**Title**: Chief Underwriting Officer
**Evergreen Life Insurance Company**
**Date**: January 20, 2025

---

This agreement enables Evergreen Life Insurance to modernize their life insurance operations with AI-powered underwriting and administration technology.


---

<a id="file-week5-knowledge-base-contracts-contract-with-fasttrack-insurance-services-for-claimllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with FastTrack Insurance Services for Claimllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with FastTrack Insurance Services for Claimllm.md`

# Contract with FastTrack Insurance Services for Claimllm

**Contract Date:** May 10, 2025
**Contract Number:** CL-2025-0234

---

## Terms

1. **Parties Involved**: This contract is entered into between Insurellm, Inc. ("Provider") and FastTrack Insurance Services ("Client") on May 10, 2025.

2. **License Grant**: Insurellm grants FastTrack Insurance Services a non-exclusive, non-transferable license to use the Claimllm Advanced Tier platform.

3. **Payment Terms**: FastTrack Insurance Services agrees to make monthly payments of $9,500 for the duration of this 18-month contract, totaling $171,000. Payments due on the 1st of each month.

4. **Claims Volume**: Advanced Tier supports up to 25,000 claims annually. FastTrack projects 22,000 claims in year 1.

5. **Confidentiality**: Both parties shall maintain confidentiality regarding each other's proprietary information for the contract duration plus 5 years post-termination.

## Renewal

1. **Automatic Renewal**: This contract automatically renews for successive 12-month terms unless either party provides written notice of non-renewal at least 45 days prior to expiration.

2. **Pricing Review**: Renewal pricing will be discussed 60 days prior to term end. Price increases limited to 8% annually.

## Features

1. **Included Features**: FastTrack Insurance Services will have access to Claimllm Advanced Tier features:
   - Intelligent FNOL Processing with multi-channel intake
   - Automated Triage and Routing with ML algorithms
   - Computer Vision Damage Assessment for auto and property claims
   - Predictive Fraud Detection with network analysis
   - Smart Document Processing with OCR and NLP
   - Dynamic Reserve Setting with AI-powered modeling
   - Vendor Management Platform for 150+ vendors
   - Payment Automation with multi-party splits
   - Claimant Communication Hub (SMS, email, app)
   - Advanced Analytics and reporting dashboards

2. **Integration Capabilities**: API integration with FastTrack's existing claims systems (Guidewire, Duck Creek compatibility).

3. **Mobile Access**: Full-featured mobile app for adjusters in the field with offline capability.

## Support

1. **Customer Support**: Insurellm will provide priority support to FastTrack Insurance Services:
   - Dedicated support team available Monday-Saturday 6 AM - 8 PM EST
   - Emergency support 24/7 for critical issues
   - Response time: 3 hours for critical, 8 hours for standard

2. **Training**: Comprehensive training program:
   - 3-week implementation with dedicated project manager
   - Training for up to 30 claims staff members
   - Quarterly refresher webinars
   - Online knowledge base access

3. **System Updates**: Regular platform enhancements pushed monthly with advance notification. Maintenance windows on Sundays 12 AM - 4 AM EST.

---

**Signatures:**

**Insurellm, Inc.**
Sarah Chen, VP of Sales
Date: May 10, 2025

**FastTrack Insurance Services**
Rebecca Martinez, COO
Date: May 10, 2025

---

This contract represents the agreement between Insurellm and FastTrack Insurance Services for streamlined, AI-powered claims processing operations.


---

<a id="file-week5-knowledge-base-contracts-contract-with-fortress-business-underwriters-for-bizllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Fortress Business Underwriters for Bizllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Fortress Business Underwriters for Bizllm.md`

# Contract with Fortress Business Underwriters for Bizllm

---

## Terms

1. **Agreement Effective Date**: This contract is effective as of February 1, 2025.
2. **Duration**: This agreement will remain in effect for a term of 24 months, concluding on January 31, 2027.
3. **Subscription Type**: Fortress Business Underwriters agrees to subscribe to the **Professional Tier** of Bizllm, at a cost of $12,000/month, totaling $288,000 for the duration of this contract.
4. **Payment Terms**: Payments are due on the 5th of each month. Late payments will incur a penalty of 2% per month.
5. **Scope of Use**: License covers up to 50 named users within Fortress Business Underwriters' organization, with additional user licenses available at $150/month per user.
6. **Termination Clause**: Either party may terminate this agreement with 60 days' written notice prior to the end of the term. If terminated early, a termination fee equal to 25% of remaining contract value will apply.

---

## Renewal

1. **Automatic Renewal**: This agreement will automatically renew for an additional 24-month term unless either party provides written notice of non-renewal at least 60 days before the expiration date.
2. **Price Adjustments**: Subscription fees may be adjusted for the renewal term based on Consumer Price Index (CPI) changes or enhanced feature availability, with 90 days' prior notice provided to Fortress Business Underwriters.
3. **Upgrade Options**: Client may upgrade to Enterprise Tier at any time with 30 days' notice and prorated pricing adjustment.

---

## Features

1. **Access to Professional Tier Features**: Fortress Business Underwriters will have access to all Professional Tier features, including:
   - Multi-Line Underwriting Engine for general liability, professional liability, property, workers' comp, and cyber insurance
   - Business Intelligence Integration with automated data gathering
   - Cyber Risk Assessment with digital security posture evaluation
   - Workers' Compensation Optimization tools
   - Commercial Property Evaluation with catastrophe modeling
   - Professional Liability Specialization for multiple industry sectors
   - Portfolio Management Dashboard with predictive analytics
   - Agent and Broker Portal with commission tracking
   - Claims Management Integration with AI-powered subrogation identification

2. **Advanced Analytics**: Access to enhanced reporting capabilities including loss ratio analysis, geographic heat maps, and competitive benchmarking tools.

3. **API Access**: Limited API access for integrating Bizllm with existing underwriting workbenches and agency management systems (up to 100,000 API calls/month).

4. **Custom Workflows**: Ability to configure up to 10 custom underwriting workflows tailored to Fortress's specific business lines and risk appetites.

---

## Support

1. **Technical Support**: Fortress Business Underwriters will receive priority technical support from Insurellm, including:
   - Dedicated account manager with monthly check-ins
   - 24/7 emergency technical support hotline
   - Response time guarantee: 2 hours for critical issues, 8 hours for standard issues

2. **Training**: Insurellm will provide:
   - Initial comprehensive onboarding (40 hours) for up to 20 staff members
   - Quarterly advanced training sessions on new features and best practices
   - Access to online learning portal with video tutorials and documentation
   - Annual certification program for power users

3. **Updates and Maintenance**:
   - Monthly platform updates with new features and enhancements
   - Scheduled maintenance windows: Saturday 11 PM - Sunday 3 AM EST
   - Minimum 72 hours advance notice for all planned maintenance
   - Zero-downtime updates for non-critical improvements

4. **Integration Support**: Dedicated integration specialist to assist with:
   - Connection to policy administration systems (Duck Creek, Guidewire, etc.)
   - Data migration from legacy underwriting platforms
   - Third-party data provider integrations (Verisk, LexisNexis, CoreLogic)

---

**Signatures:**

_________________________________
**Michael Torres**
**Title**: Chief Revenue Officer
**Insurellm, Inc.**
**Date**: February 1, 2025

_________________________________
**Robert Chen**
**Title**: Chief Underwriting Officer
**Fortress Business Underwriters**
**Date**: February 1, 2025

---

*This contract outlines the terms of the relationship between Insurellm and Fortress Business Underwriters for the Bizllm product, establishing a partnership to transform commercial insurance underwriting operations.*


---

<a id="file-week5-knowledge-base-contracts-contract-with-globalre-partners-for-rellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with GlobalRe Partners for Rellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with GlobalRe Partners for Rellm.md`

# Contract with GlobalRe Partners for Rellm - AI-Powered Enterprise Reinsurance Solution

**Contract Date:** April 28, 2025
**Contract Number:** RE-2025-E-0203
**Parties:**
- Insurellm, Inc.
- GlobalRe Partners International, Ltd.

---

## Terms

1. **Coverage:** Insurellm agrees to provide GlobalRe Partners with enterprise access to the Rellm platform, including white-label capabilities, unlimited treaty and facultative reinsurance administration, dedicated infrastructure, and full API access for their global reinsurance operations.

2. **Duration:** This agreement is effective for a period of 48 months from the contract date, representing Insurellm's most strategic long-term reinsurance partnership.

3. **Payment:** GlobalRe Partners shall pay custom Enterprise Tier pricing of $45,000 per month for months 1-12, $48,000 per month for months 13-24, $52,000 per month for months 25-36, and $56,000 per month for months 37-48, totaling $2,412,000 over the contract term.

4. **Reinsurance Volume**: Enterprise Tier supports unlimited treaties and facultative certificates. GlobalRe currently manages 450+ treaty relationships and 8,000+ facultative placements annually.

5. **Service Level Agreement:** Insurellm guarantees 99.95% platform uptime measured monthly, with 10% monthly credit for each hour of unplanned downtime, maximum 50% monthly credit.

6. **Confidentiality:** Both parties agree to maintain the highest level of confidentiality regarding proprietary AI algorithms, reinsurance pricing models, cedent data, catastrophe modeling, and strategic initiatives.

7. **Data Security:** Insurellm maintains SOC 2 Type II compliance, ISO 27001 certification, and annual third-party security audits with penetration testing.

8. **Business Continuity:** Guaranteed 2-hour recovery time objective (RTO) and 30-minute recovery point objective (RPO) with geographically diverse data centers.

9. **Global Operations:** Platform supports multi-currency (35+ currencies), multi-language (12 languages), and multi-jurisdiction regulatory compliance.

---

## Renewal

This agreement includes a mutual 120-day renewal notice period. GlobalRe Partners receives most-favored-customer pricing guarantees and priority access to all new reinsurance features. Contract may be extended in 12 or 24-month increments with provisions for joint innovation initiatives in catastrophe modeling and climate risk analytics.

---

## Features

GlobalRe Partners will receive the complete Rellm Enterprise suite with advanced reinsurance capabilities:

1. **Unlimited Reinsurance Administration:** Full support for GlobalRe's 450+ treaty relationships and 8,000+ annual facultative placements with scalability to 1,000+ treaties and 50,000+ facultative certificates.

2. **White-Label Platform:** Complete branding customization:
   - Custom domains (portal.globalrepartners.com, cedents.globalrepartners.com, brokers.globalrepartners.com)
   - Branded portals for cedents, brokers, and retrocessionaires
   - Multi-language interface (English, Spanish, French, German, Mandarin, Japanese, Portuguese, Dutch, Italian, Korean, Arabic, Russian)
   - Customized reporting templates and market presentations

3. **Advanced AI-Driven Analytics:** Enterprise-grade reinsurance analytics:
   - Predictive risk modeling across all lines of business
   - Treaty portfolio optimization and capital allocation
   - Retrocessional optimization and protection tower design
   - Pricing analytics with market cycle intelligence
   - Loss development and IBNR prediction
   - Ultimate loss forecasting with confidence intervals
   - Reserve adequacy modeling
   - Commutation opportunity identification

4. **Comprehensive Risk Assessment Module:** State-of-the-art risk evaluation:
   - Cedent financial strength analysis with early warning indicators
   - Portfolio exposure aggregation across all treaties
   - Clash analysis and accumulation monitoring
   - Geographic concentration heat maps
   - Industry and line of business diversification metrics
   - Emerging risk identification (cyber, climate, pandemic)
   - Counterparty credit risk assessment
   - Retrocessional credit risk monitoring

5. **Catastrophe Modeling Integration:** Best-in-class CAT modeling:
   - Integration with all major vendors (RMS, AIR, CoreLogic, KCC)
   - Multi-peril catastrophe analysis
   - Probable maximum loss (PML) calculations at all return periods
   - Exceedance probability curves and tail value-at-risk
   - Climate change scenario modeling
   - Secondary uncertainty and model blending
   - Real-time CAT event tracking and loss estimation
   - Pre-CAT exposure management and post-CAT claims projection

6. **Treaty Administration:** Complete treaty lifecycle management:
   - Treaty structuring and quota share optimization
   - Excess of loss layer optimization
   - Sliding scale commission calculation
   - Loss corridor and aggregate deductible tracking
   - Reinstatement premium automation
   - Cash call processing and premium allocation
   - Loss reserve bordereaux processing
   - Treaty accounting and reconciliation
   - Multi-year contract administration

7. **Facultative Reinsurance Platform:** Comprehensive fac management:
   - Digital submission intake from brokers and cedents
   - AI-powered underwriting decision support
   - Automated risk grading and pricing recommendations
   - Peer pricing comparison and market intelligence
   - Quote generation with terms and conditions
   - Binder and certificate issuance
   - Premium and claims tracking by certificate
   - Portfolio monitoring and aggregation

8. **Customizable Dashboard:** Enterprise-grade analytics:
   - Real-time portfolio performance metrics
   - Combined ratio tracking by treaty, cedent, line of business, geography
   - Premium volume and growth analytics
   - Claims development and loss ratio trending
   - Reserve adequacy indicators
   - Capital utilization and ROE analysis
   - Market share and competitive positioning
   - Broker and cedent relationship metrics

9. **Regulatory Compliance Tools:** Global compliance support:
   - Multi-jurisdiction regulatory reporting (US, EU, UK, Asia-Pacific, Latin America)
   - Solvency II compliance for European operations
   - IFRS 17 reporting and analytics
   - US statutory accounting (SAP)
   - Tax reporting and withholding management
   - Sanctions screening (OFAC, UN, EU)
   - Anti-money laundering (AML) monitoring
   - Audit trail and documentation repository

10. **Client and Broker Portals:** Stakeholder engagement platforms:
    - Cedent portal for submissions, bordereaux, reports, and analytics
    - Broker portal for quote requests, binding, and commissions
    - Retrocessionaire portal for downstream placements
    - Real-time data sharing and document exchange
    - Secure messaging and collaboration tools
    - Mobile app access for on-the-go access
    - Customized views by relationship

11. **Complete API Access:** Unlimited API integration:
    - Real-time integration with GlobalRe's core systems
    - Accounting system integration (SAP, Oracle)
    - Data warehouse synchronization
    - Catastrophe modeling platform connectivity
    - Broker trading platforms (Ebix, Sequel)
    - Lloyd's platform integration (Whitespace, PPL)
    - Industry data providers (AM Best, S&P, Moody's)
    - Economic and market data feeds

12. **Advanced Retrocessional Management:** Retro optimization:
    - Retrocessional program structuring
    - Protection tower analytics and gap analysis
    - Retro market intelligence and pricing
    - Counterparty diversification optimization
    - Credit risk monitoring
    - Collateral management
    - Retro recovery tracking

13. **Climate Risk Analytics:** Forward-looking climate modeling:
    - IPCC climate scenario analysis (RCP 2.6, 4.5, 8.5)
    - Transition risk assessment
    - Physical risk modeling for perils (hurricane, wildfire, flood, drought)
    - Sea level rise impact analysis
    - Temperature trend incorporation
    - Climate-adjusted pricing recommendations
    - Stranded asset identification
    - Green reinsurance opportunities

---

## Support

Insurellm commits to comprehensive Enterprise-level support for GlobalRe Partners:

1. **Dedicated Success Team:**
   - Executive sponsor (CEO-level) with quarterly strategic reviews
   - Dedicated Senior Vice President of Customer Success with bi-weekly engagement
   - Technical Account Manager for platform optimization
   - Solutions Architect team (2 FTE) for strategic initiatives
   - Catastrophe modeling specialist for analytics support
   - Quarterly executive business reviews with C-suite participation from both organizations

2. **24/7/365 Premium Support:**
   - Guaranteed 10-minute response for P1 critical issues (during catastrophe events: 5 minutes)
   - 30-minute response for P2 high-priority issues
   - 2-hour response for P3 standard issues
   - Dedicated support team of 10+ specialists familiar with GlobalRe's operations
   - Named support engineers for each major functional area
   - Private collaboration channels (Slack, Microsoft Teams) with direct engineering access
   - Quarterly on-site support visits (minimum 8 per year, plus CAT event visits)

3. **Comprehensive Implementation:**
   - 18-month phased implementation program with 5 major releases
   - Dedicated program management office (PMO) with weekly steering committee meetings
   - Migration of 450+ treaty relationships and historical data (10 years)
   - Integration with 8,000+ facultative certificates
   - Training for 200+ GlobalRe staff across underwriting, actuarial, accounting, IT
   - Regional training sessions (North America, Europe, Asia)
   - Parallel processing with legacy systems for 6 months
   - Go-live support with 16-week on-site Insurellm team presence (8-12 people)

4. **Training and Enablement:**
   - Comprehensive role-based training (underwriters, actuaries, accountants, claim handlers, IT, executives)
   - Executive education on AI in reinsurance and emerging risk
   - Actuarial training on predictive modeling and machine learning
   - Catastrophe modeling workshop series
   - Train-the-trainer certification for GlobalRe's learning team
   - Annual user conference attendance (12 attendees, all expenses paid including travel)
   - Monthly advanced training webinars on new features
   - Unlimited online learning platform access with 150+ courses
   - Custom training content for GlobalRe-specific processes

5. **Custom Development:**
   - 4,000 hours annually of custom development included
   - Dedicated development team (6 developers, 2 QA, 1 PM) for GlobalRe-specific features
   - Priority feature requests with guaranteed product roadmap inclusion
   - Early access to beta features 120 days before general release
   - Joint innovation projects in climate risk, AI underwriting, blockchain
   - Co-development of industry-leading capabilities
   - Input into 5-year product strategy and vision

6. **Integration Services:**
   - Enterprise integration with GlobalRe's complex ecosystem:
     - SAP ERP for finance and accounting
     - Socotra reinsurance administration platform
     - RMS RiskLink catastrophe modeling
     - AIR Touchstone
     - Moody's RMS LifeRisks
     - Sequel broker trading platform
     - Lloyd's Whitespace and PPL
     - ACORD messaging standards
     - SWIFT for payments
     - Data warehouse on Snowflake
     - Tableau and PowerBI for analytics
   - Dedicated integration team (3 FTE integration engineers)
   - Monthly integration health assessments
   - Performance optimization and load testing
   - API governance and versioning support

7. **Analytics and Reporting:**
   - Custom dashboard development (unlimited)
   - Real-time operational dashboards for underwriting, claims, accounting
   - Executive dashboards with strategic KPIs
   - Automated reporting suite (daily, weekly, monthly, quarterly, annual)
   - Regulatory reporting templates for all jurisdictions
   - Ad-hoc analytics support (unlimited requests with 24-hour SLA for standard, 4-hour for urgent)
   - Industry benchmarking against top 50 global reinsurers
   - Catastrophe exposure and PML reporting
   - Predictive analytics and scenario modeling consultation (bi-weekly sessions)
   - Embedded actuarial and data science team support

8. **Catastrophe Response:**
   - Dedicated CAT war room activation during major events
   - Real-time loss estimation and exposure reporting
   - Claims projections and reserve recommendations
   - Cedent outreach and data collection coordination
   - Retrocessional recovery tracking
   - Post-CAT analysis and lessons learned
   - Annual CAT preparedness exercises and disaster recovery testing

9. **Regulatory and Compliance Support:**
   - Quarterly compliance reviews for all operating jurisdictions
   - Annual regulatory update briefings
   - Solvency II and IFRS 17 implementation support
   - Audit preparation and documentation assistance
   - Regulatory examination support
   - Industry association engagement (IAIS, NAIC, EIOPA)

10. **Continuous Improvement:**
    - Monthly process optimization sessions
    - Quarterly efficiency audits with detailed ROI analysis
    - Best practice sharing from global reinsurance market
    - Innovation lab partnership for emerging technologies:
      - Advanced AI and machine learning
      - Blockchain for smart contracts
      - Climate science and forward-looking modeling
      - Cyber risk quantification
      - Pandemic and systemic risk modeling
    - Joint research publications and thought leadership
    - Speaking opportunities at major industry conferences (Monte Carlo Rendez-Vous, Baden-Baden, SIRC)
    - Participation in industry working groups and standard-setting bodies

---

**Signatures:**

_________________________________
**Jennifer Rodriguez**
**Title**: Chief Executive Officer
**Insurellm, Inc.**
**Date**: April 28, 2025

_________________________________
**Sir Charles Pemberton**
**Title**: Group Chief Executive Officer
**GlobalRe Partners International, Ltd.**
**Date**: April 28, 2025

---

This agreement establishes GlobalRe Partners as Insurellm's flagship enterprise reinsurance partner, representing the most comprehensive and strategic partnership in Insurellm's history. This collaboration will drive innovation in reinsurance technology, catastrophe modeling, climate risk analytics, and AI-powered underwriting, setting new standards for the global reinsurance industry. This contract supersedes all prior agreements and communications.


---

<a id="file-week5-knowledge-base-contracts-contract-with-greenfield-holdings-for-markellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with GreenField Holdings for Markellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with GreenField Holdings for Markellm.md`

# Contract with GreenField Holdings for Markellm

**Effective Date:** November 15, 2023  
**Contract Duration:** 12 months  

## Terms
1. **Parties to the Agreement**: This contract is entered into between Insurellm, hereafter referred to as "Provider," and GreenField Holdings, hereafter referred to as "Client."
2. **Scope of Services**: Provider agrees to grant the Client access to the Markellm platform, enabling GreenField Holdings to connect with potential insurance customers through the AI-powered marketplace.
3. **Compliance**: Both parties agree to adhere to applicable laws and regulations that govern information security and consumer data protection.

## Renewal
1. **Automatic Renewal**: This contract will automatically renew for sequential one-year terms unless either party provides a written notice of non-renewal at least 30 days prior to the expiration of the current term.
2. **Annual Review**: Upon renewal, both parties may review and negotiate the terms, including any modifications to pricing based on performance metrics outlined in Section 4.

## Features
1. **AI-Powered Matching**: Access to advanced algorithms that connect GreenField Holdings with tailored insurance leads.
2. **Real-Time Quotes**: Ability to provide customers with instant quotes from multiple insurance providers, facilitating faster decision-making processes.
3. **Customized Recommendations**: Utilization of customizable consumer profiles to enhance marketing strategies and optimize customer engagement.
4. **Data Insights**: Access to analytics dashboards for real-time insights into market trends and consumer behavior, helping GreenField Holdings refine their product offerings.

## Support
1. **Customer Support Access**: The Client will have access to dedicated support through phone and email during normal business hours to address any inquiries or technical issues.
2. **Training and Resources**: Provider will offer onboarding training resources to ensure GreenField Holdings can effectively utilize the Markellm platform.
3. **Performance Reviews**: Quarterly performance reviews will be conducted to analyze platform effectiveness, customer acquisition rates, and marketing strategies, ensuring both parties are aligned on objectives.

## Pricing
- **Basic Listing Fee**: GreenField Holdings agrees to pay a monthly fee of $199 for a featured listing on the Markellm platform.
- **Performance-Based Pricing**: An additional fee of $25 per acquired customer lead will be charged, reflecting successful connections made through the Markellm platform.

**Signatures:**  
_________________________                           _________________________  
**[Name], Title**                                   **[Name], Title**  
Insurellm                                           GreenField Holdings  
**Date:** ____________                             **Date:** ____________


---

<a id="file-week5-knowledge-base-contracts-contract-with-greenvalley-insurance-for-homellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with GreenValley Insurance for Homellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with GreenValley Insurance for Homellm.md`

# Contract with GreenValley Insurance for Homellm

**Contract Date:** October 6, 2023  
**Contract Number:** HV-2023-0458  
**Parties:**  
- Insurellm, Inc.  
- GreenValley Insurance, LLC  

---

## Terms

1. **Coverage:** Insurellm agrees to provide GreenValley Insurance with access to the Homellm product, allowing for personalized home insurance offerings tailored to customers.
   
2. **Duration:** This agreement is effective for a period of 12 months from the contract date, after which it will automatically renew unless terminated by either party with a written 30-day notice.

3. **Payment:** GreenValley Insurance shall pay a monthly fee of $10,000, due by the 5th of every month for the Standard Tier package. 

4. **Confidentiality:** Both parties agree to maintain the confidentiality of proprietary information disclosed during the execution of this contract.

5. **Liability:** Insurellm's liability under this agreement shall be limited to direct damages and shall not exceed the total fees paid by GreenValley Insurance in the last 12 months prior to the date of the claim.

---

## Renewal

Unless either party provides a written notice of termination at least 30 days prior to the expiration of the contract term, this agreement will automatically renew for an additional one-year term under the same terms and conditions.

---

## Features

GreenValley Insurance will receive the following features with Homellm:

1. **AI-Powered Risk Assessment:** Access to advanced AI algorithms for real-time risk evaluations.
   
2. **Dynamic Pricing Model:** Flexible premium adjustments based on ongoing risk analysis.

3. **Instant Claim Processing:** Automated claim management to accelerate processing times significantly.

4. **Predictive Maintenance Alerts:** Alerts for potential maintenance needs to mitigate risks.

5. **Multi-Channel Integration:** Capability to integrate seamlessly with existing systems for unified customer management.

6. **Customer Portal:** A user-friendly portal for their customers for policy and claims management.

---

## Support

Insurellm commits to providing comprehensive support to GreenValley Insurance, which includes:

1. **Onboarding:** An extensive training program for the GreenValley staff to ensure effective use of Homellm.
   
2. **Dedicated Support Team:** A dedicated support team available 24/7 to address any technical issues or inquiries.

3. **Regular Updates:** Insurellm will offer ongoing updates and enhancements to the Homellm platform, including new features and security improvements.

4. **Feedback Implementation:** Insurellm will actively solicit feedback from GreenValley Insurance to ensure Homellm continues to meet their evolving needs.

---

**Signatures:**

_________________________________  
**[Name]**  
**Title**: CEO  
**Insurellm, Inc.**

_________________________________  
**[Name]**  
**Title**: COO  
**GreenValley Insurance, LLC**  

---

This agreement represents the complete understanding of both parties regarding the use of the Homellm product and supersedes any prior agreements or communications.


---

<a id="file-week5-knowledge-base-contracts-contract-with-greenstone-insurance-for-homellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Greenstone Insurance for Homellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Greenstone Insurance for Homellm.md`

# Contract with Greenstone Insurance for Homellm

---

## Terms

1. **Parties**: This Contract ("Agreement") is entered into on this day, [Insert Date], between Insurellm ("Provider"), located at [Provider Address], and Greenstone Insurance ("Customer"), located at [Customer Address].

2. **Services Provided**: Provider agrees to deliver the Homellm product, which includes AI-powered risk assessment, dynamic pricing model, instant claim processing, predictive maintenance alerts, multi-channel integration, and access to a customer portal as specified in the provided Product Summary.

3. **Contract Duration**: This Agreement shall commence on [Insert Start Date] and continue for a period of [Insert Duration, e.g., 12 months] unless terminated earlier as per the provisions herein.

4. **Payment Terms**: 
   - The Customer shall pay an amount of $10,000 per month for the Standard Tier of the Homellm service.
   - Payments are due within 30 days of invoicing.

5. **Customization**: Any additional customization requests outside the standard offerings will require a separate agreement and associated costs.

---

## Renewal

1. **Automatic Renewal**: This Agreement will automatically renew for additional one-year terms unless either party provides written notice of termination at least 60 days prior to the end of the current term.

2. **Renewal Terms Review**: Prior to each renewal, the Provider and Customer will review the terms and pricing. Adjustments may be made based on the current features and market conditions.

---

## Features

- **AI-Powered Risk Assessment**: Customer will have access to enhanced risk evaluation tools, allowing for personalized underwriting based on real-time data analysis.
  
- **Dynamic Pricing Model**: The Customer can leverage flexible premiums adjusted according to customer risk profiles.

- **Instant Claim Processing**: Claims submitted by the Customer's clients will be processed through an automated system, with most claims resolved within hours.

- **Predictive Maintenance Alerts**: The Customer will receive alerts regarding potential maintenance needs for insured properties, enhancing client satisfaction and reducing claims.

- **Multi-Channel Integration**: Homellm will integrate with the Customer's existing platforms to create seamless service delivery.

- **Customer Portal**: A dedicated portal will be provided, allowing the Customer's clients to manage their accounts 24/7.

---

## Support

1. **Training**: Provider will offer a comprehensive training program at the start of the term to ensure the Customer's staff can effectively use the Homellm product.

2. **Ongoing Support**: The Provider will supply ongoing technical support via email and phone during business hours (9 am - 5 pm EST) throughout the contract duration.

3. **Updates and Improvements**: Customer will receive all software updates and feature enhancements as they become available, without additional charge.

--- 

**AGREEMENT SIGNATURES**

By signing below, the parties acknowledge their acceptance of the terms of this Agreement.

**For Insurellm:**

______________________________  
[Name], [Title]  
Date: ______________________

**For Greenstone Insurance:**

______________________________  
[Name], [Title]  
Date: ______________________

--- 

*This contract is intended for illustrative purposes only and does not constitute a real legal document.*


---

<a id="file-week5-knowledge-base-contracts-contract-with-guardian-life-partners-for-lifellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Guardian Life Partners for Lifellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Guardian Life Partners for Lifellm.md`

# Contract with Guardian Life Partners for Lifellm

---

## Terms

1. **Agreement Effective Date**: This contract is effective as of March 1, 2025.
2. **Duration**: This agreement will remain in effect for a term of 24 months, concluding on February 28, 2027.
3. **Subscription Type**: Guardian Life Partners agrees to subscribe to the **Growth Tier** of Lifellm, at a cost of $7,500/month, totaling $180,000 for the duration of this contract.
4. **Policy Capacity**: Growth Tier supports up to 10,000 active policies with underwriting for 3,000 new applications annually.
5. **Payment Terms**: Payments are due on the 1st of each month via ACH transfer. Late payments incur a 1.5% monthly penalty.
6. **User Licenses**: Contract includes 25 named user licenses (underwriters, administrators, agents). Additional licenses: $120/month per user.
7. **Termination Clause**: Either party may terminate with 60 days' written notice. Early termination before month 12 requires payment of 30% of remaining contract value.

---

## Renewal

1. **Automatic Renewal**: This agreement will automatically renew for an additional 24-month term unless either party provides written notice of non-renewal at least 60 days before expiration.
2. **Price Protection**: Pricing increases capped at 7% annually for first two renewals.
3. **Enterprise Upgrade**: If Guardian upgrades to Enterprise tier at renewal, receives 12% discount on incremental cost for first renewal period.

---

## Features

1. **Access to Growth Tier Features**: Guardian Life Partners will have comprehensive access to:
   - AI-Powered Underwriting with accelerated decision-making (60% of applications instant decision)
   - Predictive Risk Modeling with machine learning mortality analysis
   - **Digital Health Integration** with wearables and health tracking apps (Fitbit, Apple Health, Garmin)
   - Automated Policy Management with full policy lifecycle support
   - Smart Document Processing with medical record analysis
   - Customer Portal with policyholder self-service
   - Compliance Automation across all 50 states
   - **Advanced Reporting** with predictive analytics

2. **Digital Health Features:**
   - Wearable device integration for wellness programs
   - Activity tracking and health score calculation
   - Premium discount automation based on health behaviors
   - Wellness challenge campaigns
   - Health goal tracking and rewards management

3. **Advanced Underwriting:**
   - Automated underwriting for face amounts up to $500,000
   - Accelerated underwriting (no medical exam) for qualified applicants
   - Predictive models trained on 10M+ life insurance applications
   - Risk stratification and pricing optimization
   - Decline rescue recommendations

4. **Agent Portal:**
   - Agent-facing tools for 200+ independent agents
   - Real-time application status tracking
   - Commission calculation and reporting
   - E-application with digital signature
   - Marketing materials and quote tools

---

## Support

1. **Technical Support**: Guardian Life Partners will receive enhanced support:
   - Priority support line Monday-Friday 7 AM - 8 PM EST
   - Email and chat support with 6-hour response time for critical issues
   - Dedicated support engineer for complex integrations
   - 24/7 emergency hotline for system outages

2. **Training**: Comprehensive training program:
   - Initial onboarding (4 weeks) for up to 20 staff members (40 hours total)
   - Role-specific training: underwriters, administrators, IT, agents
   - Quarterly product update webinars
   - Annual certification program for underwriters
   - Access to online learning platform with 30+ courses
   - Train-the-trainer program for agent network

3. **Updates and Maintenance**:
   - Monthly platform updates with new features
   - Bi-weekly security enhancements
   - Maintenance windows: Saturday 11 PM - Sunday 3 AM EST
   - 72-hour advance notice for major updates
   - Dedicated staging environment for testing updates

4. **Account Management**:
   - Named Customer Success Manager with bi-weekly check-ins
   - Quarterly business reviews with metrics analysis
   - Annual strategic planning session
   - Direct escalation path to Director of Customer Success
   - Industry benchmarking reports

5. **Integration Support**: Technical assistance for integrating Lifellm with:
   - Guardian's policy administration system (iPipeline, VPAS, or custom)
   - Agent management system (Salesforce, Applied Systems)
   - Medical data providers (MIB, Milliman IntelliScript, ExamOne)
   - Payment processing and billing systems
   - CRM and marketing automation platforms

6. **Wellness Program Support:**
   - Assistance designing wellness initiatives
   - Health program configuration and gamification
   - Marketing templates for wellness campaigns
   - Best practices from other carriers' successful programs

---

**Signatures:**

_________________________________
**Michael Torres**
**Title**: Chief Revenue Officer
**Insurellm, Inc.**
**Date**: March 1, 2025

_________________________________
**Jonathan Park**
**Title**: President & CEO
**Guardian Life Partners**
**Date**: March 1, 2025

---

*This contract establishes Guardian Life Partners as a strategic partner leveraging Lifellm's advanced AI underwriting and digital health integration to modernize life insurance operations.*


---

<a id="file-week5-knowledge-base-contracts-contract-with-harmony-health-plans-for-healthllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Harmony Health Plans for Healthllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Harmony Health Plans for Healthllm.md`

# Contract with Harmony Health Plans for Healthllm

---

## Terms

1. **Agreement Effective Date**: This contract is effective as of January 25, 2025.
2. **Duration**: This agreement will remain in effect for a term of 24 months, concluding on January 24, 2027.
3. **Subscription Type**: Harmony Health Plans agrees to subscribe to the **Professional Tier** of Healthllm, at a cost of $15,000/month, totaling $360,000 for the duration of this contract.
4. **Member Coverage**: Professional Tier supports up to 50,000 covered members. Harmony currently covers 38,000 members across 3 states.
5. **Payment Terms**: Payments are due on the 5th of each month via wire transfer. Late payments incur a 2% monthly penalty.
6. **User Licenses**: Contract includes 60 named user licenses. Additional licenses available at $150/month per user.
7. **Termination Clause**: Either party may terminate with 90 days' written notice. Early termination after month 12 has no penalty; before month 12 requires 25% of remaining contract value.

---

## Renewal

1. **Automatic Renewal**: This agreement will automatically renew for an additional 24-month term unless either party provides written notice of non-renewal at least 90 days before expiration.
2. **Price Protection**: Pricing increases capped at 6% annually for first two renewal periods.
3. **Volume Discounts**: If member count exceeds 75,000 at renewal, Harmony receives 10% discount on incremental cost.

---

## Features

1. **Access to Professional Tier Features**: Harmony Health Plans will have comprehensive access to:
   - Intelligent Plan Design with AI-powered optimization
   - Real-Time Eligibility Verification with provider network integration
   - AI-Driven Claims Adjudication with automated processing
   - **Predictive Healthcare Analytics** for population health management
   - Provider Network Management with contract optimization
   - Member Engagement Platform with mobile-first design
   - **Advanced Medication Management** with PBM integration
   - Regulatory Compliance Engine with ACA and state mandate tracking
   - **Enhanced Analytics** with predictive modeling

2. **Predictive Healthcare Analytics:**
   - High-risk member identification for care management
   - Disease progression modeling (diabetes, hypertension, CHF)
   - Hospital readmission prediction
   - Emergency department overutilization alerts
   - Care gap identification for quality measures (HEDIS)
   - Preventive care intervention recommendations
   - Cost trend forecasting and budget planning

3. **Advanced Medication Management:**
   - Complete formulary management and tier optimization
   - Prior authorization automation with clinical criteria
   - Step therapy enforcement
   - Medication adherence scoring and intervention triggers
   - Drug interaction checking with severity classification
   - Generic substitution recommendations with savings calculations
   - Specialty pharmacy management
   - Medication therapy management (MTM) program support

4. **Value-Based Care Tools:**
   - ACO (Accountable Care Organization) performance tracking
   - Shared savings calculation
   - Quality measure monitoring (HEDIS, STAR ratings)
   - Provider pay-for-performance scorecards
   - Risk adjustment and HCC coding support

5. **Care Management Platform:**
   - Case management workflows for high-cost members
   - Disease management program support
   - Care coordinator tools and dashboards
   - Member outreach campaign management
   - Social determinants of health (SDOH) screening

---

## Support

1. **Technical Support**: Harmony Health Plans will receive priority support:
   - Dedicated support team available 24/7 for critical issues
   - Standard support Monday-Saturday 6 AM - 9 PM EST
   - Response time: 4 hours for critical, 8 hours for high priority, 24 hours for standard
   - Named technical support engineer familiar with Harmony's environment
   - Private support portal with ticket tracking

2. **Training**: Comprehensive training program:
   - 6-week implementation with dedicated project manager
   - Training for up to 40 staff members (60 hours total training)
   - Role-specific tracks: claims processors, case managers, provider relations, IT, executives
   - Quarterly advanced training webinars
   - Annual refresher certification program
   - Unlimited access to online learning platform with 75+ courses
   - Custom training materials for Harmony's specific workflows

3. **Updates and Maintenance**:
   - Monthly platform updates with new features and enhancements
   - Bi-weekly security patches and bug fixes
   - Regulatory updates as healthcare laws change (ACA, state mandates)
   - Maintenance windows: Saturday 10 PM - Sunday 3 AM EST
   - 96-hour advance notice for major updates
   - Staging environment for testing updates before production

4. **Account Management**:
   - Named Senior Customer Success Manager with bi-weekly check-ins
   - Quarterly executive business reviews with ROI analysis
   - Annual strategic planning session with product roadmap preview
   - Direct escalation path to VP of Customer Success
   - Industry benchmarking reports comparing Harmony to similar plans

5. **Integration Support**: Comprehensive integration assistance:
   - Integration with Harmony's core systems:
     - HealthRules policy administration system
     - Provider credentialing platform
     - Express Scripts PBM
     - Availity clearinghouse for claims
     - Member portal and mobile app
     - Salesforce CRM
   - Dedicated integration specialist (30% FTE allocation)
   - Quarterly integration health checks and optimization
   - API monitoring and performance tuning

6. **Analytics and Reporting:**
   - Custom dashboard development (up to 10 dashboards)
   - Automated reporting suite (daily, weekly, monthly, quarterly)
   - Ad-hoc analytics requests (up to 15 per month)
   - Predictive modeling consultation (monthly sessions)
   - Benchmark reports against regional health plans
   - Data export capabilities in multiple formats

7. **Compliance and Regulatory Support:**
   - Quarterly compliance reviews
   - Annual HIPAA security risk assessment
   - ACA reporting assistance (1094/1095 forms, MLR reporting)
   - State filing support for form and rate approvals
   - Quality measure calculation support (HEDIS, STAR)
   - Audit preparation and documentation assistance

---

**Signatures:**

_________________________________
**Sarah Chen**
**Title**: Vice President of Sales
**Insurellm, Inc.**
**Date**: January 25, 2025

_________________________________
**Dr. Karen Phillips**
**Title**: President & Chief Executive Officer
**Harmony Health Plans**
**Date**: January 25, 2025

---

*This contract establishes Harmony Health Plans as a strategic partner leveraging Healthllm's advanced AI and predictive analytics to improve member outcomes while managing costs effectively.*


---

<a id="file-week5-knowledge-base-contracts-contract-with-heritage-life-assurance-for-lifellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Heritage Life Assurance for Lifellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Heritage Life Assurance for Lifellm.md`

# Contract with Heritage Life Assurance for Lifellm

**Contract Date:** February 12, 2025
**Contract Number:** LF-2025-0045

---

## Terms

1. **Parties Involved**: This contract is entered into between Insurellm, Inc. ("Provider") and Heritage Life Assurance ("Client").

2. **Scope of Services**: Provider agrees to deliver Lifellm Growth Tier, including AI-powered underwriting, predictive risk modeling, digital health integration, and policy management capabilities.

3. **Payment Terms**: Client shall pay $7,500 per month for 18 months. Total contract value: $135,000. Payments due on the 1st via ACH.

4. **Policy Volume**: Growth Tier supports up to 10,000 active policies. Heritage currently administers 6,200 policies.

5. **Contract Duration**: 18 months commencing February 12, 2025 and ending August 11, 2026.

## Renewal

1. **Automatic Renewal**: This agreement automatically renews for 12-month terms unless either party provides 45-day written notice of non-renewal.

2. **Renewal Pricing**: Pricing adjustments communicated 75 days prior to renewal, capped at 8% annual increase.

## Features

1. **AI-Powered Underwriting**: Heritage Life Assurance will benefit from:
   - Accelerated underwriting with 65% instant decisions
   - Medical record analysis and risk scoring
   - Mortality prediction models
   - Automated decisioning for face amounts up to $750,000

2. **Predictive Risk Modeling**: Advanced analytics considering:
   - Comprehensive medical histories
   - Prescription drug databases
   - Lifestyle and occupation factors
   - Family history and genetic markers
   - Predictive health trajectories

3. **Digital Health Integration**:
   - Wearable device connections (Fitbit, Apple Watch)
   - Health app integrations
   - Wellness program platform
   - Premium discount automation
   - Activity tracking and rewards

4. **Automated Policy Management**:
   - Digital policy issuance
   - Beneficiary updates and management
   - Premium billing integration
   - Policy conversion processing
   - Lapse and reinstatement automation

5. **Customer Portal**: Policyholder self-service including:
   - 24/7 policy access
   - Digital insurance cards
   - Claims submission
   - Premium payment processing
   - Coverage updates

6. **Advanced Reporting**:
   - Application conversion analytics
   - Underwriting productivity metrics
   - Policy persistency reporting
   - Agent performance dashboards

## Support

1. **Technical Support**: Heritage will receive priority support:
   - Monday-Friday 7 AM - 7 PM EST
   - Email, phone, and chat support
   - 8-hour response time for critical issues
   - Online knowledge base

2. **Training**: Training program includes:
   - 3-week implementation
   - Training for up to 15 staff members (25 hours)
   - Quarterly webinars on platform updates
   - Online training library access

3. **Updates**: Monthly platform enhancements and security patches. Maintenance windows: Sunday 1 AM - 5 AM EST.

4. **Account Management**: Named customer success manager with quarterly business reviews.

---

**Signatures:**

**Insurellm, Inc.**
Michael Torres, Chief Revenue Officer
Date: February 12, 2025

**Heritage Life Assurance**
Melissa Zhang, VP of Operations
Date: February 12, 2025

---

This contract enables Heritage Life Assurance to leverage Lifellm's AI technology for modernized life insurance underwriting and administration.


---

<a id="file-week5-knowledge-base-contracts-contract-with-metropolitan-life-group-for-lifellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Metropolitan Life Group for Lifellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Metropolitan Life Group for Lifellm.md`

# Contract with Metropolitan Life Group for Lifellm

**Contract Date:** April 5, 2025
**Contract Number:** LF-2025-E-0087
**Parties:**
- Insurellm, Inc.
- Metropolitan Life Group, Inc.

---

## Terms

1. **Coverage:** Insurellm agrees to provide Metropolitan Life Group with enterprise access to the Lifellm platform, including white-label capabilities, full customization, dedicated support, and enterprise-grade security for their nationwide life insurance operations managing 50,000+ active policies.

2. **Duration:** This agreement is effective for a period of 36 months from the contract date, representing a strategic long-term partnership.

3. **Payment:** Metropolitan Life Group shall pay custom Enterprise Tier pricing of $28,000 per month for months 1-12, $30,500 per month for months 13-24, and $33,000 per month for months 25-36, totaling $1,098,000 over the contract term.

4. **Service Level Agreement:** Insurellm guarantees 99.9% uptime measured monthly, with 10% monthly credit for each 0.1% below target, maximum 30% credit.

5. **Confidentiality:** Both parties agree to maintain the highest level of confidentiality regarding AI algorithms, underwriting models, policyholder data, and strategic initiatives.

6. **Data Security:** Insurellm commits to maintaining HIPAA compliance, SOC 2 Type II certification, and annual third-party security audits.

7. **Disaster Recovery:** 4-hour recovery time objective (RTO) and 30-minute recovery point objective (RPO).

---

## Renewal

This agreement includes a mutual 90-day renewal notice period. Metropolitan Life Group receives guaranteed enterprise pricing at or below market rates for renewal. Contract may be extended in 12 or 24-month increments with mutual agreement.

---

## Features

Metropolitan Life Group will receive the complete Lifellm Enterprise suite:

1. **Unlimited Policy Administration:** No capacity restrictions, supporting Metropolitan's 50,000+ active policies with scalability to 200,000+ as business expands.

2. **White-Label Platform:** Complete branding customization:
   - Custom domains (life.metropolitanlifegroup.com)
   - Branded mobile apps (iOS and Android) with custom UI/UX
   - Customized email templates and policyholder communications
   - Co-branded agent portals and marketing materials

3. **Advanced AI Underwriting:** State-of-the-art underwriting capabilities:
   - Instant decisioning for 75% of applications up to $1M face amount
   - Predictive mortality models trained on 50M+ data points
   - Genetic risk assessment integration (when legally permitted)
   - Accelerated underwriting with no medical exam for qualified applicants
   - Alternative data sources (social media, financial, education)

4. **Comprehensive Digital Health Integration:**
   - Wearable integrations: Apple Watch, Fitbit, Garmin, Oura Ring, Whoop
   - Health app integrations: Apple Health, Google Fit, MyFitnessPal
   - Biometric screening integration with Quest Diagnostics, LabCorp
   - Wellness program platform with challenges, rewards, gamification
   - Premium discount automation based on verified health behaviors
   - Long-term health trajectory modeling

5. **Complete API Access:** Unlimited API calls supporting:
   - Real-time integration with Metropolitan's core policy admin system
   - Agent management system synchronization
   - Third-party data provider integrations (MIB, IntelliScript, ExamOne, Clareto, Lifescore)
   - Custom workflow automation
   - Data warehouse bidirectional sync

6. **Predictive Analytics Suite:**
   - Lapse and persistency prediction modeling
   - Cross-sell and upsell opportunity identification
   - Agent productivity analytics and optimization
   - Competitive positioning and market share analysis
   - Lifetime value prediction for policyholders

7. **Advanced Policy Management:**
   - Automatic premium loan processing
   - Policy conversion and exchange support
   - Dividend calculation and distribution (whole life)
   - Non-forfeiture options automation
   - Reinstatement processing with re-underwriting
   - Settlement options administration

8. **Agent Network Platform:**
   - Support for 5,000+ independent agents and career agents
   - Hierarchical permissions and agency structures
   - Real-time commission calculation and reporting
   - Advanced quoting engine with need analysis tools
   - Automated licensing and appointment tracking
   - Agent recruiting and onboarding workflows

9. **Regulatory and Compliance:**
   - 50-state compliance monitoring and form filing
   - Automated NAIC reporting
   - AML (Anti-Money Laundering) screening integration
   - OFAC (Office of Foreign Assets Control) checking
   - Escheatment and unclaimed property tracking
   - Audit trail and compliance reporting

10. **Blockchain Policy Verification:**
   - Immutable policy records on private blockchain
   - Fraud prevention through distributed ledger
   - Beneficiary verification and claims authentication
   - Regulatory audit transparency

---

## Support

Insurellm commits to comprehensive Enterprise-level support for Metropolitan Life Group:

1. **Dedicated Success Team:**
   - Executive sponsor (C-suite level) with quarterly strategic reviews
   - Dedicated Customer Success Director with weekly touchpoints
   - Technical Account Manager for system optimization
   - Solutions Architect for ongoing innovation projects
   - Quarterly executive business reviews with CEO participation

2. **24/7/365 Premium Support:**
   - Guaranteed 15-minute response for P1 critical issues
   - 1-hour response for P2 high-priority issues
   - 4-hour response for P3 standard issues
   - Named support team familiar with Metropolitan's environment
   - Private Slack channel with engineering team access
   - Annual on-site support visits (minimum 6 per year)

3. **Comprehensive Implementation:**
   - 12-month phased implementation program with 3 major releases
   - Dedicated project management office (PMO) with weekly steering committee
   - Migration of 50,000+ existing policies from legacy system
   - Training for 150+ Metropolitan staff and 500+ top-producing agents
   - Parallel processing with legacy system for 90 days
   - Go-live support with 8-week on-site Insurellm team presence

4. **Training and Enablement:**
   - Comprehensive training programs for all roles
   - Executive briefings on AI and technology trends
   - Train-the-trainer certification program
   - Annual user conference attendance (5 attendees, all expenses paid)
   - Quarterly advanced training sessions
   - Unlimited online learning platform access
   - Custom training content development

5. **Custom Development:**
   - 2,000 hours annually of custom development included
   - Dedicated development team for Metropolitan-specific features
   - Priority feature requests with guaranteed roadmap inclusion
   - Early access to beta features (90 days before general release)
   - Joint innovation projects and co-development opportunities
   - Input into product strategy and 3-year roadmap

6. **Integration Services:**
   - Enterprise integration with Metropolitan's systems:
     - iPipeline policy administration
     - Salesforce CRM and agent management
     - DocuSign for digital signatures
     - Multiple payment processors
     - Data warehouse (Snowflake)
     - BI platforms (Tableau, PowerBI)
   - Dedicated integration engineer (50% FTE)
   - Quarterly integration health assessments
   - Performance optimization and load testing

7. **Analytics and Reporting:**
   - Custom executive dashboard development (unlimited)
   - Real-time operational dashboards
   - Automated reporting suite (daily, weekly, monthly, quarterly, annual)
   - Ad-hoc analytics support (unlimited requests)
   - Industry benchmarking against top 50 life insurers
   - Predictive modeling consultation (quarterly sessions)
   - Data science partnership for advanced analytics projects

8. **Continuous Improvement:**
   - Monthly process optimization reviews
   - Semi-annual efficiency audits with ROI analysis
   - Best practice sharing and peer learning opportunities
   - Innovation lab access for emerging technologies (AI, blockchain, quantum computing)
   - Joint whitepapers and case studies
   - Speaking opportunities at industry conferences

---

**Signatures:**

_________________________________
**Jennifer Rodriguez**
**Title**: Chief Executive Officer
**Insurellm, Inc.**
**Date**: April 5, 2025

_________________________________
**Richard Thompson**
**Title**: Chairman & Chief Executive Officer
**Metropolitan Life Group, Inc.**
**Date**: April 5, 2025

---

This agreement establishes Metropolitan Life Group as Insurellm's flagship enterprise life insurance partner, representing a strategic partnership to transform life insurance through cutting-edge AI technology and innovation. This contract supersedes all prior agreements and communications.


---

<a id="file-week5-knowledge-base-contracts-contract-with-national-claims-network-for-claimllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with National Claims Network for Claimllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with National Claims Network for Claimllm.md`

# Contract with National Claims Network for Claimllm

**Contract Date:** April 20, 2025
**Contract Number:** CL-2025-E-0198
**Parties:**
- Insurellm, Inc.
- National Claims Network Corp.

---

## Terms

1. **Coverage:** Insurellm agrees to provide National Claims Network with enterprise access to the Claimllm platform, including white-label capabilities, unlimited claims capacity, advanced fraud analytics, and dedicated infrastructure to support their nationwide claims operations processing over 100,000 claims annually.

2. **Duration:** This agreement is effective for a period of 36 months from the contract date, representing Insurellm's longest-term contract commitment to date.

3. **Payment:** National Claims Network shall pay custom Enterprise Tier pricing of $35,000 per month for months 1-12, $38,000 per month for months 13-24, and $41,000 per month for months 25-36, totaling $1,368,000 over the contract term.

4. **Service Level Agreement:** Insurellm guarantees 99.95% uptime with financial credits for downtime: 5% monthly credit for each hour of unplanned downtime, maximum 50% monthly credit.

5. **Confidentiality:** Both parties agree to maintain the highest level of confidentiality regarding proprietary AI models, fraud detection algorithms, claimant PII, and business strategies.

6. **Data Security:** Insurellm commits to maintaining SOC 2 Type II compliance, annual penetration testing, and end-to-end encryption for all data at rest and in transit.

7. **Business Continuity:** Insurellm provides disaster recovery with 4-hour RTO (Recovery Time Objective) and 1-hour RPO (Recovery Point Objective).

---

## Renewal

This agreement includes a mutual 120-day renewal notice period. National Claims Network receives guaranteed enterprise pricing for renewal equal to or better than new enterprise customers at renewal time. Contract may be extended in 12-month increments with mutual written agreement.

---

## Features

National Claims Network will receive the complete Claimllm Enterprise suite:

1. **Unlimited Claims Processing:** No volume restrictions, supporting National's processing of 100,000+ claims annually with scalability to 500,000+ claims as business grows.

2. **White-Label Platform:** Complete branding customization including:
   - Custom domain names (claims.nationalclaimsnetwork.com)
   - Branded mobile apps (iOS and Android)
   - Customized email templates and communications
   - Co-branded claimant portals

3. **Advanced Computer Vision:** State-of-the-art damage assessment:
   - Auto damage analysis with 95%+ accuracy on repair estimates
   - Property damage evaluation (roofs, siding, interiors, water damage)
   - Medical imaging analysis for injury claims
   - 3D reconstruction from photo sets
   - Integration with all major estimating platforms

4. **Enterprise Fraud Analytics:**
   - Real-time fraud scoring on all claims
   - Social network analysis across 10+ years of historical data
   - Dark web monitoring for organized fraud rings
   - Predictive models trained on 5M+ historical claims
   - Link analysis connecting related parties, addresses, and claims patterns
   - Integration with third-party fraud databases (NICB, ISO ClaimSearch)

5. **Complete API Access:** Unlimited API calls supporting:
   - Real-time integrations with 50+ carrier policy systems
   - Bi-directional data sync with National's data warehouse
   - Third-party integrations (repair networks, medical providers, legal vendors)
   - Custom automation workflows

6. **AI-Powered Litigation Prediction:** Predictive analytics identifying claims with high litigation probability:
   - Attorney involvement prediction (85%+ accuracy)
   - Recommended settlement ranges based on jurisdiction and case law
   - Early intervention recommendations
   - Litigation cost estimation

7. **Catastrophe Claims Management:** Specialized tools for major events:
   - Rapid deployment playbooks for natural disasters
   - Geographic clustering and resource allocation
   - Emergency vendor network activation
   - Real-time damage assessment using satellite imagery
   - Mobile claims units with offline capability

8. **Advanced Vendor Management:**
   - Network of 5,000+ preferred vendors nationwide
   - AI-powered vendor matching and assignment
   - Real-time capacity management and scheduling
   - Quality scoring and performance analytics
   - Automated vendor payments and 1099 management

9. **Predictive Analytics Suite:**
   - Claim outcome prediction and reserve optimization
   - Subrogation opportunity identification
   - Salvage value estimation
   - Customer satisfaction prediction and intervention triggers
   - Cycle time optimization recommendations

---

## Support

Insurellm commits to comprehensive Enterprise-level support for National Claims Network:

1. **Dedicated Success Team:**
   - Executive sponsor (VP level) with monthly strategic reviews
   - Dedicated Customer Success Manager with daily availability
   - Technical Account Manager for system optimization
   - Solutions Architect for ongoing innovation
   - Quarterly executive business reviews with CEO participation

2. **24/7/365 Premium Support:**
   - Guaranteed 10-minute response time for P1 critical issues
   - 30-minute response for P2 high-priority issues
   - 2-hour response for P3 standard issues
   - Dedicated support hotline with no phone tree
   - Private Slack channel with engineering team access
   - Annual on-site support visits (minimum 4 per year)

3. **Comprehensive Implementation:**
   - 9-month phased implementation program
   - Dedicated project management office (PMO)
   - Executive steering committee with monthly meetings
   - Migration of 3 years of historical claims data
   - Training for 200+ National Claims Network staff
   - Parallel processing period with legacy system
   - Go-live support with on-site Insurellm team (4 weeks)

4. **Training and Enablement:**
   - Role-based training programs (adjusters, supervisors, fraud investigators, IT, executives)
   - Train-the-trainer program for National's learning team
   - Certification programs with continuing education credits
   - Annual user conference attendance (3 attendees)
   - Quarterly advanced training sessions
   - Unlimited access to online learning platform

5. **Custom Development:**
   - 1,000 hours annually of custom development included
   - Dedicated development team for National-specific features
   - Priority feature requests with guaranteed roadmap inclusion
   - Beta program participation for all new features
   - Input into product strategy and direction

6. **Integration Services:**
   - Enterprise integration with National's systems:
     - Policy administration systems (multiple carriers)
     - Data warehouse and business intelligence platforms
     - Financial systems (SAP, Oracle)
     - Document management (SharePoint, M-Files)
     - Communication platforms (Twilio, SendGrid)
   - Ongoing integration support with 4-hour response SLA
   - Quarterly integration health assessments

7. **Analytics and Reporting:**
   - Custom executive dashboard development
   - Real-time operational dashboards
   - Automated daily, weekly, and monthly reporting
   - Ad-hoc analytics support (up to 20 requests/month)
   - Industry benchmarking and competitive analysis
   - Predictive modeling consultation

8. **Continuous Improvement:**
   - Quarterly process optimization workshops
   - Annual efficiency audits with recommendations
   - Best practice sharing from across Insurellm customer base
   - Innovation labs to pilot emerging technologies (AI, blockchain, IoT)

---

**Signatures:**

_________________________________
**Jennifer Rodriguez**
**Title**: Chief Executive Officer
**Insurellm, Inc.**
**Date**: April 20, 2025

_________________________________
**Amanda Richardson**
**Title**: President & Chief Operating Officer
**National Claims Network Corp.**
**Date**: April 20, 2025

---

This agreement represents a strategic partnership between Insurellm and National Claims Network, establishing National Claims Network as Insurellm's flagship enterprise claims processing partner. This contract supersedes all prior agreements and communications.


---

<a id="file-week5-knowledge-base-contracts-contract-with-pinnacle-insurance-co--for-homellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Pinnacle Insurance Co. for Homellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Pinnacle Insurance Co. for Homellm.md`

# Contract with Pinnacle Insurance Co. for Homellm

## Terms
This contract ("Contract") is entered into as of this 1st day of January 2024 ("Effective Date") by and between Insurellm ("Provider"), a Delaware corporation with its principal place of business at 1234 Innovation Drive, San Francisco, CA 94105, and Pinnacle Insurance Co. ("Client"), a Texas corporation with its principal place of business at 4567 Protection Plaza, Houston, TX 77001. 

1. **License Grant**: Insurellm hereby grants the Client a non-exclusive, non-transferable license to use Homellm in accordance with the terms of this Contract.
2. **Payment Terms**: The Client agrees to pay an initial setup fee of $15,000 and a monthly subscription fee of $10,000 for the duration of the Contract.
3. **Term**: The initial term of this Contract shall last for a period of two (2) years from the Effective Date.

## Renewal
1. **Renewal Terms**: At the end of the initial term, this Contract shall automatically renew for additional one-year terms unless either party provides written notice of termination at least thirty (30) days prior to the expiration of the current term.
2. **Adjustment of Fees**: Subscription fees may be adjusted annually based on consumer price index changes, not to exceed 5% per year.

## Features
1. **AI-Powered Risk Assessment**: Utilized for tailored underwriting decisions specific to individual homeowner policies.
2. **Dynamic Pricing Model**: Monthly premiums adjusted based on real-time risk evaluations, ensuring fair pricing for Pinnacle’s customers.
3. **Instant Claim Processing**: Claims resolved in hours rather than weeks, significantly improving customer satisfaction and operational efficiency.
4. **Predictive Maintenance Alerts**: Alerts sent to customers advising them of potential risks unique to their property, supporting proactive maintenance.
5. **Multi-Channel Integration**: Seamless access to customer data through existing systems in Pinnacle Insurance's infrastructure.
6. **Customer Portal**: A user-friendly interface allowing policy management, claims submission, and coverage updates at any time.

## Support
1. **Technical Support**: Insurellm shall provide 24/7 technical support via an email and phone assistance for the duration of this Contract.
2. **Training**: Insurellm will conduct an onsite training session for Client employees upon implementation, and quarterly training webinars will be made available thereafter.
3. **Updates and Maintenance**: Insurellm will provide regular system updates and maintenance, ensuring that the software is operating at peak efficiency.

By signing below, both parties agree to the terms set forth in this Contract for the use of the Homellm product.

____  
**Insurellm Authorized Signature**  
Name: Sarah Johnson  
Title: VP of Sales  
Date: ____________

____  
**Pinnacle Insurance Co. Authorized Signature**  
Name: Tom Anderson  
Title: Chief Operating Officer  
Date: ____________


---

<a id="file-week5-knowledge-base-contracts-contract-with-premier-adjusters-inc--for-claimllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Premier Adjusters Inc. for Claimllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Premier Adjusters Inc. for Claimllm.md`

# Contract with Premier Adjusters Inc. for Claimllm

---

## Terms

1. **Agreement Effective Date**: This contract is effective as of February 15, 2025.
2. **Duration**: This agreement will remain in effect for a term of 24 months, concluding on February 14, 2027.
3. **Subscription Type**: Premier Adjusters Inc. agrees to subscribe to the **Advanced Tier** of Claimllm, at a cost of $9,500/month, totaling $228,000 for the duration of this contract.
4. **Claims Volume**: Advanced Tier supports up to 25,000 claims annually. Current baseline estimate: 18,000 claims/year.
5. **Payment Terms**: Payments are due on the 5th of each month via wire transfer. Late payments will incur a penalty of 1.8% per month.
6. **Performance Guarantees**: Insurellm guarantees average FNOL-to-assignment time of less than 2 hours, and fraud detection accuracy of 85%+ on confirmed fraud cases.
7. **Termination Clause**: Either party may terminate this agreement with 60 days' written notice. No early termination fees after 12 months.

---

## Renewal

1. **Automatic Renewal**: This agreement will automatically renew for an additional 24-month term unless either party provides written notice of non-renewal at least 60 days before expiration.
2. **Pricing Adjustments**: Renewal pricing subject to annual CPI adjustment, maximum 7% increase.
3. **Tier Flexibility**: Premier may move to Enterprise tier at renewal or annually with 45 days' notice and prorated adjustment.

---

## Features

1. **Access to Advanced Tier Features**: Premier Adjusters Inc. will have access to comprehensive claims automation:
   - Intelligent FNOL Processing across all communication channels
   - Automated Triage and Routing with ML-based severity assessment
   - **Computer Vision Damage Assessment** with photo/video analysis and automated repair cost estimation
   - **Predictive Fraud Detection** with network analysis and anomaly detection
   - Smart Document Processing with OCR, NLP, and auto-extraction from medical records, police reports, and estimates
   - Dynamic Reserve Setting with AI-powered predictive modeling
   - Vendor Management Platform with automated assignment and performance tracking
   - Payment Automation for approved claims with multi-party splitting
   - Claimant Communication Hub with omnichannel messaging
   - **Advanced Analytics** with predictive cycle time modeling and settlement optimization

2. **Computer Vision Capabilities:**
   - Automated vehicle damage assessment from photos (dents, scratches, structural damage)
   - Property damage evaluation (roof, siding, interior damage)
   - Severity scoring and repair cost estimation
   - Parts identification and replacement recommendations
   - Integration with estimating systems (CCC, Mitchell, Audatex)

3. **Fraud Analytics:**
   - Social network analysis to identify claim rings
   - Geospatial anomaly detection
   - Behavioral pattern matching against known fraud indicators
   - Third-party data enrichment (public records, social media)
   - Predictive fraud scoring with explanation rationale

4. **Vendor Network:**
   - Support for 200+ preferred vendors (repair shops, medical providers, attorneys)
   - Automated work assignment based on location, capacity, and quality scores
   - Real-time vendor availability and scheduling
   - Vendor performance dashboards and scorecards

---

## Support

1. **Technical Support**: Premier Adjusters Inc. will receive priority advanced support:
   - Dedicated technical support team
   - 24/7 emergency hotline for critical system issues
   - Response time: 2 hours critical, 6 hours high priority, 12 hours standard
   - Dedicated Slack channel for real-time communication

2. **Training**: Comprehensive training program:
   - 4-week implementation with on-site support (first 2 weeks)
   - Training for up to 40 staff members (adjusters, supervisors, IT)
   - Role-specific training tracks (FNOL specialists, senior adjusters, fraud investigators)
   - Monthly advanced training webinars on new features
   - Annual adjuster certification program
   - Access to online training portal with 50+ courses

3. **Updates and Maintenance**:
   - Monthly platform updates with new features
   - Bi-weekly security patches and improvements
   - Maintenance windows: Saturday 11 PM - Sunday 4 AM EST
   - 72-hour advance notice for major updates
   - Option to delay non-critical updates by up to 30 days

4. **Account Management**:
   - Named Customer Success Manager with weekly check-ins (first 90 days), then bi-weekly
   - Quarterly executive business reviews with metrics analysis
   - Annual strategic planning session
   - Direct escalation path to VP of Customer Success

5. **Integration Services**:
   - Integration with Premier's core systems:
     - Guidewire ClaimCenter
     - Salesforce CRM
     - DocuSign for settlement documents
     - Payment processing systems (CheckFree, AvidXchange)
   - Custom API development (up to 100 hours included)
   - Ongoing integration support and optimization

6. **Data and Analytics:**
   - Custom dashboard development (up to 5 dashboards)
   - Monthly data exports in preferred format
   - Benchmark comparisons against industry standards
   - Predictive analytics consultation sessions

---

**Signatures:**

_________________________________
**Sarah Chen**
**Title**: Vice President of Sales
**Insurellm, Inc.**
**Date**: February 15, 2025

_________________________________
**David Kowalski**
**Title**: President & CEO
**Premier Adjusters Inc.**
**Date**: February 15, 2025

---

*This contract establishes Premier Adjusters Inc. as a strategic partner of Insurellm, leveraging advanced AI-powered claims technology to deliver superior service to their clients while optimizing operational efficiency.*


---

<a id="file-week5-knowledge-base-contracts-contract-with-rapid-claims-associates-for-claimllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Rapid Claims Associates for Claimllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Rapid Claims Associates for Claimllm.md`

# Contract with Rapid Claims Associates for Claimllm

**Contract Date:** March 1, 2025
**Contract Number:** CL-2025-0063
**Parties:**
- Insurellm, Inc.
- Rapid Claims Associates, LLC

---

## Terms

1. **Coverage:** Insurellm agrees to provide Rapid Claims Associates with access to the Claimllm platform, enabling AI-powered claims processing, automated triage, and streamlined claims management across property, casualty, and auto lines.

2. **Duration:** This agreement is effective for a period of 12 months from the contract date, with automatic renewal provisions unless terminated with 30-day written notice.

3. **Payment:** Rapid Claims Associates shall pay a monthly fee of $4,500, due by the 1st of every month for the Core Tier package, supporting up to 5,000 claims annually.

4. **Overage Fees:** If claims volume exceeds 5,000 annually, overage fees of $0.90 per claim apply, billed quarterly.

5. **Confidentiality:** Both parties agree to maintain confidentiality of proprietary information, claimant data, and processing methodologies disclosed during this contract.

6. **Data Ownership:** Rapid Claims Associates retains ownership of all claims data. Insurellm may use anonymized, aggregated data for product improvement.

7. **Liability:** Insurellm's liability is limited to direct damages not exceeding total fees paid in the preceding 6 months.

---

## Renewal

Unless either party provides written notice of termination at least 30 days prior to contract expiration, this agreement automatically renews for successive 12-month terms. Pricing may be adjusted annually with 60 days' advance notice, capped at 10% increase per year.

---

## Features

Rapid Claims Associates will receive the following Core Tier features:

1. **Intelligent FNOL Processing:** Multi-channel first notice of loss intake via:
   - Mobile app integration
   - Web portal submission
   - Email parsing with NLP extraction
   - Phone system integration with IVR
   - Chatbot-assisted intake

2. **Automated Triage and Routing:** Machine learning algorithms assess claim severity and complexity to route appropriately:
   - Low-complexity claims → automated processing
   - Medium-complexity claims → junior adjuster queue
   - High-complexity/high-value claims → senior adjuster assignment
   - Fraud-flagged claims → special investigation unit

3. **Basic Document Processing:** OCR and NLP extraction from:
   - Police reports
   - Repair estimates
   - Medical bills and records
   - Witness statements
   - Photo and video evidence

4. **Standard Fraud Detection:** Rule-based fraud screening including:
   - Duplicate claim detection
   - Unusual pattern identification
   - Loss location verification
   - Claimant history review

5. **Claimant Communication Hub:** Automated status updates via:
   - SMS text messages
   - Email notifications
   - Mobile app push notifications
   - Scheduled status update intervals

6. **Basic Reporting:** Standard dashboards tracking:
   - Claims volume and cycle time
   - Average settlement amounts
   - Adjuster productivity metrics
   - Customer satisfaction scores

7. **Payment Processing:** Integration with payment systems for:
   - Direct deposit (ACH)
   - Check issuance
   - Digital wallets (PayPal, Venmo)
   - Simple multi-party splits

---

## Support

Insurellm commits to providing comprehensive support to Rapid Claims Associates:

1. **Onboarding:** 2-week implementation program including:
   - System configuration and data migration
   - Training for up to 10 claims staff members (12 hours total)
   - Process workflow mapping and optimization
   - Integration with existing claims management system

2. **Technical Support:**
   - Email and phone support Monday-Friday 8 AM - 6 PM EST
   - Response time: 8 hours for critical issues, 24 hours for standard requests
   - Online knowledge base and FAQ access
   - Monthly platform office hours for questions

3. **Platform Updates:**
   - Quarterly feature releases with new capabilities
   - Monthly security patches and bug fixes
   - Release notes and changelog documentation
   - Advance notice of breaking changes (minimum 30 days)

4. **Account Management:**
   - Named customer success manager
   - Semi-annual business review meetings
   - Usage analytics and optimization recommendations
   - Assistance with tier upgrade evaluation when volume grows

5. **Integration Support:** Technical assistance connecting Claimllm with:
   - Existing claims management systems
   - Policy administration platforms
   - Vendor management networks (repair shops, medical providers)
   - Payment processing systems

---

**Signatures:**

_________________________________
**Sarah Chen**
**Title**: Vice President of Sales
**Insurellm, Inc.**
**Date**: March 1, 2025

_________________________________
**Marcus Johnson**
**Title**: Chief Claims Officer
**Rapid Claims Associates, LLC**
**Date**: March 1, 2025

---

This agreement represents the complete understanding between Insurellm and Rapid Claims Associates regarding the Claimllm platform and supersedes any prior communications or agreements.


---

<a id="file-week5-knowledge-base-contracts-contract-with-roadway-insurance-inc--for-carllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Roadway Insurance Inc. for Carllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Roadway Insurance Inc. for Carllm.md`

# Contract with Roadway Insurance Inc. for Carllm

---

## Terms

1. **Agreement Effective Date**: This contract is effective as of January 1, 2025.
2. **Duration**: This agreement will remain in effect for a term of 12 months, concluding on December 31, 2025.
3. **Subscription Type**: Roadway Insurance Inc. agrees to subscribe to the **Professional Tier** of Carllm, at a cost of $2,500/month, totaling $30,000 for the duration of this contract.
4. **Payment Terms**: Payments are due on the first of each month. Late payments will incur a penalty of 1.5% per month.
5. **Termination Clause**: Either party may terminate this agreement with 30 days' written notice prior to the end of the term. If terminated early, fees will be calculated on a pro-rata basis.

---

## Renewal

1. **Automatic Renewal**: This agreement will automatically renew for an additional 12-month term unless either party provides written notice of non-renewal at least 30 days before the expiration date.
2. **Price Adjustments**: Subscription fees may be adjusted for the renewal term in accordance with market conditions and the company's pricing policies, with 60 days' prior notice provided to Roadway Insurance Inc.

---

## Features

1. **Access to Core Features**: Roadway Insurance Inc. will have access to all Professional Tier features, including:
   - AI-Powered Risk Assessment
   - Advanced Analytics & Fraud Detection
   - Instant Quoting System
   - Customizable Coverage Plans
   - Customer Insights Dashboard
   
2. **Mobile Integration**: All features will be accessible through a mobile application that Insurellm will provide.
3. **Customer Support**: Includes 24/7 automated customer support via AI chatbots and access to dedicated account management support during business hours.

---

## Support

1. **Technical Support**: Roadway Insurance Inc. will receive priority technical support from Insurellm for any issues arising from the Carllm product.
2. **Training**: Insurellm will provide up to 5 training sessions for Roadway Insurance Inc. staff on the effective use of the Carllm platform, scheduled at mutual convenience.
3. **Updates and Maintenance**: Regular updates to the Carllm platform will be conducted quarterly, and any maintenance outages will be communicated at least 48 hours in advance.

---

*This contract outlines the terms of the relationship between Insurellm and Roadway Insurance Inc. for the Carllm product, emphasizing the collaborative spirit aimed at transforming the auto insurance landscape.*


---

<a id="file-week5-knowledge-base-contracts-contract-with-safehaven-property-insurance-for-homellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with SafeHaven Property Insurance for Homellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with SafeHaven Property Insurance for Homellm.md`

# Contract with SafeHaven Property Insurance for Homellm

**Contract Date:** May 3, 2025
**Contract Number:** HM-2025-E-0112
**Parties:**
- Insurellm, Inc.
- SafeHaven Property Insurance, Inc.

---

## Terms

1. **Coverage:** Insurellm agrees to provide SafeHaven Property Insurance with enterprise access to the Homellm platform, including white-label capabilities, unlimited policies, dedicated infrastructure, and comprehensive IoT integration for their property insurance operations.

2. **Duration:** This agreement is effective for a period of 36 months from the contract date.

3. **Payment:** SafeHaven Property Insurance shall pay custom Enterprise Tier pricing of $22,000 per month for months 1-12, $24,000 per month for months 13-24, and $26,000 per month for months 25-36, totaling $864,000 over the contract term.

4. **Policy Volume**: Enterprise Tier supports unlimited policies. SafeHaven currently has 45,000 active homeowners policies across 6 states.

5. **Service Level Agreement:** Insurellm guarantees 99.9% platform uptime measured monthly, with 7% monthly credit for each 0.1% below target, maximum 35% monthly credit.

6. **Confidentiality:** Both parties agree to maintain strict confidentiality of proprietary algorithms, property data, pricing models, and business strategies.

7. **Data Security:** Insurellm maintains SOC 2 Type II compliance, ISO 27001 certification, and annual third-party security audits.

---

## Renewal

This agreement includes a 90-day mutual renewal notice period. SafeHaven receives most-favored-customer pricing and priority access to new features including climate risk modeling and IoT innovations.

---

## Features

SafeHaven Property Insurance will receive the complete Homellm Enterprise suite:

1. **Unlimited Policy Administration:** Full support for SafeHaven's 45,000+ policies with scalability to 200,000+ policies as business expands.

2. **White-Label Platform:** Complete branding customization:
   - Custom domains (quote.safehavenproperty.com, myhome.safehavenproperty.com)
   - Branded mobile apps for iOS and Android with custom UI
   - Customized policyholder communications
   - Co-branded agent and broker portals

3. **Advanced AI Risk Assessment:** Enterprise-grade property risk analysis:
   - Aerial imagery analysis for roof condition, vegetation, and hazards
   - Property characteristic assessment (age, construction, square footage)
   - Location-based risk scoring (wildfire, flood, hail, wind, earthquake)
   - Catastrophe modeling integration (RMS, AIR, CoreLogic)
   - Replacement cost estimation with inflation trending
   - Neighborhood risk assessment
   - Claims history analysis across all carriers
   - Credit-based insurance scoring

4. **Dynamic Pricing Model:** Sophisticated pricing engine:
   - Real-time rate optimization across 200+ rating variables
   - Competitive intelligence and market positioning
   - Capacity-based dynamic pricing
   - Multi-policy bundling discounts
   - Loyalty and tenure credits
   - Loss-free discount automation
   - Telematics and IoT-based discounts

5. **Instant Claims Processing:** Advanced claims automation:
   - AI-driven FNOL with photo/video upload
   - Computer vision damage assessment
   - Automated repair cost estimation
   - Contractor network integration with 2,000+ vendors
   - Claims routing and assignment
   - Payment automation with multi-party splits
   - Fraud detection with pattern analysis
   - Subrogation opportunity identification

6. **Predictive Maintenance Alerts:** IoT-powered risk prevention:
   - Integration with smart home devices (water leak sensors, smoke detectors, security systems)
   - Weather alert system with pre-storm notifications
   - Freeze warning and pipe burst prevention
   - Roof deterioration monitoring
   - HVAC and appliance failure prediction
   - Wildfire proximity alerts
   - Proactive policyholder communication to prevent losses

7. **Multi-Channel Integration:** Unified platform:
   - Agent portal for 1,500+ independent agents
   - Direct-to-consumer quoting engine
   - Broker portal with co-branding
   - Call center integration
   - Web and mobile app quoting
   - Smart home device connectivity

8. **Customer Portal:** Comprehensive self-service:
   - 24/7 policy access and document retrieval
   - Coverage modification requests
   - Digital insurance cards
   - Claims submission and tracking
   - Payment processing and billing history
   - Smart home device management
   - Maintenance reminders and home care tips
   - Disaster preparedness resources

9. **IoT Device Integration:** Smart home platform:
   - Water leak detection systems (Flo by Moen, Phyn, LeakSmart)
   - Smart smoke and CO detectors (Nest Protect, First Alert)
   - Security systems (Ring, SimpliSafe, ADT)
   - Smart thermostats (Nest, Ecobee)
   - Weather stations
   - Roof monitoring sensors
   - Premium discounts for IoT adoption (up to 20%)
   - Real-time alerts and intervention protocols

10. **Complete API Access:** Unlimited API calls:
    - Integration with SafeHaven's core systems
    - Third-party data providers (CoreLogic, Verisk, LexisNexis)
    - Catastrophe modeling systems
    - Agent management platforms
    - Payment processors
    - Document management systems
    - Marketing automation

11. **Multi-State Operations:** Comprehensive support:
    - State-specific forms and endorsements for all 6 states
    - Regulatory compliance monitoring
    - Rate and form filing management
    - Multi-state licensing tracking
    - Catastrophe response protocols by state

12. **Catastrophe Management:** Disaster response tools:
    - Pre-CAT modeling and exposure management
    - Real-time storm tracking and impact assessment
    - CAT claims triage and routing
    - Mobile claims team dispatch
    - Vendor surge capacity activation
    - Policyholder communication campaigns
    - Emergency payment processing

---

## Support

Insurellm commits to comprehensive Enterprise-level support for SafeHaven Property Insurance:

1. **Dedicated Success Team:**
   - VP-level executive sponsor with quarterly strategic reviews
   - Senior Customer Success Manager with bi-weekly check-ins
   - Technical Account Manager for system optimization
   - Solutions Architect for IoT and innovation projects
   - Quarterly executive business reviews with detailed metrics

2. **24/7/365 Premium Support:**
   - 20-minute response time for P1 critical issues
   - 1-hour response for P2 high-priority issues
   - 4-hour response for P3 standard issues
   - Dedicated support team familiar with SafeHaven's operations
   - Private Slack channel with engineering access
   - Emergency CAT response team (15-minute response during disasters)
   - Quarterly on-site visits (minimum 4 per year)

3. **Comprehensive Implementation:**
   - 8-month phased implementation program
   - Dedicated project manager and PMO
   - Migration of 45,000 policies from legacy system
   - Training for 60+ staff members
   - Agent training program for 200+ top-producing agents
   - Parallel processing for 90 days
   - Go-live support with 6-week on-site presence

4. **Training and Enablement:**
   - Comprehensive role-based training programs
   - Underwriter certification on AI risk assessment
   - Claims adjuster training on computer vision tools
   - IoT device training for customer service reps
   - Train-the-trainer program for SafeHaven's team
   - Annual user conference attendance (5 attendees, all expenses)
   - Monthly advanced training webinars
   - Unlimited online learning platform access

5. **Custom Development:**
   - 1,200 hours annually of custom development
   - Dedicated development resources for SafeHaven-specific features
   - Priority feature requests with roadmap inclusion
   - Beta access to new features 60 days before general release
   - Joint innovation projects for smart home and IoT
   - Climate risk modeling enhancements

6. **Integration Services:**
   - Enterprise integration with SafeHaven's systems:
     - Duck Creek policy administration
     - Applied Epic agency management
     - Guidewire ClaimCenter
     - IoT platforms (Nationwide Canopy, Ting, others)
     - Catastrophe modeling (RMS RiskLink)
     - Payment processors
     - Salesforce CRM
   - Dedicated integration engineer (40% FTE)
   - Quarterly integration health assessments
   - Load testing before peak seasons (hurricane, wildfire)

7. **Analytics and Reporting:**
   - Custom dashboard development (up to 20 dashboards)
   - Real-time operational dashboards for underwriting and claims
   - Executive dashboards with drill-down analytics
   - Automated reporting suite (daily, weekly, monthly, quarterly)
   - Ad-hoc analytics support (25 requests/month)
   - Industry benchmarking against top property insurers
   - Catastrophe exposure and aggregation reporting
   - IoT adoption and loss prevention analytics

8. **IoT and Innovation Support:**
   - Quarterly IoT strategy sessions
   - New smart home device evaluation and integration
   - Pilot programs for emerging technologies
   - Consumer education materials for IoT programs
   - Marketing campaign support for smart home initiatives

9. **Catastrophe Response:**
   - Dedicated CAT support during disaster events
   - Pre-CAT system preparation and testing
   - Real-time claims surge capacity support
   - Post-CAT analysis and lessons learned
   - Annual CAT preparedness drills

10. **Continuous Improvement:**
    - Quarterly process optimization workshops
    - Annual efficiency audits with ROI documentation
    - Best practice sharing from insurance industry
    - Innovation lab for climate risk, AI, and IoT
    - Joint whitepapers and case studies
    - Speaking opportunities at industry events

---

**Signatures:**

_________________________________
**Jennifer Rodriguez**
**Title**: Chief Executive Officer
**Insurellm, Inc.**
**Date**: May 3, 2025

_________________________________
**Laura Mitchell**
**Title**: President & Chief Executive Officer
**SafeHaven Property Insurance, Inc.**
**Date**: May 3, 2025

---

This agreement establishes SafeHaven Property Insurance as a leading enterprise partner in property insurance innovation, leveraging Homellm's AI, IoT integration, and catastrophe management capabilities. This contract supersedes all prior agreements.


---

<a id="file-week5-knowledge-base-contracts-contract-with-stellar-insurance-co--for-rellm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Stellar Insurance Co. for Rellm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Stellar Insurance Co. for Rellm.md`

# Contract with Stellar Insurance Co. for Rellm

## Terms
This contract is made between **Insurellm**, located at 123 Innovation Lane, San Francisco, CA, and **Stellar Insurance Co.**, located at 456 Galaxy Road, Chicago, IL. The effective date of this agreement is **January 1, 2024**. 

### Duration
The initial term of this agreement shall be for **12 months**, commencing from the effective date. The contract will automatically renew for successive **12-month periods** unless either party provides written notice of non-renewal at least **30 days** prior to the expiration of the current term.

### Payment Terms
Stellar Insurance Co. agrees to pay Insurellm a monthly subscription fee of **$10,000** for the **Professional Plan** of the Rellm product. Payments are due on the **1st of each month**.

### Termination
Either party may terminate this agreement with a **30-day written notice**. In the event of a material breach, the non-breaching party may terminate immediately, provided a written notice is given.

## Renewal
This contract will renew automatically for additional 12-month terms unless written notice is provided by either party 30 days prior to the renewal date. Upon renewal, pricing may be adjusted based on agreed-upon inflation adjustments or additional services requested by Stellar Insurance Co.

## Features
Stellar Insurance Co. will receive access to the following features of the Rellm product:

- **AI-Driven Analytics**: Predictive insights into risk exposures tailored for the reinsurance industry.
- **Seamless Integrations**: Compatibility with existing systems for policy management and claims processing.
- **Risk Assessment Module**: Comprehensive evaluation of risk profiles using advanced modeling techniques.
- **Customizable Dashboard**: Tailored user interface presenting relevant metrics and performance indicators.
- **Regulatory Compliance Tools**: Features to ensure adherence to local and international regulations.
- **Client and Broker Portals**: Dedicated portals for enhanced communication and document sharing.

## Support
Insurellm provides Stellar Insurance Co. with the following support services:

- **24/7 Technical Support**: Access to dedicated support representatives via phone and online chat.
- **Quarterly Account Review**: Meetings to discuss performance metrics and uncover additional needs.
- **Training Sessions**: Initial orientation and ongoing training opportunities to maximize the effectiveness of Rellm usage.
- **Updates and Upgrades**: Regular software updates and enhancements are included as part of the subscription.

Stellar Insurance Co. acknowledges receipt of the Rellm product summary and agrees to the terms set forth above. By signing below, both parties confirm their acceptance of this contract.

**For Insurellm**  
______________________________  
[Signature]  
[Name, Title]  
[Date]  

**For Stellar Insurance Co.**  
______________________________  
[Signature]  
[Name, Title]  
[Date]


---

<a id="file-week5-knowledge-base-contracts-contract-with-summit-commercial-insurance-for-bizllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Summit Commercial Insurance for Bizllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Summit Commercial Insurance for Bizllm.md`

# Contract with Summit Commercial Insurance for Bizllm

**Contract Date:** March 15, 2025
**Contract Number:** BZ-2025-0091
**Parties:**
- Insurellm, Inc.
- Summit Commercial Insurance, LLC

---

## Terms

1. **Coverage:** Insurellm agrees to provide Summit Commercial Insurance with access to the Bizllm platform, enabling comprehensive commercial insurance underwriting and policy administration across multiple lines including general liability, professional liability, and property coverage.

2. **Duration:** This agreement is effective for a period of 18 months from the contract date, after which it will automatically renew unless terminated by either party with a written 45-day notice.

3. **Payment:** Summit Commercial Insurance shall pay a monthly fee of $6,000, due by the 1st of every month for the Business Tier package.

4. **Confidentiality:** Both parties agree to maintain strict confidentiality of proprietary information, trade secrets, and customer data disclosed during the execution of this contract.

5. **Liability:** Insurellm's liability under this agreement shall be limited to direct damages and shall not exceed the total fees paid by Summit Commercial Insurance in the last 12 months prior to the date of the claim.

6. **Data Security:** Insurellm commits to maintaining industry-standard encryption and security protocols to protect all client data processed through the Bizllm platform.

---

## Renewal

Unless either party provides a written notice of termination at least 45 days prior to the expiration of the contract term, this agreement will automatically renew for an additional 18-month term under the same terms and conditions, subject to pricing adjustments communicated at least 90 days in advance.

---

## Features

Summit Commercial Insurance will receive the following features with Bizllm Business Tier:

1. **Multi-Line Underwriting Engine:** Comprehensive underwriting platform supporting general liability, professional liability, property, and workers' compensation insurance products.

2. **Business Intelligence Integration:** Automated data gathering from business registries, financial databases, and industry reports for streamlined underwriting.

3. **Commercial Property Evaluation:** Advanced property risk modeling incorporating location data, building characteristics, and catastrophe modeling.

4. **Workers' Compensation Optimization:** Integrated tools analyzing payroll data, industry classifications, and claims history for accurate pricing.

5. **Portfolio Management Dashboard:** Analytics providing line-of-business performance, loss ratios, and renewal rates insights.

6. **Agent and Broker Portal:** Dedicated portals enabling distribution partners to quote, bind, and service policies efficiently.

---

## Support

Insurellm commits to providing comprehensive support to Summit Commercial Insurance, which includes:

1. **Onboarding:** A 3-week intensive training program for up to 15 Summit Commercial staff members to ensure effective use of Bizllm, including hands-on workshops and certification.

2. **Dedicated Support Team:** A dedicated account manager and technical support team available Monday-Friday 7 AM to 7 PM EST, with emergency support available 24/7.

3. **Regular Updates:** Insurellm will provide quarterly platform updates and enhancements, including new features, security improvements, and regulatory compliance updates.

4. **Integration Assistance:** Technical support for integrating Bizllm with Summit's existing policy administration and claims management systems.

5. **Performance Reviews:** Quarterly business reviews to assess platform utilization, identify optimization opportunities, and discuss strategic initiatives.

---

**Signatures:**

_________________________________
**Michael Torres**
**Title**: Chief Revenue Officer
**Insurellm, Inc.**

_________________________________
**Patricia Lawson**
**Title**: Vice President of Operations
**Summit Commercial Insurance, LLC**

---

This agreement represents the complete understanding of both parties regarding the use of the Bizllm product and supersedes any prior agreements or communications.


---

<a id="file-week5-knowledge-base-contracts-contract-with-techdrive-insurance-for-carllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with TechDrive Insurance for Carllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with TechDrive Insurance for Carllm.md`

# Contract with TechDrive Insurance for Carllm

**Contract Date:** October 1, 2024  
**Contract Duration:** 12 months

---

## Terms

1. **Parties Involved**: This contract is entered into between Insurellm (the "Provider") and TechDrive Insurance (the "Customer").
   
2. **License Grant**: Insurellm grants TechDrive Insurance a non-exclusive, non-transferable license to use the Carllm product as per the selected pricing tier (Professional Tier at $2,500/month).
   
3. **Payment Terms**: TechDrive Insurance agrees to make monthly payments of $2,500 for the duration of this contract, due on the 5th of each month.
   
4. **Confidentiality**: Both parties shall maintain confidentiality regarding each other’s proprietary information throughout the duration of this contract and for three years following its termination.

## Renewal

1. **Automatic Renewal**: This contract shall automatically renew for additional one-year terms unless either party provides written notice of non-renewal at least 30 days prior to the contract expiration.
   
2. **Pricing Review**: The pricing for any renewal period shall be discussed 60 days prior to the end of the term and agreed upon in writing.

## Features

1. **Included Features**: Under the Professional Tier, TechDrive Insurance will have access to the following features of Carllm:
   - AI-Powered Risk Assessment
   - Instant Quoting
   - Customizable Coverage Plans
   - Fraud Detection
   - Customer Insights Dashboard
   - Mobile Integration
   - Automated Customer Support

2. **System Requirements**: TechDrive Insurance must ensure that their existing systems meet the technical requirements to integrate with Carllm, as outlined in the onboarding documentation provided by Insurellm.

## Support

1. **Customer Support**: Insurellm will provide 24/7 customer support to TechDrive Insurance via AI-driven chatbots, ensuring timely resolution of inquiries and issues.

2. **Training**: TechDrive Insurance staff will receive onboarding training sessions to ensure effective utilization of the Carllm platform, scheduled within the first two weeks of contract commencement.

3. **System Updates**: The Provider will push regular updates to improve system performance and add new features. TechDrive Insurance will receive prior notification of any significant upgrades that may affect current operations.

---

**Signatures:**

**Insurellm Representative:**  
Name: John Smith  
Title: Account Manager  
Date: ____________

**TechDrive Insurance Representative:**  
Name: Sarah Johnson  
Title: Operations Director  
Date: ____________  

This contract will serve as the foundational agreement for the ongoing collaboration between Insurellm and TechDrive Insurance in optimizing their auto insurance offerings through the Carllm product.


---

<a id="file-week5-knowledge-base-contracts-contract-with-united-healthcare-alliance-for-healthllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with United Healthcare Alliance for Healthllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with United Healthcare Alliance for Healthllm.md`

# Contract with United Healthcare Alliance for Healthllm

**Contract Date:** May 15, 2025
**Contract Number:** HL-2025-E-0156
**Parties:**
- Insurellm, Inc.
- United Healthcare Alliance, LLC

---

## Terms

1. **Coverage:** Insurellm agrees to provide United Healthcare Alliance with enterprise access to the Healthllm platform, including extensive customization, multi-state support, dedicated infrastructure, and premium support services for their nationwide health insurance operations covering 250,000+ members across 12 states.

2. **Duration:** This agreement is effective for a period of 48 months from the contract date, representing Insurellm's most strategic long-term healthcare partnership.

3. **Payment:** United Healthcare Alliance shall pay custom Enterprise Tier pricing of $52,000 per month for months 1-12, $56,000 per month for months 13-24, $60,000 per month for months 25-36, and $64,000 per month for months 37-48, totaling $2,784,000 over the contract term.

4. **Service Level Agreement:** Insurellm guarantees 99.95% uptime measured monthly, with financial credits: 7% monthly credit for each hour of unplanned downtime exceeding the SLA, maximum 50% monthly credit.

5. **Confidentiality:** Both parties agree to maintain the highest level of confidentiality regarding AI algorithms, predictive models, member PHI, provider contracts, and strategic initiatives.

6. **Security and Compliance:** Insurellm commits to maintaining HIPAA compliance, HITRUST certification, SOC 2 Type II, and annual third-party security audits with penetration testing.

7. **Business Continuity:** Guaranteed 2-hour recovery time objective (RTO) and 15-minute recovery point objective (RPO) with active-active data center configuration.

---

## Renewal

This agreement includes a mutual 120-day renewal notice period. United Healthcare Alliance receives most-favored-customer pricing guarantees and priority access to all new features. Contract may be extended in 12 or 24-month increments with mutual written agreement and will include joint planning for next-generation healthcare technology initiatives.

---

## Features

United Healthcare Alliance will receive the complete Healthllm Enterprise suite with custom enhancements:

1. **Unlimited Member Administration:** No capacity restrictions, supporting United's 250,000+ members with scalability to 1 million+ members as business expands.

2. **Multi-State Operations:** Complete support for health insurance administration across all 12 states where United operates:
   - State-specific plan designs and benefit variations
   - 50-state regulatory compliance monitoring
   - Multi-state network adequacy reporting
   - State-specific form filing and rate approvals
   - Local market competitive intelligence

3. **White-Label Platform:** Complete branding customization:
   - Custom domains (members.unitedhealthcarealliance.com, providers.unitedhealthcarealliance.com)
   - Branded mobile apps for iOS and Android with full UI/UX customization
   - Customized member communications and marketing materials
   - Co-branded provider portals and broker platforms

4. **Advanced AI Claims Adjudication:** Enterprise-grade claims processing:
   - Auto-adjudication rate of 85%+ for clean claims
   - Real-time fraud detection with 92%+ accuracy
   - Predictive payment integrity scoring
   - Provider billing pattern analysis
   - Upcoding and unbundling detection
   - Coordination of benefits (COB) automation
   - Subrogation opportunity identification

5. **Population Health Management:** Comprehensive analytics for value-based care:
   - Real-time risk stratification across entire member population
   - Chronic disease identification and progression modeling
   - Predictive analytics for 30+ conditions
   - Hospital readmission prevention protocols
   - Care gap analysis for HEDIS and STAR measures
   - Social determinants of health (SDOH) integration
   - Health equity analytics and disparity identification

6. **Complete API Access:** Unlimited API calls supporting:
   - Real-time integration with United's core systems
   - Provider portal and directory synchronization
   - Claims clearinghouse EDI transactions (837, 835, 834, 270/271)
   - Pharmacy benefit manager (PBM) integration
   - Health Information Exchange (HIE) connectivity
   - Data warehouse bidirectional sync
   - Third-party vendor integrations (lab systems, imaging centers, etc.)

7. **Advanced Provider Network Management:**
   - Credentialing and re-credentialing for 15,000+ providers
   - Contract management with version control and approval workflows
   - Provider performance scorecards and tiering
   - Network adequacy modeling and gap analysis
   - Cost and quality analytics by provider
   - Center of Excellence (COE) program management
   - Value-based payment arrangement tracking

8. **Comprehensive Medication Management:**
   - Multi-tier formulary management (national and state-specific)
   - Prior authorization with clinical decision support
   - Step therapy and quantity limit enforcement
   - Specialty pharmacy program management
   - Biosimilar and generic substitution optimization
   - Medication adherence prediction and intervention
   - Drug spend forecasting and budgeting
   - Manufacturer rebate tracking and optimization

9. **Member Engagement Suite:**
   - Omnichannel communication platform (SMS, email, push, voice)
   - Personalized member portal with AI-powered chatbot
   - Telehealth platform integration (video visits, e-consults)
   - Preventive care reminder campaigns
   - Wellness program platform with incentives and gamification
   - Member satisfaction surveying and feedback analysis
   - Health literacy tools and educational content

10. **Quality and Performance Management:**
    - HEDIS measure calculation and reporting
    - STAR ratings optimization for Medicare Advantage
    - CAHPS survey administration and analysis
    - Quality improvement initiative tracking
    - Provider pay-for-performance administration
    - Shared savings calculation for ACO programs
    - Risk adjustment and HCC coding validation

11. **Advanced Analytics and Business Intelligence:**
    - Real-time operational dashboards for all user roles
    - Executive dashboards with KPIs and trend analysis
    - Predictive modeling for medical cost trends
    - Member churn and retention analysis
    - Market share and competitive positioning reports
    - Financial forecasting and budget variance analysis
    - Custom analytics with embedded data science team support

12. **Regulatory Compliance and Reporting:**
    - ACA compliance monitoring (MLR, essential health benefits, preventive services)
    - Multi-state regulatory filing management
    - CMS reporting for Medicare Advantage products
    - State insurance department examinations support
    - HIPAA privacy and security compliance with audit trails
    - Fraud, waste, and abuse (FWA) detection and reporting
    - Annual compliance certification and attestation

---

## Support

Insurellm commits to comprehensive Enterprise-level support for United Healthcare Alliance:

1. **Dedicated Success Team:**
   - Executive sponsor (CEO-level) with monthly strategic reviews
   - Dedicated Vice President of Customer Success with weekly engagement
   - Senior Technical Account Manager for system optimization
   - Solutions Architect team for ongoing innovation (2 FTE)
   - Data Science team for advanced analytics projects (1.5 FTE)
   - Quarterly executive business reviews with C-suite from both companies

2. **24/7/365 Premium Support:**
   - Guaranteed 10-minute response for P1 critical issues
   - 30-minute response for P2 high-priority issues
   - 2-hour response for P3 standard issues
   - Dedicated support team of 8+ specialists familiar with United's environment
   - Private war room for incident management
   - Dedicated Slack and Microsoft Teams channels with engineering access
   - Quarterly on-site support visits (minimum 8 per year)

3. **Comprehensive Implementation:**
   - 18-month phased implementation program with 4 major go-live events
   - Dedicated program management office (PMO) with weekly steering committee
   - Migration of 250,000+ member records from legacy systems
   - Integration with 15,000+ provider records and credentialing data
   - Training for 300+ United staff across all departments
   - Training for 100+ key provider practices and health systems
   - Parallel processing with legacy system for 120 days
   - Go-live support with 12-week on-site Insurellm team presence (6-10 people)

4. **Training and Enablement:**
   - Comprehensive role-based training programs for all staff
   - Executive leadership training on healthcare AI and analytics
   - Train-the-trainer certification for United's L&D team
   - Annual user conference attendance (10 attendees, all expenses paid)
   - Monthly advanced training sessions on new features
   - Unlimited online learning platform access with 200+ courses
   - Custom training content development for United-specific processes
   - Clinical training for care management and utilization review staff

5. **Custom Development:**
   - 3,000 hours annually of custom development included
   - Dedicated development team (4 developers, 1 PM, 1 QA) for United-specific features
   - Priority feature requests with guaranteed product roadmap inclusion
   - Beta access to all new features 120 days before general release
   - Joint innovation projects and co-development opportunities
   - Input into 5-year product strategy and roadmap
   - Potential for United to influence industry direction through partnership

6. **Integration Services:**
   - Enterprise integration with United's complex system landscape:
     - HealthEdge iBridge policy administration
     - Epic care management system integration
     - Salesforce Health Cloud CRM
     - Multiple PBMs (CVS Caremark, Express Scripts)
     - Availity and Change Healthcare clearinghouses
     - Truven Health Analytics
     - Provider credentialing systems (CAQH ProView)
     - NCQA HEDIS reporting systems
     - Financial systems (Oracle ERP, Workday)
     - Data lake on Snowflake and AWS
   - Dedicated integration team (2 FTE integration engineers)
   - Monthly integration health assessments with optimization
   - Performance tuning and load testing before peak periods (open enrollment)

7. **Analytics and Reporting:**
   - Custom dashboard development (unlimited)
   - Real-time operational dashboards for claims, enrollment, utilization
   - Executive dashboards with drill-down capabilities
   - Automated reporting suite (daily, weekly, monthly, quarterly, annual)
   - Ad-hoc analytics support (unlimited requests with 48-hour SLA)
   - Industry benchmarking against top 100 health plans
   - Predictive modeling consultation (bi-weekly sessions)
   - Embedded data science team for advanced projects
   - Access to Insurellm's proprietary healthcare benchmarking database

8. **Compliance and Regulatory Support:**
   - Monthly compliance reviews with detailed documentation
   - Annual HIPAA security risk assessment with remediation planning
   - Annual HITRUST assessment support
   - ACA reporting (1094/1095 forms, MLR calculations, essential health benefits)
   - Medicare Advantage CMS reporting support
   - Multi-state regulatory filing coordination
   - Quality measure calculation (HEDIS, STAR, CAHPS)
   - External audit support (state exams, CMS audits, accreditation)
   - Fraud, waste, and abuse program support

9. **Continuous Improvement:**
   - Bi-weekly process optimization workshops
   - Quarterly efficiency audits with detailed ROI analysis
   - Best practice sharing from across Insurellm's customer base
   - Innovation lab partnership for emerging technologies:
     - AI and machine learning advancements
     - Blockchain for claims and credentialing
     - Natural language processing for clinical documentation
     - Predictive analytics for population health
   - Joint whitepapers and case studies for industry publication
   - Speaking opportunities at major industry conferences (AHIP, HIMSS)
   - Collaboration on thought leadership and regulatory advocacy

---

**Signatures:**

_________________________________
**Jennifer Rodriguez**
**Title**: Chief Executive Officer
**Insurellm, Inc.**
**Date**: May 15, 2025

_________________________________
**James Patterson**
**Title**: Chairman & Chief Executive Officer
**United Healthcare Alliance, LLC**
**Date**: May 15, 2025

---

This agreement establishes United Healthcare Alliance as Insurellm's flagship enterprise health insurance partner, representing the most comprehensive strategic partnership in Insurellm's history. This partnership will drive innovation in healthcare technology and set new standards for AI-powered health insurance operations. This contract supersedes all prior agreements and communications.


---

<a id="file-week5-knowledge-base-contracts-contract-with-velocity-auto-solutions-for-carllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with Velocity Auto Solutions for Carllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with Velocity Auto Solutions for Carllm.md`

# Contract with Velocity Auto Solutions for Carllm

**Contract Date:** October 1, 2023  
**Contract Number:** C-12345-2023  
**Client:** Velocity Auto Solutions  
**Product:** Carllm Auto Insurance Solution  

---

## Terms

1. **Duration**: This contract is effective for a period of 12 months from the contract date.  
2. **Payment Schedule**: Velocity Auto Solutions agrees to pay Insurellm the total fee associated with the selected subscription tier on a monthly basis, beginning on the contract date.  
3. **Confidentiality**: Both parties agree to keep all proprietary information confidential and not to disclose it to any third parties without written consent.  
4. **Intellectual Property**: All components of Carllm and any related technology are the property of Insurellm, and license is granted to Velocity Auto Solutions for internal use only.  

## Renewal

1. **Automatic Renewal**: This contract will automatically renew for successive 12-month periods unless either party provides written notice at least 30 days prior to the end of the initial term or any renewal term.  
2. **Rate Adjustment**: Subscription pricing may be subject to adjustment, with Insurellm providing a 60-day advance notice of any changes prior to renewal.  

## Features

1. **Included Features**:  
   - AI-Powered Risk Assessment  
   - Instant Quoting and Customizable Coverage Plans  
   - Fraud Detection Systems  
   - Customer Insights Dashboard  
   - Automated Customer Support  

2. **Feature Enhancements**: Velocity Auto Solutions will receive updates to the Carllm product as outlined in the Insurellm 2025-2026 Roadmap, including mobile integration and telematics-based pricing enhancements.

## Support

1. **Customer Support**: Velocity Auto Solutions will have access to Insurellm’s customer support team via email or chatbot, available 24/7.  
2. **Technical Maintenance**: Regular maintenance and updates to the Carllm platform will be conducted by Insurellm, with any downtime communicated in advance.  
3. **Training & Resources**: Initial training sessions will be provided for Velocity Auto Solutions’ staff to ensure effective use of the Carllm suite. Regular resources and documentation will be made available online.

---

**Accepted and Agreed:**  
**For Velocity Auto Solutions**  
Signature: _____________________  
Name: John Doe  
Title: CEO  
Date: _____________________  

**For Insurellm**  
Signature: _____________________  
Name: Jane Smith  
Title: VP of Sales  
Date: _____________________


---

<a id="file-week5-knowledge-base-contracts-contract-with-wellcare-insurance-co--for-healthllm-md"></a>
## File: `week5/knowledge-base/contracts/Contract with WellCare Insurance Co. for Healthllm.md`

> **Path in repository:** `week5/knowledge-base/contracts/Contract with WellCare Insurance Co. for Healthllm.md`

# Contract with WellCare Insurance Co. for Healthllm

**Contract Date:** March 8, 2025
**Contract Number:** HL-2025-0021
**Parties:**
- Insurellm, Inc.
- WellCare Insurance Co.

---

## Terms

1. **Coverage:** Insurellm agrees to provide WellCare Insurance Co. with access to the Healthllm platform, enabling comprehensive health insurance operations including plan design, eligibility verification, claims adjudication, and member engagement.

2. **Duration:** This agreement is effective for a period of 12 months from the contract date, with automatic renewal unless terminated with 30-day written notice.

3. **Payment:** WellCare Insurance Co. shall pay a monthly fee of $8,000, due by the 1st of every month for the Essential Tier package.

4. **Member Coverage**: Essential Tier supports health insurance administration for up to 15,000 covered members. Current enrollment: 11,000 members.

5. **Confidentiality:** Both parties agree to maintain strict confidentiality of proprietary information, protected health information (PHI), and member data in compliance with HIPAA regulations.

6. **HIPAA Compliance:** Insurellm operates as a Business Associate and maintains full HIPAA compliance including Business Associate Agreement (BAA).

7. **Liability:** Insurellm's liability is limited to direct damages not exceeding the total fees paid in the preceding 12 months.

---

## Renewal

Unless either party provides written notice of termination at least 30 days prior to contract expiration, this agreement automatically renews for successive 12-month terms. Pricing may be adjusted annually with 60 days' advance notice, capped at 10% increase per year.

---

## Features

WellCare Insurance Co. will receive the following Essential Tier features:

1. **Intelligent Plan Design:** AI-powered tools for creating competitive health plans:
   - Market trend analysis and competitive benchmarking
   - Member demographic analysis
   - Healthcare utilization pattern analysis
   - Benefit structure optimization
   - Deductible and copay modeling
   - Network configuration recommendations

2. **Real-Time Eligibility Verification:** Instant coverage verification:
   - Provider network integration for real-time checking
   - Member status validation
   - Coverage level confirmation
   - Dependent eligibility verification
   - Prior authorization status
   - Reduces claim denials due to eligibility issues

3. **AI-Driven Claims Adjudication:** Automated claims processing:
   - Machine learning-based claims review
   - Fraud detection and prevention
   - Payment accuracy verification
   - Auto-adjudication for clean claims
   - Denial management and appeals tracking
   - Learning from historical claim patterns

4. **Provider Network Management:** Comprehensive network administration:
   - Provider contract management
   - Credentialing and re-credentialing workflows
   - Network adequacy monitoring
   - Provider performance metrics
   - Contract negotiation analytics
   - Cost savings opportunity identification

5. **Member Engagement Platform:** Mobile-first member portal:
   - Digital ID cards
   - Claims status tracking
   - Provider directory search
   - Coverage information access
   - Telehealth service integration
   - Push notifications for preventive care

6. **Basic Medication Management:**
   - Formulary management tools
   - Prior authorization workflows
   - Generic substitution recommendations
   - Drug interaction checking
   - Medication adherence tracking

7. **Regulatory Compliance Engine:**
   - ACA (Affordable Care Act) compliance monitoring
   - State mandate tracking
   - HIPAA privacy and security compliance
   - Automated regulatory reporting
   - Form filing and approval tracking

8. **Standard Analytics:** Dashboards tracking:
   - Claims volume and processing time
   - Medical loss ratio (MLR)
   - Member satisfaction scores
   - Provider network utilization
   - Cost per member per month (PMPM)

---

## Support

Insurellm commits to providing comprehensive support to WellCare Insurance Co.:

1. **Onboarding:** 4-week implementation program including:
   - System configuration for WellCare's plan designs
   - Training for up to 15 staff members (30 hours total)
   - Integration with existing systems (policy admin, provider network)
   - Data migration for current 11,000 members
   - Provider network data import and validation

2. **Technical Support:**
   - Email and phone support Monday-Friday 7 AM - 7 PM EST
   - Response time: 8 hours for critical issues, 24 hours for standard
   - Online ticketing system with status tracking
   - Knowledge base and FAQ library
   - Video tutorials and user guides

3. **Platform Updates:**
   - Quarterly feature releases with new capabilities
   - Monthly security patches and bug fixes
   - Regulatory compliance updates as laws change
   - Release notes and upgrade documentation
   - Advance notice of updates (minimum 21 days)

4. **Account Management:**
   - Named customer success manager
   - Quarterly business review meetings
   - Usage analytics and optimization recommendations
   - Industry trends and best practices sharing
   - Assistance with tier upgrade evaluation

5. **Compliance Support:**
   - Annual HIPAA compliance review
   - Regulatory update notifications
   - State insurance department filing assistance
   - ACA reporting support (1095 forms)
   - Audit preparation assistance

6. **Integration Support:** Technical assistance connecting Healthllm with:
   - Existing policy administration systems
   - Provider credentialing systems
   - Pharmacy benefit managers (PBMs)
   - Clearinghouses for EDI transactions
   - Member portal and mobile apps

---

**Signatures:**

_________________________________
**Sarah Chen**
**Title**: Vice President of Sales
**Insurellm, Inc.**
**Date**: March 8, 2025

_________________________________
**Dr. Raymond Foster**
**Title**: Chief Medical Officer & COO
**WellCare Insurance Co.**
**Date**: March 8, 2025

---

This agreement enables WellCare Insurance Co. to modernize their health insurance operations with AI-powered technology while ensuring regulatory compliance and improved member outcomes.


---

<a id="file-week5-knowledge-base-employees-alex-chen-md"></a>
## File: `week5/knowledge-base/employees/Alex Chen.md`

> **Path in repository:** `week5/knowledge-base/employees/Alex Chen.md`

# HR Record

# Alex Chen

## Summary
- **Date of Birth:** March 15, 1990
- **Job Title:** Backend Software Engineer
- **Location:** San Francisco, California
- **Current Salary:** $115,000  

## Insurellm Career Progression
- **April 2020:** Joined Insurellm as a Junior Backend Developer. Focused on building APIs to enhance customer data security.
- **October 2021:** Promoted to Backend Software Engineer. Took on leadership for a key project developing a microservices architecture to support the company's growing platform.
- **March 2023:** Awarded the title of Senior Backend Software Engineer due to exemplary performance in scaling backend services, reducing downtime by 30% over six months.

## Annual Performance History
- **2020:**  
  - Completed onboarding successfully.  
  - Met expectations in delivering project milestones.  
  - Received positive feedback from the team leads.

- **2021:**  
  - Achieved a 95% success rate in project delivery timelines.  
  - Awarded "Rising Star" at the annual company gala for outstanding contributions.  

- **2022:**  
  - Exceeded goals by optimizing existing backend code, improving system performance by 25%.  
  - Conducted training sessions for junior developers, fostering knowledge sharing.  

- **2023:**  
  - Led a major overhaul of the API internal architecture, enhancing security protocols.  
  - Contributed to the company’s transition to a cloud-based infrastructure.  
  - Received an overall performance rating of 4.8/5.

## Compensation History
- **2020:** Base Salary: $80,000  
- **2021:** Base Salary Increase to $90,000; Received a performance bonus of $5,000.  
- **2022:** Base Salary Increase to $100,000; Performance bonus of $7,500 due to exceptional project outcomes.  
- **2023:** Base Salary Increase to $115,000; Performance bonus of $10,000 for leading pivotal projects.

## Other HR Notes
- Participates regularly in Insurellm's Diversity & Inclusion initiatives, championing tech accessibility for underrepresented communities.
- Completed several certifications in cloud architecture and DevOps, contributing to professional growth.
- Plans for a professional development course in AI and machine learning to further enhance backend capabilities in Insurellm's offerings.
- Acknowledged for volunteer efforts in local tech meetups, bringing seasoned engineers to mentor aspiring coders.  

Alex Chen continues to be a vital asset at Insurellm, contributing significantly to innovative backend solutions that help shape the future of insurance technology.


---

<a id="file-week5-knowledge-base-employees-alex-harper-md"></a>
## File: `week5/knowledge-base/employees/Alex Harper.md`

> **Path in repository:** `week5/knowledge-base/employees/Alex Harper.md`

# HR Record

# Alex Harper

## Summary
- **Date of Birth**: March 15, 1993
- **Job Title**: Sales Development Representative (SDR)
- **Location**: Denver, Colorado
- **Current Salary**: $75,000  

## Insurellm Career Progression
- **July 2021**: Joined Insurellm as a Sales Development Representative, focusing on lead generation and nurturing B2B relationships.  
- **January 2022**: Promoted to Senior Sales Development Representative due to exceptional performance in converting leads into clients.  
- **October 2022**: Completed an Internal Leadership Training Program, enhancing skills in team collaboration and strategic selling. Currently mentoring junior SDRs.  
- **April 2023**: Became involved in a cross-departmental project to streamline the customer onboarding process, showcasing initiative and leadership.  

## Annual Performance History  
- **2021**:  
  - **Performance Rating**: 4.5/5  
  - **Key Achievements**: Exceeded lead generation targets by 30%. Introduced a new CRM analytics tool resulting in improved tracking of customer interactions.  

- **2022**:  
  - **Performance Rating**: 4.8/5  
  - **Key Achievements**: Awarded "SDR of the Year" for outstanding contributions. Instrumental in securing 15 new B2B contracts, surpassing targets by 40%.  

- **2023**:  
  - **Performance Rating**: 4.7/5  
  - **Key Achievements**: Played a key role in the launch of a new product line with a 25% increase in lead-to-conversion rates. Completed advanced sales negotiation training with high marks.  

## Compensation History  
- **2021**:  
  - **Base Salary**: $55,000  
  - **Bonus**: $5,500 (10% of base due to performance)  

- **2022**:  
  - **Base Salary**: $65,000 (Promotion to Senior SDR)  
  - **Bonus**: $13,000 (20% of base due to performance)  

- **2023**:  
  - **Base Salary**: $75,000  
  - **Bonus**: $15,000 (20% of base)  

## Other HR Notes  
- **Training Completed**:  
  - CRM Analytics & Data Management Workshop (2021)  
  - Leadership Training Program (2022)  
  - Advanced Sales Negotiation Course (2023)  

- **Awards**:  
  - Insurellm "SDR of the Year" Award (2022)  
  - Monthly MVP Recognition (3 times in 2023)  

- **Interests**:  
  - In Alex's spare time, they enjoy participating in community volunteer programs, particularly those focused on financial literacy.  
  - Alex is also an avid runner and has participated in several charity marathons.  

- **Feedback from HR**:  
  - Alex Harper is noted for their work ethic, positive attitude, and willingness to go above and beyond for both clients and colleagues. Recognized for fostering a team spirit within the SDR team.


---

<a id="file-week5-knowledge-base-employees-alex-thomson-md"></a>
## File: `week5/knowledge-base/employees/Alex Thomson.md`

> **Path in repository:** `week5/knowledge-base/employees/Alex Thomson.md`

# HR Record

# Alex Thomson

## Summary
- **Date of Birth:** March 15, 1995
- **Job Title:** Sales Development Representative (SDR)
- **Location:** Austin, Texas
- **Current Salary:** $65,000  

## Insurellm Career Progression
- **November 2022** - Joined Insurellm as a Sales Development Representative. Alex Thomson quickly adapted to the team, demonstrating exceptional communication and rapport-building skills.
- **January 2023** - Promoted to Team Lead for special projects due to Alex's initiative in driving B2B customer outreach programs.  
- **August 2023** - Developed a training module for new SDRs at Insurellm, enhancing onboarding processes based on feedback and strategies that Alex Thomson pioneered.  
- **Current** - Continues to excel in the role, leading a small team of 5 SDRs while collaborating closely with the marketing department to identify new lead-generation strategies.  

## Annual Performance History  
- **2022** - Rated as "Exceeds Expectations." Alex Thomson achieved 150% of the sales target within the first three months.  
- **2023** - Rated "Outstanding." Recognized for innovative lead-generation tactics which contributed to a 30% increase in qualified leads for the sales team.  

### Highlights:
- Consistently maintained a 30-minute response time to inbound leads.
- Successfully coordinated webinars for product launches, which attracted over 2,000 potential customers.

## Compensation History
- **2022**: Base Salary - $55,000 | Bonus - $5,000  
- **2023**: Base Salary - $65,000 | Bonus - $10,000 (for exceeding sales targets and exceptional teamwork)  
- **Projected for 2024**: Anticipated salary increase due to Alex Thomson's significant contributions and successful completion of leadership training.

## Other HR Notes
- Alex Thomson is an active member of the Diversity and Inclusion committee at Insurellm and has participated in various community outreach programs.  
- Alex has received external training on advanced CRM usage, which has subsequently improved team efficiency and productivity.
- Continuous professional development through attending sales conventions and workshops, with plans to pursue certification in Sales Enablement in 2024.
- Recognized by peers for promoting a supportive and high-energy team environment, often organizing team-building activities to enhance camaraderie within the SDR department. 

--- 
**Comment:** Alex Thomson is considered a cornerstone of Insurellm’s sales team and has a bright future within the organization.


---

<a id="file-week5-knowledge-base-employees-amanda-foster-md"></a>
## File: `week5/knowledge-base/employees/Amanda Foster.md`

> **Path in repository:** `week5/knowledge-base/employees/Amanda Foster.md`

# HR Record

# Amanda Foster

## Summary
- **Date of Birth:** August 14, 1982
- **Job Title:** HR Business Partner
- **Location:** San Francisco, California
- **Current Salary:** $115,000

## Insurellm Career Progression
- **September 2016 - Present:** HR Business Partner
  - Partners with engineering and product leadership teams
  - Supports 85 employees across multiple departments
  - Leads talent acquisition strategy for technical roles
  - Drives performance management and organizational development initiatives

- **March 2013 - August 2016:** Senior HR Generalist at TechVentures Inc.
  - Managed full-cycle HR operations for 150-person startup
  - Led benefits administration and employee relations

- **June 2009 - February 2013:** HR Coordinator at Enterprise Corp.
  - Supported recruiting and onboarding processes
  - Assisted with HR compliance and policy implementation

## Annual Performance History
- **2023:** Rating: 4.5/5
  *Strong performance. Successfully led diversity hiring initiative resulting in 40% increase in underrepresented candidates. Effective partner to leadership.*

- **2022:** Rating: 4.3/5
  *Exceeded expectations. Implemented new performance review system well-received by employees. Strong employee relations skills.*

- **2021:** Rating: 4.0/5
  *Good performance. Managed challenging employee situations effectively. Supported smooth remote-to-hybrid transition.*

- **2020:** Rating: 3.7/5
  *Solid performance during unprecedented pandemic challenges. Helped navigate layoffs and policy changes with empathy.*

- **2019:** Rating: 4.2/5
  *Strong year. Improved hiring velocity for engineering roles by 35%. Built strong relationships with department heads.*

- **2018:** Rating: 4.1/5
  *Good performance. Successfully scaled HR support as company grew rapidly.*

- **2017:** Rating: 3.9/5
  *Solid first full year. Learning Insurellm culture and building credibility with leadership.*

- **2016:** Rating: 3.8/5
  *Good onboarding. Quick to understand business needs and HR priorities.*

## Compensation History
- **2023:** Base Salary: $115,000 + Bonus: $12,000
- **2022:** Base Salary: $110,000 + Bonus: $10,000
- **2021:** Base Salary: $105,000 + Bonus: $8,000
- **2020:** Base Salary: $100,000 + Bonus: $5,000
- **2019:** Base Salary: $96,000 + Bonus: $8,000
- **2018:** Base Salary: $92,000 + Bonus: $7,000
- **2017:** Base Salary: $88,000 + Bonus: $6,000
- **2016:** Base Salary: $85,000

## Other HR Notes
- **Education:** MS in Human Resources Management from Cornell University, BA in Psychology from UCLA
- **Certifications:** SHRM-SCP, Certified Diversity Professional
- **Recognition:** HR Excellence Award 2023 for diversity initiatives
- **Leadership:** Chairs Insurellm's Diversity & Inclusion committee
- **Skills:** Expert in talent acquisition, performance management, employee relations, and organizational development. Strong coach and advisor to leadership.
- **Feedback:** Trusted HR partner with excellent judgment and discretion. Strategic thinker who balances employee advocacy with business needs. Strong emotional intelligence.


---

<a id="file-week5-knowledge-base-employees-avery-lancaster-md"></a>
## File: `week5/knowledge-base/employees/Avery Lancaster.md`

> **Path in repository:** `week5/knowledge-base/employees/Avery Lancaster.md`

# Avery Lancaster

## Summary
- **Date of Birth**: March 15, 1985
- **Job Title**: Co-Founder & Chief Executive Officer (CEO)
- **Location**: San Francisco, California
- **Current Salary**: $225,000  

## Insurellm Career Progression
- **2015 - Present**: Co-Founder & CEO  
  Avery Lancaster co-founded Insurellm in 2015 and has since guided the company to its current position as a leading Insurance Tech provider. Avery is known for her innovative leadership strategies and risk management expertise that have catapulted the company into the mainstream insurance market.  

- **2013 - 2015**: Senior Product Manager at Innovate Insurance Solutions  
  Before launching Insurellm, Avery was a leading Senior Product Manager at Innovate Insurance Solutions, where she developed groundbreaking insurance products aimed at the tech sector.  

- **2010 - 2013**: Business Analyst at Edge Analytics  
  Prior to joining Innovate, Avery worked as a Business Analyst, focusing on market trends and consumer preferences in the insurance space. This position laid the groundwork for Avery’s future entrepreneurial endeavors.

## Annual Performance History
- **2015**: **Exceeds Expectations**  
  Avery’s leadership during Insurellm's foundational year led to successful product launches and securing initial funding.  

- **2016**: **Meets Expectations**  
  Growth continued, though challenges arose in operational efficiency that required Avery's attention.  

- **2017**: **Developing**  
  Market competition intensified, and monthly sales metrics were below targets. Avery implemented new strategies which required a steep learning curve.  

- **2018**: **Exceeds Expectations**  
  Under Avery’s pivoted vision, Insurellm launched two new successful products that significantly increased market share.  

- **2019**: **Meets Expectations**  
  Steady growth, however, some team tensions led to a minor drop in employee morale. Avery recognized the need to enhance company culture.  

- **2020**: **Below Expectations**  
  The COVID-19 pandemic posed unforeseen operational difficulties. Avery faced criticism for delayed strategy shifts, although efforts were eventually made to stabilize the company.  

- **2021**: **Exceptional**  
  Avery's decisive transition to remote work and rapid adoption of digital tools led to record-high customer satisfaction levels and increased sales.  

- **2022**: **Satisfactory**  
  Avery focused on rebuilding team dynamics and addressing employee concerns, leading to overall improvement despite a saturated market.  

- **2023**: **Exceeds Expectations**  
  Market leadership was regained with innovative approaches to personalized insurance solutions. Avery is now recognized in industry publications as a leading voice in Insurance Tech innovation.

## Compensation History
- **2015**: $150,000 base salary + Significant equity stake  
- **2016**: $160,000 base salary + Equity increase  
- **2017**: $150,000 base salary + Decrease in bonus due to performance  
- **2018**: $180,000 base salary + performance bonus of $30,000  
- **2019**: $185,000 base salary + market adjustment + $5,000 bonus  
- **2020**: $170,000 base salary (temporary reduction due to COVID-19)  
- **2021**: $200,000 base salary + performance bonus of $50,000  
- **2022**: $210,000 base salary + retention bonus  
- **2023**: $225,000 base salary + $75,000 performance bonus  

## Other HR Notes
- **Professional Development**: Avery has actively participated in leadership training programs and industry conferences, representing Insurellm and fostering partnerships.  
- **Diversity & Inclusion Initiatives**: Avery has championed a commitment to diversity in hiring practices, seeing visible improvements in team representation since 2021.  
- **Work-Life Balance**: Feedback revealed concerns regarding work-life balance, which Avery has approached by implementing flexible working conditions and ensuring regular check-ins with the team.
- **Community Engagement**: Avery led community outreach efforts, focusing on financial literacy programs, particularly aimed at underserved populations, improving Insurellm's corporate social responsibility image.  

Avery Lancaster has demonstrated resilience and adaptability throughout her career at Insurellm, positioning the company as a key player in the insurance technology landscape.


---

<a id="file-week5-knowledge-base-employees-brandon-walker-md"></a>
## File: `week5/knowledge-base/employees/Brandon Walker.md`

> **Path in repository:** `week5/knowledge-base/employees/Brandon Walker.md`

# HR Record

# Brandon Walker

## Summary
- **Date of Birth:** December 5, 1993
- **Job Title:** Technical Support Specialist
- **Location:** Remote (Based in Phoenix, Arizona)
- **Current Salary:** $62,000

## Insurellm Career Progression
- **October 2021 - Present:** Technical Support Specialist
  - Provides tier 2/3 technical support for all Insurellm products
  - Troubleshoots complex technical issues for enterprise clients
  - Creates knowledge base articles and internal documentation
  - Maintains 4.8/5 customer satisfaction rating

- **May 2019 - September 2021:** Support Specialist at TechHelp Inc.
  - Handled tier 1 technical support for SaaS products
  - Resolved customer issues via phone, email, and chat

- **January 2018 - April 2019:** IT Help Desk Technician at Regional Bank
  - Provided internal IT support for bank employees
  - Managed ticket queue and resolved hardware/software issues

## Annual Performance History
- **2023:** Rating: 3.3/5
  *Meets basic expectations. Good technical knowledge but customer satisfaction scores declined slightly. Needs to improve empathy in customer interactions.*

- **2022:** Rating: 2.9/5
  *Below expectations. Struggled with increased ticket volume and complex escalations. Response times often exceeded SLA targets. Enrolled in customer service training.*

- **2021:** Rating: 3.6/5
  *Adequate performance for a new hire. Good technical skills but needs to develop better troubleshooting methodology.*

## Compensation History
- **2023:** Base Salary: $62,000 + Bonus: $1,500
- **2022:** Base Salary: $60,000 + Bonus: $0 (no bonus due to performance)
- **2021:** Base Salary: $58,000 (started mid-year)

## Other HR Notes
- **Education:** Associate Degree in Information Technology from Phoenix Community College
- **Certifications:** CompTIA A+, working toward Network+ certification
- **Performance Improvement Plan:** Currently on 90-day PIP (started August 2023) focusing on response time improvements and customer communication skills
- **Skills:** Strong in system troubleshooting, SQL basics, and API debugging. Needs improvement in soft skills and time management.
- **Development:** Working with manager on structured troubleshooting approach and empathetic customer communication
- **Feedback:** Technically competent but struggles under pressure. Tends to focus on technical details rather than customer experience. Improving but needs consistent focus.


---

<a id="file-week5-knowledge-base-employees-carlos-rodriguez-md"></a>
## File: `week5/knowledge-base/employees/Carlos Rodriguez.md`

> **Path in repository:** `week5/knowledge-base/employees/Carlos Rodriguez.md`

# HR Record

# Carlos Rodriguez

## Summary
- **Date of Birth:** October 12, 1989
- **Job Title:** Solutions Engineer
- **Location:** Remote (Based in Miami, Florida)
- **Current Salary:** $125,000

## Insurellm Career Progression
- **June 2019 - Present:** Solutions Engineer
  - Provides technical expertise during enterprise sales cycles
  - Conducts product demonstrations and proof-of-concept implementations
  - Works closely with sales team to close complex deals
  - Supports post-sale technical implementation and integration

- **March 2017 - May 2019:** Senior Support Engineer at CloudTech Solutions
  - Led technical support team for enterprise SaaS platform
  - Handled escalated technical issues and customer implementations

- **January 2015 - February 2017:** Application Developer at FinTech Systems
  - Developed financial software applications
  - Worked with Java, Python, and SQL technologies

## Annual Performance History
- **2023:** Rating: 4.9/5
  *Outstanding performance. Instrumental in closing $3M in new business. Excellent technical presentations and client relationships.*

- **2022:** Rating: 4.6/5
  *Exceeded expectations. Strong technical demos that significantly influenced win rates. Great collaboration with sales team.*

- **2021:** Rating: 4.4/5
  *Solid performance with good sales support. Needed to improve documentation of technical solutions.*

- **2020:** Rating: 3.9/5
  *Good performance during challenging remote transition. Some gaps in product knowledge addressed through training.*

- **2019:** Rating: 4.1/5
  *Strong start as Solutions Engineer. Quick learner with excellent technical communication skills.*

## Compensation History
- **2023:** Base Salary: $125,000 + Bonus: $22,000
- **2022:** Base Salary: $118,000 + Bonus: $18,000
- **2021:** Base Salary: $110,000 + Bonus: $14,000
- **2020:** Base Salary: $102,000 + Bonus: $10,000
- **2019:** Base Salary: $95,000 + Bonus: $8,000

## Other HR Notes
- **Education:** MS in Computer Science from University of Florida
- **Certifications:** AWS Solutions Architect Professional, Salesforce Certified Technical Architect
- **Languages:** Fluent in English and Spanish, frequently supports Latin American clients
- **Recognition:** Solutions Engineer of the Year 2023
- **Skills:** Expert in API integrations, cloud architecture, and technical sales. Strong presenter with ability to explain complex concepts to non-technical audiences.
- **Feedback:** Top performer who combines deep technical knowledge with excellent sales acumen. Natural leader who mentors junior SEs.


---

<a id="file-week5-knowledge-base-employees-daniel-park-md"></a>
## File: `week5/knowledge-base/employees/Daniel Park.md`

> **Path in repository:** `week5/knowledge-base/employees/Daniel Park.md`

# HR Record

# Daniel Park

## Summary
- **Date of Birth:** October 3, 1991
- **Job Title:** QA Engineer
- **Location:** Austin, Texas
- **Current Salary:** $88,000

## Insurellm Career Progression
- **September 2020 - Present:** QA Engineer
  - Develops and executes test plans for all Insurellm products
  - Builds automated test suites using Selenium and Cypress
  - Manages bug tracking and quality metrics
  - Collaborates with development teams on quality standards

- **May 2018 - August 2020:** QA Analyst at SoftwareTest Inc.
  - Performed manual and automated testing for web applications
  - Created test documentation and test cases

- **July 2016 - April 2018:** Junior QA Tester at AppQuality Corp.
  - Conducted manual testing and regression testing
  - Learned QA fundamentals and testing methodologies

## Annual Performance History
- **2023:** Rating: 4.2/5
  *Strong performance. Expanded test automation coverage to 65%. Found critical bugs preventing major production issues.*

- **2022:** Rating: 3.9/5
  *Good performance. Improved automated testing but missed some edge cases in major release. Learning from experience.*

- **2021:** Rating: 4.0/5
  *Solid year. Successfully implemented new test framework. Good collaboration with engineering teams.*

- **2020:** Rating: 3.7/5
  *Adequate performance in first year. Building knowledge of products and establishing testing processes.*

## Compensation History
- **2023:** Base Salary: $88,000 + Bonus: $7,000
- **2022:** Base Salary: $82,000 + Bonus: $5,000
- **2021:** Base Salary: $76,000 + Bonus: $6,000
- **2020:** Base Salary: $72,000 + Bonus: $3,000

## Other HR Notes
- **Education:** BS in Computer Science from Texas State University
- **Certifications:** ISTQB Certified Tester, Selenium WebDriver Certified
- **Skills:** Expert in test automation (Selenium, Cypress, Jest), API testing, performance testing, CI/CD integration
- **Professional Development:** Completed Advanced Test Automation workshop (2023). Learning performance testing tools.
- **Recognition:** Quality Champion Award 2023 for preventing critical production bug
- **Feedback:** Detail-oriented QA professional with strong technical skills. Proactive in identifying quality risks. Good advocate for quality throughout development process.


---

<a id="file-week5-knowledge-base-employees-david-kim-md"></a>
## File: `week5/knowledge-base/employees/David Kim.md`

> **Path in repository:** `week5/knowledge-base/employees/David Kim.md`

# HR Record

# David Kim

## Summary
- **Date of Birth:** September 22, 1992
- **Job Title:** DevOps Engineer
- **Location:** New York, New York
- **Current Salary:** $118,000

## Insurellm Career Progression
- **August 2021 - Present:** DevOps Engineer
  - Manages AWS infrastructure for all Insurellm products
  - Implemented CI/CD pipelines reducing deployment time by 60%
  - Led migration to Kubernetes, improving system scalability and reliability

- **March 2019 - July 2021:** Junior DevOps Engineer
  - Assisted with infrastructure monitoring and incident response
  - Automated manual deployment processes using Jenkins and Terraform
  - Supported senior engineers in cloud infrastructure management

- **June 2017 - February 2019:** Systems Administrator at CloudFirst Solutions
  - Maintained Linux servers and network infrastructure
  - Provided technical support for cloud-based services

## Annual Performance History
- **2023:** Rating: 4.5/5
  *Strong performance with excellent infrastructure improvements. Successfully led Kubernetes migration with minimal downtime.*

- **2022:** Rating: 3.5/5
  *Adequate performance but struggled with on-call responsibilities. Improved response times after additional training.*

- **2021:** Rating: 4.0/5
  *Solid first year as DevOps Engineer. Quick learner who adapted well to increased responsibilities.*

## Compensation History
- **2023:** Base Salary: $118,000 + Bonus: $12,000
- **2022:** Base Salary: $108,000 + Bonus: $8,000
- **2021:** Base Salary: $100,000 + Bonus: $5,000
- **2020:** Base Salary: $85,000 + Bonus: $4,000
- **2019:** Base Salary: $75,000

## Other HR Notes
- **Certifications:** AWS Certified Solutions Architect (2022), Certified Kubernetes Administrator (2023)
- **Training:** Completed advanced Docker and container orchestration courses. Currently pursuing AWS DevOps Professional certification.
- **On-Call Rotation:** Participates in weekly on-call rotation for production systems.
- **Feedback:** Technically strong with excellent problem-solving abilities. Working on improving communication with non-technical stakeholders.


---

<a id="file-week5-knowledge-base-employees-emily-carter-md"></a>
## File: `week5/knowledge-base/employees/Emily Carter.md`

> **Path in repository:** `week5/knowledge-base/employees/Emily Carter.md`

# HR Record

# Emily Carter

## Summary
- **Date of Birth:** August 12, 1990
- **Job Title:** Account Executive
- **Location:** Austin, Texas
- **Current Salary:** $70,000  

## Insurellm Career Progression
- **2021-Present:** Account Executive  
  - Responsibilities include managing a portfolio of B2B clients, conducting sales presentations, and ensuring customer satisfaction.  
  - Achievements: 
    - Exceeded annual sales target by 30% in 2022.
    - Instrumental in acquiring 15 new corporate clients in half a year.
  
- **2019-2021:** Sales Coordinator  
  - Supported the sales team with administrative tasks, lead generation, and customer follow-ups.
  - Achievements:
    - Implemented a new lead tracking system that improved workflow efficiency by 25%.  
    - Received "Employee of the Month" award twice for outstanding contribution to team goals.  

- **2017-2019:** Marketing Intern  
  - Assisted with market research and campaign development for social media outreach.  
  - Achievements:  
    - Contributed ideas for a social media campaign that increased brand awareness by 40% within 6 months.  

## Annual Performance History
| Year | Performance Rating | Key Highlights |
|------|--------------------|----------------|
| 2023 | 4.8/5              | Recognized for exceptional client feedback and teamwork during product launches. |
| 2022 | 4.5/5              | Led a successful cross-selling initiative that boosted revenue in existing accounts. |
| 2021 | 4.2/5              | Successfully onboarded new clients and established strong relationships that resulted in renewals. |

## Compensation History
| Year | Base Salary | Bonus         | Total Compensation |
|------|-------------|---------------|--------------------|
| 2023 | $70,000     | $10,000       | $80,000            |
| 2022 | $65,000     | $8,000        | $73,000            |
| 2021 | $60,000     | $5,000        | $65,000            |

## Other HR Notes
- **Professional Development:** Emily is currently enrolled in a leadership training program to enhance her management skills and aims to move into a senior account role within the next 2 years.  
- **Volunteer Work:** Actively participates in community outreach programs, representing Insurellm in charity events to promote corporate social responsibility.  
- **Interests:** In her spare time, Emily enjoys hiking, photography, and volunteering at local animal shelters.  
- **Team Feedback:** Colleagues describe Emily as a highly motivated team player who consistently uplifts everyone around her.  

Emily Carter exemplifies the kind of talent that drives Insurellm's success and is an invaluable asset to the company.


---

<a id="file-week5-knowledge-base-employees-emily-tran-md"></a>
## File: `week5/knowledge-base/employees/Emily Tran.md`

> **Path in repository:** `week5/knowledge-base/employees/Emily Tran.md`

# HR Record

# Emily Tran

## Summary
- **Date of Birth:** March 18, 1991
- **Job Title:** Digital Marketing Specialist
- **Location:** San Francisco, CA
- **Current Salary:** $75,000  

---

## Insurellm Career Progression
- **February 2020 - Present**: Digital Marketing Specialist  
   - Emily Tran has been pivotal in enhancing Insurellm's online presence through targeted social media campaigns and SEO strategies.
   - Successfully managed a team of interns for the 'Spring Into Safety' initiative, increasing customer engagement by 35%.

- **June 2018 - January 2020**: Marketing Coordinator  
  - Assisted in the development and execution of marketing campaigns to promote Insurellm's products.
  - Collected and analyzed data on customer demographics to inform Insurellm’s marketing strategies.

- **January 2017 - May 2018**: Marketing Intern  
  - Supported the Marketing team by collaborating on content creation and digital advertising projects.
  - Gained hands-on experience with marketing automation tools, enriching her skillset for her role in Insurellm.

---

## Annual Performance History
- **2023**:  
  - Performance Rating: Exceeds Expectations  
  - Key Achievements: Led the "Tech the Halls" campaign that resulted in a 50% increase in leads during the holiday season. 
  - Emily Tran's innovative strategies and attention to detail have made her stand out among her peers.

- **2022**:  
  - Performance Rating: Meets Expectations  
  - Key Achievements: Enhanced Insurellm's email marketing strategy, achieving a 25% open rate increase.

- **2021**:  
  - Performance Rating: Meets Expectations  
  - Key Achievements: Contributed to the launch of a customer referral program that resulted in a 15% growth in B2C customers.

---

## Compensation History
- **2023**:  
  - Base Salary: $75,000  
  - Bonus: $10,000 for exceeding annual targets.

- **2022**:  
  - Base Salary: $70,000  
  - Bonus: $5,000 for achieving marketing milestones.

- **2021**:  
  - Base Salary: $67,500  
  - No bonus due to reallocation of marketing funds during the pandemic.

---

## Other HR Notes
- **Training Completed**:  
  - Advanced Digital Marketing Workshop (2021)  
  - Analytics and Reporting in Digital Advertising (2022)

- **Professional Development Goals**:  
  - Emily Tran aims to become a Marketing Manager within the next two years, focusing on leading larger campaigns and developing junior team members.

- **Hobbies**:  
  - Emily enjoys photography and regularly contributes to Insurellm's social media content with her own high-quality images.
  - She is also passionate about sustainability and organizes monthly team volunteer events for environmental awareness. 

---

Emily Tran continues to be a valuable asset to Insurellm, driving innovative marketing strategies that resonate with a diverse customer base. Her contributions have significantly enhanced the company's branding and customer outreach efforts.


---

<a id="file-week5-knowledge-base-employees-james-wilson-md"></a>
## File: `week5/knowledge-base/employees/James Wilson.md`

> **Path in repository:** `week5/knowledge-base/employees/James Wilson.md`

# HR Record

# James Wilson

## Summary
- **Date of Birth:** April 5, 1978
- **Job Title:** Chief Technology Officer (CTO)
- **Location:** San Francisco, California
- **Current Salary:** $285,000

## Insurellm Career Progression
- **January 2017 - Present:** Chief Technology Officer
  - Reports directly to CEO, member of executive leadership team
  - Oversees all technology strategy and engineering operations
  - Manages 85-person engineering, product, and data organization
  - Led company through major platform modernization and cloud migration
  - Drove adoption of AI/ML capabilities across product suite

- **March 2012 - December 2016:** VP of Engineering at TechScale Inc.
  - Built and scaled engineering organization from 15 to 60 engineers
  - Led product development for B2B SaaS platform
  - Drove technical strategy and architecture decisions

- **June 2008 - February 2012:** Senior Engineering Manager at CloudSoft Corp.
  - Managed multiple engineering teams
  - Delivered major platform features and infrastructure improvements

- **August 2003 - May 2008:** Software Architect at Enterprise Systems Inc.
  - Designed large-scale distributed systems
  - Led technical architecture for critical business applications

## Annual Performance History
- **2023:** Rating: 4.9/5
  *Outstanding performance. Successfully led AI transformation initiative. Exceptional strategic leadership and team building. Key driver of company growth.*

- **2022:** Rating: 4.7/5
  *Exceeded expectations. Strong execution on platform modernization. Improved engineering productivity and velocity significantly.*

- **2021:** Rating: 4.6/5
  *Excellent performance navigating remote transition. Built strong engineering culture and maintained high delivery standards.*

- **2020:** Rating: 4.4/5
  *Strong performance during challenging year. Successfully pivoted technology strategy for remote-first world.*

- **2019:** Rating: 4.8/5
  *Exceptional leadership. Scaled engineering organization effectively while maintaining quality and culture.*

- **2018:** Rating: 4.5/5
  *Excellent year with successful cloud migration. Strong technical vision and execution.*

- **2017:** Rating: 4.3/5
  *Strong start as CTO. Quickly assessed technical landscape and began strategic improvements.*

## Compensation History
- **2023:** Base Salary: $285,000 + Bonus: $125,000 + Equity refresh
- **2022:** Base Salary: $270,000 + Bonus: $110,000 + Equity refresh
- **2021:** Base Salary: $255,000 + Bonus: $100,000
- **2020:** Base Salary: $240,000 + Bonus: $85,000
- **2019:** Base Salary: $225,000 + Bonus: $95,000
- **2018:** Base Salary: $210,000 + Bonus: $80,000
- **2017:** Base Salary: $195,000 + Bonus: $70,000 + Significant equity grant

## Other HR Notes
- **Education:** MS in Computer Science from MIT, BS in Computer Engineering from Stanford University
- **Board Participation:** Serves on technical advisory board for two InsurTech startups
- **Industry Recognition:** Named to InsureTech 100 list (2021, 2022, 2023), speaker at major technology conferences
- **Patents:** 5 patents in distributed systems and insurance technology
- **Leadership:** Known for building high-performing teams and fostering innovation culture. Strong mentor to technical leaders.
- **Strategic Impact:** Transformed Insurellm's technology from legacy systems to modern cloud-native architecture. Key architect of AI strategy.
- **Feedback:** Visionary technology leader with exceptional strategic thinking and execution capabilities. Trusted partner to CEO and board. Critical to company's technical success and future growth.


---

<a id="file-week5-knowledge-base-employees-jennifer-adams-md"></a>
## File: `week5/knowledge-base/employees/Jennifer Adams.md`

> **Path in repository:** `week5/knowledge-base/employees/Jennifer Adams.md`

# HR Record

# Jennifer Adams

## Summary
- **Date of Birth:** July 7, 1997
- **Job Title:** Sales Development Representative
- **Location:** Remote (Based in Denver, Colorado)
- **Current Salary:** $58,000

## Insurellm Career Progression
- **March 2023 - Present:** Sales Development Representative
  - Generates qualified leads for enterprise sales team
  - Conducts outbound prospecting via phone, email, and LinkedIn
  - Researches target accounts in insurance industry
  - Books discovery meetings for account executives

- **June 2022 - February 2023:** SDR Intern
  - Completed 9-month internship program
  - Learned sales processes and CRM tools
  - Shadowed senior SDRs and participated in training

- **August 2019 - May 2022:** Customer Service Representative at RetailCo
  - Handled customer inquiries and resolved issues
  - Developed communication and problem-solving skills

## Annual Performance History
- **2023:** Rating: 3.0/5
  *Meets basic expectations. Achieved 78% of lead generation quota. Shows effort but struggles with conversion rates. Needs improvement in discovery call quality.*

## Compensation History
- **2023:** Base Salary: $58,000 + Commission: $4,200
- **2022:** Intern Stipend: $22/hour

## Other HR Notes
- **Education:** BA in Business Administration from University of Denver (graduated 2022)
- **Skills:** Learning Salesforce, LinkedIn Sales Navigator, and sales prospecting techniques
- **Development Plan:** Enrolled in sales skills training program. Manager providing weekly coaching on objection handling and qualification techniques.
- **Challenges:** Struggles with phone confidence and needs to improve research quality before outreach. Working on building pipeline consistency.
- **Feedback:** Enthusiastic and coachable. Shows potential but needs more experience and skill development. Sometimes gives up too easily when facing rejection. Improving gradually with support.
- **Goals:** Aiming to hit 100% of quota in Q4 2024 and qualify for SDR of the Quarter recognition


---

<a id="file-week5-knowledge-base-employees-jessica-liu-md"></a>
## File: `week5/knowledge-base/employees/Jessica Liu.md`

> **Path in repository:** `week5/knowledge-base/employees/Jessica Liu.md`

# HR Record

# Jessica Liu

## Summary
- **Date of Birth:** April 30, 1996
- **Job Title:** Frontend Developer
- **Location:** Remote (Based in Seattle, Washington)
- **Current Salary:** $92,000

## Insurellm Career Progression
- **July 2022 - Present:** Frontend Developer
  - Develops user interfaces for Rellm reinsurance platform using React
  - Implements responsive designs and ensures cross-browser compatibility
  - Collaborates with UX designers and backend engineers

- **January 2020 - June 2022:** Junior Frontend Developer
  - Built UI components for internal tools and customer-facing applications
  - Fixed bugs and improved performance of existing web applications
  - Participated in code reviews and learned best practices

- **June 2018 - December 2019:** Web Developer Intern at StartupLabs
  - Created landing pages and marketing websites
  - Learned HTML, CSS, JavaScript, and React fundamentals

## Annual Performance History
- **2023:** Rating: 4.1/5
  *Good performance with steady contribution to team goals. Delivered features on time with good code quality.*

- **2022:** Rating: 3.7/5
  *Solid transition to Frontend Developer role. Showed improvement in technical skills but needed more guidance on complex features.*

- **2021:** Rating: 3.4/5
  *Adequate performance with some challenges. Struggled with React state management initially but improved after mentoring.*

- **2020:** Rating: 3.8/5
  *Good start as Junior Developer. Eager to learn and receptive to feedback.*

## Compensation History
- **2023:** Base Salary: $92,000 + Bonus: $6,000
- **2022:** Base Salary: $85,000 + Bonus: $4,000
- **2021:** Base Salary: $72,000 + Bonus: $2,000
- **2020:** Base Salary: $68,000

## Other HR Notes
- **Education:** BS in Computer Science from University of Manchester
- **Skills:** Proficient in React, TypeScript, HTML/CSS, Jest for testing. Learning Next.js and GraphQL.
- **Professional Development:** Completed Advanced React Patterns course (2023). Actively contributes to open-source projects.
- **Work Style:** Prefers remote work. Strong written communicator. Participates actively in team standups and planning sessions.
- **Feedback:** Reliable developer with good attention to UI details. Improving technical decision-making skills. Would benefit from more ownership of larger features.


---

<a id="file-week5-knowledge-base-employees-jordan-blake-md"></a>
## File: `week5/knowledge-base/employees/Jordan Blake.md`

> **Path in repository:** `week5/knowledge-base/employees/Jordan Blake.md`

# HR Record

# Jordan Blake

## Summary
- **Date of Birth:** March 15, 1993
- **Job Title:** Sales Development Representative (SDR)
- **Location:** Austin, Texas
- **Current Salary:** $65,000  

## Insurellm Career Progression
- **2021-06:** Joined Insurellm as an Entry-Level SDR  
- **2022-02:** Promoted to Junior SDR after exceeding quarterly targets by 25%  
- **2022-12:** Recognized as SDR of the Month for three consecutive months  
- **2023-05:** Participated in the Insurellm Leadership Training Program  

## Annual Performance History
- **2021:** First year at Insurellm; achieved 90% of monthly targets.  
  - **Feedback:** Strong potential shown in lead generation; needs improvement in follow-up techniques.  
- **2022:** Achieved 120% of targets; pioneered outreach strategies that increased customer engagement.  
  - **Feedback:** Jordan's innovative approach contributed significantly to team success; recommended for leadership training.  
- **2023:** Set to exceed annual targets by 30% in Q3; initiated successful partnerships that broadened market reach.  
  - **Feedback:** Exceptional communicator; exemplifies the values of Insurellm and promotes team collaboration.

## Compensation History
- **2021-06:** Starting Salary: $50,000  
- **2022-04:** Merit-based increase: $55,000 (based on performance review)  
- **2023-06:** Performance bonus awarded: $5,000 (for exceeding goals as recognized in annual review)  
- **2023-09:** Salary adjustment due to promotion to Senior SDR: $65,000  

## Other HR Notes
- Jordan has shown an interest in continuing education, actively participating in company-sponsored sales webinars.  
- Notable for involvement in the Insurellm volunteer program, assisting local charity events related to financial literacy.  
- Employee wellness advocate, consistently promotes team bonding activities and stress-relief workshops.  
- Plans to enroll in a course for advanced sales strategies in Q4 2023, aiming to further enhance his skills at Insurellm.


---

<a id="file-week5-knowledge-base-employees-jordan-k--bishop-md"></a>
## File: `week5/knowledge-base/employees/Jordan K. Bishop.md`

> **Path in repository:** `week5/knowledge-base/employees/Jordan K. Bishop.md`

# HR Record

# Jordan K. Bishop

## Summary
- **Date of Birth:** March 15, 1990
- **Job Title:** Frontend Software Engineer
- **Location:** Austin, Texas
- **Current Salary:** $92,000

## Insurellm Career Progression
- **June 2018:** Hired as a Frontend Software Engineer.
- **August 2019:** Promoted to Senior Frontend Software Engineer due to outstanding contributions to the Insurellm web application redesign project.
- **March 2021:** Led a cross-functional team for the launch of Insurellm's customer portal, enhancing user experience and engagement.
- **January 2022:** Transitioned to a mentorship role, where Jordan K. Bishop began training junior engineers, which affected the focus on personal projects.
- **August 2023:** Returned to core development tasks but faced challenges adapting to new frameworks, leading to performance reviews reflecting a need for improvement.

## Annual Performance History
- **2019:** Exceeds Expectations - Continuously delivered high-quality code and participated actively in team meetings.
- **2020:** Meets Expectations - Jordan K. Bishop maintained steady performance but faced challenges due to a higher workload from multiple projects.
- **2021:** Exceeds Expectations - Recognized for leadership during the customer portal project; received the “Innovation Award” for creative problem-solving.
- **2022:** Meets Expectations - While mentoring others, the shift in focus led to fewer contributions to new features, marking a decrease in performance.
- **2023:** Needs Improvement - Transitioning back to development has resulted in difficulties with recent technologies, prompting a performance improvement plan.

## Compensation History
- **June 2018:** Starting Salary - $85,000
- **June 2019:** Salary Increase - $95,000 (Promotion to Senior Engineer)
- **June 2021:** Salary Increase - $105,000 with bonus for project leadership.
- **June 2022:** Salary Freeze due to company budget adjustments.
- **June 2023:** Salary Adjustment - $92,000 after performance review; adjustments made in consideration of recent struggles with adaptation.

## Other HR Notes
- Jordan K. Bishop has been an integral part of club initiatives, including the Insurellm Code Reviews and Feedback Group, providing peer support.
- Active participant in the company's Diversity and Inclusion committee, promoting a positive work culture.
- Jordan has expressed interest in professional development courses, particularly those focused on modern web technologies, which are being considered for sponsorship by Insurellm.
- Engaged in a 6-month performance improvement plan as of August 2023, focusing on skill development and consistent performance monitoring. 

Jordan K. Bishop is a valued member of the Insurellm family, exhibiting a commitment to growth and development despite recent challenges.


---

<a id="file-week5-knowledge-base-employees-kevin-zhang-md"></a>
## File: `week5/knowledge-base/employees/Kevin Zhang.md`

> **Path in repository:** `week5/knowledge-base/employees/Kevin Zhang.md`

# HR Record

# Kevin Zhang

## Summary
- **Date of Birth:** March 27, 1990
- **Job Title:** Mobile Developer
- **Location:** San Francisco, California
- **Current Salary:** $128,000

## Insurellm Career Progression
- **May 2020 - Present:** Mobile Developer
  - Leads iOS development for Marketllm consumer mobile app
  - Built Android version achieving 4.6 star rating on Play Store
  - Implemented push notification system increasing user engagement by 42%
  - Manages mobile release cycles and app store submissions

- **February 2018 - April 2020:** iOS Developer at AppWorks Studio
  - Developed consumer mobile applications for various clients
  - Specialized in Swift and iOS frameworks

- **July 2015 - January 2018:** Junior Mobile Developer at StartupTech
  - Built mobile features for social networking app
  - Learned iOS and Android development fundamentals

## Annual Performance History
- **2023:** Rating: 4.6/5
  *Excellent performance. Successfully launched Android app on time and under budget. Strong technical leadership.*

- **2022:** Rating: 4.4/5
  *Exceeded expectations with major iOS app redesign. Improved app performance and user retention significantly.*

- **2021:** Rating: 4.2/5
  *Strong performance. Delivered all planned features and maintained high app quality standards.*

- **2020:** Rating: 4.0/5
  *Good first year at Insurellm. Quick to learn insurance domain and contribute meaningfully to mobile strategy.*

## Compensation History
- **2023:** Base Salary: $128,000 + Bonus: $16,000
- **2022:** Base Salary: $120,000 + Bonus: $14,000
- **2021:** Base Salary: $112,000 + Bonus: $12,000
- **2020:** Base Salary: $105,000 + Bonus: $8,000

## Other HR Notes
- **Education:** BS in Computer Science from UC Berkeley
- **Skills:** Expert in Swift, Kotlin, React Native, mobile UI/UX patterns, App Store optimization
- **Recognition:** Mobile Innovation Award 2023 for Android app launch
- **Open Source:** Active contributor to mobile development open-source projects
- **Speaking:** Presented at Mobile DevCon 2023 on cross-platform development strategies
- **Feedback:** Highly skilled mobile developer with excellent product sense. Takes ownership of mobile platform and drives continuous improvement. Strong mentor to other developers.


---

<a id="file-week5-knowledge-base-employees-lisa-anderson-md"></a>
## File: `week5/knowledge-base/employees/Lisa Anderson.md`

> **Path in repository:** `week5/knowledge-base/employees/Lisa Anderson.md`

# HR Record

# Lisa Anderson

## Summary
- **Date of Birth:** November 18, 1985
- **Job Title:** Marketing Manager
- **Location:** Austin, Texas
- **Current Salary:** $105,000

## Insurellm Career Progression
- **April 2019 - Present:** Marketing Manager
  - Leads demand generation and content marketing teams
  - Manages $2M annual marketing budget
  - Oversees digital campaigns, events, and brand initiatives
  - Increased qualified leads by 65% since 2021

- **January 2016 - March 2019:** Senior Marketing Specialist at GrowthTech
  - Managed B2B marketing campaigns for SaaS products
  - Specialized in content marketing and marketing automation

- **June 2012 - December 2015:** Marketing Coordinator at Enterprise Solutions
  - Supported marketing team with campaign execution
  - Managed social media and email marketing programs

## Annual Performance History
- **2023:** Rating: 4.7/5
  *Outstanding performance. Led successful rebranding initiative and achieved record lead generation numbers. Excellent team leadership.*

- **2022:** Rating: 4.4/5
  *Exceeded expectations. Strong campaign performance and improved marketing ROI by 38%.*

- **2021:** Rating: 4.1/5
  *Solid performance with good lead quality improvements. Successfully navigated shift to digital events.*

- **2020:** Rating: 3.8/5
  *Good performance during challenging pandemic year. Adapted marketing strategy effectively to all-digital approach.*

- **2019:** Rating: 4.0/5
  *Strong start as Marketing Manager. Quick to understand insurance tech market and develop effective strategies.*

## Compensation History
- **2023:** Base Salary: $105,000 + Bonus: $18,000
- **2022:** Base Salary: $98,000 + Bonus: $15,000
- **2021:** Base Salary: $92,000 + Bonus: $12,000
- **2020:** Base Salary: $88,000 + Bonus: $8,000
- **2019:** Base Salary: $85,000 + Bonus: $10,000

## Other HR Notes
- **Education:** MBA in Marketing from University of Texas at Austin, BA in Communications
- **Certifications:** Google Analytics Certified, HubSpot Marketing Automation Expert
- **Recognition:** Marketing Excellence Award 2023, led award-winning rebranding campaign
- **Team Leadership:** Manages team of 5 marketing specialists. Known for developing talent and creating high-performing culture.
- **Skills:** Expert in demand generation, content marketing, marketing analytics, marketing automation (HubSpot, Marketo), and brand strategy
- **Feedback:** Strategic marketing leader with strong analytical skills and creative vision. Excellent cross-functional collaborator who drives measurable business results.


---

<a id="file-week5-knowledge-base-employees-marcus-johnson-md"></a>
## File: `week5/knowledge-base/employees/Marcus Johnson.md`

> **Path in repository:** `week5/knowledge-base/employees/Marcus Johnson.md`

# HR Record

# Marcus Johnson

## Summary
- **Date of Birth:** February 17, 1988
- **Job Title:** Customer Success Manager
- **Location:** New York, New York
- **Current Salary:** $98,000

## Insurellm Career Progression
- **April 2020 - Present:** Customer Success Manager
  - Manages portfolio of 25 enterprise clients generating $5M in annual revenue
  - Achieved 95% client retention rate over past three years
  - Leads quarterly business reviews and strategic planning sessions with clients

- **September 2018 - March 2020:** Customer Success Associate
  - Supported senior CSMs with client onboarding and training
  - Managed day-to-day communication with mid-market clients
  - Created customer success playbooks and best practices documentation

- **January 2016 - August 2018:** Account Manager at SaaS Solutions Inc.
  - Managed B2B client relationships in software sector
  - Focused on upselling and customer retention

## Annual Performance History
- **2023:** Rating: 4.7/5
  *Exceptional performance with highest client satisfaction scores in the team. Successfully expanded three key accounts.*

- **2022:** Rating: 4.3/5
  *Strong performance with good retention numbers. Faced challenges with one difficult client but resolved successfully.*

- **2021:** Rating: 3.8/5
  *Solid year but missed expansion revenue targets in Q2 and Q3. Improved significantly in Q4.*

- **2020:** Rating: 4.0/5
  *Good transition to CSM role. Quickly built rapport with enterprise clients and demonstrated strategic thinking.*

## Compensation History
- **2023:** Base Salary: $98,000 + Bonus: $15,000
- **2022:** Base Salary: $92,000 + Bonus: $12,000
- **2021:** Base Salary: $85,000 + Bonus: $8,000
- **2020:** Base Salary: $78,000 + Bonus: $10,000
- **2019:** Base Salary: $68,000 + Bonus: $5,000
- **2018:** Base Salary: $65,000

## Other HR Notes
- **Education:** BA in Business Administration from NYU Stern School of Business
- **Certifications:** Certified Customer Success Manager (CCSM), Salesforce Administrator
- **Recognition:** Customer Champion Award 2023 for highest NPS scores
- **Mentorship:** Actively mentors new Customer Success Associates
- **Feedback:** Excellent relationship builder with deep product knowledge. Strong strategic advisor to clients. Known for going above and beyond to ensure client success.


---

<a id="file-week5-knowledge-base-employees-maxine-thompson-md"></a>
## File: `week5/knowledge-base/employees/Maxine Thompson.md`

> **Path in repository:** `week5/knowledge-base/employees/Maxine Thompson.md`

# HR Record

# Maxine Thompson

## Summary
- **Date of Birth:** January 15, 1991
- **Job Title:** Data Engineer
- **Location:** Austin, Texas
- **Current Salary:** $120,000  

## Insurellm Career Progression
- **January 2017 - October 2018**: **Junior Data Engineer**  
  * Maxine joined Insurellm as a Junior Data Engineer, focusing primarily on ETL processes and data integration tasks. She quickly learned Insurellm's data architecture, collaborating with other team members to streamline data workflows.  
- **November 2018 - December 2020**: **Data Engineer**  
  * In her new role, Maxine expanded her responsibilities to include designing comprehensive data models and improving data quality measures. Though she excelled in technical skills, communication issues with non-technical teams led to some project delays.  
- **January 2021 - Present**: **Senior Data Engineer**  
  * Maxine was promoted to Senior Data Engineer after successfully leading a pivotal project that improved data retrieval times by 30%. She now mentors junior engineers and is involved in strategic data initiatives, solidifying her position as a valued asset at Insurellm. She was recognized as Insurellm Innovator of the year in 2023, receiving the prestigious IIOTY 2023 award.  

## Annual Performance History
- **2017**: *Meets Expectations*  
  Maxine showed potential in her role but struggled with initial project deadlines. Her adaptability and willingness to learn made positive impacts on her team.  

- **2018**: *Exceeds Expectations*  
  Maxine improved significantly, becoming a reliable team member with strong problem-solving skills. She took on leadership in a project that automated data entry processes.  

- **2019**: *Needs Improvement*  
  During this year, difficult personal circumstances affected Maxine's performance. She missed key deadlines and had several communication issues with stakeholders.  

- **2020**: *Meets Expectations*  
  Maxine focused on regaining her footing and excelling with technical skills. She was stable, though not standout, in her contributions. Feedback indicated a need for more proactivity.  

- **2021**: *Exceeds Expectations*  
  Maxine spearheaded the transition to a new data warehousing solution, significantly enhancing Insurellm’s data analytics capabilities. This major achievement bolstered her reputation within the company.  

- **2022**: *Outstanding*  
  Maxine continued her upward trajectory, successfully implementing machine learning algorithms to predict customer behavior, which was well-received by the leadership team and improved client satisfaction.  

- **2023**: *Exceeds Expectations*  
  Maxine has taken on mentoring responsibilities and is leading a cross-functional team for data governance initiatives, showcasing her leadership and solidifying her role at Insurellm.  

## Compensation History
- **2017**: $70,000 (Junior Data Engineer)  
- **2018**: $75,000 (Junior Data Engineer)  
- **2019**: $80,000 (Data Engineer)  
- **2020**: $84,000 (Data Engineer)  
- **2021**: $95,000 (Senior Data Engineer)  
- **2022**: $110,000 (Senior Data Engineer)  
- **2023**: $120,000 (Senior Data Engineer)  

## Other HR Notes
- Maxine participated in various company-sponsored trainings related to big data technologies and cloud infrastructure.  
- She was recognized for her contributions with the prestigious Insurellm IIOTY Innovator Award in 2023.  
- Maxine is currently involved in the women-in-tech initiative and participates in mentorship programs to guide junior employees.  
- Future development areas include improving her stakeholder communication skills to ensure smoother project transitions and collaboration.


---

<a id="file-week5-knowledge-base-employees-maya-thompson-md"></a>
## File: `week5/knowledge-base/employees/Maya Thompson.md`

> **Path in repository:** `week5/knowledge-base/employees/Maya Thompson.md`

# HR Record

# Maya Thompson

## Summary
- **Date of Birth:** June 14, 1993
- **Job Title:** Data Engineer
- **Location:** New York, New York
- **Current Salary:** $110,000

## Insurellm Career Progression
- **March 2021 - Present:** Data Engineer
  - Builds and maintains data pipelines for all Insurellm products
  - Manages data warehouse infrastructure on Snowflake
  - Optimized ETL processes reducing processing time by 45%
  - Collaborates with data science and analytics teams

- **July 2019 - February 2021:** Junior Data Engineer at DataFlow Systems
  - Developed ETL pipelines for enterprise data integration
  - Worked with Airflow, Python, and SQL

- **June 2017 - June 2019:** Data Analyst at Analytics Corp.
  - Analyzed business data and created reports
  - Transitioned from analysis to engineering role

## Annual Performance History
- **2023:** Rating: 4.3/5
  *Strong performance. Delivered critical data infrastructure improvements. Good collaboration with stakeholders.*

- **2022:** Rating: 4.5/5
  *Excellent performance. Led successful migration to Snowflake. Strong technical expertise and project management.*

- **2021:** Rating: 4.0/5
  *Good first year at Insurellm. Quickly ramped up on data infrastructure and delivered reliable pipelines.*

## Compensation History
- **2023:** Base Salary: $110,000 + Bonus: $12,000
- **2022:** Base Salary: $102,000 + Bonus: $14,000
- **2021:** Base Salary: $95,000 + Bonus: $8,000

## Other HR Notes
- **Education:** MS in Data Science from Columbia University, BS in Mathematics from University of Michigan
- **Skills:** Expert in Python, SQL, Airflow, dbt, Snowflake, AWS data services
- **Certifications:** AWS Certified Data Analytics, Snowflake SnowPro Core
- **Professional Development:** Regularly attends data engineering conferences and contributes to tech blog
- **Feedback:** Strong technical contributor with excellent data architecture skills. Reliable and detail-oriented. Good communicator who translates technical concepts for non-technical stakeholders.


---

<a id="file-week5-knowledge-base-employees-michael-o'brien-md"></a>
## File: `week5/knowledge-base/employees/Michael O'Brien.md`

> **Path in repository:** `week5/knowledge-base/employees/Michael O'Brien.md`

# HR Record

# Michael O'Brien

## Summary
- **Date of Birth:** May 20, 1984
- **Job Title:** Account Executive
- **Location:** Chicago, Illinois
- **Current Salary:** $95,000

## Insurellm Career Progression
- **January 2017 - Present:** Account Executive
  - Manages enterprise sales for Midwest territory
  - Focuses on reinsurance and large insurance carrier accounts
  - Generated $8.2M in new business over past 3 years
  - Maintains book of business worth $12M ARR

- **June 2014 - December 2016:** Senior Sales Representative at InsureTech Partners
  - Sold insurance software solutions to mid-market companies
  - Consistently exceeded quota by 30-50%

- **August 2010 - May 2014:** Sales Representative at Business Solutions Inc.
  - B2B software sales for various industries
  - Developed foundational sales skills and territory management

## Annual Performance History
- **2023:** Rating: 3.4/5
  *Meets expectations but below peak performance. Hit 92% of quota. Faced headwinds in reinsurance market. Need to diversify pipeline.*

- **2022:** Rating: 3.8/5
  *Good performance with solid quota attainment at 105%. Some key deals slipped to next quarter affecting timing.*

- **2021:** Rating: 4.5/5
  *Excellent year. Exceeded quota at 142%. Closed two major enterprise deals. Strong relationship building.*

- **2020:** Rating: 3.6/5
  *Challenging year with pandemic impact. Hit 88% of quota but showed resilience and adapted to virtual selling.*

- **2019:** Rating: 4.2/5
  *Strong performance at 125% quota attainment. Expanded territory successfully.*

- **2018:** Rating: 4.0/5
  *Solid year with 110% quota achievement. Building strong pipeline in new territory.*

- **2017:** Rating: 3.5/5
  *Good onboarding year. Learning curve with insurance industry specifics but showed promise.*

## Compensation History
- **2023:** Base Salary: $95,000 + Commission: $48,000
- **2022:** Base Salary: $92,000 + Commission: $62,000
- **2021:** Base Salary: $88,000 + Commission: $88,000
- **2020:** Base Salary: $85,000 + Commission: $42,000
- **2019:** Base Salary: $82,000 + Commission: $68,000
- **2018:** Base Salary: $78,000 + Commission: $58,000
- **2017:** Base Salary: $75,000 + Commission: $35,000

## Other HR Notes
- **Education:** BA in Business from University of Illinois
- **Awards:** Sales Excellence Award 2021, President's Club member 2019, 2021
- **Pipeline Management:** Currently working to rebuild pipeline after softer 2023. Manager providing additional support and marketing resources.
- **Skills:** Strong at enterprise relationship building and complex deal negotiation. Experienced with long sales cycles.
- **Development Focus:** Working on account-based selling strategies and leveraging social selling techniques
- **Feedback:** Seasoned sales professional with deep industry knowledge. Performs best with large strategic deals. Needs to maintain consistent prospecting discipline.


---

<a id="file-week5-knowledge-base-employees-michelle-rivera-md"></a>
## File: `week5/knowledge-base/employees/Michelle Rivera.md`

> **Path in repository:** `week5/knowledge-base/employees/Michelle Rivera.md`

# HR Record

# Michelle Rivera

## Summary
- **Date of Birth:** December 16, 1988
- **Job Title:** Product Designer
- **Location:** New York, New York
- **Current Salary:** $118,000

## Insurellm Career Progression
- **February 2019 - Present:** Product Designer
  - Leads design for Rellm reinsurance platform
  - Creates user experiences for complex B2B workflows
  - Collaborates with product managers and engineers
  - Conducts user research with enterprise clients

- **August 2016 - January 2019:** Senior UX/UI Designer at DesignStudio NYC
  - Designed digital products for various clients
  - Specialized in enterprise software and complex workflows

- **May 2013 - July 2016:** UX Designer at CreativeAgency
  - Created user interfaces for consumer and business applications
  - Developed skills in user research and interaction design

## Annual Performance History
- **2023:** Rating: 4.8/5
  *Outstanding performance. Led major Rellm redesign that improved user efficiency by 40%. Exceptional user research and design execution.*

- **2022:** Rating: 4.5/5
  *Exceeded expectations. Strong design leadership and excellent collaboration with engineering team.*

- **2021:** Rating: 4.3/5
  *Strong performance. Successfully balanced multiple design projects and maintained high quality standards.*

- **2020:** Rating: 4.1/5
  *Good performance adapting to remote design collaboration. Maintained design quality during challenging year.*

- **2019:** Rating: 4.0/5
  *Solid first year at Insurellm. Quick to learn complex insurance domain and establish design process.*

## Compensation History
- **2023:** Base Salary: $118,000 + Bonus: $16,000
- **2022:** Base Salary: $112,000 + Bonus: $14,000
- **2021:** Base Salary: $105,000 + Bonus: $12,000
- **2020:** Base Salary: $98,000 + Bonus: $10,000
- **2019:** Base Salary: $92,000 + Bonus: $8,000

## Other HR Notes
- **Education:** MFA in Interaction Design from School of Visual Arts, BFA in Graphic Design from Parsons
- **Skills:** Expert in Figma, Sketch, prototyping, user research methodologies, information architecture, design systems
- **Recognition:** Design Excellence Award 2023, featured in UX Design Magazine for Rellm case study
- **Speaking:** Presented at UX Week 2023 on "Designing for Complex Enterprise Workflows"
- **Mentorship:** Mentors junior designers and leads design critique sessions
- **Feedback:** Exceptional designer with rare ability to simplify complex problems. Strong strategic thinker who balances user needs with business goals. Trusted design leader.


---

<a id="file-week5-knowledge-base-employees-nina-patel-md"></a>
## File: `week5/knowledge-base/employees/Nina Patel.md`

> **Path in repository:** `week5/knowledge-base/employees/Nina Patel.md`

# HR Record

# Nina Patel

## Summary
- **Date of Birth:** July 25, 1991
- **Job Title:** Business Intelligence Analyst
- **Location:** Chicago, Illinois
- **Current Salary:** $82,000

## Insurellm Career Progression
- **February 2021 - Present:** Business Intelligence Analyst
  - Builds dashboards and reports using Tableau and Looker for executive team
  - Analyzes business metrics across all product lines
  - Partners with sales and marketing teams on data-driven insights

- **August 2019 - January 2021:** Junior BI Analyst
  - Created SQL queries and basic reports for business stakeholders
  - Supported senior analysts with data extraction and validation
  - Maintained existing dashboards and fixed data quality issues

- **May 2017 - July 2019:** Data Analyst at RetailMetrics Inc.
  - Analyzed retail sales data and customer behavior patterns
  - Built Excel-based reporting tools for operations team

## Annual Performance History
- **2023:** Rating: 3.5/5
  *Meets expectations but has room for growth. Delivered all required reports but showed limited proactivity in identifying new insights.*

- **2022:** Rating: 3.2/5
  *Below expectations. Struggled with complex SQL queries and missed several deadlines. Enrolled in advanced analytics training.*

- **2021:** Rating: 3.8/5
  *Solid performance in first year as BI Analyst. Demonstrated good grasp of business metrics and stakeholder communication.*

- **2020:** Rating: 4.0/5
  *Strong performance as Junior Analyst. Showed initiative and eagerness to learn new tools.*

- **2019:** Rating: 3.9/5
  *Good onboarding year. Quick to adapt to Insurellm's data systems.*

## Compensation History
- **2023:** Base Salary: $82,000 + Bonus: $4,000
- **2022:** Base Salary: $78,000 + Bonus: $2,000
- **2021:** Base Salary: $75,000 + Bonus: $5,000
- **2020:** Base Salary: $65,000 + Bonus: $3,000
- **2019:** Base Salary: $60,000

## Other HR Notes
- **Education:** BS in Statistics from University of Illinois at Chicago
- **Skills:** Proficient in SQL, Tableau, Looker, Excel. Learning Python for advanced analytics.
- **Development Areas:** Needs to improve proactive problem-solving and complex analytical thinking. Working with mentor to develop these skills.
- **Training:** Completed Advanced SQL course (2022), enrolled in Data Science fundamentals program (2023)
- **Feedback:** Reliable team member with strong attention to detail. Works well on defined projects but needs guidance on ambiguous problems.


---

<a id="file-week5-knowledge-base-employees-oliver-spencer-md"></a>
## File: `week5/knowledge-base/employees/Oliver Spencer.md`

> **Path in repository:** `week5/knowledge-base/employees/Oliver Spencer.md`

# HR Record

# Oliver Spencer

## Summary
- **Date of Birth**: May 14, 1990
- **Job Title**: Backend Software Engineer
- **Location**: Austin, Texas
- **Current Salary**: $125,000  

## Insurellm Career Progression
- **March 2018**: Joined Insurellm as a Backend Developer I, focusing on API development for customer management systems.
- **July 2019**: Promoted to Backend Developer II after successfully leading a team project to revamp the claims processing system, reducing response time by 30%.
- **June 2021**: Transitioned to Backend Software Engineer with a broader role in architecture and system design, collaborating closely with the DevOps team.
- **September 2022**: Assigned as the lead engineer for the new "Innovate" initiative, aimed at integrating AI-driven solutions into existing products.
- **January 2023**: Awarded a mentorship role to guide new hires in backend technology and best practices within Insurellm.

## Annual Performance History
- **2018**: **3/5** - Adaptable team player but still learning to take initiative.
- **2019**: **4/5** - Demonstrated strong problem-solving skills, outstanding contribution on the claims project.
- **2020**: **2/5** - Struggled with time management; fell behind on deadlines during a high-traffic release period.
- **2021**: **4/5** - Made a significant turnaround with organized work habits and successful project management.
- **2022**: **5/5** - Exceptional performance during the "Innovate" initiative, showcasing leadership and creativity.
- **2023**: **3/5** - Maintaining steady work; expectations for innovation not fully met, leading to discussions about goals.

## Compensation History
- **March 2018**: Initial salary of $80,000.
- **July 2019**: Salary increased to $90,000 post-promotion.
- **June 2021**: Salary raised to $105,000 after role transition.
- **September 2022**: Salary adjustment to $120,000 due to increased responsibilities and performance.
- **January 2023**: Revised salary of $125,000 in recognition of mentorship role.

## Other HR Notes
- Oliver enjoys a strong rapport with team members and is known for organizing regular team-building activities.
- Participated in Insurellm’s Hackathon in 2022, where he led a project that won “Best Overall Solution.” 
- Pursuing AWS Certified Solutions Architect certification to enhance cloud skillset.
- Has expressed interest in further leadership opportunities within Insurellm and may consider project management roles in the future.


---

<a id="file-week5-knowledge-base-employees-priya-sharma-md"></a>
## File: `week5/knowledge-base/employees/Priya Sharma.md`

> **Path in repository:** `week5/knowledge-base/employees/Priya Sharma.md`

# HR Record

# Priya Sharma

## Summary
- **Date of Birth:** January 8, 1986
- **Job Title:** Senior Data Scientist
- **Location:** San Francisco, California
- **Current Salary:** $145,000

## Insurellm Career Progression
- **March 2018 - Present:** Senior Data Scientist
  - Leads machine learning initiatives for risk prediction models
  - Built recommendation engine for Marketllm increasing conversion by 28%
  - Mentors team of 3 junior data scientists
  - Published 2 research papers on insurance ML applications

- **June 2015 - February 2018:** Data Scientist at FinML Analytics
  - Developed predictive models for financial services clients
  - Specialized in customer churn prediction and fraud detection

- **August 2012 - May 2015:** Research Scientist at UC Berkeley AI Lab
  - Conducted research in machine learning and natural language processing
  - Published 5 peer-reviewed papers

## Annual Performance History
- **2023:** Rating: 4.9/5
  *Exceptional performance. Led breakthrough AI-driven underwriting project. Excellent technical leadership and mentorship.*

- **2022:** Rating: 4.7/5
  *Outstanding work on risk prediction models. Strong collaboration with product team and technical innovation.*

- **2021:** Rating: 4.5/5
  *Exceeded expectations with successful launch of recommendation engine. Effective mentor to junior team members.*

- **2020:** Rating: 4.3/5
  *Strong performance despite remote transition challenges. Maintained high-quality model development.*

- **2019:** Rating: 4.6/5
  *Excellent contributions to fraud detection systems. Recognized for thought leadership in ML applications.*

- **2018:** Rating: 4.2/5
  *Solid first year. Quick to understand insurance domain and apply ML expertise effectively.*

## Compensation History
- **2023:** Base Salary: $145,000 + Bonus: $25,000
- **2022:** Base Salary: $138,000 + Bonus: $22,000
- **2021:** Base Salary: $130,000 + Bonus: $20,000
- **2020:** Base Salary: $122,000 + Bonus: $18,000
- **2019:** Base Salary: $115,000 + Bonus: $15,000
- **2018:** Base Salary: $108,000 + Bonus: $12,000

## Other HR Notes
- **Education:** PhD in Computer Science (Machine Learning) from Stanford University
- **Publications:** 7+ peer-reviewed papers in ML conferences and journals
- **Speaking:** Regular speaker at ML and InsurTech conferences. Represented Insurellm at 4 major conferences in 2023.
- **Patents:** Co-inventor on 2 pending patents for insurance ML applications
- **Recognition:** Data Science Excellence Award 2023, featured in InsureTech Innovation Magazine
- **Skills:** Expert in Python, TensorFlow, PyTorch, scikit-learn, SQL, and cloud ML platforms
- **Feedback:** World-class technical talent with strong business acumen. Natural leader who elevates entire team. Key retention priority.


---

<a id="file-week5-knowledge-base-employees-rachel-martinez-md"></a>
## File: `week5/knowledge-base/employees/Rachel Martinez.md`

> **Path in repository:** `week5/knowledge-base/employees/Rachel Martinez.md`

# HR Record

# Rachel Martinez

## Summary
- **Date of Birth:** June 8, 1987
- **Job Title:** Product Manager
- **Location:** San Francisco, California
- **Current Salary:** $135,000

## Insurellm Career Progression
- **March 2019 - Present:** Product Manager
  - Leads product strategy for Carllm, the auto insurance portal
  - Successfully launched three major feature releases that increased user engagement by 45%
  - Manages cross-functional teams including engineering, design, and sales

- **January 2017 - February 2019:** Associate Product Manager
  - Supported product development for Marketllm marketplace
  - Conducted user research and competitive analysis
  - Collaborated with engineering teams on feature prioritization

- **June 2015 - December 2016:** Business Analyst at TechInsure Corp
  - Analyzed market trends and customer behavior in insurance tech sector
  - Created business requirements documents for new product initiatives

## Annual Performance History
- **2023:** Rating: 4.6/5
  *Exceptional year with successful launch of AI-powered claims prediction feature. Strong leadership and stakeholder management.*

- **2022:** Rating: 4.2/5
  *Met all product milestones but faced challenges with team alignment during Q3. Improved communication strategies by year end.*

- **2021:** Rating: 4.8/5
  *Outstanding performance. Led product redesign that reduced customer churn by 20%. Received Product Excellence Award.*

- **2020:** Rating: 3.8/5
  *Solid performance but struggled with remote team coordination during pandemic transition. Adapted well by Q4.*

- **2019:** Rating: 4.0/5
  *Strong start as Product Manager. Successfully transitioned from APM role with minimal friction.*

## Compensation History
- **2023:** Base Salary: $135,000 + Bonus: $20,000
- **2022:** Base Salary: $128,000 + Bonus: $15,000
- **2021:** Base Salary: $120,000 + Bonus: $18,000
- **2020:** Base Salary: $110,000 + Bonus: $8,000
- **2019:** Base Salary: $105,000 + Bonus: $10,000

## Other HR Notes
- **Professional Development:** Completed Product Leadership Certification from Pragmatic Institute (2021). Regular attendee at ProductCon and InsurTech conferences.
- **Mentorship:** Currently mentors two Associate Product Managers and actively participates in the Women in Tech initiative at Insurellm.
- **Skills:** Expert in Agile/Scrum methodologies, JIRA, Figma, SQL, and product analytics tools.
- **Feedback:** Known for her strategic thinking and ability to balance customer needs with business objectives. Strong communicator who bridges technical and business stakeholders effectively.


---

<a id="file-week5-knowledge-base-employees-robert-chen-md"></a>
## File: `week5/knowledge-base/employees/Robert Chen.md`

> **Path in repository:** `week5/knowledge-base/employees/Robert Chen.md`

# HR Record

# Robert Chen

## Summary
- **Date of Birth:** February 28, 1983
- **Job Title:** Senior Full Stack Engineer
- **Location:** San Francisco, California
- **Current Salary:** $152,000

## Insurellm Career Progression
- **January 2016 - Present:** Senior Full Stack Engineer
  - Technical lead for Homellm home insurance portal
  - Architects full-stack solutions using React, Node.js, and PostgreSQL
  - Mentors team of 6 engineers
  - Led 3 major platform releases

- **June 2012 - December 2015:** Full Stack Developer at WebSolutions Inc.
  - Built web applications for enterprise clients
  - Worked with various JavaScript frameworks and backend technologies

- **August 2008 - May 2012:** Software Engineer at TechStartup
  - Developed features for SaaS platform
  - Gained experience across full technology stack

## Annual Performance History
- **2023:** Rating: 4.8/5
  *Exceptional performance. Led critical platform modernization project. Outstanding technical leadership and mentorship.*

- **2022:** Rating: 4.6/5
  *Exceeded expectations. Delivered major features ahead of schedule with high quality. Strong team collaboration.*

- **2021:** Rating: 4.4/5
  *Strong performance with successful migration to microservices architecture. Effective technical decision-making.*

- **2020:** Rating: 4.2/5
  *Good performance maintaining productivity during remote transition. Supported team well through change.*

- **2019:** Rating: 4.5/5
  *Excellent year with successful Homellm rewrite. Strong architectural contributions.*

- **2018:** Rating: 4.3/5
  *Solid performance with consistent high-quality delivery. Growing into technical leadership role.*

- **2017:** Rating: 4.1/5
  *Good performance. Expanding expertise across full stack and taking on more complex features.*

- **2016:** Rating: 4.0/5
  *Strong start at Insurellm. Quick to learn domain and contribute effectively.*

## Compensation History
- **2023:** Base Salary: $152,000 + Bonus: $28,000
- **2022:** Base Salary: $145,000 + Bonus: $25,000
- **2021:** Base Salary: $138,000 + Bonus: $22,000
- **2020:** Base Salary: $132,000 + Bonus: $20,000
- **2019:** Base Salary: $125,000 + Bonus: $18,000
- **2018:** Base Salary: $118,000 + Bonus: $15,000
- **2017:** Base Salary: $112,000 + Bonus: $12,000
- **2016:** Base Salary: $105,000 + Bonus: $10,000

## Other HR Notes
- **Education:** MS in Computer Science from Stanford University, BS in Computer Engineering from MIT
- **Technical Expertise:** Expert in React, Node.js, TypeScript, PostgreSQL, AWS, microservices architecture
- **Recognition:** Engineering Excellence Award 2023, Technical Leadership Award 2021
- **Mentorship:** Mentored 12 engineers during tenure. Known for developing junior talent into strong contributors.
- **Patents:** Co-inventor on 1 patent for insurance processing optimization
- **Feedback:** World-class engineer with exceptional technical and leadership skills. Trusted advisor to engineering leadership. Critical to company's technical success.


---

<a id="file-week5-knowledge-base-employees-samantha-greene-md"></a>
## File: `week5/knowledge-base/employees/Samantha Greene.md`

> **Path in repository:** `week5/knowledge-base/employees/Samantha Greene.md`

# Samantha Greene

## Summary
- **Date of Birth:** October 14, 1990
- **Job Title:** HR Generalist
- **Location:** Denver, Colorado
- **Current Salary:** $70,000

## Insurellm Career Progression
- **2020** - Joined Insurellm as a HR Coordinator
  - Responsibilities included assisting with recruitment processes and managing employee onboarding.
- **2021** - Promoted to HR Generalist
  - Transitioned to a role with expanded responsibilities, including handling employee relations and benefits administration.
- **2022** - Completed the HR Leadership Development Program
  - Enhanced skills in conflict resolution and strategic planning.
- **2023** - Actively involved in initiating the company’s Diversity and Inclusion programs.
  - Samantha Greene played a key role in launching mentorship initiatives and employee resource groups.

## Annual Performance History
- **2020:** Exceeds Expectations  
  Samantha Greene demonstrated exceptional organizational skills and contributed to a streamlined onboarding process, earning commendations from senior leadership.

- **2021:** Meets Expectations  
  While proficient in her new role, Samantha Greene struggled with time management during peak recruitment seasons, resulting in occasional missed deadlines. 

- **2022:** Below Expectations  
  Samantha Greene faced challenges in balancing employee relations issues, thereby impacting her performance. Gaps in communication and follow-up led to a push for additional training.

- **2023:** Meets Expectations  
  After attending workshops focused on conflict resolution, Samantha Greene successfully improved her handling of employee grievances, though minor issues still arose in managing multitasking within projects.

## Compensation History
- **2020:** Base Salary - $55,000  
  The entry-level salary matched industry standards for HR Coordinators with limited experience.

- **2021:** Base Salary - $65,000  
  Following her promotion, Samantha Greene received a raise commensurate with her new responsibilities.

- **2022:** Base Salary - $65,000  
  No increase as a result of performance concerns; however, Samantha Greene continued to receive positive feedback for her participation in diversity initiatives.

- **2023:** Base Salary - $70,000  
  Recognized for substantial improvement in employee relations management and contributions to company culture, leading to a well-deserved increase.

## Other HR Notes
- Samantha Greene has expressed interest in pursuing an HR certification (SHRM-CP) to further her career growth within Insurellm. 
- Participated in Insurellm's employee wellness program, promoting mental health resources among staff.
- Actively volunteers with local nonprofits and encourages staff involvement in community outreach programs, enhancing Insurellm's corporate social responsibility initiatives. 

Samantha Greene is a valuable asset to Insurellm, continuously working on professional development and contributing to a supportive workplace culture.


---

<a id="file-week5-knowledge-base-employees-samuel-trenton-md"></a>
## File: `week5/knowledge-base/employees/Samuel Trenton.md`

> **Path in repository:** `week5/knowledge-base/employees/Samuel Trenton.md`

# HR Record

# Samuel Trenton

## Summary
- **Date of Birth:** April 12, 1989
- **Job Title:** Senior Data Scientist
- **Location:** Austin, Texas
- **Current Salary:** $115,000  

## Insurellm Career Progression
- **January 2020 - Present:** Senior Data Scientist  
  *Promoted for demonstrating exceptional analytical skills and leadership potential. Led several projects that improved customer segmentation strategies, resulting in a 15% increase in customer retention.*

- **June 2018 - December 2019:** Data Scientist  
  *Joined the Insurellm team and worked on developing predictive modeling techniques to assess risk for both B2B and B2C customers. Received recognition for the success of the "Risk Assessment Model" project.*

- **August 2016 - May 2018:** Junior Data Analyst  
  *Started at Insurellm as a Junior Data Analyst, focusing on data cleaning and preliminary analysis of customer data. Received training in various data visualization techniques, which aided in the transition to a Data Scientist role.*

## Annual Performance History
- **2023:** Rating: 4.5/5  
  *Samuel exceeded expectations, successfully leading a cross-departmental project on AI-driven underwriting processes.*

- **2022:** Rating: 3.0/5  
  *Some challenges in meeting deadlines and collaboration with the engineering team. Received constructive feedback and participated in a team communication workshop.*

- **2021:** Rating: 4.0/5  
  *There was notable improvement in performance. Worked to enhance model accuracy, leading to improved risk assessment outcomes for B2C customers.*

- **2020:** Rating: 3.5/5  
  *Exhibited a solid performance during the initial year as a Senior Data Scientist but had struggles adapting to new leadership expectations.*

## Compensation History
- **2023:** Base Salary: $115,000 + Bonus: $15,000  
  *Annual bonus based on successful project completions and performance metrics.*

- **2022:** Base Salary: $110,000 + Bonus: $10,000  
  *Slight decrease in bonus due to performance challenges during the year.*

- **2021:** Base Salary: $105,000 + Bonus: $12,000  
  *Merit-based increase, reflecting consistent contributions to the data science team.*

- **2020:** Base Salary: $100,000 + Bonus: $8,000  
  *Initial compensation as Senior Data Scientist, with a focus on building rapport with cross-functional teams.*

## Other HR Notes
- **Professional Development:** Completed several workshops on machine learning and AI applications in insurance. Currently pursuing an online certification in deep learning.

- **Engagement in Company Culture:** Regularly participates in team-building events and contributes to the internal newsletter, sharing insights on data science trends.

- **Areas for Improvement:** Collaboration with engineering teams has been noted as an area needing focus. Samuel has expressed a desire to work closely with tech teams to align data initiatives better.

- **Personal Interests:** Has a keen interest in hiking and photography, often sharing his photography from weekend hikes with colleagues, fostering positive team relationships.


---

<a id="file-week5-knowledge-base-employees-sarah-williams-md"></a>
## File: `week5/knowledge-base/employees/Sarah Williams.md`

> **Path in repository:** `week5/knowledge-base/employees/Sarah Williams.md`

# HR Record

# Sarah Williams

## Summary
- **Date of Birth:** November 3, 1994
- **Job Title:** UX Designer
- **Location:** Remote (Based in Portland, Oregon)
- **Current Salary:** $95,000

## Insurellm Career Progression
- **January 2022 - Present:** UX Designer
  - Leads design for Homellm home insurance portal
  - Conducted comprehensive user research resulting in 35% improvement in user satisfaction scores
  - Collaborates with product and engineering teams on feature design

- **June 2020 - December 2021:** Junior UX Designer
  - Supported senior designers on Marketllm marketplace redesign
  - Created wireframes, prototypes, and user flow diagrams
  - Participated in user testing and feedback sessions

- **August 2018 - May 2020:** UI/UX Designer at StartupHub Inc.
  - Designed mobile and web interfaces for various startup clients
  - Worked closely with developers to implement design systems

## Annual Performance History
- **2023:** Rating: 4.4/5
  *Strong design contributions with excellent user research skills. Led successful Homellm redesign project.*

- **2022:** Rating: 4.0/5
  *Good first year as UX Designer. Showed initiative and creativity, though sometimes needed guidance on complex projects.*

- **2021:** Rating: 3.6/5
  *Adequate performance but struggled with time management on multiple concurrent projects. Improved by year end.*

- **2020:** Rating: 4.2/5
  *Solid performance as Junior Designer. Quick to learn Insurellm's design system and processes.*

## Compensation History
- **2023:** Base Salary: $95,000 + Bonus: $8,000
- **2022:** Base Salary: $88,000 + Bonus: $6,000
- **2021:** Base Salary: $78,000 + Bonus: $3,000
- **2020:** Base Salary: $70,000

## Other HR Notes
- **Education:** BFA in Graphic Design from Rhode Island School of Design
- **Skills:** Expert in Figma, Sketch, Adobe Creative Suite. Proficient in HTML/CSS for design prototyping.
- **Professional Development:** Completed UX Research Certification from Nielsen Norman Group (2023). Regularly attends design conferences.
- **Portfolio:** Maintains active design portfolio showcasing Insurellm work (approved for external sharing).
- **Feedback:** Creative thinker with strong empathy for users. Works well remotely and maintains excellent communication with distributed teams.


---

<a id="file-week5-knowledge-base-employees-tyler-brooks-md"></a>
## File: `week5/knowledge-base/employees/Tyler Brooks.md`

> **Path in repository:** `week5/knowledge-base/employees/Tyler Brooks.md`

# HR Record

# Tyler Brooks

## Summary
- **Date of Birth:** September 9, 1998
- **Job Title:** Junior Backend Developer
- **Location:** Austin, Texas
- **Current Salary:** $75,000

## Insurellm Career Progression
- **August 2022 - Present:** Junior Backend Developer
  - Develops backend services for Carllm auto insurance portal
  - Works with Python, Django, and PostgreSQL
  - Participates in code reviews and learns from senior engineers
  - Fixed 45+ bugs and implemented 12 minor features

- **June 2021 - July 2022:** Software Engineering Intern
  - Completed 14-month internship program at Insurellm
  - Worked on various backend tasks and learned company tech stack
  - Contributed to internal tools development

## Annual Performance History
- **2023:** Rating: 3.2/5
  *Meets basic expectations. Shows potential but needs to improve code quality and take more initiative. Sometimes requires excessive guidance on tasks.*

- **2022:** Rating: 3.5/5
  *Adequate performance for a junior developer. Good learning attitude but needs to develop stronger problem-solving skills.*

## Compensation History
- **2023:** Base Salary: $75,000 + Bonus: $2,000
- **2022:** Base Salary: $72,000 + Bonus: $1,500
- **2021:** Intern Stipend: $30/hour

## Other HR Notes
- **Education:** BS in Computer Science from University of Texas at Austin (graduated 2021)
- **Skills:** Proficient in Python and SQL. Learning system design and API development best practices.
- **Development Areas:** Needs to improve debugging skills, code documentation, and independent problem-solving. Working with mentor on technical growth.
- **Training:** Enrolled in advanced Python course and backend architecture fundamentals program
- **Feedback:** Eager to learn but sometimes lacks confidence. Needs encouragement to ask questions earlier rather than struggling alone. Shows promise with continued mentorship and experience.
- **Career Goals:** Aspires to become a mid-level backend engineer within 2 years


---

<a id="file-week5-knowledge-base-products-bizllm-md"></a>
## File: `week5/knowledge-base/products/Bizllm.md`

> **Path in repository:** `week5/knowledge-base/products/Bizllm.md`

# Product Summary

# Bizllm

## Summary

Bizllm is Insurellm's enterprise-grade commercial insurance platform designed to revolutionize how insurers serve business customers. From small businesses to large corporations, Bizllm provides comprehensive tools for underwriting, policy administration, and risk management across multiple commercial lines including general liability, professional liability, property, workers' compensation, and cyber insurance. By leveraging AI and industry-specific data analytics, Bizllm enables commercial insurers to assess complex risks accurately, price policies competitively, and deliver exceptional service to business clients.

## Features

### 1. Multi-Line Underwriting Engine
Bizllm's sophisticated underwriting platform handles diverse commercial insurance products within a single unified system. AI-powered risk assessment evaluates business operations, industry-specific exposures, and financial stability to generate accurate quotes across multiple coverage types.

### 2. Business Intelligence Integration
The platform automatically gathers and analyzes data from business registries, financial databases, industry reports, and third-party risk intelligence sources to provide comprehensive underwriting insights without manual research.

### 3. Cyber Risk Assessment
Specialized cyber insurance capabilities include automated evaluation of digital security postures, breach history analysis, and IT infrastructure assessment. The platform identifies vulnerabilities and recommends risk mitigation measures to reduce exposure.

### 4. Workers' Compensation Optimization
Integrated workers' comp tools analyze payroll data, industry classifications, claims history, and safety programs to accurately price coverage and identify opportunities for premium credits through loss control initiatives.

### 5. Commercial Property Evaluation
Advanced property risk modeling incorporates location data, building characteristics, catastrophe modeling, and environmental hazards to assess property risks accurately. Integration with aerial imagery and IoT sensors provides real-time property condition monitoring.

### 6. Professional Liability Specialization
Industry-specific professional liability underwriting for sectors including healthcare, legal, accounting, technology, and consulting. The platform evaluates professional credentials, claims history, and industry-specific risk factors.

### 7. Portfolio Management Dashboard
Comprehensive analytics provide insurers with portfolio-level insights including line-of-business performance, loss ratios, renewal rates, and geographic concentrations. Predictive analytics identify profitable growth opportunities and emerging risks.

### 8. Agent and Broker Portal
Dedicated portals enable distribution partners to quote, bind, and service commercial policies efficiently. Real-time commission tracking, marketing materials, and training resources support productive agency relationships.

### 9. Claims Management Integration
Seamless connection with claims systems enables fast incident reporting, reserve establishment, and loss tracking. AI-powered tools identify subrogation opportunities and predict claim severity for better reserves.

## Pricing

Bizllm's pricing structure reflects the complexity and value of commercial insurance operations:

- **Business Tier:** $6,000/month for regional commercial insurers writing select lines of business, including core underwriting and policy administration.
- **Professional Tier:** $12,000/month for multi-line carriers, adding cyber risk tools, advanced analytics, and expanded integration capabilities.
- **Enterprise Tier:** Custom pricing for national and specialty commercial insurers requiring full customization, API access, dedicated environments, and white-label options.

All tiers include implementation services, staff training, and continuous platform updates.

## Roadmap

Bizllm's forward-looking development roadmap includes:

- **Q2 2025:** Launch of Bizllm version 1.0 with core multi-line underwriting, quoting, and policy administration.
- **Q4 2025:** Introduction of enhanced cyber insurance capabilities including active threat monitoring and breach response coordination.
- **Q2 2026:** Release of embedded IoT integration for real-time risk monitoring in property and workers' comp lines.
- **Q4 2026:** Launch of parametric insurance module enabling rapid payout triggers for weather events and business interruption.
- **Q2 2027:** Introduction of climate risk modeling tools incorporating forward-looking environmental data and transition risk analysis.
- **Q4 2027:** Expansion into international markets with country-specific commercial insurance products and regulatory compliance.

Bizllm empowers commercial insurers to compete effectively in complex markets while delivering the digital experiences today's business customers demand. Transform your commercial insurance operations with Bizllm!


---

<a id="file-week5-knowledge-base-products-carllm-md"></a>
## File: `week5/knowledge-base/products/Carllm.md`

> **Path in repository:** `week5/knowledge-base/products/Carllm.md`

# Product Summary

# Carllm

## Summary

Carllm is an innovative auto insurance product developed by Insurellm, designed to streamline the way insurance companies offer coverage to their customers. Powered by cutting-edge artificial intelligence, Carllm utilizes advanced algorithms to deliver personalized auto insurance solutions, ensuring optimal coverage while minimizing costs. With a robust infrastructure that supports both B2B and B2C customers, Carllm redefines the auto insurance landscape and empowers insurance providers to enhance customer satisfaction and retention.

## Features

- **AI-Powered Risk Assessment**: Carllm leverages artificial intelligence to analyze driver behavior, vehicle conditions, and historical claims data. This enables insurers to make informed decisions and set competitive premiums that reflect true risk profiles.

- **Instant Quoting**: With Carllm, insurance companies can offer near-instant quotes to customers, enhancing the customer experience. The AI engine processes data in real-time, drastically reducing the time it takes to generate quotes.

- **Customizable Coverage Plans**: Carllm allows insurers to create flexible and tailored insurance packages based on individual customer needs. This customization improves customer engagement and retention.

- **Fraud Detection**: The product incorporates advanced analytics to identify potentially fraudulent claims, significantly reducing the risk of losses for insurance providers.

- **Customer Insights Dashboard**: Carllm provides insurers with a powerful dashboard that offers deep insights into customer behavior, claims patterns, and market trends, enabling informed decision-making and strategic planning.

- **Mobile Integration**: Carllm is designed to work seamlessly with mobile applications, providing both insurers and end-users access to policy management and claims reporting on the go.

- **Automated Customer Support**: Leveraging AI chatbots, Carllm offers 24/7 customer support, helping to resolve inquiries quickly and efficiently, thus improving customer satisfaction.

## Pricing

Carllm is offered under a subscription-based pricing model tailored to meet the needs of insurance companies of all sizes. Our pricing tiers are designed to provide maximum flexibility and value:

- **Basic Tier**: $1,000/month
  - Ideal for small insurance firms.
  - Access to core features and standard reporting.

- **Professional Tier**: $2,500/month
  - For medium-sized companies.
  - All Basic Tier features plus advanced analytics and fraud detection.

- **Enterprise Tier**: $5,000/month
  - Customized solutions for large insurance firms.
  - Comprehensive support, full feature access, and integration with existing systems.

Contact our sales team for a personalized quote and discover how Carllm can transform your auto insurance offerings!

## 2025-2026 Roadmap

In our commitment to continuous improvement and innovation, Insurellm has outlined the following roadmap for Carllm:

### Q1 2025: Launch Feature Enhancements
- **Expanded data integrations** for better risk assessment.
- **Enhanced fraud detection algorithms** to reduce losses.

### Q2 2025: Customer Experience Improvements
- Launch of a new **mobile app** for end-users.
- Introduction of **telematics-based pricing** to provide even more tailored coverage options.

### Q3 2025: Global Expansion
- Begin pilot programs for international insurance markets.
- Collaborate with local insurers to offer compliant, localized versions of Carllm.

### Q4 2025: AI and Machine Learning Upgrades
- Implement next-gen machine learning models for predictive analysis.
- Roll out customer insights dashboard updates based on user feedback.

### 2026: Scaling and Partnerships
- Increase partnerships with automakers for integrated insurance solutions.
- Enhance the **AI customer support system** to include multi-language support.

Carllm is not just an auto insurance product; it is a transformative tool for the insurance industry. Join us on this exciting journey as we redefine the future of auto insurance with technology and customer-centric solutions.


---

<a id="file-week5-knowledge-base-products-claimllm-md"></a>
## File: `week5/knowledge-base/products/Claimllm.md`

> **Path in repository:** `week5/knowledge-base/products/Claimllm.md`

# Product Summary

# Claimllm

## Summary

Claimllm is Insurellm's revolutionary claims processing platform that transforms the claims experience for insurers, adjusters, and policyholders. Powered by advanced AI, machine learning, and computer vision, Claimllm automates claims handling across all insurance lines—from first notice of loss through final settlement. By dramatically reducing processing time, improving accuracy, and enhancing fraud detection, Claimllm enables insurers to deliver exceptional claims service while significantly reducing operational costs. The platform seamlessly integrates with existing policy administration and core systems to create a unified insurance ecosystem.

## Features

### 1. Intelligent FNOL Processing
Claimllm's AI-powered first notice of loss intake captures claim details through multiple channels including mobile apps, web portals, phone integrations, and chatbots. Natural language processing extracts key information automatically, creating structured claim files without manual data entry.

### 2. Automated Triage and Routing
Machine learning algorithms instantly assess claim severity, complexity, and fraud potential to route claims to appropriate handlers. Simple claims enter straight-through processing while complex cases receive immediate adjuster assignment with pre-populated investigation guidance.

### 3. Computer Vision Damage Assessment
Advanced image recognition technology analyzes photos and videos of damaged property or vehicles to estimate repair costs accurately. The system identifies damage types, measures extent, and generates preliminary estimates in minutes rather than days.

### 4. Predictive Fraud Detection
Sophisticated fraud analytics evaluate claims against historical patterns, network analysis, and anomaly detection to flag suspicious claims for investigation. The system learns continuously from confirmed fraud cases to improve detection accuracy.

### 5. Smart Document Processing
Optical character recognition and natural language processing automatically extract information from medical records, police reports, repair estimates, and supporting documentation. The system validates information against policy terms and flags discrepancies for review.

### 6. Dynamic Reserve Setting
AI-powered predictive modeling analyzes claim characteristics, historical outcomes, and current case details to recommend accurate reserves. Automated reserve adjustments occur as new information becomes available, ensuring financial accuracy.

### 7. Vendor Management Platform
Integrated tools coordinate with repair shops, medical providers, lawyers, and other service providers. Automated assignment based on location, capacity, and performance metrics ensures efficient vendor utilization and quality outcomes.

### 8. Payment Automation
Straight-through payment processing for approved claims includes direct deposit, digital payments, and traditional check issuance. Multi-party payment splitting handles complex scenarios involving mortgagees, lessors, and medical providers.

### 9. Claimant Communication Hub
Omnichannel communication tools keep claimants informed via their preferred method—text, email, app notifications, or phone. Automated status updates reduce incoming inquiries while improving customer satisfaction.

### 10. Analytics and Reporting
Comprehensive dashboards track key metrics including cycle time, loss ratios, settlement patterns, and customer satisfaction. Predictive analytics identify process bottlenecks and opportunities for improvement.

## Pricing

Claimllm offers flexible pricing models to accommodate insurers of all sizes:

- **Core Tier:** $4,500/month for smaller insurers processing up to 5,000 claims annually, including essential automation features and standard integrations.
- **Advanced Tier:** $9,500/month for mid-sized insurers handling up to 25,000 claims annually, adding computer vision, predictive analytics, and expanded vendor management.
- **Enterprise Tier:** Custom pricing for high-volume insurers requiring unlimited claim capacity, full API access, dedicated infrastructure, advanced fraud analytics, and white-label capabilities.

All tiers include comprehensive implementation, claims staff training, and continuous platform enhancements.

## Roadmap

Claimllm's ambitious development roadmap includes:

- **Q1 2025:** Launch of Claimllm version 1.0 with core claims processing automation, FNOL capture, and basic fraud detection.
- **Q3 2025:** Introduction of advanced computer vision capabilities for property and auto damage assessment with repair cost estimation.
- **Q1 2026:** Release of predictive litigation analytics identifying claims likely to involve attorneys and recommending settlement strategies.
- **Q3 2026:** Launch of blockchain-based subrogation network enabling automated inter-carrier claim recovery and settlement.
- **Q1 2027:** Introduction of real-time settlement negotiation AI that optimizes settlement amounts based on claim details and historical outcomes.
- **Q3 2027:** Expansion into catastrophe claims management with disaster response coordination and large-loss handling capabilities.

Claimllm represents the future of insurance claims—faster, smarter, and more customer-centric. Transform your claims operation and deliver the service your policyholders deserve!


---

<a id="file-week5-knowledge-base-products-healthllm-md"></a>
## File: `week5/knowledge-base/products/Healthllm.md`

> **Path in repository:** `week5/knowledge-base/products/Healthllm.md`

# Product Summary

# Healthllm

## Summary

Healthllm is Insurellm's comprehensive health insurance platform that empowers insurance providers to deliver modern, personalized health coverage. By combining advanced AI technology with healthcare data analytics, Healthllm streamlines every aspect of health insurance operations—from plan design and enrollment to claims processing and member engagement. Built for the complexities of the healthcare industry, Healthllm helps insurers reduce costs, improve member outcomes, and navigate the evolving regulatory landscape with confidence.

## Features

### 1. Intelligent Plan Design
Healthllm's AI-powered tools help insurers create competitive health plans by analyzing market trends, member demographics, and healthcare utilization patterns. The platform suggests optimal benefit structures, deductibles, and network configurations to maximize both member value and profitability.

### 2. Real-Time Eligibility Verification
Integrated eligibility checking ensures instant verification of coverage status, reducing claim denials and improving provider satisfaction. The system connects with healthcare provider networks for seamless real-time validation.

### 3. AI-Driven Claims Adjudication
Automated claims processing uses machine learning to review claims for accuracy, identify potential fraud, and expedite legitimate payments. The system learns from historical data to continuously improve processing accuracy and efficiency.

### 4. Predictive Healthcare Analytics
Advanced analytics identify high-risk members who would benefit from preventive care interventions, enabling insurers to implement proactive wellness programs that reduce long-term costs and improve member health outcomes.

### 5. Provider Network Management
Comprehensive tools for managing provider relationships, contract negotiations, and network adequacy. The platform tracks provider performance metrics and identifies opportunities for cost savings through strategic partnerships.

### 6. Member Engagement Platform
A mobile-first member portal provides easy access to coverage information, digital ID cards, claims status, provider directories, and telehealth services. Push notifications keep members informed about preventive care opportunities and wellness programs.

### 7. Medication Management
Integration with pharmacy benefit managers enables formulary management, prior authorization automation, and medication adherence tracking. AI-powered tools identify cost-saving generic alternatives and flag potential drug interactions.

### 8. Regulatory Compliance Engine
Built-in compliance monitoring ensures adherence to ACA requirements, state mandates, and HIPAA regulations. Automated reporting simplifies regulatory filings and reduces compliance risk.

## Pricing

Healthllm offers tiered pricing to serve health insurers across the spectrum:

- **Essential Tier:** $8,000/month for regional health plans, providing core platform capabilities and standard integrations.
- **Professional Tier:** $15,000/month for larger insurers, including advanced analytics, predictive modeling, and expanded integration options.
- **Enterprise Tier:** Custom pricing for national carriers and health systems requiring extensive customization, multi-state support, dedicated infrastructure, and premium support services.

All plans include implementation support, staff training, and ongoing platform enhancements.

## Roadmap

Healthllm's strategic development roadmap includes:

- **Q1 2025:** Launch of Healthllm version 1.0 featuring core claims processing, eligibility verification, and member portal.
- **Q3 2025:** Introduction of predictive analytics module for population health management and risk stratification.
- **Q1 2026:** Release of advanced AI claims adjudication with automated fraud detection and payment optimization.
- **Q3 2026:** Launch of social determinants of health (SDOH) integration, enabling holistic member care and targeted interventions.
- **Q1 2027:** Introduction of value-based care management tools supporting ACO and bundled payment models.
- **Q3 2027:** Global expansion with international healthcare system integrations and multi-language support.

Healthllm represents Insurellm's commitment to transforming health insurance through technology that improves outcomes for insurers, providers, and members alike. Join us in building the future of health insurance!


---

<a id="file-week5-knowledge-base-products-homellm-md"></a>
## File: `week5/knowledge-base/products/Homellm.md`

> **Path in repository:** `week5/knowledge-base/products/Homellm.md`

# Product Summary

# Homellm

## Summary
Homellm is an innovative home insurance product developed by Insurellm that leverages advanced AI technology to revolutionize the way insurance providers offer coverage to homeowners. Designed for both B2B and B2C segments, Homellm empowers insurers to provide personalized, data-driven policies, enhancing customer experience while minimizing risk and operational costs. By integrating seamlessly with existing systems, Homellm helps insurance companies streamline their processes and stay competitive in the ever-evolving insurance industry.

## Features
### 1. AI-Powered Risk Assessment
Homellm utilizes sophisticated AI algorithms to analyze vast datasets, allowing insurance companies to assess risks accurately. This feature provides real-time insights for underwriting decisions, enabling insurers to tailor policies to individual customer needs.

### 2. Dynamic Pricing Model
With Homellm's innovative dynamic pricing model, insurance providers can offer flexible premiums based on real-time risk evaluations and historical data. This adaptability ensures that customers pay a fair price that accurately reflects their unique risk profile.

### 3. Instant Claim Processing
The AI-driven claims management system in Homellm automates the entire claims process, reducing processing time from weeks to hours. Insurers can resolve claims quickly and efficiently, leading to enhanced customer satisfaction.

### 4. Predictive Maintenance Alerts
Homellm incorporates predictive analytics to advise homeowners on potential risks and maintenance needs. By preventing issues before they arise, this feature helps customers minimize hazards, lowering the likelihood of claims.

### 5. Multi-Channel Integration
Homellm seamlessly integrates into existing insurance platforms, providing a centralized hub for managing customer policies and claims. Insurance providers can easily access customer data, allowing for improved service delivery across various channels.

### 6. Customer Portal
A user-friendly online portal and mobile application enables customers to manage their policies, submit claims, and view coverage details 24/7. Homellm prioritizes transparency and ease of use, helping insurers foster trust and long-term relationships with their customers.

## Pricing
At Insurellm, we believe in providing value without compromising quality. The pricing for Homellm is structured based on the size of the insurance provider and the level of customization required. 

- **Basic Tier:** Starting at $5,000/month for small insurers with basic integration features.
- **Standard Tier:** Starting at $10,000/month for medium-sized insurers including advanced analytics and reporting tools.
- **Enterprise Tier:** Custom pricing for large insurance companies that require full customization, dedicated support, and additional features, such as enterprise-grade security and compliance.

All tiers include a comprehensive training program and ongoing updates to ensure optimal performance.

## Roadmap
The development roadmap for Homellm includes the following key milestones:

- **Q1 2024:** Launch of Homellm version 1.0, featuring core functionalities and integrations.
- **Q3 2024:** Introduction of enhanced analytics capabilities, including visualization tools and advanced reporting features.
- **Q1 2025:** Release of Homellm version 2.0, with expanded predictive maintenance alerts and automated underwriting processes.
- **Q3 2025:** Establish partnerships with IoT device manufacturers to provide integrated solutions for proactive risk management.
- **Q1 2026:** Ongoing improvements based on user feedback and industry trends, ensuring that Homellm remains at the forefront of home insurance technology. 

With Homellm, Insurellm is committed to transforming the landscape of home insurance, ensuring both innovation and reliability for all insurance providers and their customers. Explore the future of home insurance today with Homellm!


---

<a id="file-week5-knowledge-base-products-lifellm-md"></a>
## File: `week5/knowledge-base/products/Lifellm.md`

> **Path in repository:** `week5/knowledge-base/products/Lifellm.md`

# Product Summary

# Lifellm

## Summary

Lifellm is an advanced life insurance platform developed by Insurellm that revolutionizes how insurance providers offer life coverage to their customers. Leveraging cutting-edge AI and predictive analytics, Lifellm enables insurers to provide personalized life insurance policies with streamlined underwriting, accurate risk assessment, and exceptional customer experiences. Designed for both B2B and B2C markets, Lifellm helps insurance companies modernize their life insurance operations while reducing costs and improving customer satisfaction.

## Features

### 1. AI-Powered Underwriting
Lifellm's sophisticated AI engine analyzes health records, lifestyle data, and demographic information to accelerate the underwriting process. What traditionally took weeks can now be completed in hours or even minutes, enabling insurers to issue policies faster while maintaining accuracy.

### 2. Predictive Risk Modeling
Advanced machine learning algorithms assess mortality risk by analyzing vast datasets including medical histories, genetic markers, and lifestyle factors. This enables insurers to price policies more accurately and identify opportunities for coverage expansion.

### 3. Digital Health Integration
Lifellm seamlessly integrates with wearables and health tracking apps, allowing insurers to offer dynamic policies that reward healthy behaviors. This creates win-win scenarios where customers maintain better health while enjoying premium discounts.

### 4. Automated Policy Management
The platform provides a comprehensive suite of tools for policy administration, including beneficiary management, premium calculations, coverage adjustments, and policy renewals. Automation reduces administrative burden and minimizes errors.

### 5. Smart Document Processing
Lifellm utilizes natural language processing and optical character recognition to automatically extract and validate information from medical records, applications, and supporting documentation, significantly reducing manual data entry.

### 6. Customer Portal
A user-friendly portal enables policyholders to manage their coverage, update beneficiaries, access policy documents, and track wellness incentives 24/7. Mobile app integration ensures customers can manage their life insurance anywhere.

### 7. Compliance Automation
Built-in regulatory compliance tools ensure that policies meet state and federal requirements, with automatic updates as regulations change. This reduces compliance risk for insurers operating across multiple jurisdictions.

## Pricing

Lifellm's flexible pricing structure accommodates insurance providers of all sizes:

- **Starter Tier:** $3,500/month for small insurers, including core underwriting features and basic integrations.
- **Growth Tier:** $7,500/month for mid-sized companies, adding predictive analytics, digital health integration, and advanced reporting.
- **Enterprise Tier:** Custom pricing for large insurance providers requiring full customization, white-label options, dedicated support, and enterprise-grade security.

All tiers include comprehensive onboarding, training programs, and regular platform updates.

## Roadmap

The development roadmap for Lifellm includes these strategic milestones:

- **Q2 2025:** Launch of Lifellm version 1.0 with core AI underwriting and policy management capabilities.
- **Q4 2025:** Introduction of digital health platform integrations with major wearable device manufacturers and health app providers.
- **Q2 2026:** Release of Lifellm version 2.0 featuring enhanced predictive modeling, genetic risk assessment capabilities, and blockchain-based policy verification.
- **Q4 2026:** Launch of embedded life insurance API allowing partners to offer life coverage within their own platforms and applications.
- **Q2 2027:** Expansion into international markets with localized regulatory compliance features and multi-currency support.

With Lifellm, Insurellm is transforming life insurance into a modern, customer-centric experience that benefits both insurers and policyholders. Experience the future of life insurance technology today!


---

<a id="file-week5-knowledge-base-products-markellm-md"></a>
## File: `week5/knowledge-base/products/Markellm.md`

> **Path in repository:** `week5/knowledge-base/products/Markellm.md`

# Product Summary

# Markellm

## Summary

Markellm is an innovative two-sided marketplace designed to seamlessly connect consumers with insurance companies. Powered by advanced matching AI, Markellm transforms the insurance shopping experience, making it more efficient, personalized, and accessible. Whether you're a homeowner searching for the best rates on home insurance or an insurer looking to reach new customers, Markellm acts as the ultimate bridge, delivering tailored solutions for all parties involved. With a user-friendly interface and powerful algorithms, Markellm not only saves time but also enhances decision-making in the often-complex insurance landscape.

## Features

- **AI-Powered Matching**: Markellm utilizes sophisticated AI algorithms to match consumers with the most suitable insurance products based on their individual needs and preferences. This ensures that both parties get the best possible options.

- **User-Friendly Interface**: Designed with user experience in mind, Markellm features an intuitive interface that allows consumers to easily browse and compare various insurance offerings from multiple providers.

- **Real-Time Quotes**: Consumers can receive real-time quotes from different insurance companies, empowering them to make informed decisions quickly without endless back-and-forth communication.

- **Customized Recommendations**: Based on user profiles and preferences, Markellm provides personalized insurance recommendations, ensuring consumers find the right coverage at competitive rates.

- **Secure Transactions**: Markellm prioritizes security, employing robust encryption methods to ensure that all transactions and data exchanges are safe and secure.

- **Customer Support**: Our dedicated support team is always available to assist both consumers and insurers throughout the process, providing guidance and answering any questions that may arise.

- **Data Insights**: Insurers gain access to valuable data insights through Markellm's analytics dashboard, helping them understand market trends and consumer behavior to refine their offerings.

## Pricing

At Markellm, we believe in transparency and flexibility. Our pricing structure is designed to accommodate different types of users—whether you're a consumer seeking insurance or an insurance provider seeking customers.

### For Consumers:
- **Free Membership**: Access to the marketplace at no cost, allowing unlimited browsing and comparisons.
- **Premium Features**: Optional subscription at $9.99/month for advanced analytics on choices, priority customer support, and enhanced customization options.

### For Insurance Companies:
- **Basic Listing Fee**: $199/month for a featured listing on the platform, providing exposure to thousands of potential customers.
- **Performance-Based Pricing**: Option for variable pricing based on successful customer acquisitions— pay $25 per lead generated through Markellm.

## 2025-2026 Roadmap

### Q1 2025
- Launch a mobile app version of Markellm, making it even easier for consumers and insurers to connect on-the-go.
- Introduce a referral program that rewards users for promoting Markellm to their network.

### Q2 2025
- Expand the marketplace to include additional insurance products, such as life and health insurance.
- Partner with third-party data aggregators to enhance the accuracy of our AI matching capabilities.

### Q3 2025
- Initiate a comprehensive marketing campaign targeting both consumers and insurers to increase user acquisition and brand awareness.
- Release user testimonials and case studies showcasing successful matches made through Markellm.

### Q4 2026
- Implement machine learning enhancements to our AI algorithm, further increasing the precision and personalization of matches.
- Explore international expansion opportunities, launching in select markets outside the US.

Markellm is committed to improving the insurance experience for both consumers and providers. By leveraging technology and user insights, we aim to become the leading platform in the insurance marketplace ecosystem. Join us on this exciting journey towards smarter, more efficient insurance solutions!


---

<a id="file-week5-knowledge-base-products-rellm-md"></a>
## File: `week5/knowledge-base/products/Rellm.md`

> **Path in repository:** `week5/knowledge-base/products/Rellm.md`

# Product Summary

# Rellm: AI-Powered Enterprise Reinsurance Solution

## Summary

Rellm is an innovative enterprise reinsurance product developed by Insurellm, designed to transform the way reinsurance companies operate. Harnessing the power of artificial intelligence, Rellm offers an advanced platform that redefines risk management, enhances decision-making processes, and optimizes operational efficiencies within the reinsurance industry. With seamless integrations and robust analytics, Rellm enables insurers to proactively manage their portfolios and respond to market dynamics with agility.

## Features

### AI-Driven Analytics
Rellm utilizes cutting-edge AI algorithms to provide predictive insights into risk exposures, enabling users to forecast trends and make informed decisions. Its real-time data analysis empowers reinsurance professionals with actionable intelligence.

### Seamless Integrations
Rellm's architecture is designed for effortless integration with existing systems. Whether it's policy management, claims processing, or financial reporting, Rellm connects seamlessly with diverse data sources to create a unified ecosystem.

### Risk Assessment Module
The comprehensive risk assessment module within Rellm allows insurers to evaluate risk profiles accurately. By leveraging historical data and advanced modeling techniques, Rellm provides a clear picture of potential liabilities and expected outcomes.

### Customizable Dashboard
Rellm features a customizable dashboard that presents key metrics and performance indicators in an intuitive interface. Users can tailor their view to focus on what matters most to their business, enhancing user experience and productivity.

### Regulatory Compliance Tools
Rellm includes built-in compliance tracking features to help organizations meet local and international regulatory standards. This ensures that reinsurance practices remain transparent and accountable.

### Client and Broker Portals
Rellm offers dedicated portals for both clients and brokers, facilitating real-time communication and documentation sharing. This strengthens partnerships and drives operational excellence across the board.

## Pricing

Insurellm offers flexible pricing plans for Rellm to cater to various business needs:

- **Basic Plan**: $5,000/month
  - Includes access to core features and standard integrations.
  
- **Professional Plan**: $10,000/month
  - Includes all features, advanced integrations, and priority customer support.
  
- **Enterprise Plan**: Custom pricing
  - Tailored solutions with personalized features, extensive integrations, and dedicated account management.

Join the growing number of organizations leveraging Rellm to enhance their reinsurance processes while driving profitability and compliance. 

## 2025-2026 Roadmap

At Insurellm, we are committed to the continuous improvement of Rellm. Our roadmap for 2025-2026 includes:

- **Q3 2025**: 
  - Launch of the Rellm Mobile App for on-the-go insights and management.
  - Introduction of augmented reality (AR) features for interactive risk assessments.

- **Q1 2026**: 
  - Deployment of advanced machine learning models for even more accurate risk predictions.
  - Expansion of integration capabilities to support emerging technologies in the insurance sector.

- **Q3 2026**: 
  - Release of a community platform for Rellm users to exchange insights, tips, and best practices.
  - Launch of Rellm 2.0, featuring enhanced user interface and premium features based on user feedback.

Experience the future of reinsurance with Rellm, where innovation meets reliability. Let Insurellm help you navigate the complexities of the reinsurance market smarter and faster.


---

<a id="file-week5-pro-implementation-answer-py"></a>
## File: `week5/pro_implementation/answer.py`

> **Path in repository:** `week5/pro_implementation/answer.py`

```python
from openai import OpenAI
from dotenv import load_dotenv
from chromadb import PersistentClient
from litellm import completion
from pydantic import BaseModel, Field
from pathlib import Path
from tenacity import retry, wait_exponential


load_dotenv(override=True)

# MODEL = "openai/gpt-6-luna"
MODEL = "groq/openai/gpt-oss-120b"
DB_NAME = str(Path(__file__).parent.parent / "preprocessed_db")
KNOWLEDGE_BASE_PATH = Path(__file__).parent.parent / "knowledge-base"
SUMMARIES_PATH = Path(__file__).parent.parent / "summaries"

collection_name = "docs"
embedding_model = "text-embedding-3-large"
wait = wait_exponential(multiplier=1, min=10, max=240)

openai = OpenAI()

chroma = PersistentClient(path=DB_NAME)
collection = chroma.get_or_create_collection(collection_name)

RETRIEVAL_K = 20
FINAL_K = 10

SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing the company Insurellm.
You are chatting with a user about Insurellm.
Your answer will be evaluated for accuracy, relevance and completeness, so make sure it only answers the question and fully answers it.
If you don't know the answer, say so.
For context, here are specific extracts from the Knowledge Base that might be directly relevant to the user's question:
{context}

With this context, please answer the user's question. Be accurate, relevant and complete.
"""


class Result(BaseModel):
    page_content: str
    metadata: dict


class RankOrder(BaseModel):
    order: list[int] = Field(
        description="The order of relevance of chunks, from most relevant to least relevant, by chunk id number"
    )


@retry(wait=wait)
def rerank(question, chunks):
    system_prompt = """
You are a document re-ranker.
You are provided with a question and a list of relevant chunks of text from a query of a knowledge base.
The chunks are provided in the order they were retrieved; this should be approximately ordered by relevance, but you may be able to improve on that.
You must rank order the provided chunks by relevance to the question, with the most relevant chunk first.
Reply only with the list of ranked chunk ids, nothing else. Include all the chunk ids you are provided with, reranked.
"""
    user_prompt = f"The user has asked the following question:\n\n{question}\n\nOrder all the chunks of text by relevance to the question, from most relevant to least relevant. Include all the chunk ids you are provided with, reranked.\n\n"
    user_prompt += "Here are the chunks:\n\n"
    for index, chunk in enumerate(chunks):
        user_prompt += f"# CHUNK ID: {index + 1}:\n\n{chunk.page_content}\n\n"
    user_prompt += "Reply only with the list of ranked chunk ids, nothing else."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = completion(model=MODEL, messages=messages, response_format=RankOrder)
    reply = response.choices[0].message.content
    order = RankOrder.model_validate_json(reply).order
    return [chunks[i - 1] for i in order]


def make_rag_messages(question, history, chunks):
    context = "\n\n".join(
        f"Extract from {chunk.metadata['source']}:\n{chunk.page_content}" for chunk in chunks
    )
    system_prompt = SYSTEM_PROMPT.format(context=context)
    return (
        [{"role": "system", "content": system_prompt}]
        + history
        + [{"role": "user", "content": question}]
    )


@retry(wait=wait)
def rewrite_query(question, history=None):
    """Rewrite the user's question to be a more specific question that is more likely to surface relevant content in the Knowledge Base."""
    if history is None:
        history = []

    message = f"""
You are in a conversation with a user.
You are about to look up information in a Knowledge Base to answer the user's question.

This is the history of your conversation so far with the user:
{history}

And this is the user's current question:
{question}

Since the conversation is contextual, understand the meaning of the user question and add details based on the history.
Condense everything in a single contextually-rich VERY short and specific question, most likely to surface content.

EXAMPLE:
user: Who is the founder? -> Query: who is the founder?
assistant: The founder is FooBar
user: What role covers? -> Query: What role FooBar covers?
...

IMPORTANT: Respond ONLY with the precise knowledgebase query, nothing else.
"""
    response = completion(model=MODEL, messages=[{"role": "system", "content": message}])
    return response.choices[0].message.content


def merge_chunks(chunks, reranked):
    merged = chunks[:]
    existing = [chunk.page_content for chunk in chunks]
    for chunk in reranked:
        if chunk.page_content not in existing:
            merged.append(chunk)
    return merged


def fetch_context_unranked(question):
    query = openai.embeddings.create(model=embedding_model, input=[question]).data[0].embedding
    results = collection.query(query_embeddings=[query], n_results=RETRIEVAL_K)
    chunks = []
    for result in zip(results["documents"][0], results["metadatas"][0]):
        chunks.append(Result(page_content=result[0], metadata=result[1]))
    return chunks


def fetch_context(original_question, history=None):
    rewritten_question = rewrite_query(original_question, history)
    print(rewritten_question)
    chunks1 = fetch_context_unranked(original_question)
    chunks2 = fetch_context_unranked(rewritten_question)
    chunks = merge_chunks(chunks1, chunks2)
    reranked = rerank(original_question, chunks)
    return reranked[:FINAL_K]


@retry(wait=wait)
def answer_question(question: str, history: list[dict] = []) -> tuple[str, list]:
    """
    Answer a question using RAG and return the answer and the retrieved context
    """
    chunks = fetch_context(question, history)
    messages = make_rag_messages(question, history, chunks)
    response = completion(model=MODEL, messages=messages)
    return response.choices[0].message.content, chunks
```


---

<a id="file-week5-pro-implementation-ingest-py"></a>
## File: `week5/pro_implementation/ingest.py`

> **Path in repository:** `week5/pro_implementation/ingest.py`

```python
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from chromadb import PersistentClient
from tqdm import tqdm
from litellm import completion
from multiprocessing import Pool
from tenacity import retry, wait_exponential


load_dotenv(override=True)

MODEL = "openai/gpt-6-luna"

DB_NAME = str(Path(__file__).parent.parent / "preprocessed_db")
collection_name = "docs"
embedding_model = "text-embedding-3-large"
KNOWLEDGE_BASE_PATH = Path(__file__).parent.parent / "knowledge-base"
AVERAGE_CHUNK_SIZE = 100
wait = wait_exponential(multiplier=1, min=10, max=240)


WORKERS = 3

openai = OpenAI()


class Result(BaseModel):
    page_content: str
    metadata: dict


class Chunk(BaseModel):
    headline: str = Field(
        description="A brief heading for this chunk, typically a few words, that is most likely to be surfaced in a query",
    )
    summary: str = Field(
        description="A few sentences summarizing the content of this chunk to answer common questions"
    )
    original_text: str = Field(
        description="The original text of this chunk from the provided document, exactly as is, not changed in any way"
    )

    def as_result(self, document):
        metadata = {"source": document["source"], "type": document["type"]}
        return Result(
            page_content=self.headline + "\n\n" + self.summary + "\n\n" + self.original_text,
            metadata=metadata,
        )


class Chunks(BaseModel):
    chunks: list[Chunk]


def fetch_documents():
    """A homemade version of the LangChain DirectoryLoader"""

    documents = []

    for folder in KNOWLEDGE_BASE_PATH.iterdir():
        doc_type = folder.name
        for file in folder.rglob("*.md"):
            with open(file, "r", encoding="utf-8") as f:
                documents.append({"type": doc_type, "source": file.as_posix(), "text": f.read()})

    print(f"Loaded {len(documents)} documents")
    return documents


def make_prompt(document):
    how_many = (len(document["text"]) // AVERAGE_CHUNK_SIZE) + 1
    return f"""
You take a document and you split the document into overlapping chunks for a KnowledgeBase.

The document is from the shared drive of a company called Insurellm.
The document is of type: {document["type"]}
The document has been retrieved from: {document["source"]}

A chatbot will use these chunks to answer questions about the company.
You should divide up the document as you see fit, being sure that the entire document is returned across the chunks - don't leave anything out.
This document should probably be split into at least {how_many} chunks, but you can have more or less as appropriate, ensuring that there are individual chunks to answer specific questions.
There should be overlap between the chunks as appropriate; typically about 25% overlap or about 50 words, so you have the same text in multiple chunks for best retrieval results.

For each chunk, you should provide a headline, a summary, and the original text of the chunk.
Together your chunks should represent the entire document with overlap.

Here is the document:

{document["text"]}

Respond with the chunks.
"""


def make_messages(document):
    return [
        {"role": "user", "content": make_prompt(document)},
    ]


@retry(wait=wait)
def process_document(document):
    messages = make_messages(document)
    response = completion(model=MODEL, extra_body={"reasoning_effort": "none"}, messages=messages, response_format=Chunks)
    reply = response.choices[0].message.content
    doc_as_chunks = Chunks.model_validate_json(reply).chunks
    return [chunk.as_result(document) for chunk in doc_as_chunks]


def create_chunks(documents):
    """
    Create chunks using a number of workers in parallel.
    If you get a rate limit error, set the WORKERS to 1.
    """
    chunks = []
    with Pool(processes=WORKERS) as pool:
        for result in tqdm(pool.imap_unordered(process_document, documents), total=len(documents)):
            chunks.extend(result)
    return chunks


def create_embeddings(chunks):
    chroma = PersistentClient(path=DB_NAME)
    if collection_name in [c.name for c in chroma.list_collections()]:
        chroma.delete_collection(collection_name)

    texts = [chunk.page_content for chunk in chunks]
    emb = openai.embeddings.create(model=embedding_model, input=texts).data
    vectors = [e.embedding for e in emb]

    collection = chroma.get_or_create_collection(collection_name)

    ids = [str(i) for i in range(len(chunks))]
    metas = [chunk.metadata for chunk in chunks]

    collection.add(ids=ids, embeddings=vectors, documents=texts, metadatas=metas)
    print(f"Vectorstore created with {collection.count()} documents")


if __name__ == "__main__":
    documents = fetch_documents()
    chunks = create_chunks(documents)
    create_embeddings(chunks)
    print("Ingestion complete")
```


---
