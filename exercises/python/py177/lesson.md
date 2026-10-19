# Lowercase without losing the original

Use lower as a second example of a string method.

## Make a lowercase copy

- **Call `status.lower()`.** The dot finds the method; the parentheses run it.

- **Use the returned result.** Assign it to a new name. The original string stays unchanged.

- **Change case deliberately.** Numbers and punctuation stay in place. Lowercasing is appropriate for this label, not every kind of text.

## Walk through an example

```python
raw = "READY-7!"
normalized = raw.lower()
print(normalized)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

The string method `lower()` returns a version with uppercase letters changed to lowercase. Its calling shape is the same as strip: put the method after a dot and keep the parentheses. A method name without parentheses refers to the tool rather than running it.

Like strip, lower leaves the original string unchanged. The returned value needs to be assigned or used. Numbers and punctuation in the text stay as they are; lower is not a general cleaning rule.

Case normalization can make a display label consistent, but it is a choice you should state. Passwords, for example, must not be silently lowercased. Here we are working only with a status label.

Read the example in three steps: create raw text, make normalized text, display the normalized value. The next lesson will combine methods you have now practiced individually. Pip's dashboard used to shout every status, including 'everything is quiet'.

</details>

## Before you run

Which characters in READY-7! change, and which remain?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
