# Functions that take functions

Pass callbacks and apply a transformation pipeline in order.

## Pass each result to the next step

- **Functions can be inputs.** Each supplied step accepts one current value.

- **Apply steps in order.** Feed each returned result into the next operation.

- **Keep an empty pipeline valid.** With no steps, the original value is already the result. Exceptions should propagate.

## Walk through an example

```python
steps = [lambda n: n + 2, lambda n: n * 3]
value = 4
for step in steps:
    value = step(value)
# (4 + 2) * 3 == 18
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Functions are values: you can store them in variables, put them in a list and pass them as arguments. A higher-order function takes a function or returns one. Call a callback when you need its result; merely referring to it does not execute it.

A pipeline passes the result of one stage into the next. Stage order matters: multiplying then adding differs from adding then multiplying. An empty pipeline leaves its input unchanged, which is a useful identity behavior.

`map` and `filter` are familiar higher-order tools, but a clear loop can express a pipeline without obscuring control flow. Let exceptions propagate unless the pipeline contract defines a recovery strategy; otherwise a failing stage should not produce a falsely successful result. Pip arranged the pipeline alphabetically. The mathematics declined to cooperate.

</details>

## Before you run

Why is passing a function name different from passing a call like function(value)?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
