# True, False, and nothing supplied

Read a comparison result and distinguish None from zero.

## Ask a question with an expression

- **Compare values with `==`.** The result is a boolean: `True` or `False`.

- **Use `>` to ask whether a number is greater.** Zero is equal to zero, but it is not greater than zero.

- **Check missing values with `is None`.** `None` represents no supplied value; it is different from a valid numeric zero.

## Walk through an example

```python
setting = None
print(setting is None)
print(0 == None)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A comparison asks a question and produces a **boolean**: either True or False. The names use capital first letters and no quotes. `==` asks whether two values are equal, while `=` assigns a value to a name. `>` asks whether the left value is greater; `<` asks whether it is smaller. Adding `=` makes the boundary inclusive: `>=` and `<=`.

You can print a comparison to inspect its answer before using it to control the program. `3 > 2` produces True; `3 == 2` produces False. These values are different from the strings "True" and "False".

**None** is Python's absence marker. A function that supplies no return value gives None. It is not zero, an empty string, or the word "None". Use `value is None` when the question is specifically whether a value is absent.

The example asks two different questions about a missing setting. Pip calls every missing value 'probably twelve'. We will keep absence explicit.

</details>

## Before you run

Why is jobs == 0 a question, while jobs = 0 is an instruction?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
