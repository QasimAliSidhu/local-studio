# A status message worth reading

Format a decimal inside an f-string after learning basic interpolation.

## Choose how a number looks

- **Keep the value inside braces.** An f-string inserts expressions into a message.

- **Add the display rule after a colon.** `f"{rate:.2f}"` displays two digits after the decimal point.

- **Separate display from arithmetic.** `2.5` can appear as `2.50` in the message while the numeric variable stays unchanged.

## Walk through an example

```python
name = "Mira"
rate = 7.5
message = f"{name}: {rate:.2f}/s"
print(message)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An f-string already lets you insert values into a message. A **format specifier** controls how an inserted value is displayed. Put a colon after the expression inside its braces, followed by the formatting rule.

The rule `.2f` displays a number with two digits after the decimal point. In `f"{rate:.2f}"`, a rate of 2.5 becomes the text 2.50. Formatting changes the representation used in that message; the numeric rate itself stays 2.5.

Keep literal punctuation outside the braces and the expression plus format rule inside. The example displays Mira: 7.50/s. You can build the message in a variable to check it before printing.

Two decimal places are a display choice, not a universal precision guarantee. We will discuss floating-point arithmetic after comparisons. For now, the supplied value formats cleanly. Pip's previous dashboard had thirty decimal places and no room for the service name.

</details>

## Before you run

Has the value stored in rate changed because the message shows 2.50?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
