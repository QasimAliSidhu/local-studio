# A record with a declared shape

Use TypedDict as documentation while constructing a fresh record.

## Describe a dictionary's shape

- **Use `TypedDict` for named fields.** It documents the expected key names and value types.

- **Keep runtime behavior in mind.** The result is an ordinary dictionary; the declaration does not validate its contents automatically.

- **Construct the promised shape.** Return a fresh dictionary with exactly the declared fields and preserve values the contract says to keep.

## Walk through an example

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    active: bool

def new_user(name: str) -> User:
    return {"name": name, "active": True}
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

TypedDict describes expected dictionary keys and their value types for static analysis. At runtime its instances are ordinary dictionaries. It does not automatically validate an incoming JSON object or supply missing fields.

Named fields are clearer than a long tuple when callers need to remember several meanings. A declaration like `class Ticket(TypedDict): id: int` helps tools and people understand the shape. You still construct the dictionary and perform any required validation yourself.

Separate a trusted constructor from an untrusted parser when useful. This mission receives valid inputs and builds a known shape; an earlier validation exercise handles hostile values. Returning a fresh record prevents one caller's later edits from changing another call's result. Pip's schema was a sticky note saying 'dictionary probably'. We have upgraded the sticky note.

</details>

## Before you run

Why must a JSON request still be validated even if you annotate it as Ticket?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
