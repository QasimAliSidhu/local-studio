# Unpack inputs without guessing the signature

Use * and ** to pass tuple and dictionary arguments.

## Forward the caller's arguments

- **Unpack positional inputs with `*args`.** In a call, the tuple's members become separate positional arguments.

- **Unpack named inputs with `**kwargs`.** Its entries become keyword arguments.

- **Return the operation's outcome.** Forward once, preserve the argument containers and let failures propagate.

## Walk through an example

```python
def add(left, right=0):
    return left + right

args = (3,)
kwargs = {"right":4}
print(add(*args, **kwargs))
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A call can unpack positional arguments from an iterable with `*args` and keyword arguments from a mapping with `**kwargs`. Here the stars are call syntax, not multiplication or exponentiation. The argument container types and position make the meaning clear.

The matching function-definition forms collect extra arguments: `def wrapper(*args, **kwargs)` receives a tuple of positional values and a dictionary of keyword values. Those names are conventions, not mandatory spellings. This is useful when a wrapper should forward a call without knowing every parameter in advance.

In the example, the tuple supplies the first argument and the dictionary supplies a named argument. The receiving function still applies its normal signature rules; unpacking does not make invalid arguments valid.

Keep the forwarded call exact, including empty containers. The next lesson uses this to wrap a function with extra behavior. Pip forwards every request with an extra biscuit parameter. Most interfaces do not accept it.

</details>

## Before you run

How is *args inside a call different from *args in a definition?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
