# Functional log aggregation

Filter successful events and add their amounts.

## Filter, then add the matching amounts

- **Read each status explicitly.** `.get("status")` can handle an absent status without a lookup error.

- **Keep only the specified success value.** Other statuses do not contribute to the total.

- **Accumulate without changing events.** A generator expression can supply qualifying amounts to `sum`; an empty sum is zero.

## Walk through an example

```python
events = [{"ok": True, "ms": 12}, {"ok": False, "ms": 90}]
total = sum(event["ms"] for event in events if event["ok"])
# 12
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Separate a data pipeline into three questions: **which records qualify**, **what value each produces**, and **how those values combine**. A generator can pass one value at a time into an aggregation.

> [!WARNING]
> Do not mutate the input while aggregating. Keep filtering decisions distinct from output construction.

</details>

## Before you run

Can the input be consumed only once? Are you changing any record while reading it?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
