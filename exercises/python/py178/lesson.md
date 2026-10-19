# Put a value inside a message

Build a basic f-string before using format specifiers.

## Put a value inside text

- **Start with `f`.** An f-string begins like `f"Worker {name}"`.

- **Put expressions inside braces.** `{name}` inserts the variable's current value; text outside braces stays literal.

- **Let Python display numbers.** You can insert several values without converting each one to a string yourself.

## Walk through an example

```python
name = "Mira"
jobs = 3
message = f"{name} has {jobs} jobs"
print(message)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A string written with f before its opening quote is an **f-string**. Text inside braces `{...}` is evaluated and inserted into the message. Text outside braces stays as written. This is useful when a sentence includes a named value.

In `f"Worker {name}"`, the braces mean 'insert the current value of name here'. Leaving off the f means the braces are ordinary characters instead. Quoting the word name inside the braces would insert that word rather than reading the variable.

An f-string can include several values, including numbers. Python makes a readable text representation when inserting them. You do not need to convert an integer to a string yourself for this form.

Predict the example: it displays Mira has 3 jobs. The variable names and braces are not in the output. Pip has requested a dashboard where every message contains its name. For one lesson, we can indulge that.

</details>

## Before you run

What would print("{name} has {jobs} jobs") display without the f?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
