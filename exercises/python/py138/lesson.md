# Update the record, spare the original

Merge dictionaries and deliberately copy nested mutable data.

## Merge without changing the inputs

- **Create a fresh dictionary.** `{**base, **changes}` expands the entries into a new outer mapping.

- **Let later entries win.** A key present in `changes` replaces the corresponding value, even when the new value is `None`.

- **Know the copy depth.** This is a shallow merge: nested objects remain shared unless you copy them separately.

## Walk through an example

```python
base = {"name": "Mira", "active": True}
updated = {**base, **{"active": False}}
# base stays active; updated is inactive.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Assigning `record[key] = value` inserts or replaces one entry. `update(other)` applies entries from another mapping and mutates the target. `{**base, **changes}` creates a new dictionary in which later entries win. These are shallow operations.

A patch is not the same as a replacement record. Fields absent from the patch normally remain, while present fields override even when their values are empty or None. Here we explicitly allow that override; another API might use None to mean deletion, but it would need to say so.

Avoid changing caller-owned dictionaries while preparing a request. The input may be reused for a retry or comparison. Values nested inside the record remain shared unless the contract requests deeper copying. Pip updated a profile by deleting every unspecified field. The profile is now admirably minimalist and entirely unusable.

In a dictionary display, `**mapping` expands all key/value pairs from that mapping. This is not exponentiation: it appears where dictionary entries belong. Later entries replace earlier entries with the same key.

</details>

## Before you run

Would a shallow merge make a nested list independent?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
