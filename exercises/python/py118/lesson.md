# Test the test, detective

Write assertions that detect several different broken implementations.

## Check the behavior of a supplied function

- **Call the candidate.** Test what it does rather than inspecting its source text.

- **Use assertions for expected results.** A false assertion raises `AssertionError`.

- **Choose revealing cases.** Zero, a negative input and a positive input expose different mistakes; successful checks need no explicit result.

## Walk through an example

```python
def check_identity(candidate):
    assert candidate(0) == 0
    assert candidate(9) == 9
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

An assertion expresses something that must be true. `assertEqual(actual, expected)` reports the values when they differ. In ordinary Python, `assert condition` raises `AssertionError` if the condition is false. Assertions are useful for internal expectations and tests, but are not a replacement for validating untrusted input: Python can disable assert statements under optimization.

A test that only checks one happy example may approve a broken implementation. Choose cases for different risks: zero, negative numbers, and a representative positive value. Testing a candidate that always returns the same answer exposes weak tests quickly.

This mission reverses the usual roles. You supply the checks and our suite feeds them both a correct function and impostors. Pip's first test was 'seems fine'. Pip's second test was 'still seems fine'. We need stronger evidence.

</details>

## Before you run

Why would checking only candidate(4) let an always-8 function pass?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
