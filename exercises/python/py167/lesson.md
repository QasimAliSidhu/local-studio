# Recursion with an exit sign

Use a base case and reduce a nested problem on each call.

## Give recursion a stopping case

- **Recognize a leaf first.** An integer already has the numeric value you need.

- **Apply the same rule to smaller parts.** For a list, process each child and combine the returned sums.

- **Make the empty case natural.** An empty list contributes zero. Deep or cyclic inputs need additional care beyond this task's guarantees.

## Walk through an example

```python
def leaf_sum(node):
    if isinstance(node, int):
        return node
    return sum(leaf_sum(child) for child in node)

# leaf_sum([1, [2, 3]]) == 6
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A recursive function calls itself on a smaller version of the problem. It needs a base case that returns without another recursive call, plus a step that makes progress toward that base case. Without either, it can recurse until Python's recursion limit is reached.

Nested trees are a natural example because each child has the same shape as its parent. A flat loop is often simpler for flat data. Recursion uses call-stack space, so it is not a universal replacement for iteration, especially for extremely deep structures.

Define the allowed input shape precisely. Here leaves are integers and branches are lists; there are no cyclic references. An empty branch contributes zero. Negative and zero leaves still count as values. Pip put an exit sign in every hallway except the one leading to itself. Your base case needs to do actual work.

</details>

## Before you run

Why would a list containing itself violate this function's termination assumptions?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
