# Slices and errors

Go makes failure explicit with a **value, error** return pair. Validate input before indexing into slices. A caller can inspect an error without recovering from a panic.

## Return errors as values

```go
func First(values []int) (int, error) {
    if len(values) == 0 {
        return 0, fmt.Errorf("empty slice")
    }
    return values[0], nil
}
```

## Think it through

Which validations prevent an index panic? What is the correct result for two empty input slices?

> **Watch for this:** Check lengths before using matching indices. Return a descriptive error for invalid data.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
