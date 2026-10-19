# Build a tool of your own

Explain def, a function body and a call before asking for a function.

## Define first, then call

- **Begin with `def`.** `def greet():` names a function. The colon starts its body.

- **Indent the instructions.** The indented lines belong to the function; defining them does not run them yet.

- **Call with parentheses.** An unindented `greet()` runs the body once. Define it before the call.

## Walk through an example

```python
def ring_bell():
    print("Ding!")

ring_bell()
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

You have called Python's built-in print and len tools. Now you will **define** a function: give a name to instructions you want to reuse. `def` begins a definition. The name comes next, followed by parentheses and a colon.

The indented lines below the definition are its **body**. Use four spaces of indentation. They belong to the function and run when it is called, not merely because the definition has been read. A call uses the name with parentheses, just like print.

In the example, Python first defines ring_bell without printing. The final unindented line calls it, so the body runs and the console displays Ding!. Without that final call, the script would define the tool but never use it.

Keep this first function simple: no parameters or return statement yet. Those get their own next lessons. Pip has been calling a function that nobody defined. We are starting with the other half of the agreement.

</details>

## Before you run

What would the example print if the final ring_bell() line were removed?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
