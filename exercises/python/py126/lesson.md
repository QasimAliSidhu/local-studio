# Choose one response

Order if/elif/else branches so specific rules are reachable.

## Put specific branches first

- **Test the largest threshold first.** A status of `503` also meets lower thresholds, so order matters.

- **Continue with `elif`.** Python runs the first matching branch in an `if` / `elif` / `else` chain.

- **Finish with the remaining case.** An `else` handles valid inputs that met none of the earlier thresholds.

## Walk through an example

```python
if status >= 500:
    label = "server error"
elif status >= 400:
    label = "client error"
else:
    label = "other"
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An `if` branch runs only when its condition is truthy. `elif` tries another condition if earlier branches did not match, and `else` handles the remaining case. Only one branch in this chain runs. Indentation defines which instructions belong to each branch.

Branch order matters when conditions overlap. A general condition placed first can swallow a more specific case. Write the priority rule in words, then test overlaps deliberately. Independent `if` statements mean something different: several bodies can run.

An early return can make a guard clause clear, especially for invalid or exceptional states. It also means later code is skipped. Keep your decision table small enough to reason about and use exact status values rather than guessing from substrings. Pip would like every server response to be 'probably fine'. The monitoring team has declined.

</details>

## Before you run

Why would checking status >= 200 first misclassify a 503?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
