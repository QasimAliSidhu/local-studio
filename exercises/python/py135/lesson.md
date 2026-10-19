# A queue, with manners

Add and remove list items while protecting the caller's list.

List methods can **change the list itself**. This is called **mutation**.

## Two useful methods

- `append(value)` adds one item at the **end**. It returns `None`.
- `pop(index)` **removes and returns** an item.
- `pop()` with no index removes the **last** item. `pop(0)` removes the **first**.

## Serve a queue

A queue serves the oldest arrival first. For this small exercise, `pop(0)` picks that first item.

> [!IMPORTANT]
> <mark>Copy before changing the caller's list.</mark> `list(waiting)` makes a new outer list. Change that copy so the caller keeps its original collection.

`pop(0)` shifts the remaining items. For large, real queues, `collections.deque` provides efficient removal from the front.

**Remember the return value:** `append` changes the list but returns `None`. It does not return the updated collection.

## Walk through an example

```python
waiting = ["backup", "email"]
remaining = list(waiting)
served = remaining.pop(0)

print(served)
print(remaining)
print(waiting)
```

<div class="example-output"><span>Console output</span><pre>backup
[&#x27;email&#x27;]
[&#x27;backup&#x27;, &#x27;email&#x27;]
</pre></div>

## Before you run

Why would return waiting.append(item) produce None?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
