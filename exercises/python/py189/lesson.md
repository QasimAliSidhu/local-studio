# Choose which instruction runs

Introduce if, else and indentation using a comparison you understand.

## Choose one branch

- **Write a condition after `if`.** A true condition runs the indented instructions beneath it.

- **Use `else` for the other case.** Only the selected branch runs.

- **Keep the messages with the right condition.** Trace the supplied value first, then check which message belongs in that branch.

## Walk through an example

```python
jobs = 2
if jobs > 0:
    print("busy")
else:
    print("idle")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An `if` statement lets a boolean result choose what happens next. Put a condition after if and finish its line with a colon. The indented body runs only when that condition is True. An optional `else:` body runs when it is False.

The indentation marks the two bodies, just as indentation marked a function body earlier. An unindented line afterward runs regardless of the decision. Only one side of this if/else choice runs.

Trace the example with jobs equal to two, then with jobs equal to zero. The first case prints busy and the second prints idle. The script does not print both labels, and it does not keep repeating the condition; repetition is a later topic.

This is your first branch. More complex rules should be built from clear small decisions rather than guessed punctuation. Pip's scheduling rule was to do both choices simultaneously. The printer is still recovering.

</details>

## Before you run

Which body would run if jobs were changed to one?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
