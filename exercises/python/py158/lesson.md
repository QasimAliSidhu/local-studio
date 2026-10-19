# Checkpoint: a suspicious fallback

Repair a truthiness bug and test explicit empty settings.

## Check absence before choosing a fallback

- **A missing key is one case.** Membership tells you whether `"timeout"` was supplied.

- **A stored `None` is another case.** This contract also uses the default for that specific value.

- **Keep other stored values exactly.** An `or` fallback would accidentally replace `0`, `False` and `""` too.

## Walk through an example

```python
settings = {"delay": 0}
# settings.get("delay") or 10 gives 10, losing the explicit zero.
# A precise missing-value rule preserves zero.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A code review can begin with a function that looks elegant and is subtly wrong. Compare the implementation against each word of the contract. A compact use of `or` often hides a policy decision about empty values.

Here the caller distinguishes an omitted setting from an explicitly empty one. `None`, zero and an empty string are not interchangeable, even though each can be falsy. Membership in a dictionary distinguishes a missing key from an existing key, while an identity check distinguishes None from other values.

Work through a small decision table before editing. A correct repair should preserve good behavior on ordinary inputs and change only the violated cases. Pip suggests fixing every problem with a default of twelve. The on-call schedule has vetoed this approach.

</details>

## Before you run

Would this repair be correct if the contract treated a stored None as meaningful?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
