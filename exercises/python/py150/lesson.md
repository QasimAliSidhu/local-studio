# Maybe there is no ticket

Describe an optional result with a union and preserve valid falsy IDs.

## Say when a result can be absent

- **Use a union annotation.** `int | None` means the result may be an integer or `None`.

- **Check whether the collection is empty.** An empty list has no first item to index.

- **Preserve a real ID of zero.** A valid falsy integer is different from an absent result.

## Walk through an example

```python
def first_value(values: list[int]) -> int | None:
    return values[0] if values else None

result = first_value([0])
if result is not None:
    print(result)
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A type union permits more than one kind of value. `int | None` means an integer or the absence marker None. It does not mean zero should be treated as missing. Older code may spell the same idea as Optional[int].

Callers need to narrow an optional value before using integer-only operations. A check like `if result is not None:` communicates that distinction to readers and static analysis tools. A truthiness check would incorrectly discard a valid zero ID.

Type hints are especially useful at boundaries where a search may find nothing. They make the exceptional shape visible without forcing an exception for an expected empty result. They still need matching implementation and tests. Pip numbered the first ticket zero and then declared it nonexistent. The customer was less philosophical.

</details>

## Before you run

How would a caller safely use the result in an arithmetic expression?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
