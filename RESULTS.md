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
  - GET: 404 Not Found.
  - PUT: 400 Bad Request.
  - DELETE: 400 Bad Request.

All three attempts were refused, and the owner's rating remained unchanged.

## Part B

1. API tests can detect failures in real authentication and integration
   between the server and stored data that unit tests with stubs cannot.
   Unit tests are still useful because they are fast and isolate faults
   in individual functions.

2. Each test creates a unique user to avoid interfering with other
   students or changing shared ratings. In Project 2, I will create
   my own test data and only modify or delete records my tests created.

3. A session preserves the load balancer cookies so related requests
   reach the same server. Without these cookies, a login request may
   reach a server that does not contain the newly created user.
   I did not perform the optional three runs without a session.

4. The block excluding all three tools revealed the defect.
   A 500 response with an empty body gives the client no useful
   explanation, while a 400 response with a JSON message explains
   why the request cannot be satisfied. The test stays as a strict
   xfail to document the defect and signal when it has been fixed.

5. Base choice coverage needs:
   1 + (3 - 1) + (4 - 1) + (2 - 1) + (3 - 1) = 9 tests.
   All combinations coverage needs:
   3 × 4 × 2 × 3 = 72 combinations.

6. The other user's GET, PUT and DELETE requests returned 404, 400
   and 400 respectively. I would expect 403 Forbidden for an
   authenticated user without permission, or 404 to hide the resource.
   All attempts were refused and the rating remained unchanged.
   The different codes alone do not prove a defect because the lab
   accepts any 4xx response for these attempts.

7. The made-up token 0000000000000000 returned 200 OK and a nonempty
   list of ratings, even though it was not obtained by logging in.
   This demonstrates an authentication defect under the lab's rule
   that access requires a logged-in user's token. On a real system,
   a stranger could read the ratings exposed by this endpoint
   without valid credentials. This request does not establish
   whether unauthorized changes are possible.

8. API tests can directly check status codes, response fields and
   invalid inputs. Tests through the web pages can check visual
   layout and whether results are displayed correctly to the user.