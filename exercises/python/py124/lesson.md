# The decimal that would not behave

Use tolerances for floating-point comparisons.

## Compare the size of the difference

- **Expect representation limits.** Some decimal fractions cannot be stored exactly as binary floats.

- **Use an absolute difference.** `abs(actual - expected)` measures distance without depending on which value is larger.

- **Include the boundary.** A difference equal to the tolerance qualifies; a tolerance of zero requires equality.

## Walk through an example

```python
difference = abs((0.1 + 0.2) - 0.3)
close = difference <= 1e-9
# True, although exact equality is False
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Most decimal fractions cannot be represented exactly by a finite binary floating-point number. Operations use nearby representable values, so `0.1 + 0.2 == 0.3` is false. This is a representation issue, not Python being bored with arithmetic.

A useful comparison may allow a small difference. `abs(actual - expected) <= tolerance` is an absolute-tolerance rule. `math.isclose` also supports relative tolerance, which scales with magnitude. Choose the rule from the domain; a tolerance suitable for a sensor reading may be unsuitable for money.

Rounding for display does not repair every numerical algorithm. For exact cents, integers are often simpler; for decimal business arithmetic, the standard library's Decimal can be appropriate. This mission uses finite floats and an explicitly supplied non-negative tolerance. Pip reports the kettle temperature as 'approximately soup'. We need a number.

The built-in `abs(number)` returns its distance from zero, so both abs(-3) and abs(3) are three. Applying it to actual - expected measures the size of the difference without depending on which number is larger.

</details>

## Before you run

Why would a relative tolerance behave differently for very large values?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
