# Interfaces for storage usage

A small interface describes behavior without coupling the caller to a concrete type.

## Your task

Keep interface `Sized { Size() int64 }`. Implement `TotalSize(items []Sized) int64`, summing sizes. Empty input returns zero. Inputs are valid non-nil implementations.

Open **Challenge** to edit your code. Press **Run** to save it and run the checks.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
