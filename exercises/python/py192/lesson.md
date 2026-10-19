# A failing example is a clue

Fix one arithmetic rule using known input and expected output.

## Use a small failure as evidence

- **Compare expected and actual results.** A failing check shows a specific mismatch to investigate.

- **Try a tiny set of inputs.** Positive, zero and negative values can expose different wrong assumptions.

- **Fix the rule for every call.** Return the calculation rather than printing or hardcoding one expected answer.

## Walk through an example

```python
def broken_double(number):
    return number + 2

print(broken_double(2))
print(broken_double(5))
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **test** runs your program with an input and compares the actual result with an expected result. If the two differ, it reports a failure. Read it as a small reproducible example: 'with this input, I expected this value, but observed that value'.

A function can be valid Python and still implement the wrong rule. Syntax tells Python how to read your instructions; the contract tells you which behavior those instructions need to produce. Changing random punctuation is less useful than finding the first point where behavior differs from the rule.

The example function adds two when its name and contract say to double. It happens to work for input two, so one passing example is weak evidence. Try zero and another positive number to reveal the difference.

Start with this small arithmetic bug before debugging loops or stateful callbacks. Pip's first test was 'it ran'. We would also like it to do the requested job.

</details>

## Before you run

Which example input accidentally makes the broken rule look correct?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
