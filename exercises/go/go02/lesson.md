# Count words with maps

A missing integer entry in a Go map reads as **zero**. That makes counting straightforward once you have allocated the map. Decide how text should be normalized before using tokens as keys.

## Use map zero values

```go
counts := make(map[string]int)
for _, label := range []string{"api", "db", "api"} {
    counts[label]++
}
```

## Think it through

Are uppercase and lowercase forms equivalent in this task? How should whitespace split the input?

> **Watch for this:** You can read from a nil map, but writing to one panics. Allocate the map before updating counts.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
