# One domain, one invitation

Use a set to collect unique normalized values.

## Keep only unique values

- **Create a set with `set()`.** A set stores unique hashable values; `{}` creates a dictionary instead.

- **Normalize before deduplicating.** Equivalent domains should have the same lowercase spelling before they enter the set.

- **Do not depend on set order.** Use membership to ask whether a value exists; sets have no positional index.

## Walk through an example

```python
domains = set()
for address in ["a@Example.org", "b@example.org"]:
    domains.add(address.split("@", 1)[1].lower())
# {"example.org"}
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A set stores unique hashable values. Adding an existing value leaves the set unchanged. `value in seen` expresses membership without making ordering promises. Create an empty set with `set()`; `{}` creates an empty dictionary.

Normalization should happen before deduplication when values differing only by a permitted variation count as equivalent. Here domain names are case-insensitive for our simplified input, while local parts of addresses are irrelevant to the requested result.

Sets deliberately discard duplicates and do not provide positional indexing. If you need a stable order, keep an additional list or sort the result according to an explicit rule. Do not rely on the order you happen to see during one run. Pip invited the same company seventeen times because the capital letters kept changing. Catering has requested a set.

</details>

## Before you run

Why does deduplicating before normalizing miss some equivalents?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
