# A FIFO job queue

Build a queue that serves the oldest job first.

## Keep a queue first-in, first-out

- **Append at the back.** `deque.append(job)` adds a new arrival.

- **Remove from the front.** `deque.popleft()` removes and returns the oldest job efficiently.

- **Keep storage per instance.** Implement `__len__` for `len(queue)` and let an empty removal raise `IndexError`.

## Walk through an example

```python
class Mailbox:
    def __init__(self):
        self.messages = []

first = Mailbox()
second = Mailbox()
first.messages.append("hello")
# second.messages is still empty
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A queue follows **first in, first out**. Each queue object needs its own storage. Initialize mutable state inside the constructor so two objects do not accidentally share jobs.

> [!WARNING]
> A mutable class attribute is shared by instances. Put per-queue storage on self in __init__.

</details>

## Before you run

Which end receives new jobs? Which end removes the oldest one? What is the empty-queue contract?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
