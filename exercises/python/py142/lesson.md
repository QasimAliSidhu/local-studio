# Who is on both shifts?

Use union, intersection and difference for collection comparison.

## Compare the two collections

- **Union `|` means either set.** Intersection `&` means both sets.

- **Difference `-` has a direction.** `after - before` finds additions; `before - after` finds removals.

- **Choose new results.** These operators create sets without modifying the original inputs; duplicates have no effect on membership.

## Walk through an example

```python
before, after = {"a", "b"}, {"b", "c"}
added = after - before
removed = before - after
stayed = before & after
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Set union (`|`) includes values from either collection. Intersection (`&`) keeps values in both. Difference (`-`) keeps values in the left collection that are absent from the right. Difference is directional: `before - after` and `after - before` answer different questions.

These operators create new sets rather than changing their operands. In-place forms such as `|=` can mutate a set, so choose intentionally. Convert an input list to a set when uniqueness is the desired meaning and duplicates should not count.

Comparing snapshots is a common backend task: what was added, what disappeared, and what stayed? A precise result shape prevents a caller from mixing up the directions. Pip reports every roster change as 'someone is somewhere'. We are replacing that with three named categories.

</details>

## Before you run

Which operation would give every person appearing in either roster?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
