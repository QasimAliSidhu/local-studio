# SQLite task storage

## Your mission

- Implement `create_schema(conn)`, `add_task(conn, title)` returning the integer id, and `list_tasks(conn)` returning `(id, title)` tuples in id order.

- Schema: tasks(id INTEGER PRIMARY KEY, title TEXT NOT NULL).

- Strip titles and reject empty ones.

- Commit writes.

- Use SQL parameters.

This is a **function challenge**: Run calls the tests for debugging without completion credit. Follow the function's return-value contract.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
