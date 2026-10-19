# Two input types, one honest boundary

Narrow union inputs and validate beyond annotations.

## Convert at an honest boundary

- **State both accepted types.** `int | str` documents the input choices, but runtime checks are still your job.

- **Reject bool explicitly.** Being an `int` subclass does not make a boolean an accepted ID here.

- **Convert, then validate the result.** Malformed text and a negative integer violate the contract for different reasons from an unsupported type.

## Walk through an example

```python
def nonnegative(value: int | str) -> int:
    if isinstance(value, bool):
        raise TypeError("bool is not an ID")
    number = int(value)
    if number < 0:
        raise ValueError("negative ID")
    return number
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A parameter annotated `int | str` accepts two intended representations. The implementation must decide how each representation becomes the promised output. `isinstance` can narrow a branch, but remember that bool is an int subclass when validating identifiers.

Type hints do not encode every business rule. A string annotation says nothing about whether the string is empty, contains only digits, or fits a numeric range. Those rules belong in runtime validation and documentation.

Converting first and validating later can accidentally accept values you did not intend, such as a float truncated by int(). Preserve a clear boundary: reject unsupported types, parse supported text, then validate the parsed value. Pip's ID system accepts anything with 'number energy'. The database has no matching column type.

</details>

## Before you run

Why is int(1.9) dangerous when the contract does not accept floats?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
