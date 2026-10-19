# Compose the delivery crew

Use a dataclass for a record and inject a collaborator.

## Separate the record from its delivery

- **Use a dataclass for the record.** Annotated fields declare the recipient and text; `frozen=True` prevents ordinary field reassignment.

- **Use composition for delivery.** A dispatcher holds a transport object and delegates sending to it.

- **Preserve the transport's behavior.** Call `send` once, return its result and let its errors propagate.

## Walk through an example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Message:
    recipient: str
    text: str

# A sender can accept any transport with a send method.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Composition means one object uses another object to do part of its work. Passing a collaborator into the constructor makes the dependency explicit and lets tests supply a harmless fake instead of making a real network call.

A dataclass generates common record behavior, including initialization and equality, from annotated fields. `frozen=True` rejects ordinary field reassignment. It does not make every possible nested object deeply immutable, so choose field types deliberately.

Separate the data record from the service responsible for sending it. The service should call the supplied transport rather than construct an invisible global dependency. This improves testability and makes later transport changes local. Pip hired a notification service that only notifies itself. We are introducing a collaborator and a written contract.

The `@dataclass(frozen=True)` line applies a standard-library decorator to the class below it. It generates record behavior from the annotated fields. You do not need to write a decorator yourself yet; the advanced patterns chapter explains that general mechanism.

</details>

## Before you run

Why is passing a fake transport better than sending a real message in a unit test?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
