# Invoice totals

Calculate an invoice total using integer cents.

## Accumulate an invoice in cents

- **Unpack each pair.** Each line contains a unit price in cents and a quantity.

- **Add the line totals.** Multiply price by quantity, then add it to a local accumulator starting at zero.

- **Validate before accepting a line.** Negative prices or quantities are invalid; an empty invoice has no charges.

## Walk through an example

```python
subtotal = 0
for amount in [125, 250, 75]:
    subtotal += amount
print(subtotal)  # 450
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Represent money as **integer cents** so ordinary arithmetic stays exact. An accumulator starts with the identity for the operation: **zero** for addition. Each loop iteration contributes one line item.

> [!WARNING]
> Validate both values in a pair. A negative quantity is just as invalid as a negative price.

</details>

## Before you run

What should an empty collection contribute? Where should invalid input be rejected?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
