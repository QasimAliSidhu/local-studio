# Names inside and outside a call

Explain local names before mutation or closures.

## Keep local and module names separate

- **A module name lives outside the function.** It remains available between calls.

- **An assignment inside a function is normally local.** A local `label` can have a different value from the module's `label`.

- **Return the local value.** The call should not change the module-level name.

## Walk through an example

```python
label = "outside"
def local_label():
    label = "inside"
    return label

print(local_label())
print(label)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A name assigned inside a function normally belongs to that call's **local scope**. A name assigned at the top level belongs to the module. A local name may have the same spelling as an outer name without replacing that outer binding.

Read the example by following the two labels separately. The module label starts as outside. Calling local_label creates a local label equal to inside and returns it. Printing the module label afterward still displays outside.

A return makes the local result available to the caller; it does not promote all of the function's local names into global variables. Explicit inputs and returned results keep small calculations easy to reason about.

For now, we are discussing immutable strings and numbers. Shared mutable lists introduce a different issue, which has its own chapter after collections. Closures and nonlocal also wait until the advanced patterns chapter. Pip has put two identical name tags on two different desks. The tags do not merge the desks.

</details>

## Before you run

Predict both lines from the example before running it.

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
