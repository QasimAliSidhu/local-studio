# Manage a resource with with

## Your mission

- Implement ManagedFlag.

- It starts with active=False.

- __enter__ sets active=True and returns self.

- __exit__(exc_type, exc, traceback) sets active=False and returns False, so errors propagate.

- Reusing the same instance for sequential blocks is allowed.

This is a **function challenge**: Run calls the tests for debugging without completion credit. Follow the function's return-value contract.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
