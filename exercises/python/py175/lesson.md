# A tool can give back a value

Use len and assign its result before printing it.

## Keep the value a tool returns

- **Call `len(text)` to count characters.** Spaces count too; an empty string has length `0`.

- **Store the return value.** `characters = len(message)` gives the numeric result a name.

- **Use that result next.** Print it or calculate with it. Receiving a result does not require writing your own `return` statement yet.

## Walk through an example

```python
word = "queue"
letters = len(word)
print(letters)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Some tools give a value back for the next part of your program to use. The built-in function `len` counts the characters in a string. Calling `len("queue")` produces the number five. You can assign that result to a variable, calculate with it, or pass it into print.

This is a **return value**: a result handed back to the caller. You do not need a return statement to use a built-in tool. Later, when we build functions, we will write return statements to supply our own results.

Spaces count as characters too. An empty string has length zero. In `print(len("queue"))`, Python calculates the inner len call first, then prints its result. Splitting that into two named steps can be easier to follow at first.

Pip counted only the letters that looked productive. The standard library is less judgmental.

</details>

## Before you run

What would len("") give back?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
