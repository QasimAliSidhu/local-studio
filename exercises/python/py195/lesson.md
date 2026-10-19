# Several values, one ordered list

Keep related values together, then count them.

A **list** keeps related values together, in order. Think of it as a row of boxes, with one value in each box.

<figure class="list-picture" aria-label="The list jobs contains backup, email and report: three items.">
<figcaption><strong>jobs</strong><span>One list, three items</span></figcaption>
<div class="list-items"><code>"backup"</code><span aria-hidden="true">,</span><code>"email"</code><span aria-hidden="true">,</span><code>"report"</code></div>
</figure>

## Write a list

- Put **square brackets** `[ ]` around the values.
- Use a **comma** between items.
- Give the collection a name, such as `jobs`.

## Count the items

`len(jobs)` tells you how many items the list holds. An empty list, `[]`, has a length of **0**.

> [!TIP]
> <mark>Count items, not letters.</mark> A list containing only `"backup"` has **one item**, even though that word has six letters.

## Walk through an example

```python
jobs = ["backup", "email", "report"]
print(len(jobs))
```

<div class="example-output"><span>Console output</span><pre>3
</pre></div>

## Before you run

Why does len(["backup"]) return one rather than six?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
