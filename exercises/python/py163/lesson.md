# Inheritance, with a real reason

Override behavior and use super without duplicating initialization.

## Extend a useful base behavior

- **Inherit from the base class.** The subclass keeps the relationship and behavior the contract asks it to extend.

- **Initialize the base part.** `super().__init__(...)` sets up the fields owned by the base class.

- **Override the method deliberately.** Add the surcharge to the base cost instead of duplicating or ignoring the base calculation.

## Walk through an example

```python
class Job:
    def __init__(self, units):
        self.units = units
    def cost(self):
        return self.units

class DoubleJob(Job):
    def cost(self):
        return super().cost() * 2
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Inheritance lets a subclass reuse and specialize a base class. If a subclass does not override a method, attribute lookup can find the base implementation. An overridden method defines the specialized behavior for that subtype.

`super()` gives access to inherited behavior in a way that cooperates with Python's method resolution order. Calling `super().__init__(...)` lets the base initialize its part of the object rather than duplicating those assignments in each subclass.

Choose inheritance for an actual 'is a kind of' relationship whose behavior stays compatible with callers. A long hierarchy built only to avoid a few repeated lines can be harder to understand than composition. Here a priority job is still a job, and both expose cost(). Pip proposed that a sandwich inherit from a database because both can contain rows. The architecture review was brief.

</details>

## Before you run

When would an object containing a Job be clearer than an object inheriting Job?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
