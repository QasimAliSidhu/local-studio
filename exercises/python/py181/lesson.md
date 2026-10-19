# Multiply, divide, and keep the units

Use multiplication, division and parentheses in a named calculation.

## Keep the calculation readable

- **Multiply with `*`; divide with `/`.** Ordinary division returns a float: `8 / 2` gives `4.0`.

- **Group with parentheses.** Multiplication and division happen before addition and subtraction unless you group another part first.

- **Name the units.** Dividing `jobs` by `seconds` gives jobs per second. The divisor must not be zero.

## Walk through an example

```python
jobs = 12
seconds = 4
rate = jobs / seconds
print(rate)
# The value displayed is 3.0.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

You have used `+`, `-` and `*`. The `/` operator divides and produces a float, even when the division comes out evenly. `8 / 2` gives 4.0. The decimal point is a representation difference, not an extra item.

Multiplication and division happen before addition and subtraction. Parentheses group a calculation when you want a different order: `(2 + 3) * 4` is twenty, while `2 + 3 * 4` is fourteen. Parentheses here group arithmetic; parentheses after a tool name supply its input. Context tells you the job.

Store an intermediate calculation in a named variable if that makes the units clearer. You should be able to explain what a result means, not merely reproduce its digits. Division by zero is an error; our supplied capacity is positive.

Pip measured server speed in biscuits per worry. We will use jobs per second.

</details>

## Before you run

Predict (2 + 3) * 4 and 2 + 3 * 4 before running either.

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
