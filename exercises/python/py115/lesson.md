# The haunted default argument

Avoid shared mutable defaults across function calls.

## Avoid a shared default list

- **Defaults are created when a function is defined.** A list used as a default can survive across calls.

- **Use `None` to mean omitted.** Initialize fresh work inside the function instead.

- **Copy a supplied list too.** A fresh result protects caller-owned data and keeps separate calls independent.

## Walk through an example

```python
def add_note(note, notes=None):
    result = [] if notes is None else list(notes)
    result.append(note)
    return result
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Default argument expressions are evaluated when a function is defined, not once per call. A default like `items=[]` therefore creates one list that later calls can share. Appending into it makes a supposedly fresh call remember earlier visitors. This is a real source of bugs, even though the syntax looks friendly.

Use an immutable sentinel such as `None`, then create a new list when the caller omits the value. Also decide whether a caller-provided list should be changed. Those are separate contract choices: avoiding a shared default does not automatically make a function non-mutating.

Here the contract requests a new result every time. Copy an incoming list before appending, and use an empty list only for a missing argument. An explicitly empty list is still the caller's object. Pip has declared the shared default haunted. We have declared it a lifetime problem.

</details>

## Before you run

When is [] created in def f(items=[]), and why does that matter?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
