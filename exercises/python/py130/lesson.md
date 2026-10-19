# While the queue is still awake

Maintain a while-loop invariant and guarantee progress.

## Make progress on every pass

- **Use `while` for a changing condition.** Repeat while work remains.

- **Update both pieces of state.** Track how many batches ran and how much work is left.

- **Stop at zero.** `max(0, remaining - capacity)` avoids negative remaining work. A positive capacity makes progress possible.

## Walk through an example

```python
remaining = 8
batches = 0
while remaining > 0:
    remaining = max(0, remaining - 3)
    batches += 1
# batches is 3
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A `while` loop repeats while its condition is truthy. Unlike a for loop over a fixed range, it needs you to update the state that eventually makes the condition false. If no progress occurs, the loop may run forever.

State an invariant: a fact that remains true before and after each iteration. Here remaining work never becomes negative, and processed work plus remaining work always equals the starting workload. Each iteration removes at most the capacity of one batch.

Check termination before coding: for positive capacity, each iteration reduces positive remaining work. Zero workload therefore runs the body zero times. The runner can stop a hung program, but the goal is to understand why termination follows from your rule. Pip's retry loop had no stop condition. It is still optimistic about a printer disconnected in 2019.

The built-in `max(left, right)` returns the larger value. Using max(0, remaining - capacity) prevents the remaining count from going below zero when a final batch has spare room.

</details>

## Before you run

What would happen if capacity were zero and we did not validate it?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
