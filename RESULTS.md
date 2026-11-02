# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: "name":"A Black Siciliana"
- Step 0.12, results of the three runs without a session (optional):
- Step 0.16, blocks of "how many of the three tools are excluded":
    - 0 tools excluded.
    - 1 tool excluded.
    - 2 tools excluded.
    - 3 tools excluded
The original tests cover only the block with 1 tool excluded.

## Defect report

- Title: Excluding all available tools returns an internal server error.
- Request: POST /api/pizza with a valid authorization header and body {"excludedTools":["Knife","Pizza cutter","Scissors"]}.
- Expected result: Status 400 with a JSON error message explaining that no pizza can satisfy the restrictions.
- Actual result: Status 500 with an empty response body.
- Severity: Medium. An invalid combination of restrictions causes a server error and gives the client no useful explanation.

## Part A

- Step A4, status codes when the other user reads, changes and deletes:

## Part B

1.
2.
3.
4.
5.
6.
7.
8.