# Ordered concurrent work

A worker pool limits the number of concurrent operations. Assign each job an **index** so completion order can differ from result order. A WaitGroup lets the caller wait until every worker has finished.

## Coordinate workers and preserve order

```go
type Job struct {
    Index int
    Value string
}
// Each worker processes a job, then stores its result
// in the output slot identified by job.Index.
```

## Think it through

Can two workers write the same result slot? When should the jobs channel close? Who waits for the workers?

> **Watch for this:** Appending concurrently introduces races and changes ordering. Allocate result slots and give each job a unique index.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
