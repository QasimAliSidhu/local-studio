# Preserve error identity

Wrapping an error adds context while preserving its identity. Use **%w** in fmt.Errorf so callers can still inspect the original cause with **errors.Is**.

## Preserve the cause of an error

```go
var ErrClosed = errors.New("closed")

err := fmt.Errorf("read cache: %w", ErrClosed)
// errors.Is(err, ErrClosed) is true
```

## Think it through

Can the caller distinguish a missing record from another failure? What extra context helps locate the problem?

> **Watch for this:** Formatting with %v produces a readable message but does not wrap the underlying error.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
