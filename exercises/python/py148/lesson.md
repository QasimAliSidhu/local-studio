# Give the error a useful name

Define and raise a custom exception while retaining ordinary validation.

## Give a specific failure a name

- **Subclass a suitable exception.** `InsufficientFunds` is a specialized `ValueError` that callers can catch separately.

- **Validate the amount first.** A negative withdrawal is a different invalid request from one exceeding the balance.

- **Return only on success.** A valid withdrawal returns the new balance; a failure raises its specified error.

## Walk through an example

```python
class LimitExceeded(ValueError):
    pass

def check(value, limit):
    if value > limit:
        raise LimitExceeded("limit exceeded")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A custom exception is a class that inherits from Exception or an appropriate existing exception type. It lets callers distinguish a domain problem from unrelated failures without parsing a message string. A descriptive message still helps the human reading a traceback.

Exception type and message have different jobs. The type supports programmatic handling; the message describes this particular violation. Subclassing ValueError makes the error catchable either specifically or as a broader invalid-value problem.

Do not catch your custom exception in the same function merely to return an ambiguous default. Let the caller decide how to recover. Here invalid amounts differ from insufficient funds, so tests expect two distinct errors. Pip named every exception Oops. It saved keystrokes and cost everyone else an afternoon.

</details>

## Before you run

Why should a caller catch InsufficientFunds instead of searching an error message for words?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
