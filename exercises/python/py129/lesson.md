# Repeat responsibly

Use range and an accumulator with correct inclusive bounds.

## Repeat a small, clear update

- **Loop with `for`.** `range(start, stop)` supplies integers up to, but excluding, `stop`.

- **Start an accumulator at zero.** Add each value to the running total.

- **Match the endpoints.** Include `n` when the contract says “through n”; no iterations should still leave a valid total.

## Walk through an example

```python
total = 0
for number in range(1, 4):
    total += number
# 1 + 2 + 3 == 6
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A `for` loop takes one value at a time from an iterable. `range(stop)` generates integers from zero up to, but excluding, stop. `range(start, stop)` lets you choose the beginning. The exclusive stop is a common source of off-by-one bugs.

An accumulator stores a partial result. Initialize it before the loop, update it inside, and return it after all iterations. Initializing inside the loop throws away earlier work; returning inside the loop stops after the first item.

Empty iteration is a real case, not an error. Choose an initial value that already represents the empty result, such as zero for a sum or an empty list for collected values. Pip was told to repeat a task five times and counted zero through five. The team appreciates the enthusiasm, but the invoice does not.

</details>

## Before you run

What result would you get if return were indented inside the loop?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
