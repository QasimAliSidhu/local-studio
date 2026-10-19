# Borrow a tool from the standard library

Explain import and module-qualified calls before files or JSON.

## Borrow a standard-library tool

- **Import the module.** `import math` makes its tools available under the name `math`.

- **Use the qualified name.** `math.ceil(value)` rounds upward to the smallest integer at least as large as the value.

- **Keep the returned result.** Store it in a variable, then print it; importing alone does not perform this calculation.

## Walk through an example

```python
import math

print(math.ceil(2.3))
# This prints 3.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **module** is a Python file or library unit that groups reusable definitions. Python's **standard library** comes with the language and includes tools for mathematics, dates, structured data and more. An import makes a module available under a name in your program.

`import math` gives you the module name math. A dot selects one of its tools, so `math.ceil(value)` rounds upward to a whole number. The import does not copy its source into your editor or require a package download. Standard-library imports work on the course laptop already.

Another form, `from math import ceil`, binds that particular tool directly to the name ceil. Keep import style consistent so readers can tell where a definition comes from. Avoid a wildcard import in application code when it makes names ambiguous.

You have used methods after dots too; the shape is familiar, but math is a module here. Pip attempted to import coffee. Python reports that module is not installed.

</details>

## Before you run

Which name identifies the module and which identifies its tool?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
