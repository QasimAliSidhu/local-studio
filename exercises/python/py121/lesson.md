# Boxes, leftovers and division

Use /, // and % according to the meaning of the result.

## Count all the boxes you need

- **Count full boxes with `//`.** The divisor is the positive capacity of one box.

- **Check leftovers with `%`.** Any remainder needs one additional box.

- **Test both edges.** Zero items need no boxes; an exact multiple needs no extra box.

## Walk through an example

```python
items, size = 13, 5
whole = items // size  # 2
loose = items % size   # 3
boxes = whole + (1 if loose else 0)  # 3
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

`/` produces ordinary division, usually a float. `//` produces floor division, and `%` produces the corresponding remainder. For non-negative integers and a positive divisor, floor division counts whole groups and the remainder counts what is left.

A partial group may need another container. A ceiling calculation can be built from the whole-group count plus one if a remainder exists. Be careful at exact multiples: an already full final box does not require an extra empty box.

Floor division rounds toward negative infinity, so negative values need deliberate interpretation. This exercise avoids that ambiguity with non-negative quantities. Python integers can grow beyond machine-word size, but that does not make computations free in time or memory. Pip ordered a box for every item and a separate box for each item's feelings. The warehouse has requested arithmetic.

</details>

## Before you run

Why does items // capacity + 1 fail when items is exactly divisible?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
