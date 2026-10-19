# Invert carefully, the last one wins

Build a dictionary transformation and specify collision behavior.

## Decide what happens to collisions

- **Swap each key and value.** Iterating `.items()` gives both parts of an original dictionary entry.

- **Require hashable new keys.** Strings work as keys; mutable lists do not.

- **Name the collision rule.** A dictionary holds one value per key, so a later assignment replaces an earlier one when new keys collide.

## Walk through an example

```python
codes = {"first": "x", "second": "x"}
reverse = {value: key for key, value in codes.items()}
# {"x": "second"}
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A dictionary comprehension builds a mapping from a key expression and a value expression. Iterating `.items()` gives each original pair. Reversing key and value can be useful for lookup, but the original values may not be unique.

A dictionary can hold only one value per key. When multiple inputs produce the same new key, a later assignment replaces the earlier value. That is acceptable only when the contract deliberately chooses last-wins behavior. Otherwise you might reject duplicates or group several originals under one key.

The values used as new keys must be hashable. This mission restricts them to strings, so the key constraint is clear. Keep the source unchanged and let input insertion order decide which collision wins. Pip promised a reversible mapping without checking uniqueness. The lost keys are filing a support ticket.

</details>

## Before you run

What additional condition would make inversion fully reversible?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
