# Keep a helper in another module

Import a provided local module instead of duplicating its rule.

## Use a helper from another file

- **A module can be your own file.** The supplied `fees` module keeps the packaging rule in one place.

- **Import the helper you need.** A `from ... import ...` statement makes that helper available by name.

- **Call it when calculating.** Keeping the call, rather than copying today's fee, respects later changes to the rule.

## Walk through an example

```python
# fees.py provides packaging_fee(). In the caller:
from fees import packaging_fee

print(packaging_fee())
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Your own modules use the same import system as library modules. A file named fees.py can define packaging_fee; another file in the same project can use `from fees import packaging_fee`. The `.py` extension belongs in the filename, not the import statement.

This mission supplies fees.py alongside your script. Its contents are `def packaging_fee(): return 15`, written on normal indented lines. You only edit main.py. Importing the helper gives the caller a reusable rule with one home rather than another copied constant.

Defining a function inside an imported module does not call it. The caller still needs parentheses to run that function and obtain its result. Keep module-level side effects limited: importing a helper should not unexpectedly send messages or launch an application.

In a larger project you might organize modules into packages, but a local pair of files is enough to understand this boundary. Pip copied a fee rule into every file and then changed only half the copies. Finance is requesting one source of truth.

</details>

## Before you run

What is the difference between importing a function and calling it?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
