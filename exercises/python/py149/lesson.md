# Type hints are signs, not force fields

Annotate a function while implementing its runtime contract.

## Use annotations as documentation

- **Describe inputs and output.** `values: list[int]` and `-> float` express the expected types.

- **Handle the empty case before division.** `sum(values)` adds the numbers; `len(values)` counts them.

- **Keep validation separate.** Hints do not check runtime inputs automatically. Return the float required by this contract.

## Walk through an example

```python
def half(value: int) -> float:
    return value / 2

# A checker helps, but half("oops") can still be attempted at runtime.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Annotations describe the intended types of inputs and outputs: `def size(text: str) -> int`. Editors and static checkers can use them to catch mismatches before a program runs. Python itself does not enforce these annotations during an ordinary function call.

A collection hint such as `list[int]` describes both the container and its members. An empty list is still compatible with that hint. Write annotations to communicate the interface, and use explicit validation when the runtime boundary needs it.

Do not confuse a float return annotation with conversion: returning an int does not automatically turn it into a float. This exercise asks for a consistent result type, including the empty case. Pip installed a 'no bugs' sign on the server. It has had roughly the same enforcement power as a type hint without a checker.

The built-in `sum(values)` adds the numeric members of an iterable; for an empty list it returns zero. Guard the empty case before dividing by len(values), because a valid empty mean is a contract decision rather than a division by zero.

</details>

## Before you run

Would an annotation prevent a caller passing a list of strings at runtime?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
