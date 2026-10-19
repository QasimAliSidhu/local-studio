# Wrap a function without changing its job

Combine closures and forwarding to build a decorator.

## Wrap a function carefully

- **Return a wrapper from the decorator.** `@decorate` is shorthand for replacing a function with `decorate(function)`.

- **Forward and return the original call.** Use `*args` and `**kwargs`, call once and preserve the return value or exception.

- **Keep metadata with `functools.wraps`.** Record the call before invoking the original so failed calls are logged too.

## Walk through an example

```python
from functools import wraps

def announce_calls(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        print("calling")
        return operation(*args, **kwargs)
    return wrapped
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **decorator** takes a function and returns a replacement function with additional behavior. The original calculation can remain focused on its own job while the wrapper adds logging, measurement or validation. This builds on callbacks, closures and argument forwarding you have already practiced.

In `@decorate` above a function definition, Python applies the decorator and binds the resulting callable to that function's name. It is shorthand for `function = decorate(function)`. A wrapper usually accepts *args and **kwargs so it can forward the original call.

`functools.wraps(original)` copies useful metadata such as __name__ onto the wrapper. It does not execute the original function. Append the log entry once, call the original once, and return its result; losing the return value is a common wrapper bug.

We are writing a small logging decorator, not a production logging framework. Avoid recording secrets in real call logs. Pip logs that it is logging the logging function. Your wrapper should be less enthusiastic.

</details>

## Before you run

Why must the wrapper return the original function's result?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
