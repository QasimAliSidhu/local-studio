# Reject nonsense at the boundary

Raise a specific exception for an invalid domain value.

## Reject an invalid value clearly

- **Check the type first.** A boolean is an `int` subclass in Python, but this contract rejects it explicitly.

- **Check the allowed range next.** Distinguish a wrong kind of input from an integer outside the accepted limits.

- **Raise an informative exception.** Use `TypeError` or `ValueError` as requested, with a message identifying the port.

## Walk through an example

```python
def positive(value):
    if value <= 0:
        raise ValueError("value must be positive")
    return value
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An exception interrupts normal control flow and travels outward until matching handling is found. `raise ValueError("message")` reports that an argument has an unacceptable value. A useful message states the violated rule rather than blaming the caller.

Validate before performing work that would produce an invalid result. Differentiate type errors from range errors when the contract requires it. In Python, bool is a subclass of int, so a naive integer check can accept True as one; explicit type rules matter at interfaces.

A function should not silently clamp or guess unless that behavior is specified. Rejecting an invalid port is safer than turning it into a different port behind the caller's back. Exceptions are not failures of learning; they are part of expressing the contract. Pip's parser accepts 'roughly twelve'. The network stack does not.

</details>

## Before you run

Why is isinstance(True, int) an important surprise for validation?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
