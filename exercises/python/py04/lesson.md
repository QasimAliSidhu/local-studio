# Scope and pure functions

Apply a discount without changing the original prices.

## Calculate from inputs without leaving changes

- **Build a new list.** The caller's prices and the module default must remain unchanged.

- **Apply the stated integer rule.** `//` floors the discounted calculation to integer units.

- **Validate the percentage boundary.** Zero and one hundred are valid; values outside that range must be rejected.

## Walk through an example

```python
def add_fee(amounts, fee):
    return [amount + fee for amount in amounts]

original = [10, 20]
updated = add_fee(original, 3)
# original remains [10, 20]
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A function call has its own **local variables**. Assigning a new local name does not change a global name. A **pure transformation** returns a new value and leaves the input collection unchanged.

> [!WARNING]
> Changing prices in place creates a side effect. Validate the percentage before building the result.

</details>

## Before you run

If two names refer to the same list, what happens when one name changes an element? How does building a new list avoid that?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
