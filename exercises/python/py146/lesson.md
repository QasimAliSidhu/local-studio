# Catch the error you expect

Handle selected conversion failures without masking unrelated bugs.

## Catch only the expected conversion errors

- **Try the conversion.** `int(raw)` accepts valid integer text, including permitted whitespace and a sign.

- **Catch the relevant failures.** `ValueError` covers malformed text; `TypeError` covers an unsupported input such as `None`.

- **Preserve valid zero.** Return the converted integer on success, rather than treating a falsy result as a failure.

## Walk through an example

```python
try:
    value = int(raw)
except (ValueError, TypeError):
    value = None
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A `try` block contains work that may raise an exception. A matching `except` block handles a specific kind of failure; code after the handler can continue. Catching `Exception` around a large function may hide unrelated programming mistakes and make debugging harder.

Put the smallest relevant operation in the try block. `int(text)` raises ValueError for malformed numeric text and TypeError for an unsuitable object such as None. This contract accepts strings or None, so both conversion errors have defined fallback behavior.

Handling an error should leave a result with a clear meaning. A fallback of None signals that parsing failed; zero remains a successful value. In a user-facing API you might instead return structured error information. Pip used to catch every error and return 'all good'. Monitoring briefly became very cheerful and entirely wrong.

</details>

## Before you run

What kind of bug could a broad except around a whole request handler conceal?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
