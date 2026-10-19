# Cache expiry

## Your mission

- Implement `Cache`: `set(key, value, ttl, now)` stores a value with deadline now+ttl; negative TTL raises ValueError.

- `get(key, now)` returns the stored value if now is before deadline, otherwise None.

- Overwrites replace the deadline.

- Each instance is independent.

This is a **function challenge**: Run calls the tests for debugging without completion credit. Follow the function's return-value contract.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
