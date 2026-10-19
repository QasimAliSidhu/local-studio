# Lazy work is sometimes good work

Yield values on demand and stop consuming when the caller stops.

## Produce values only when requested

- **Use an iterator for one-at-a-time work.** `iter` obtains one and `next` asks it for another value.

- **Use `yield` or a generator expression.** Computation can pause between results instead of building a whole list.

- **Respect one-shot inputs.** Avoid pre-consuming or restarting the source; yield qualifying values in their original order.

## Walk through an example

```python
def positives(values):
    for value in values:
        if value > 0:
            yield value

stream = positives(iter([-1, 3, 4]))
next(stream)  # 3; 4 has not been requested yet
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A generator function contains `yield`. Calling it creates an iterator without running the entire body. Each request for a next value resumes execution until another yield or completion. This supports streaming data without building the full result in memory.

Laziness also affects side effects: input values should not be consumed before the caller asks for output. A generator can skip several nonmatching values before yielding a match, but it should not eagerly read past that match.

Iterators are usually one-shot. Once exhausted, they do not automatically restart. Lists are reusable collections; an iterator over a list tracks a particular traversal. Choose the interface according to the workload. Pip calls every unfinished task 'lazy evaluation'. This is the one lesson where the phrase might be justified.

The built-in iter(collection) supplies an iterator and next(iterator) asks for its next value. A generator expression such as `(value * 2 for value in values)` is the lazy counterpart of a list comprehension: it yields results on demand rather than constructing a full list.

</details>

## Before you run

Why can a lazy iterator handle a very large stream better than a list comprehension?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
