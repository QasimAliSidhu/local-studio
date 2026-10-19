# Trim the space around the message

Call one string method and keep its returned result.

## Trim the outside, keep the inside

- **Call a method after a dot.** `raw.strip()` asks the string to remove whitespace from both ends.

- **Keep the returned text.** Strings are immutable: assign the result to `clean`; `raw` stays unchanged.

- **Keep internal spaces.** `strip()` removes outside spaces, tabs and line breaks, rather than every space in the message.

## Walk through an example

```python
raw = "  night shift  "
clean = raw.strip()
print(clean)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **method** is a named tool attached to a value. Put a dot after that value, then the method's name and parentheses. For a string, `raw.strip()` makes a version without whitespace at either end. Whitespace includes spaces, tabs and line breaks.

The empty parentheses mean we supply no extra arguments in this call. The string before the dot is already the thing the method works on. You have used built-in calls such as len(message); this is another calling form, with its object on the left.

Strings are **immutable**: their characters are not edited in place. strip returns a new result. Assign it to a name so you can use it; the original raw string stays the same. Internal spaces stay too, because only the outside is trimmed.

The example preserves the space between night and shift. Pip's last cleanup removed every space and produced a very long username.

</details>

## Before you run

Does strip remove the space between night and shift in the example?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
