# Local names, local business

Read a global constant while keeping call-specific variables local.

## Choose a default without changing it

- **Read the module constant when needed.** `REGION` supplies the default only when `region is None`.

- **Preserve an explicit empty region.** An empty string is different from a missing value.

- **Build and return the label.** Use local values; leave the module constant unchanged.

## Walk through an example

```python
PREFIX = "job"

def make_label(number):
    label = f"{PREFIX}-{number}"
    return label
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Each function call has its own local namespace. Assigning `label = ...` inside a function creates or rebinds that local name. It does not automatically rebind a name with the same spelling outside the function.

When reading an ordinary name, Python looks through enclosing scopes and then the module and built-ins. A module-level constant can supply a default rule, but a local result should be returned explicitly. Uppercase names are a convention for constants, not an enforcement mechanism.

Assignment inside a function makes that name local unless `global` or `nonlocal` says otherwise. Reading a name before its local assignment can produce `UnboundLocalError`; moving a line at random does not explain the real issue. Prefer explicit inputs and outputs when the job does not require shared state. Pip says all variables should be global because sharing is caring. Pip is not reviewing this pull request.

</details>

## Before you run

Why would adding global REGION make this tiny function harder to use safely?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
