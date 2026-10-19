# Deduplicate job IDs

Remove duplicate IDs while preserving their first-seen order.

## Remember membership and order separately

- **Use a set for “seen before?”.** Membership tells you whether this value has already appeared.

- **Use a list for the result.** Append only the first occurrence, in its original position relative to the other first occurrences.

- **Keep case significant.** Distinct strings stay distinct; converting straight to a set would not express first-seen order.

## Walk through an example

```python
seen = set()
ordered = []
for tag in ["api", "db", "api"]:
    if tag not in seen:
        seen.add(tag)
        ordered.append(tag)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **set** answers whether a value has appeared before. A **list** preserves the order you choose. Combining them lets you keep the first occurrence of each value without sorting the input.

> [!WARNING]
> Converting directly to a set removes duplicates but does not express the required first-seen order.

</details>

## Before you run

Which operation records that an item has been seen? Which operation preserves its original position?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
