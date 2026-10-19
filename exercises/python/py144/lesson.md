# Merge the tag clouds

Accumulate unique values from nested collections without aliasing.

## Build a union without borrowing storage

- **Start a fresh set for each call.** Reusing an input set would let updates change the caller's data.

- **Use `update(group)` for the members.** `add(value)` inserts a single value instead; a list itself is not hashable.

- **Preserve the stated spelling.** Collect exact values, including an empty string, without silently trimming or lowercasing them.

## Walk through an example

```python
all_tags = set()
for tags in [["api", "sql"], ["sql", "go"]]:
    all_tags.update(tags)
# {"api", "sql", "go"}
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A set can be updated with values from any iterable. `update(values)` adds each element, while `add(value)` inserts the argument itself. Adding a list fails because lists are unhashable; updating from a list of strings adds its string members.

Repeated updates build a union across many collections. Initialize a fresh accumulator inside the call so separate requests do not leak data. If inputs are sets, avoid using the first input as the accumulator unless mutation is explicitly allowed.

Normalize values according to the contract and discard values only when a rule says to. This mission keeps exact tag spellings, including an empty string; it does not silently trim or lowercase. Pip keeps tidying people's labels without asking. One team's 'US' tag became 'us', which changed the meeting agenda considerably.

</details>

## Before you run

What is the difference between result.add(group) and result.update(group)?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
