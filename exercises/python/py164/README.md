# Compose the delivery crew

## Your mission

- Define frozen dataclass Notice(recipient:str, text:str).

- Implement Dispatcher(transport).

- deliver(notice) calls transport.send(notice.recipient, notice.text) once and returns that call's result.

- Let transport errors propagate.

This is a **function challenge**: Run calls the tests for debugging without completion credit. Follow the function's return-value contract.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
