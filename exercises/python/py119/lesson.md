# Breadcrumbs in the console

Trace intermediate state while preserving a useful return value.

## Trace an update without losing its result

- **Predict a tiny example first.** Work out how the total changes after each input.

- **Print an identifiable trace.** A label such as `total=N` explains which value you are observing.

- **Return the final answer separately.** An empty input has no updates to print but still has a numeric total.

## Walk through an example

```python
total = 0
for amount in [3, 2]:
    total += amount
    print(f"total={total}")
# total=3, then total=5
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A trace records how state changes during execution. When a total is wrong, observing the total after each input can reveal the first step that diverges from your prediction. Start with a tiny example and predict the trace by hand before running it.

Use messages that identify the values you need. A hundred anonymous numbers can be less useful than three labeled observations. Remove temporary noisy tracing when the investigation ends, or use deliberate logging appropriate to the application. Never log secrets just because the console is convenient.

Tracing is an observation, not the returned result. A function can print diagnostics and still return a numeric answer. Here the output itself is part of the exercise contract so tests can verify your reasoning. Pip left breadcrumb logs in production. Unfortunately, they were all labeled 'breadcrumb'.

</details>

## Before you run

What trace would reveal that a print call was accidentally placed before the addition?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
