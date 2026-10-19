# A name can change its mind

Reassign a variable using its previous value.

## Update a value in three steps

- **Read the old value.** In `jobs = jobs + 1`, the right-hand `jobs` means the value already stored.

- **Calculate, then assign.** Add one, then make `jobs` refer to that result.

- **Trace each print at its own line.** An earlier printed result stays the same when the variable changes later. Names are case-sensitive.

## Walk through an example

```python
jobs = 2
print(jobs)
jobs = jobs + 1
print(jobs)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Assignment can bind an existing name to a new value. In `jobs = jobs + 1`, Python first reads the old jobs value, adds one, and then assigns the result back to jobs. This is not a circular mathematical equation; it is a sequence of actions.

A print observes the value at that point in the script. It does not change later when the variable is reassigned. Trace the example one line at a time: first jobs is two, the first print displays two, the update makes jobs three, and the final print displays three.

Variable names are case-sensitive, so jobs and Jobs are different names. A new name must be assigned before you can read it. The mission keeps a single name so you can focus on the update.

This is the beginning of program state: values changing as work happens. Pip's work counter was stuck at 'busy'. A number is easier to audit.

</details>

## Before you run

In the example, why does the first printed line remain 2?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
