# Pass a tool without running it yet

Use a function as a value before callbacks, lambdas or pipelines.

## Pass a function as a value

- **Pass the tool without calling it yet.** `operation` refers to the function; `operation(value)` calls it.

- **Let the caller choose the behavior.** Your helper should use the supplied operation instead of guessing a replacement.

- **Preserve the outcome.** Call once, return its result unchanged and let an exception reach the caller.

## Walk through an example

```python
def double(number):
    return number * 2

def apply_once(value, operation):
    return operation(value)

print(apply_once(4, double))
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A function is a value you can pass to another function. Writing its name refers to the tool; adding parentheses calls it. In `apply_once(4, double)`, double is supplied for later use. In `double(4)`, it runs now and produces a result.

A function received for the caller to invoke is often called a **callback**. The receiving function can use any suitable callable rather than hardcoding one particular operation. Its contract must say which inputs it will pass and how often it will call the tool.

In the example, apply_once gets the number four and a reference to double. It calls double with four and returns eight. A different supplied operation can reuse the same wrapper. No new anonymous-function syntax is needed yet.

Do not silently call a callback twice or discard its returned value. Side effects and expensive operations would then happen twice too. Pip repeatedly presses the doorbell to confirm the doorbell works. Our contract says once.

</details>

## Before you run

Why is passing double different from passing double(4)?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
