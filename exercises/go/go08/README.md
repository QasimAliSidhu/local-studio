# Ordered concurrent work

A bounded worker pool limits parallelism. Indexed jobs let workers finish in any order while keeping results ordered.

## Your task

`Squares(ctx context.Context, values []int, workers int) ([]int,error)` computes each square with at most workers goroutines. Preserve order and input. Reject workers < 1. Honor canceled contexts and wait for workers before returning. Empty valid input returns an empty result. Use channels and sync.WaitGroup.

Open **Challenge** to edit your code. Press **Run** to save it and run the checks.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
