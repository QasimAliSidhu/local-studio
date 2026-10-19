# Clean up the robot username

Combine familiar string methods with one new replacement rule.

## Clean the text in a clear order

- **Trim first.** `strip()` removes whitespace at the edges.

- **Normalize the case.** `lower()` makes a lowercase result; chaining passes each returned string to the next method.

- **Replace each internal space.** `replace(" ", "_")` makes two spaces become two underscores. These methods leave the original string unchanged.

## Walk through an example

```python
raw = "  Night Shift  "
clean = raw.strip().lower().replace(" ", "_")
print(clean)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

You have used strip to trim and lower to change case. The method `replace(old, new)` returns text with each occurrence of old replaced by new. Its two inputs are separated by a comma. `text.replace(" ", "_")` changes each ASCII space into an underscore.

You can keep each intermediate result in a named variable or **chain** the methods. In `raw.strip().lower()`, Python first trims raw, then calls lower on the returned string. Read the chain left to right.

The original raw string remains unchanged. Trimming removes only outside whitespace, and replacing each space does not collapse repeated spaces. Two internal spaces therefore become two underscores. These rules are specific to a handle, not to every kind of user input.

The example turns Night Shift into night_shift after trimming. Pip would like to include twelve invisible spaces in its handle. The name-tag printer has declined.

</details>

## Before you run

Why do two internal spaces produce two underscores?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
