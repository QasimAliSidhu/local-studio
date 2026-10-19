# A dictionary is not a tiny list

Use keys, membership and get without confusing absence with None.

## Look up by key

- **Write `{key: value}` pairs.** A dictionary maps keys to values; lookup is by key, not position.

- **Check membership with `key in mapping`.** A present value of `None`, zero or `False` is still present.

- **Choose the right view.** `.keys()`, `.values()` and `.items()` supply keys, values and pairs. `.get()` can supply a default for a missing key.

## Walk through an example

```python
settings = {"timeout": None}
print("timeout" in settings)  # True
print(settings.get("retries", 3))  # 3
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A dictionary maps keys to values. `mapping[key]` retrieves a value and raises KeyError when the key is missing. `mapping.get(key, default)` supplies a default instead. `key in mapping` tests keys, not values.

Missing keys and present keys whose value is None are distinct states. `get` without a default cannot distinguish them by itself. If your rule treats a present None as meaningful, test membership before choosing a fallback. Keys must be hashable; immutable strings and integers are common choices, while mutable lists cannot be keys.

Dictionaries preserve insertion order, but lookup is by key rather than a positional index. A numeric key is still a key, not a request for the nth item. Pip stored the Wi-Fi password under key 'somewhere'. It is technically a mapping; the naming review is ongoing.

A dictionary literal uses `{key: value}` pairs, separated by commas. The colon connects a key to its value. `mapping.keys()` provides the keys, `mapping.values()` the values, and `mapping.items()` the key/value pairs. Choose the view that matches the question you are answering.

</details>

## Before you run

Why would settings.get(key) or fallback violate this contract?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
