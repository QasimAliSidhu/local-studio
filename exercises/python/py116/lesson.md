# A counter with a private office

Use a closure and nonlocal for intentionally retained state.

## Keep state in a closure

- **Return an inner function.** It can remember names from the enclosing call after that call finishes.

- **Use `nonlocal` to reassign that remembered name.** This differs from creating a new local or writing module state.

- **Create a new closure per counter.** Each returned counter owns its own count and updates it independently.

## Walk through an example

```python
def make_counter(start):
    current = start
    def tick():
        nonlocal current
        current += 1
        return current
    return tick
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An inner function can retain access to variables from its enclosing function after that outer call has finished. This combination of a function and its retained environment is a closure. Separate outer calls create separate environments, which is useful for small independent counters or configured callbacks.

Reading an enclosing name requires no extra keyword. Rebinding it inside the inner function requires `nonlocal`; otherwise the assignment makes a new local name, and an earlier read fails. `nonlocal` refers to an enclosing function scope, while `global` refers to module scope.

Stateful code is appropriate when state is the point. Make that state deliberate and scoped rather than letting unrelated calls share a global counter. A closure is not automatically safe under simultaneous access; that is a separate concern. Pip wants private offices for integers. This is the budget version.

</details>

## Before you run

How would storing current at module scope break independent counters?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
