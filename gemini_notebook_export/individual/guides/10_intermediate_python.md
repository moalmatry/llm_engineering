# 10_intermediate_python.ipynb

> **Original Path:** `guides/10_intermediate_python.ipynb`

---

# Intermediate Level Python

## A briefing on more advanced features of Python

This section assumes you're up to speed on the foundations - and now we cover some important features of python that we use on the course.

1. Comprehensions  
2. Generators  
3. Sub-classes, Type Hints, Pydantic  
4. Decorators
5. Docker (not really python, but we use it to run python code!)

```python
# First let's create some things:

fruits = ["Apples", "Bananas", "Pears"]

book1 = {"title": "Great Expectations", "author": "Charles Dickens"}
book2 = {"title": "Bleak House", "author": "Charles Dickens"}
book3 = {"title": "An Book By No Author"}
book4 = {"title": "Moby Dick", "author": "Herman Melville"}

books = [book1, book2, book3, book4]
```

# Part 1: List and dict comprehensions

```python
# Simple enough to start

for fruit in fruits:
    print(fruit)
```

```python
# Let's make a new version of fruits

fruits_shouted = []
for fruit in fruits:
    fruits_shouted.append(fruit.upper())

fruits_shouted
```

```python
# You probably already know this
# There's a nice Python construct called "list comprehension" that does this:

fruits_shouted2 = [fruit.upper() for fruit in fruits]
fruits_shouted2
```

```python
# But you may not know that you can do this to create dictionaries, too:

fruit_mapping = {fruit: fruit.upper() for fruit in fruits}
fruit_mapping
```

```python
# you can also use the if statement to filter the results

fruits_with_longer_names_shouted = [fruit.upper() for fruit in fruits if len(fruit)>5]
fruits_with_longer_names_shouted
```

```python
fruit_mapping_unless_starts_with_a = {fruit: fruit.upper() for fruit in fruits if not fruit.startswith('A')}
fruit_mapping_unless_starts_with_a
```

```python
# Another comprehension

[book['title'] for book in books]
```

```python
# This code will fail with an error because one of our books doesn't have an author

[book['author'] for book in books]
```

```python
# But this will work, because get() returns None

[book.get('author') for book in books]
```

```python
# And this variation will filter out the None

[book.get('author') for book in books if book.get('author')]
```

```python
# And this version will convert it into a set, removing duplicates

set([book.get('author') for book in books if book.get('author')])
```

```python
# And finally, this version is even nicer
# curly braces creates a set, so this is a set comprehension

{book.get('author') for book in books if book.get('author')}
```

# Part 2: Generators

We use Generators in the course because AI models can stream back results.

If you've not used Generators before, please start with this excellent intro from ChatGPT:

https://chatgpt.com/share/672faa6e-7dd0-8012-aae5-44fc0d0ec218

Try pasting some of its examples into a cell.

```python
# First define a generator; it looks like a function, but it has yield instead of return

import time

def come_up_with_fruit_names():
    for fruit in fruits:
        time.sleep(1) # thinking of a fruit
        yield fruit
```

```python
# Then use it

for fruit in come_up_with_fruit_names():
    print(fruit)
```

```python
# Here's another one

def authors_generator():
    for book in books:
        if book.get("author"):
            yield book.get("author")
```

```python
# Use it

for author in authors_generator():
    print(author)
```

```python
# Here's the same thing written with list comprehension

def authors_generator():
    for author in [book.get("author") for book in books if book.get("author")]:
        yield author
```

```python
# Use it

for author in authors_generator():
    print(author)
```

```python
# Here's a nice shortcut
# You can use "yield from" to yield each item of an iterable

def authors_generator():
    yield from [book.get("author") for book in books if book.get("author")]
```

```python
# Use it

for author in authors_generator():
    print(author)
```

```python
# And finally - we can replace the list comprehension with a set comprehension

def unique_authors_generator():
    yield from {book.get("author") for book in books if book.get("author")}
```

```python
# Use it

for author in unique_authors_generator():
    print(author)
```

```python
# And for some fun - press the stop button in the toolbar when bored!
# It's like we've made our own Large Language Model... although not particularly large..
# See if you understand why it prints a letter at a time, instead of a word at a time. If you're unsure, try removing the keyword "from" everywhere in the code.

import random
import time

pronouns = ["I", "You", "We", "They"]
verbs = ["eat", "detest", "bathe in", "deny the existence of", "resent", "pontificate about", "juggle", "impersonate", "worship", "misplace", "conspire with", "philosophize about", "tap dance on", "dramatically renounce", "secretly collect"]
adjectives = ["turqoise", "smelly", "arrogant", "festering", "pleasing", "whimsical", "disheveled", "pretentious", "wobbly", "melodramatic", "pompous", "fluorescent", "bewildered", "suspicious", "overripe"]
nouns = ["turnips", "rodents", "eels", "walruses", "kumquats", "monocles", "spreadsheets", "bagpipes", "wombats", "accordions", "mustaches", "calculators", "jellyfish", "thermostats"]

def infinite_random_sentences():
    while True:
        yield from random.choice(pronouns)
        yield " "
        yield from random.choice(verbs)
        yield " "
        yield from random.choice(adjectives)
        yield " "
        yield from random.choice(nouns)
        yield ". "

for letter in infinite_random_sentences():
    print(letter, end="", flush=True)
    time.sleep(0.02)
```

# Exercise

Write some python classes for the books example.

Write a Book class with a title and author. Include a method has_author()

Write a BookShelf class with a list of books. Include a generator method unique_authors()

# Part 3: Sub-classes, Type Hints, Pydantic

Here are some intermediate level details of Classes from our AI friend, including use of type hints, inheritance and class methods. This includes a Book example.

https://chatgpt.com/share/67348aca-65fc-8012-a4a9-fd1b8f04ba59

And here is a comprehensive tutorial on Pydantic classes covering everything you need to know about Pydantic.

https://chatgpt.com/share/68064537-6cfc-8012-93e1-f7dd0932f321

## Part 4: Decorators

Here is a briefing, with an example from OpenAI Agents SDK:

https://chatgpt.com/share/6806474d-3880-8012-b2a2-87b3ee4489da

## Part 5: Docker

Here is a convenient tutorial to introduce Docker.

In the last section, this also covers an answer to a question in Week 6 - what does it mean to run an MCP server in Docker? But you can ignore this question if you're not on week 6 yet.

https://chatgpt.com/share/6814bc1d-2f3c-8012-9b18-dddc82ea421b

```python
# You need to install docker to run this example
# This will download the Docker image for python 3.12, create a container,
# Run some python code and print the result

!docker run --rm python:3.12 python -c "print(2 + 2)"
```
