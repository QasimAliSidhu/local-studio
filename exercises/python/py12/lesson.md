# Cache expiry

Keep cached values valid only until their expiry time.

## Store a value with its deadline

- **Calculate expiry from the supplied clock.** A deadline is `now + ttl`, which keeps time-dependent tests predictable.

- **Compare time explicitly.** A value is valid before the deadline and expired exactly at the deadline.

- **Separate presence from truthiness.** Zero, `False` and an empty string can all be valid cached values. Keep each cache instance independent.

## Walk through an example

```python
now = 100
ttl = 10
entry = {"value": 0, "expires_at": now + ttl}
expired = 110 >= entry["expires_at"]  # True
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An expiring cache needs both a **stored value** and an **expiry time**. Expiration is a comparison against the current clock. A cached zero, False, or empty string can still be a valid hit.

> [!WARNING]
> Do not use truthiness to decide whether a key exists. Check membership and expiry separately.

</details>

## Before you run

Is an entry valid exactly at its deadline? Can your tests control the clock?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
