# Small helpers, fewer tiny disasters

Compose functions and reuse a supplied helper.

## Let each helper own one rule

- **Call the supplied helper.** `service_fee(subtotal)` calculates the fee from the current rule.

- **Combine named parts.** Add the subtotal, returned service fee and delivery charge.

- **Avoid copying the helper's formula.** Calling it keeps checkout correct when the service-fee rule changes.

## Walk through an example

```python
def add_fee(amount, fee):
    return amount + fee

def checkout(amount):
    return add_fee(amount, 10)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

One function can call another. The caller waits for the helper's return value, then uses it like any other value. This lets you give a meaningful name to a small rule and apply that rule in more than one place.

Reuse is also about keeping rules consistent. Copying a formula into several functions means a future correction can miss one copy. Calling a helper gives the rule one home. The helper's parameters and return value form an interface; callers need not duplicate its internal instructions.

Watch argument units and order at the boundary. A helper expecting cents cannot safely receive pounds merely because both values are numbers. We test helper use by replacing it temporarily: if the caller ignores the helper, the replacement result cannot flow through. Pip calls this a surprise inspection. We call it dependency testing.

</details>

## Before you run

Why does replacing the helper reveal a copied fee formula?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
