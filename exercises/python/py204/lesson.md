# A small anonymous sorting rule

Introduce lambda and key functions before using them in reports.

## Tell sorting what to compare

- **Use `sorted` for a new list.** The original order in the caller's list stays untouched.

- **Supply a key function.** A short `lambda` can select the `"name"` field from each record.

- **Separate list and record ownership.** This task permits references to the same dictionaries; you still must not edit them.

## Walk through an example

```python
records = [{"name":"B","score":2},{"name":"A","score":1}]
ordered = sorted(records, key=lambda record: record["score"])
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **lambda** creates a small function from one expression: `lambda item: item["score"]`. Parameters go after lambda and the expression goes after its colon. The expression's result is returned automatically. Use a named def when several statements or a useful descriptive name would be clearer.

`sorted(items, key=...)` calls the supplied key function for each item and orders by those key values. It returns a new list instead of changing the original order. The callback concept is the same one you just practiced.

A tuple key gives a tie-breaker: `(score, name)` sorts by score first and then name. Negating a numeric score can make that part descending while the name stays ascending. You will use that pattern in the next mission.

Keep these rules readable. Lambda is a convenience, not a requirement to squeeze a whole program onto one line. Pip sorted reports by the number of exclamation marks. We are specifying the key.

</details>

## Before you run

When would a named def make a key function easier to read?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
