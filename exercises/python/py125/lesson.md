# The door has three rules

Combine comparisons with and, or and not.

## Combine the admission rules

- **Use `or` for alternatives.** A ticket or staff status can satisfy the first rule.

- **Use `and` for requirements together.** Passing one rule is insufficient when another must also hold.

- **Use `not` to reverse a boolean.** Group the alternatives with parentheses, then apply the rule excluding a banned visitor.

## Walk through an example

```python
allowed = (has_ticket or is_staff) and not is_banned
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Comparisons produce boolean results. `==` checks equality, `!=` checks inequality, and ordering operators compare size or position. Logical `and` requires both conditions, `or` accepts either, and `not` reverses a truth value.

Translate a sentence into small rules before combining it. Parentheses make mixed logic easier to read even when precedence would produce the same result. A banned user should not sneak through because an `or` condition was grouped incorrectly.

Python's logical operators can return operands instead of literal booleans. When your contract promises a bool, a comparison or an explicit `bool(...)` conversion makes the intent clear. Identity `is` answers whether two references point to the same object; use equality `==` to compare text values. Pip's access policy was 'looks friendly'. The security team has requested actual conditions.

</details>

## Before you run

Which case would expose a mistaken expression has_ticket or is_staff and not is_banned?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
