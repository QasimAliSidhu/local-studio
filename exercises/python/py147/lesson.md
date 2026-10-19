# Always put the mop away

Use finally for cleanup on success and failure.

## Guarantee cleanup

- **Put the operation in `try`.** Read and keep its result normally.

- **Put cleanup in `finally`.** That block runs when the read succeeds and when it raises an exception.

- **Let the original error continue.** Cleanup should not invent a success result or hide the failure.

## Walk through an example

```python
try:
    result = resource.read()
    return result
finally:
    resource.close()
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A `finally` block runs when control leaves its try statement, including after a successful return or an exception. This makes it suitable for cleanup that must happen regardless of the operation's result. It does not mean you should catch and suppress the original exception.

Keep cleanup small and reliable. A return or a new exception inside finally can replace the original result or error, which is often an unpleasant surprise. Context managers, introduced with `with`, package acquisition and cleanup into reusable operations; file objects already support them.

This mission uses a supplied resource object so you can observe the protocol without opening a real connection. Call its work method, propagate its result or failure, and close exactly once. Pip washed the mop only on successful cleaning days. The cupboard has requested a finally clause.

</details>

## Before you run

How could a return statement inside finally accidentally hide an error?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
