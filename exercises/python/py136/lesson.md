# Comprehend the work order

Transform and filter a sequence with enumerate and comprehensions.

## Transform, then filter with care

- **Read the comprehension aloud.** `[expression for item in items if condition]` builds one new list from qualifying items.

- **Number before filtering when positions matter.** `enumerate(..., start=1)` retains the original positions even when some items are skipped.

- **Keep the exact text rule.** Empty strings and strings containing spaces are different. Use an ordinary loop if it is clearer.

## Walk through an example

```python
labels = [f"{position}: {name}"
          for position, name in enumerate(["A", "", "B"], 1)
          if name]
# ["1: A", "3: B"]
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A list comprehension combines iteration, an output expression and an optional filter: `[expression for item in items if condition]`. It builds a new list. Read it as 'produce this expression for each item that passes this condition'. Prefer an ordinary loop when a comprehension becomes difficult to explain.

`enumerate(items, start=1)` supplies a counter alongside each value, which avoids manually keeping an index in sync. Filtering after enumeration preserves the original positions; numbering after filtering would have a different meaning.

`zip(left, right)` pairs corresponding items and normally stops at the shorter input. When equal lengths are required, `zip(..., strict=True)` can expose a mismatch. Choose these tools because their behavior fits the contract, not because shorter code earns extra points. Pip submitted a one-line expression nobody could read. It has been framed as a warning.

</details>

## Before you run

How would the output change if you filtered first and enumerated afterward?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
