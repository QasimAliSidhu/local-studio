# Paginate query results

Return one page of items using a new list slice.

## Translate a page into a slice

- **Convert from one-based pages.** Page one begins at index zero; each later page advances by the page size.

- **Take a new list slice.** The stop is excluded, and a slice past the end naturally contains fewer items or no items.

- **Validate both controls.** Require positive integers and reject booleans explicitly rather than accepting their integer behavior.

## Walk through an example

```python
items = ["a", "b", "c", "d", "e"]
start = 2
size = 2
window = items[start:start + size]  # ["c", "d"]
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Page numbers are usually **one-based** while list indices are **zero-based**. Convert the page once, then use slicing. Python slices naturally return fewer items at the end of a collection.

> [!WARNING]
> In Python, bool is a subclass of int. Reject booleans explicitly when the contract requires an actual integer.

</details>

## Before you run

Where does page one start? What should happen when the requested page begins beyond the last item?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
