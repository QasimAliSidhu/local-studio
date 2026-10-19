# Read the check before changing the code

Connect an assertion with a precise behavioral rule.

## Check what each term means

- **Read the contract before editing.** Decide which charge applies per item and which applies once per order.

- **Test more than one item.** A single-item case can hide misplaced parentheses or a repeated fee.

- **Test zero items too.** Boundary cases reveal whether the fixed charge is being applied correctly.

## Walk through an example

```python
def add_fee(amount, fee):
    return amount + fee

assert add_fee(10, 2) == 12
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An **assertion** states a condition a test expects to be true. Plain Python `assert result == expected` raises AssertionError when the condition is false. Our test runner reports actual and expected values using more descriptive assertions, but the basic idea is the same.

Separate a test failure from a syntax error. A failing equality assertion usually means the program ran and returned the wrong result. A SyntaxError means Python could not read the program. Inspect the reported line and the kind of error before deciding what to fix.

Use boundary cases that distinguish competing interpretations of a rule. Here the fee applies once to the whole order, even when the item quantity is zero. That empty-order case is not an invitation to guess a different business policy.

Assertions are useful for tests and internal expectations, not a replacement for validating untrusted input: Python can disable them under optimization. Pip has written 'correct' in a comment. An assertion requires evidence.

</details>

## Before you run

Which test case proves the fee applies once even when no items are ordered?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
