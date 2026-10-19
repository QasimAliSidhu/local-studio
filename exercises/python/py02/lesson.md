# Count API responses

Count how often each status code appears.

## Count one occurrence at a time

- **Start with an empty dictionary.** Each status code will be a key and its count will be the value.

- **Use zero for a new key.** `counts.get(code, 0)` provides the count before the next increment.

- **Keep the accumulator across the loop.** Initialize once per call, then update for every input occurrence.

## Walk through an example

```python
counts = {}
for event in ["read", "write", "read"]:
    counts[event] = counts.get(event, 0) + 1
# {"read": 2, "write": 1}
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A dictionary maps a **key** to its current **count**. The first time a key appears, its count starts at zero. Each later occurrence updates that same entry.

> [!WARNING]
> Do not reset the whole dictionary inside the loop. Keep the accumulated counts across iterations.

</details>

## Before you run

Can your loop handle a key it has never seen before? What should an empty input return?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
