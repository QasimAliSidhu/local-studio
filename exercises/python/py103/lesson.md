# Quotes are not comments

Distinguish the text Python prints from notes Python ignores.

## Tell text and comments apart

- **Match the outer quotes.** A string can use single quotes or double quotes; the opening and closing kind must match.

- **Choose the convenient kind.** Single outer quotes let you include double quotes inside your message.

- **Notice where `#` sits.** Outside a string it starts an ignored comment. Inside a string it is text that prints.

## Walk through an example

```python
# A note for the next engineer
print('The robot says "ready".')
print("Queue #7")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Quotes have a precise job: they surround text that belongs to a string. You can use a matching pair of single quotes or a matching pair of double quotes. Using single quotes on the outside makes it convenient to include double quotes inside the text, and vice versa.

A `#` outside a string starts a **comment**. Python ignores the rest of that line. A comment can explain your intention to another person; it does not display a message. A `#` inside quotes is ordinary string content and will be printed.

Read the example carefully. The first line is a note, so it produces no output. The second line displays a sentence containing quotation marks. The last instruction displays the hash character because it is inside its string.

You do not need backslash escapes for this mission: choose the convenient outer quote style instead. There are no new function definitions, return values or hidden wrappers to maintain. Pip has submitted a comment saying 'this is definitely correct'. Python ignores that too.

</details>

## Before you run

Which of the example lines is ignored, and why?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
