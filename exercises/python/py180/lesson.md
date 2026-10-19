# Split the message, join the pieces

Use lists of words as the bridge between text and collection processing.

## Move between text and words

- **Split on whitespace with `text.split()`.** Runs of spaces, tabs and newlines separate words without creating empty pieces.

- **Join with the separator on the left.** `"-".join(parts)` places one dash between string members, with none at the edges.

- **Preserve the agreed spelling.** Splitting and joining do not require changing case. No words means an empty result string.

## Walk through an example

```python
parts = "  night   shift  ".split()
label = "-".join(parts)
print(label)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

The string method `split()` breaks text on whitespace and returns a list of words. With no separator argument it treats runs of spaces, tabs and line breaks as separators and omits empty pieces. `split(",")` instead splits on literal commas and can preserve empty fields.

To go in the other direction, call `separator.join(parts)`. The separator string supplies the text placed between members. For example, `"-".join(["night", "shift"])` produces night-shift. It does not put a dash at either end.

This method returns a new string; neither the input text nor an existing list is edited. The list members must be strings. Use a real parser for formats with quoting rules, such as CSV, which we will study later.

This lesson waits until lists and loops are familiar, so a list of pieces is no mystery. Pip has been splitting logs with scissors. The digital version leaves less confetti.

</details>

## Before you run

How would split(" ") behave differently for repeated spaces?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
