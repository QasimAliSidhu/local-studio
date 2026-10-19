# Preserve error identity

Wrapping an error adds context while allowing errors.Is to recognize the original cause.

## Your task

Define package variable `ErrNotFound = errors.New("not found")`. `Lookup(values map[string]string, key string) (string,error)` returns a present value, including empty strings. Missing keys return an error wrapping ErrNotFound and mentioning the key.

Open **Challenge** to edit your code. Press **Run** to save it and run the checks.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
