# HTTP client with context

A context carries a request deadline or cancellation signal. Attach it to the outgoing HTTP request so the transport can stop work when the caller no longer needs the response.

## Connect cancellation to HTTP work

```go
request, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
if err != nil { return err }
response, err := client.Do(request)
if err != nil { return err }
defer response.Body.Close()
```

## Think it through

What happens on a non-success HTTP status? Who owns closing the response body?

> **Watch for this:** Close the body only after Do succeeds, and preserve cancellation by using the supplied context.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
