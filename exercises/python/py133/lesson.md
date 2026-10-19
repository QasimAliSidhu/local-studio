# First, last, and absolutely not there

Pick the first and last items without going past the ends.

An **index** is an item's position. Python starts counting positions at **0**.

<figure class="list-picture" aria-label="backup is at index zero, email at index one, and report at index two.">
<figcaption><strong>jobs</strong><span>Positions start at zero</span></figcaption>
<div class="index-map"><div class="index-item"><span>Index 0</span><code>"backup"</code></div><div class="index-item"><span>Index 1</span><code>"email"</code></div><div class="index-item"><span>Index 2</span><code>"report"</code></div></div>
</figure>

## Pick one item

- `jobs[0]` selects the **first** item.
- `jobs[-1]` selects the **last** item.
- The last positive index is `len(jobs) - 1`.

> [!WARNING]
> <mark>Check for an empty collection before indexing.</mark> An empty list has no first or last item. An invalid index raises `IndexError`.

## Lists and tuples

Both support indexes and `len`. A list can grow or have items replaced; a tuple's existing items cannot be reassigned. A list inside a tuple can still change.

**First and last describe the original order.** They do not mean smallest and largest.

## Walk through an example

```python
jobs = ["backup", "email", "report"]
print(jobs[0])
print(jobs[-1])
```

<div class="example-output"><span>Console output</span><pre>backup
report
</pre></div>

## Before you run

Why is the last item not necessarily the largest item?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
