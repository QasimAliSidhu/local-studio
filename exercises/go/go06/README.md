# HTTP client with context

A reusable http.Client controls connection behavior. A request context lets callers cancel work.

## Your task

`FetchStatus(ctx context.Context, client *http.Client, url string) (int,error)` makes one GET with the context and returns its HTTP status, even for 404. Always close a received response body. Network failures return an error.

Open **Challenge** to edit your code. Press **Run** to save it and run the checks.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
