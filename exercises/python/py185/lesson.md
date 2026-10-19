# Give your function an input

Distinguish a parameter in a definition from an argument in a call.

## Give the same function different inputs

- **Name a parameter in the definition.** In `def greet(name):`, `name` is the input name used inside the body.

- **Supply an argument in a call.** `greet("Mira")` makes `name` refer to `"Mira"` during that call.

- **Use the supplied value.** Build the greeting from `name` so the same body works for another caller too.

## Walk through an example

```python
def welcome(name):
    print(f"Welcome, {name}!")

welcome("Mira")
welcome("Pip")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A function can accept an input so the same instructions work with different values. The definition puts a **parameter name** between its parentheses: `def greet(name):`. A call supplies an **argument value**, such as greet("Mira"). During that call, name refers to the supplied string.

Use the parameter inside the body just like another variable. Do not put quotes around its name when you mean its value. An f-string can insert that value into a greeting, using the syntax you have already practiced.

Every call supplies its own input. The example calls welcome twice, once for Mira and once for Pip, so it prints two different messages. The body is written only once. This is the practical reason for introducing a function rather than duplicating instructions.

Define the function before calling it. Pip would like all callers to say its name, but the whole point is that Mira can call too.

</details>

## Before you run

In welcome("Mira"), which part is the argument and which name is the parameter?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
