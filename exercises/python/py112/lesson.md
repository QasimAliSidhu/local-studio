# Two answers, one return trip

Return and unpack tuples without losing the remainder.

## Return two related values

- **Make a tuple with a comma.** `return minutes, seconds_left` hands back one pair of values.

- **Unpack the pair in order.** The caller can assign its first and second values to separate names.

- **Remember the one-item form.** `(7,)` is a tuple; `(7)` is just the integer in parentheses. Use `//` and `%` for complete minutes and leftover seconds.

## Walk through an example

```python
def split_boxes(items):
    return items // 6, items % 6

full, loose = split_boxes(14)
# full == 2, loose == 2
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Comma-separated return values form a tuple. A caller can unpack it into the same number of names: `first, second = result`. The position of each value is part of the contract; swapping them creates a valid tuple with the wrong meaning.

Tuples are useful for a small, fixed group of related results. When a group grows or positions become difficult to remember, a named record is usually clearer. Unpacking does not run the calculation twice; it assigns each component from one returned result.

Integer division and remainder are handy when dividing a quantity into full units and leftovers. `//` counts complete groups and `%` gives what remains. For non-negative values, these describe exactly how many full minutes fit into a duration. Pip's time tracker reports ninety seconds as one and a half coffee breaks. Your interface must be more conventional.

The comma creates the tuple. Unpacking assigns its first and second members to the two caller names. A one-item tuple needs a trailing comma, such as `(7,)`; `(7)` alone is just a parenthesized integer.

</details>

## Before you run

What happens if you use / instead of // for minutes?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
