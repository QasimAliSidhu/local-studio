# Async without the spaghetti

Await coroutines concurrently while retaining input order.

## Await several operations together

- **Call an `async def` to get a coroutine.** Awaiting lets cooperative asynchronous work share the event loop; it is not automatically a background thread.

- **Gather the operations concurrently.** `asyncio.gather` returns results in input order even when completion order differs.

- **Keep waiting asynchronous.** Blocking calls stall the event loop. Use the supplied fetch operation and let its errors propagate.

## Walk through an example

```python
import asyncio

async def collect(keys, fetch):
    return await asyncio.gather(*(fetch(key) for key in keys))

# asyncio.run(collect(keys, fetch)) is an entry point from synchronous code.
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An `async def` function returns a coroutine when called. Awaiting it lets an event loop manage its progress. While a coroutine waits on cooperative asynchronous work, other tasks may run. This is useful for many I/O workloads; it does not automatically make CPU-heavy Python code run in parallel.

Awaiting several calls one after another is sequential. `asyncio.gather` schedules supplied awaitables together and returns results in the same order as the supplied awaitables, even when completion order differs. Exceptions normally propagate to the awaiting caller.

Blocking operations such as time.sleep inside an async function block the event-loop thread; use async-aware operations when waiting. Our tests use fake fetch operations, so there is no network dependency. Pip made a function async and expected the coffee machine to run faster. The keyword has politely declined responsibility.

A coroutine is not a background thread. Awaiting it gives the event loop a chance to run other ready asynchronous work. The supplied fetch function already follows that async contract, so the exercise needs no live network access.

</details>

## Before you run

Why does awaiting fetch inside a normal for loop fail the concurrency test?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
