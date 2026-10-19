# Look before you index

Use short-circuit evaluation to guard an operation.

## Guard before reading a character

- **Check the input first.** `None` and an empty string have no first character to inspect.

- **Use short-circuit evaluation.** With `and`, Python skips the right side when the left side is false.

- **Return a boolean.** `and` can return an operand rather than a literal bool, so make the function's result match its contract.

## Walk through an example

```python
has_letter = bool(text and text[0].isalpha())
# The index operation is skipped for empty text.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Python evaluates logical `and` from left to right and stops as soon as a falsy operand decides the result. With `or`, it stops at the first truthy operand. This is short-circuit evaluation, and it can prevent unsafe work rather than merely save time.

For a possibly missing string, test its existence before calling a string method or indexing it. Reversing the order can produce an error before the guard is reached. An empty string has no first character; `None` has no string methods.

Because logical operators return operands, `text and ...` can return the empty string or None. If the public contract promises a boolean, wrap the combined expression in `bool` or use clear branches. Pip installed a warning sign after the trapdoor. Your guard must come before the risky operation.

</details>

## Before you run

Why does text[0] == "/" and text fail for an empty string?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
