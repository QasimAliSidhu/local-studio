# Positions and pairs without manual counters

Use enumerate and zip after ordinary loops are familiar.

## Let Python supply positions and pairs

- **Use `enumerate` for positions.** `enumerate(names, start=1)` produces `(position, name)` pairs starting at one.

- **Unpack in the loop.** The two names receive the position and its corresponding value.

- **Use `zip` for corresponding inputs.** It pairs values and normally stops at the shorter input; `strict=True` can report unequal lengths.

## Walk through an example

```python
pairs = []
for name, seconds in zip(["email", "backup"], [2, 5]):
    pairs.append((name, seconds))
# [("email", 2), ("backup", 5)]
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

`enumerate(values, start=1)` supplies a position alongside each value. A for loop can unpack each pair into two names. This removes the need to initialize and increment your own counter. Choose whether positions start at zero or one according to the contract.

`zip(left, right)` pairs corresponding values from two iterables. Normally it stops when the shorter input ends. When equal lengths are a requirement, `zip(..., strict=True)` can report a mismatch rather than silently dropping unmatched values.

The example pairs each job name with a duration and then collects those pairs into a list. We will keep equal-length inputs here. You already know loops, tuples and list append, so the new idea is which values these two tools provide.

Order still matters. Do not sort a collection when its original correspondence is meaningful. Pip paired the newest invoice with the oldest customer because both looked lonely. Corresponding positions are a better rule.

</details>

## Before you run

Why can zip silently lose an unmatched last item?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
