# Numbers do not need costumes

Distinguish numeric expressions from text that looks like arithmetic.

## Ask Python to calculate

- **Without quotes, use numbers.** `7 + 2` is an expression that evaluates to `9`.

- **Inside quotes, keep the text.** `"7 + 2"` is a string containing those characters.

- **Print the result.** `print(7 + 2)` calculates first, then displays the answer.

## Walk through an example

```python
print(7 + 2)
print("7 + 2")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

The quotes you have used make a string. Without quotes, a numeric literal such as `7` is a number. Python can calculate with numbers: `+` adds and `-` subtracts. A calculation such as `7 + 2` is an **expression**: Python evaluates it to a value.

The input to print can be an expression. In `print(7 + 2)`, Python calculates nine, then gives that value to print. In `print("7 + 2")`, the input is text, so Python displays the characters without doing arithmetic.

In the example, the console shows `9` on the first line and `7 + 2` on the second. Parentheses around print's input are still required in both cases; quotation marks make the important difference.

For now, use whole numbers. We will give values names next, then learn multiplication, division and decimal numbers in small steps. Pip has put the calculator inside quotation marks. It now works beautifully as a sign.

</details>

## Before you run

Why does the example print two different things even though both lines contain 7 + 2?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
