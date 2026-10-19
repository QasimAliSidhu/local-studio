# Give your numbers useful names

Create a variable, calculate a new value and print it.

## Give each value a name

- **Assign with `=`.** `minutes = 3` makes the name `minutes` refer to the value `3`.

- **Calculate the right side first.** In `seconds = minutes * 60`, `*` multiplies before the result is assigned.

- **Use the name without quotes.** `print(seconds)` displays its value; `print("seconds")` displays the word.

## Walk through an example

```python
minutes = 2
seconds = minutes * 60
print(seconds)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **variable** is a name referring to a value. `minutes = 3` assigns the value three to the name minutes. Read `=` as 'assign', not as a question about equality. On a later line, using the name retrieves its current value.

You can use named values in an expression. The `*` operator means multiplication, so `minutes * 60` calculates the number of seconds. The right side of an assignment is calculated first; its result is then assigned to the name on the left.

In the example, minutes refers to 2, seconds refers to 120, and `print(seconds)` displays 120. Do not quote the name when you want its value: `print("seconds")` displays the word instead.

Choose names that tell you the quantity and units. This helps prevent mixing minutes with seconds, a hobby Pip has unfortunately taken up. You do not need to define a function or accept inputs yet. This mission is still a plain script.

</details>

## Before you run

What would print("seconds") display instead?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
