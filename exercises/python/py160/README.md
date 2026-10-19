# Boss mission: the tiny ticket engine

## Your mission

- Implement ticket_engine(initial, commands).

- Copy initial (ID -> done bool).

- Commands are (action, ID) tuples: "add" inserts False and rejects an existing ID; "close" sets True and rejects a missing ID.

- Unknown actions also raise ValueError.

- Return the new state.

- Never change initial, even on failure.

This is a **function challenge**: Run calls the tests for debugging without completion credit. Follow the function's return-value contract.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
