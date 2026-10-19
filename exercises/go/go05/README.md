# Strict JSON input

Decoding and validation are separate steps. Reject unknown fields and extra JSON documents at an API boundary.

## Your task

Implement `DecodeTask(r io.Reader) (Task,error)` for `Task{Title string, Done bool}` with JSON tags. Accept one JSON object only; reject unknown fields, malformed or extra JSON, and blank titles. Trim the title. Missing done defaults to false.

Open **Challenge** to edit your code. Press **Run** to save it and run the checks.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
