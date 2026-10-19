# The bug that only happens twice

Detect accidental shared state by calling a function repeatedly.

## Look for state left behind

- **Try two calls in the same process.** A shared-state bug can be invisible on the first call.

- **Initialize per-call totals locally.** Each request needs a fresh accumulator.

- **Remove the global write.** `global AUDIT_TOTAL` directs assignment to module state; this calculation must leave that state unchanged.

## Walk through an example

```python
def total_lengths(words):
    total = 0  # new for every call
    for word in words:
        total += len(word)
    return total
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Some bugs depend on history. A function may work once and fail on a second call because it changed module state or a shared input. To reproduce this, test a sequence of calls in one process rather than restarting after every example.

A pure calculation uses its arguments and returns its result without leaving changes behind. If a running total is only needed for one call, initialize it inside that call. A cache or counter can intentionally retain state, but its contract should say so.

Diagnose the lifetime of each variable: per iteration, per call, per object, or per process. That question often explains a mysterious growing answer. The starter below accumulates into a global total; the repair is about state ownership, not adding a reset button elsewhere. Pip suggested restarting the server after each invoice. We are going to try a smaller fix.

In the buggy starter, `global AUDIT_TOTAL` explicitly directs assignments to the module-level name. That is precisely the shared state we do not want for this per-request sum. Remove the global write and initialize a local total inside each call.

</details>

## Before you run

Why might this bug disappear when each manual check uses a fresh process?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
