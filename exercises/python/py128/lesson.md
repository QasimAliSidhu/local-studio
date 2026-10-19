# Missing is not the same as empty

Distinguish truthiness from a precise missing-value test.

## Distinguish missing from empty

- **Check `is None` explicitly.** This asks whether no value was supplied.

- **Preserve other values.** `""`, `0`, `False` and `[]` can all be deliberate inputs.

- **Avoid an accidental fallback.** `supplied or fallback` replaces every falsy input, which is broader than this rule.

## Walk through an example

```python
chosen = "default" if supplied is None else supplied
# supplied == "" stays empty.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Empty containers, empty strings, zero, False and None are all falsy. That makes `if values:` convenient when you want to know whether a collection has members. It is too broad when your rule is specifically about absence.

`value or fallback` chooses the fallback for every falsy value. If an empty label or numeric zero is a legitimate user choice, this silently overwrites it. `value is None` expresses the narrower rule. Use `is` for this singleton absence marker and `==` for ordinary value equality.

Defaults belong in a documented contract, not in a guess about what the caller meant. Test an omitted value and each allowed empty value separately. Pip renamed an intentionally blank status to 'MYSTERY' because blank looked suspicious. It was a feature, briefly, until somebody noticed.

</details>

## Before you run

When would using truthiness be the correct rule instead?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
