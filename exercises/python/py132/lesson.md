# Nested loops, tiny city

Traverse a grid in a defined order using nested iteration.

## Visit a grid in a predictable order

- **Use an outer loop for rows.** Each row is visited before moving to the next.

- **Use an inner loop for columns.** Finish every column in the current row first: this is row-major order.

- **Collect coordinate tuples.** Each cell needs a `(row, column)` pair; either zero dimension means there are no cells.

## Walk through an example

```python
cells = []
for row in range(2):
    for column in range(3):
        cells.append((row, column))
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A nested loop runs an inner iteration for each outer value. With rows outside and columns inside, the traversal visits every column in the first row before moving to the next row. Reversing the loops changes order even if it visits the same coordinate pairs.

Nested iteration can multiply work: rows times columns visits, rather than rows plus columns. For a small grid that is expected. For large datasets, understand the cost before nesting searches thoughtlessly. `enumerate(sequence)` is useful when you need both a position and a value, and `zip` pairs values from separate sequences until the shorter ends.

Coordinates are pairs, naturally represented by tuples. Accumulate them in a list when order matters. An empty dimension means there are no cells. Pip drew a server room map with columns first and forgot to tell anyone. Three engineers are now in the stationery cupboard.

</details>

## Before you run

How many iterations does a 100 by 100 grid require?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
