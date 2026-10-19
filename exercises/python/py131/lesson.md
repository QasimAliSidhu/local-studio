# Skip the nonsense, stop at success

Use continue and break without skipping valid falsy results.

## Skip, stop or return

- **Skip with `continue`.** Ignore an unsuitable value and move to the next one.

- **Stop with `break` or a return.** Once you have the requested first match, later values should not replace it.

- **Check all parts of the rule.** Zero is even and non-negative. Use `None` only when no value qualifies.

## Walk through an example

```python
for number in [-2, 7, 8, 10]:
    if number < 0:
        continue
    if number % 2 == 0:
        found = number
        break
# found is 8, not 10
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

`continue` skips the rest of the current loop iteration and moves to the next item. `break` exits the loop entirely. They express different decisions: 'ignore this candidate' and 'we have found enough'.

A return inside a function can also end a search immediately by returning its result. If no item qualifies, return a clear sentinel after the loop. Do not confuse a qualifying value of zero with no result; absence is represented by None in this contract.

Search order belongs in the requirements. The first qualifying item is not necessarily the smallest one, and sorting to find a minimum can silently change the requested answer. Avoid mutating the input just to inspect it. Pip's search strategy was to stop at the first number because every number deserves encouragement. Some numbers still fail the requirement.

</details>

## Before you run

Why would if found: misinterpret a successful result of zero?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
