# Interfaces for storage usage

An **interface** describes methods a value must provide. Code using that interface can ask for the behavior it needs without knowing the concrete type behind each value.

## Program against behavior

```go
type Named interface {
    Name() string
}

func Label(value Named) string {
    return value.Name()
}
```

## Think it through

Which single method gives the information needed by the aggregator? Does your code need to know the underlying type?

> **Watch for this:** Avoid type switches when the interface already exposes the required method.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
