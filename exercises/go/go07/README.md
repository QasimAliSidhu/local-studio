# A JSON HTTP endpoint

An http.Handler can be tested directly with httptest, without opening a public network port.

## Your task

`HealthHandler() http.Handler` serves GET /health with 200 and JSON {"status":"ok"}; Content-Type must include application/json. Other paths return 404. Other methods on /health return 405 with Allow: GET.

Open **Challenge** to edit your code. Press **Run** to save it and run the checks.

**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.
