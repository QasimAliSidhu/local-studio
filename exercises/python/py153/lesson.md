# Mission: the noisy incident report

Combine string normalization, counting and deterministic ordering.

## Build the report in stages

- **Split and normalize.** `text.split()` separates whitespace-delimited words; lowercase each token as specified.

- **Count the resulting tokens.** Punctuation stays part of each word unless the contract says otherwise.

- **Sort for a predictable report.** Return word/count pairs in word order, with an empty list when there are no words.

## Walk through an example

```python
counts = {}
for word in "Ping ping PONG".split():
    key = word.lower()
    counts[key] = counts.get(key, 0) + 1
# {"ping": 2, "pong": 1}
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

Integration problems ask you to choose the tools rather than name one in advance. Break the contract into stages: tokenize the input, normalize each token, count occurrences, then produce a predictable output order. Each stage should have one clear meaning.

`text.split()` separates on arbitrary whitespace and discards empty pieces. It differs from `split(" ")`, which treats literal spaces as separators and can retain empty pieces. Lowercasing can merge equivalent words. Punctuation remains unless the contract asks you to remove it.

Sorting output makes a report reproducible even when dictionary insertion order depends on the input. Test the empty report and repeated mixed-case words. This is a small pure function you could later put behind a CLI or file-reading boundary. Pip wrote an incident report consisting entirely of 'ALERT alert Alert'. At least the word count is impressive.

</details>

## Before you run

What should change in the contract before you start removing punctuation?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
