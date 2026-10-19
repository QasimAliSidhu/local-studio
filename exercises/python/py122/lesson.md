# Parentheses prevent incident reports

Apply operator precedence and exponentiation deliberately.

## Build the calculation in stages

- **Raise with `**`.** `2 ** attempt` doubles the factor at each step, starting with `1` at attempt zero.

- **Multiply by the base.** Group the expression so its meaning stays clear.

- **Apply the cap with `min`.** `min(calculated, cap)` keeps the smaller value, including a cap of zero.

## Walk through an example

```python
base = 3
attempt = 2
delay = base * (2 ** attempt)
# 12, not (3 * 2) ** 2
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Python evaluates expressions using precedence rules. Exponentiation (`**`) binds more tightly than multiplication and division, which bind more tightly than addition and subtraction. Parentheses explicitly group work and are often worth using even when you remember the rules.

`2 + 3 * 4` is fourteen; `(2 + 3) * 4` is twenty. A correct business rule can become an incorrect expression if its grouping is lost during translation. Name an intermediate value when a formula is hard to scan.

Exponentiation expresses repeated multiplication, not an increase by a fixed amount. A backoff delay that doubles on each retry is exponential; adding two seconds on each retry is linear. In real clients, a cap and jitter often avoid synchronized retry storms. Here we implement a precise deterministic cap. Pip calls it 'waiting with ambition'.

The built-in `min(left, right)` returns the smaller of two values. The `**` operator raises a number to a power: `2 ** 0` is one, `2 ** 1` is two, and `2 ** 2` is four. These are arithmetic operations, not argument-unpacking syntax.

</details>

## Before you run

At attempt zero, why should the multiplier be one?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
