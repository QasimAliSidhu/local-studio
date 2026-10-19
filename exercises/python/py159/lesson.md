# Checkpoint: reshape the response

Select, filter and order records using several core tools.

## Filter and order as separate rules

- **Select only the requested records.** Read the boolean `done` field rather than guessing from a title or ID.

- **Sort by the numeric ID.** `sorted` returns a new list; `.sort()` changes an existing list and returns `None`.

- **Construct the output strings.** Preserve legitimate zero IDs and empty titles, and keep the original records untouched.

## Walk through an example

```python
records = [{"id":2,"name":"B"},{"id":1,"name":"A"}]
ordered = sorted(records, key=lambda record: record["id"])
# sorted creates a new list; it does not reorder records.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Data shaping is a common boundary task: the storage record may contain more fields than a response should expose. Choose the fields deliberately instead of returning every input field by accident. This exercise constructs strings rather than a public API, but the habit transfers.

Filtering and ordering are independent rules. First decide which records qualify, then ensure the output order matches the contract. Python's `sorted` returns a new list, while a list's `.sort()` mutates it and returns None. A `key` callback tells sorting which value to compare.

Preserve zero IDs and empty titles unless the rule excludes them. Being thorough means testing these boundaries, not adding guesses about nicer behavior. Pip sorted by title length because longer titles seemed more senior. The product team has supplied a less creative ordering rule.

</details>

## Before you run

Why would tickets.sort(...) violate this function's contract?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
