# The console is not the return value

Recognize a print-versus-return mistake in a graded function.

## Check the value and the console separately

- **A return value goes to the caller.** It is what another expression or a test can use.

- **A print goes to the console.** Displaying the right number does not return that number.

- **Honor both parts of the contract.** Return the requested result and leave the console quiet when printing is forbidden.

## Walk through an example

```python
def show_total(amount):
    print(amount + 2)

saved = show_total(10)
print(saved)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A familiar source of confusion is seeing the right number in the console while a test still fails. The test may be checking a returned value, not printed text. A function that only prints reaches its end without explicitly returning a value; its caller receives None.

Trace the example: show_total displays twelve, but saved becomes None because printing has not supplied a return result. The final print therefore displays None. A useful calculation can return twelve and let its caller decide whether to display it.

Read each task's contract. Some early script missions explicitly ask for console output; a function challenge normally names the function and the value it should return. Our editor labels the active file, and the assignment states the expected behavior.

This lesson repeats a concept in a debugging setting rather than introducing a new syntax shortcut. Pip printed a shipping label and considered the parcel delivered. The receiving function disagreed.

</details>

## Before you run

Why does saved become None in the example even though 12 appears in the console?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
