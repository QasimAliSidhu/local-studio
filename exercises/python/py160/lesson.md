# Boss mission: the tiny ticket engine

Process a command stream with explicit state transitions and errors.

## Describe each state transition

- **Start from an independent copy.** The caller's initial ticket state must survive success and failure unchanged.

- **Check a command against the current state.** Adding an existing ID and closing a missing ID are invalid operations.

- **Apply valid commands in order.** Reject unknown actions clearly, then return the new state only when processing succeeds.

## Walk through an example

```python
# State transition example:
# {} --("add", 7)--> {7: False}
# {7: False} --("close", 7)--> {7: True}
# Closing a missing ID must report an error.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A small command processor combines parsing, branching, state and validation. Define each command's effect before implementing the loop. The same command can be valid or invalid depending on the current state: closing a nonexistent ticket is different from closing an existing one.

Fail clearly on invalid operations rather than silently creating surprising state. Work on a copy so even a later failure cannot partially alter caller-owned data. This is a simple form of transactional thinking, although it is not a database transaction.

Break the problem into initialization, one-command handling and final output. Use readable branches; a clever nested expression is not a requirement. This checkpoint is designed to be harder than earlier drills. Ask the tutor for a hint about one failing case at a time. Pip is now managing tickets. The team has bravely left the building.

</details>

## Before you run

Why is copying before the command loop important when a later command fails?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
