# Tiny permission switches

Represent flags with binary integers and bitwise operators.

## Read permission bits as switches

- **Use `&` to keep shared bits.** Integer bitwise operations compare the individual binary positions.

- **Compare against the required mask.** Every required bit must survive the intersection with the granted bits.

- **Include the zero case.** A mask requiring no bits is satisfied. Bitwise `&` and boolean `and` do different jobs.

## Walk through an example

```python
READ, WRITE = 0b01, 0b10
granted = READ | WRITE
print(granted & READ == READ)  # True
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A binary digit is a bit, either zero or one. An integer can represent several independent flags by giving each flag a different power-of-two position. Binary literal `0b0100` is the same numeric value as decimal four; `bin(value)` shows a binary representation and `int(text, 2)` parses binary text.

Bitwise `&` keeps positions set in both operands. Bitwise `|` combines positions set in either. These operate on bits and differ from logical `and` and `or`, which choose values based on truthiness.

To require several permissions, check that every required bit appears in the granted flags: the intersection must equal the required mask. Requiring no flags is always satisfied. This is a simplified representation exercise, not a complete authorization system. Pip requested administrator access to the toaster. We granted the crumb tray read-only permissions.

</details>

## Before you run

Why would bool(granted & required) accept only one of two required permissions?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
