# A JSON HTTP endpoint

An endpoint has a **path**, allowed **methods**, a **status code**, headers, and a response body. Check the route first, then the method. Write headers before starting the body.

## Build an explicit HTTP contract

```go
func Health(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    io.WriteString(w, `{"ok":true}`)
}
```

## Think it through

When is 404 appropriate? When should the handler return 405 and an Allow header?

> **Watch for this:** The first body write commits the response headers. Set Content-Type and status before encoding JSON.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
