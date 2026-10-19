# Hand a result back

Explain return separately from printing before graded function challenges.

## Return a result to the caller

- **Use `return` for a result.** The caller can store that value, calculate with it or print it.

- **Keep printing separate.** Printing displays text in the console; it does not supply the function's return value.

- **Stop at `return`.** It ends the current call. Reaching the end without one returns `None`; `pass` is only a do-nothing placeholder.

## Walk through an example

```python
def triple(number):
    return number * 3

answer = triple(4)
print(answer)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A function can hand a result back to its caller with `return`. The caller can assign that value, calculate with it or pass it to print. Returning is different from printing: printing displays something, while returning makes a result available to another part of the program.

Read the example in order. Defining triple does not calculate yet. The call triple(4) runs the body and returns twelve. That value is assigned to answer, and print(answer) displays it. The function itself does not print.

A return ends the current call, so instructions after an unconditional return in the same body will not run. You can test a useful function with several inputs instead of tying it to one display message.

The next lesson will remove the example calls from the editor because the test runner will call your function for you. You will know exactly which function to define and which result it must return. Pip has finally learned that printing a receipt is not the same as returning the borrowed biscuits.

If a function finishes without a return statement, its result is `None`, Python's marker for no value. A provided `pass` line is a placeholder that does nothing; replace it with the instructions required by the mission.

</details>

## Before you run

Which example line displays text, and which line hands a numeric result back?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
