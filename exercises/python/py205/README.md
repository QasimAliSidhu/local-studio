# Wrap a function without changing its job

## Your mission

- Implement logged(operation, history).

- Return a wrapper preserving operation.__name__.

- Each call appends its positional args tuple to history, calls operation once with all positional and keyword arguments, and returns its result.

- Let errors propagate; their calls must still be logged.

This is a **function challenge**: Run calls the tests for debugging without completion credit. Follow the function's return-value contract.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
