# Objects that remember their own jobs

Create independent instances with attributes and methods.

## Give each object its own state

- **Define a class, create instances.** `__init__` initializes a new object's values.

- **Use `self` for this object.** Attributes such as `self.name` and `self.completed` belong to the current instance.

- **Create mutable storage per instance.** A fresh history list lets each worker remember its own jobs without sharing another worker's history.

## Walk through an example

```python
class Counter:
    def __init__(self):
        self.value = 0

    def tick(self):
        self.value += 1
        return self.value
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A class describes objects that share behavior. Calling the class creates an instance. `__init__` initializes that instance, and `self` refers to it inside instance methods. Assigning `self.completed` stores state on this particular worker rather than in a shared module variable.

A class attribute is shared through the class unless an instance overrides it. A mutable class-level list is therefore a dangerous default for per-worker history. Initialize each worker's history inside __init__ so independent workers stay independent.

Methods are functions reached through an object; Python supplies the instance as self. Their contract should still say what they return and which state they change. Object-oriented design is useful when data and behavior have a clear shared responsibility. Pip created a Worker class whose only method was take_break. We have expanded the interface.

</details>

## Before you run

What changes if completed is defined once on the class instead?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
