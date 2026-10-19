# Defaults without guesswork

Use default parameters and keyword arguments.

## Use defaults deliberately

- **Set a default in the definition.** `role="learner"` is used when the caller omits that argument.

- **Allow positional or named arguments.** Keyword arguments identify a parameter by its name.

- **Keep explicit values.** An empty string supplied by the caller is still a value; it does not mean the argument was omitted.

## Walk through an example

```python
def greet(name, prefix="Hi"):
    return f"{prefix}, {name}"

greet("Mira")
greet(name="Mira", prefix="Welcome")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A parameter can have a default value: `def greet(name, prefix="Hi")`. Callers may leave it out, pass it positionally, or use a keyword. Defaults make common calls concise, while keyword arguments make less obvious choices readable.

Required parameters come before parameters with defaults in this ordinary signature. A default is used when an argument is omitted, not when an argument happens to be empty, zero or false. A caller passing an empty prefix has made a choice you should preserve.

Keep a function's interface small and predictable. Reaching into globals for a hidden option makes repeated tests harder to reason about. For immutable strings a default is safe; we will examine the shared mutable default trap in the scope chapter. Pip wants seventeen greeting options. We have approved two parameters and a small nap.

</details>

## Before you run

How is an omitted role different from role=""?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
