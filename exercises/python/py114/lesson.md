# The list with two name tags

Distinguish aliasing, shallow copying and nested object mutation.

## Copy the container you will change

- **Assignment can create an alias.** Two names may refer to the same mutable list.

- **An outer copy is only shallow.** A copied record can still share its original `tags` list.

- **Copy the nested list too.** Add the new tag to an independent list, preserve the other fields and allow repeated tags.

## Walk through an example

```python
source = {"tags": ["new"], "owner": "Mira"}
copy = dict(source)
copy["tags"] = list(source["tags"])
copy["tags"].append("checked")
# source still has only "new"
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Assignment does not copy an object. If `other = original` and original is a list, both names refer to the same list. Appending through either name is visible through the other. Rebinding one name to a new list is different: it changes that binding rather than editing the shared object.

`list(original)` or `original.copy()` creates a shallow list copy. Its outer list is independent, but references to nested mutable objects are still shared. Copying a dictionary has the same shallow limitation. For a known shape, copying only the containers you intend to modify can be clearer than blindly copying an entire graph.

A non-mutating transformation makes retries and tests easier because the input remains usable. This mission has a dictionary containing a list, so copying just the dictionary is insufficient. Pip put two labels on one lunchbox and was surprised the second lunch vanished too.

</details>

## Before you run

Would copying only the outer dictionary protect its original tags list?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
