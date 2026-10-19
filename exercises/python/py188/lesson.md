# Each call gets fresh local work

Initialize call-specific state inside the function.

## Start fresh for each call

- **Create local work inside the function.** Initialize a total from the input for this call.

- **Update that local value.** Add the supplied bonus, including zero or a negative amount.

- **Return this call's answer.** A later call gets its own local work instead of inheriting an earlier total.

## Walk through an example

```python
def add_bonus(amount):
    total = amount
    total = total + 2
    return total

print(add_bonus(10))
print(add_bonus(10))
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A function can be called many times. Each call creates its own local names for the parameters and any local assignments. When the calculation needs a temporary running value, initialize it inside the function rather than retaining it at module level.

The example calls add_bonus twice with the same input. Each call starts from its own amount and produces twelve. It does not produce fourteen on the second call because total is not shared between calls.

The shorthand `total += bonus` means update total using its current value; for numbers it is equivalent to `total = total + bonus`. It does not alter the caller's numeric variable. You can keep the longer form while learning if it is clearer.

Later we will deliberately model retained state with objects and closures. First, make repeated pure calculations predictable. Pip has a calculator that remembers every previous invoice. Accounting has asked for fresh local work.

</details>

## Before you run

Why do repeated example calls both display 12?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
