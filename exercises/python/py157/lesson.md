# Checkpoint: aliases under pressure

Apply copying rules to a nested update without a recipe.

## Reason about both container layers

- **Identify the caller-owned objects.** The audit record and its nested events list must stay unchanged.

- **Copy the containers you will edit.** A fresh outer record alone still leaves a shared events list.

- **Keep unrelated fields and repeated events.** Add only the requested event without inventing cleanup or uniqueness rules.

## Walk through an example

```python
original = {"events": ["open"], "id": 4}
# A safe transformation returns a new dict and a new events list.
# Assigning a new name alone does not copy either container.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Checkpoints combine familiar concepts with less scaffolding. Before coding, identify which objects the caller still owns, which containers need independent copies, and which values can safely remain shared. Draw arrows between names and objects if the references feel confusing.

This update changes a nested list inside one record. A fresh outer dictionary is necessary but not sufficient; the selected list also needs to be independent. Other immutable fields can be preserved as they are.

Empty input collections should still produce valid results. Avoid a mutable default or hidden global accumulator, or a later call can inherit earlier work. Explain why your result is independent before revealing the reference solution. Pip has offered to label every object 'mine'. Ownership in Python requires slightly more precision.

</details>

## Before you run

Which nested objects could still be shared safely under this specific contract?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
