# Numbers wearing string costumes

Convert valid text to an integer before calculating.

## Convert before calculating

- **Recognize numeric text.** `"8"` is still a string; joining it with `"2"` produces `"82"`.

- **Call `int(raw)`.** Valid whole-number text becomes an integer you can calculate with.

- **Keep the original if needed.** Assign the converted value to `count`. Invalid integer text raises `ValueError`.

## Walk through an example

```python
raw = "12"
print(raw + "3")
count = int(raw)
print(count + 3)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Text from a configuration file or a form often looks like a number but is still a string. The built-in tool `int(text)` converts valid whole-number text into an integer. Its result can be assigned and used in arithmetic.

Compare the example's two lines: adding quoted "3" to raw joins strings; converting raw with int lets you add the number 3. Python does not guess which meaning you intend. A separate function, `str(value)`, gives a text representation when you need one.

Not every string is valid integer text. A decimal like "1.5" is not a whole-number representation for int. We will learn to handle conversion errors in the errors chapter; this mission supplies valid text, so there is no recovery code to invent yet.

Keep the original text and store the parsed number under a new name. Pip tried to order "12" plus "3" biscuits and created an impressive string. The kitchen requires arithmetic.

</details>

## Before you run

Why do the example's two lines display 123 and 15?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
