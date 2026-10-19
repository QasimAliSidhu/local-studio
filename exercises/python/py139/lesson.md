# Sort the tickets into departments

Group records with dict.items, setdefault and fresh lists.

## Give each group its own list

- **Choose a grouping key.** Each team becomes one key in the result dictionary.

- **Initialize only when needed.** `setdefault(key, [])` retrieves a group's list or creates one for a missing key.

- **Append in encounter order.** Use a separate list per group, preserve repeated IDs and leave source records unchanged.

## Walk through an example

```python
groups = {}
for team, job in [("ops", 7), ("web", 8), ("ops", 9)]:
    groups.setdefault(team, []).append(job)
# {"ops": [7, 9], "web": [8]}
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Grouping changes a flat collection into a mapping from group names to lists of members. Initialize a group only when you first encounter its key, then append each member. `setdefault(key, [])` can retrieve an existing list or install a new one for a missing key.

Every group must have its own list. Reusing one list for all keys makes every department see everyone else's tickets. Preserve encounter order within each group when the contract requires it. Iterating `.items()` later provides both each group key and its value.

Input records may be shared safely if the result only stores selected immutable values. If you return mutable records and later edit them, think again about ownership. This mission collects IDs, leaving the original records untouched. Pip created one department called 'miscellaneous' and assigned the entire company. It was efficient until payday.

</details>

## Before you run

What symptom would reveal that all groups accidentally share one list?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
