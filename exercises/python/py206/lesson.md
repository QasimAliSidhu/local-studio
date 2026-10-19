# Manage a resource with with

Implement the context-manager protocol after classes and cleanup are familiar.

## Enter, work, then clean up

- **Enter with `__enter__`.** Its return value becomes the name after `as` in a `with` statement.

- **Exit with `__exit__`.** Python calls it after the body, including when the body raises an error.

- **Return `False` to propagate errors.** A true return would suppress them. Keep entry and cleanup state changes balanced.

## Walk through an example

```python
class Visit:
    def __enter__(self):
        print("open")
        return self
    def __exit__(self, *details):
        print("close")
        return False

with Visit():
    print("work")
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A **context manager** defines what happens on entry to and exit from a `with` block. Python calls its __enter__ method, runs the body, and calls __exit__ when leaving, including when the body raises. It packages the try/finally cleanup pattern into a reusable object.

The value returned by __enter__ is assigned to the name after `as`. On a normal exit, __exit__ receives three None values. On failure it receives the exception type, value and traceback. Return False to let an exception continue outward; returning True would suppress it.

The two double-underscore names are special protocol hooks: Python calls them at the defined moments. You still write ordinary methods using self and the parameter rules you know. Validate the resource state inside and after a block to see that cleanup actually occurs.

File objects already implement this protocol, which makes the next chapter's file handling easier to understand. Pip would like a context manager for meetings that guarantees everyone leaves. We are starting with a simpler flag.

</details>

## Before you run

What dangerous behavior would returning True from __exit__ introduce?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
