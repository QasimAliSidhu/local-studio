# Protect the snack fund

Enforce an invariant through methods and a read-only property.

## Change state through a clear interface

- **Expose a read-only property.** `@property` lets callers read `balance` through a getter without supplying a setter.

- **Validate before changing state.** An invalid deposit must leave the old balance intact.

- **Keep the update in a method.** `deposit(amount)` applies the permitted change and returns the resulting balance.

## Walk through an example

```python
class Meter:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An invariant is a condition that should remain true for every valid object state. A wallet might require a non-negative balance. Validate both construction and later updates, or the object can enter an invalid state through one unguarded path.

A property exposes a method as an attribute-like read. Without a setter, ordinary assignment to that property fails. Store the backing value under a separate name such as `_balance`. The underscore is a convention for internal use, not a security boundary against hostile Python code.

Validate before modifying state so an exception leaves the previous valid value intact. Returning the new balance can make operations convenient while preserving the invariant. This is encapsulation: callers use a defined interface rather than reconstructing the object's rules. Pip has been placed in charge of snack funds, a decision the invariant will have to survive.

The `@property` line asks Python to expose the following getter method as an attribute-like read. It is a built-in decorator: a standard transformation applied to the method definition. There is no setter here, so ordinary assignment to balance is rejected. General-purpose decorators come later.

</details>

## Before you run

Why is a leading underscore a convention rather than a security mechanism?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
