# Return to sender

Write a function with a clear input/output contract.

## Describe the result before coding

- **Read the supplied inputs.** Multiply the quantity by the unit price to find the item cost.

- **Apply the order-level rule once.** A delivery fee belongs to the whole order, including an order with zero items.

- **Return from the provided function.** Replace `pass`; the checks call your function. Printing or adding a manual call is unnecessary here.

## Walk through an example

```python
def double(number):
    return number * 2

answer = double(6)
# answer is 12
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A function gives a group of instructions a name. `def` defines it; a later call runs it. Parameters are local names filled with arguments from that call. Indentation identifies the body, so keep every instruction belonging to the function at the same nesting level.

`return` ends the call and sends a value to the caller. Code after an unconditional return will not run. Printing a value does not make it the function's result, which matters when tests or another function need to use it.

A useful contract says which inputs are accepted and what the result means. Here we use integer cents so a simple price calculation avoids floating-point currency surprises. Validation is not required unless the contract says so. Pip asked whether a function could return a sandwich; technically it can return an object representing one. Procurement remains unconvinced.

This is the first **function challenge**, rather than a whole script. The editor provides the definition line; the checks call your function with several inputs. You do not need a call at the bottom of this file. Replace `pass`, the do-nothing placeholder, with a return statement. Printed text is not the requested result.

</details>

## Before you run

What would the caller receive if your function only printed the total?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
