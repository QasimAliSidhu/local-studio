# Slices without paper cuts

Take part of a list and understand where the slice stops.

A **slice** selects part of a collection. Write it as `values[start:stop]`.

<figure class="list-picture" aria-label="values one to three selects twenty and thirty. Index three is excluded.">
<figcaption><strong>values[1:3]</strong><span>Keep the highlighted values</span></figcaption>
<div class="slice-cells"><div><span>0</span><code>10</code></div><div class="is-selected"><span>1</span><code>20</code></div><div class="is-selected"><span>2</span><code>30</code></div><div><span>3</span><code>40</code></div></div>
</figure>

## Read the boundaries

- **start is included:** begin at that index.
- **stop is excluded:** finish just before that index.
- Omit an end to continue to the edge of the collection.

> [!TIP]
> <mark>Start here; stop before there.</mark> `values[1:3]` selects indexes **1 and 2**.

## Steps and copies

A third value controls the step: `values[start:stop:step]`. A step of `-1` walks backward; a step of `0` is invalid.

A list slice creates a **new outer list**. Nested objects are still shared. Bounds beyond an edge are clipped to the available items.

## The zero-item case

`-0` is still `0`. That makes `values[-0:]` the same as `values[0:]`: the whole list. Handle a requested count of **0** separately.

## Walk through an example

```python
values = [10, 20, 30, 40]
print(values[1:3])
print(values[::-1])
```

<div class="example-output"><span>Console output</span><pre>[20, 30]
[40, 30, 20, 10]
</pre></div>

## Before you run

Why does values[-0:] not mean an empty tail?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
