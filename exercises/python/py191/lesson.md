# Find a character by its position

Read string indexes starting at zero.

## Read a character by position

- **Start at zero.** In `"Pip"`, index `0` is `P`, index `1` is `i`, and index `2` is `p`.

- **Select with square brackets.** `name[0]` gets the first character; `name[-1]` gets the last.

- **Stay inside the string.** An unavailable position raises `IndexError`. Reading an index leaves the original text unchanged.

## Walk through an example

```python
name = "Queue"
print(name[0])
print(name[-1])
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A string has an order. An **index** identifies one character's position, starting at zero. In `"Pip"`, index 0 is P, index 1 is i, and index 2 is p. Square brackets ask for the character at a position: `name[0]`.

Negative indexes count backward from the end. Index -1 is the last character, so you do not have to calculate the length first. Strings are not changed by reading a character. Asking for a position that does not exist causes an IndexError; our supplied string is non-empty.

The example displays Q and e on separate lines. Notice the difference between parentheses, which call a tool, and square brackets, which select a position. A quoted `"0"` is text, not the numeric index expected here.

Indexing will also work on lists later, but this exercise only uses text. Pip has requested that counting start at eleven for branding reasons. Python's answer is zero.

</details>

## Before you run

Why is code[1] the second character, rather than the first?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
