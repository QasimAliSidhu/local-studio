# Validate configuration

Validate port text, then convert it to an integer.

## Validate the text before converting

- **Trim only the outer whitespace.** An empty result is invalid.

- **Require ASCII digits.** Signs, other characters and non-ASCII digit forms are outside this contract.

- **Check the numeric range.** Convert the accepted text, then require a port from `1` through `65535`.

## Walk through an example

```python
raw = " 42 "
cleaned = raw.strip()
if not cleaned.isascii() or not cleaned.isdecimal():
    raise ValueError("Expected decimal digits")
value = int(cleaned)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Configuration arrives as text. **Normalization**, **validation**, and **conversion** are separate steps. Stripping surrounding whitespace can be acceptable even when spaces inside a number are not.

> [!WARNING]
> A conversion succeeding does not prove the value meets your application rules. Check the range as well.

</details>

## Before you run

Which inputs should be accepted? Decide what empty text, signs, decimals, and out-of-range values mean before writing the conversion.

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
