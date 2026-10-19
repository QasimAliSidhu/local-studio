# Strict JSON input

A decoder can accept JSON that your endpoint should reject. Strict input handling checks **unknown fields**, **required values**, and whether any second JSON value follows the first one.

## Define a strict JSON boundary

```go
decoder := json.NewDecoder(reader)
decoder.DisallowUnknownFields()
if err := decoder.Decode(&request); err != nil {
    return err
}
// Then check that the next decode returns io.EOF.
```

## Think it through

How do you distinguish trailing whitespace from a second JSON object? Which values are invalid after decoding?

> **Watch for this:** A successful first decode does not prove the whole input contained only one value.

## Put it into practice

Read the task in **Challenge**, write your implementation, then press **Run**. Use **Tests** to inspect the expected behavior and **Console** to understand failures.

**Before revealing the solution,** explain your approach and test one edge case yourself.
