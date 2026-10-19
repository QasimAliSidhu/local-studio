# Typed task records

Validate incoming values and construct a clean task record.

## Build a clean record at the boundary

- **Validate the title as text.** Strip its outer whitespace and reject an empty result.

- **Validate a boolean as a boolean.** `bool("false")` is `True`; coercion cannot replace this type check.

- **Create a fresh, exact shape.** Keep only `title` and `done`, defaulting an absent `done` to `False`. Type hints describe this shape without enforcing it.

## Walk through an example

```python
def require_title(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("Title must be text")
    title = value.strip()
    if not title:
        raise ValueError("Title is required")
    return title
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A type annotation documents an expected shape, but it does **not validate runtime input**. Check the values you received before constructing a clean record for the rest of your application.

> [!WARNING]
> Do not use bool(value) as a substitute for validating a boolean. The string "false" is truthy.

</details>

## Before you run

Which fields may be normalized, and which must already have the correct type?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
