# Text, whole numbers and decimals

Recognize strings, ints and floats before converting between them.

## Recognize the kind of value

- **`int` means a whole number.** `12` is an integer; `1.5` is a decimal value of type `float`.

- **`str` means text.** `"12"` stays a string even though it looks numeric. `type(value)` reports the type.

- **Let the type explain `+`.** Two numbers add; two strings join. Combining text and a number needs an explicit conversion.

## Walk through an example

```python
count = 12
label = "12"
print(count + 3)
print(label + "3")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Values have **types**, meaning different kinds of information with different supported operations. A whole number such as `12` is an `int`. A number with a decimal point such as `1.5` is a `float`. Quoted text such as `"12"` is a `str`, even when its characters look numeric.

With numbers, `+` adds. With two strings, `+` joins their characters, an operation called concatenation. Python does not automatically choose how to combine a string and a number; that usually needs an explicit conversion, which we will learn later.

The built-in tool `type(value)` reports the kind of value. Its console representation contains the word class, such as `<class 'int'>`. That is Python's type label; you are not being asked to create classes here.

In the example, the first result is fifteen and the second is the text 123. Pip stored the number of snacks as text and tried adding three. The budget became enormous.

</details>

## Before you run

Is "1.5" a float or a string? Which punctuation tells you?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
