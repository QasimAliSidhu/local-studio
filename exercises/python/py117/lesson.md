# The off-by-one incident

Read a failing assertion and repair a boundary error.

## Test the boundary, then its neighbors

- **Translate the rule precisely.** One more person fits only while the current count is below capacity.

- **Distinguish `<` from `<=`.** Equality means the room is already full.

- **Try nearby cases.** Check just below capacity, exactly at capacity and a room with zero capacity.

## Walk through an example

```python
def within_budget(cost, budget):
    return cost <= budget

# An exact match is permitted.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A test compares observed behavior with an expected result. A failure is evidence about one input, not a verdict on your ability. Read the assertion and its input before changing code. If a boundary fails while ordinary cases pass, investigate the boundary rule rather than rewriting everything.

An inclusive upper bound uses `<=`; an exclusive upper bound uses `<`. Neither is universally correct. The contract decides. Test immediately below, exactly at, and immediately above a threshold to distinguish them.

The editor contains a plausible but wrong implementation. Use the failing cases to explain its mistake, fix the smallest rule, then run the whole suite. A passing example does not prove all inputs work. Pip filed this incident as 'one number being dramatic'. The incident manager would prefer a reproducible case.

</details>

## Before you run

Which single input best distinguishes < from <= here?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
