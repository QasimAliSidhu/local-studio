# Full boxes and leftovers

Use integer division and remainder before they appear in larger functions.

## Separate full groups from leftovers

- **Count full groups with `//`.** For these non-negative inputs, `14 // 6` gives `2` complete boxes.

- **Find leftovers with `%`.** `14 % 6` gives `2` items left over.

- **Check the relationship.** `full_boxes * size + loose_items` should equal the original count. The box size must be positive.

## Walk through an example

```python
items = 14
size = 6
print(items // size)
print(items % size)
# Two lines, both displaying 2.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Ordinary division answers how much each group gets, including fractions. Sometimes we need whole groups instead. For non-negative integers, `items // size` counts complete groups and `items % size` gives the leftover items. The symbols are called floor division and modulo.

With fourteen items and boxes holding six, there are two full boxes and two loose items. Reconstructing the total verifies the reasoning: two times six plus two equals fourteen. At an exact multiple, the remainder is zero.

These expressions return numeric values you can assign or print just like addition. We restrict this mission to non-negative quantities and a positive capacity. Negative floor-division behavior deserves its own careful interpretation rather than an accidental assumption.

Do not add an extra full box for the remainder: it is not full. Pip is attempting to invoice the empty space, but that is outside this contract.

</details>

## Before you run

What should both expressions produce when items is zero?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
