# Binary search

Find a target by repeatedly halving a sorted search interval.

## Keep shrinking a sorted interval

- **Inspect the middle.** Binary search requires sorted input to decide which half can still contain the target.

- **Move beyond the inspected position.** Each unsuccessful iteration must make the remaining interval smaller.

- **Stop when the interval is empty.** That means the target is absent; return the sentinel required by the task.

## Walk through an example

```python
values = [3, 8, 14, 21, 30]
left, right = 0, len(values) - 1
middle = (left + right) // 2
# values[middle] is 14
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

**Binary search** relies on sorted input. After inspecting the middle value, discard the half that cannot contain the target. Every unsuccessful iteration must make the remaining interval smaller.

> [!WARNING]
> Move a bound past the inspected middle position. Keeping the same middle can create an infinite loop.

</details>

## Before you run

What invariant describes the remaining search interval? When does an empty interval mean the target is absent?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
