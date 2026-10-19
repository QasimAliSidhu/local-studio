# Pure functions, less cleanup

Transform records immutably and use sorted with a key.

## Transform and sort without side effects

- **Construct only the requested fields.** A new dictionary keeps the output shape deliberate.

- **Use a sorting key for both rules.** Compare score descending, then name ascending when scores tie.

- **Protect every input layer.** A new list alone is insufficient if you later mutate the original record dictionaries.

## Walk through an example

```python
ordered = sorted(records, key=lambda record: record["score"], reverse=True)
# The list is new, but its records are still shared unless copied.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A pure function computes a result from explicit inputs and leaves caller-owned state unchanged. Repeating the same call with the same values produces the same result. This makes many transformations easier to test and compose.

Immutability is a design choice even when Python's objects are mutable. Construct new containers when the contract requests a transformation, and be conscious of nested references. `sorted` creates a new outer list but does not copy every record in it, so create fresh records as well when the caller needs independence.

A small lambda can supply a sorting key, while a named helper is clearer for a more substantial rule. Neither option makes an impure operation pure by itself. Pip's cleanup strategy is now 'do not spill the state in the first place'. It is surprisingly sound.

</details>

## Before you run

Why is sorted(records) alone not enough to guarantee independent result records?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
