import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"

DECIMAL_ERROR = (
    "json: cannot unmarshal number 3.5 "
    "into Go struct field Rating.stars of type int"
)

TEXT_ERROR = (
    "json: cannot unmarshal string "
    "into Go struct field Rating.stars of type int"
)


# Base choice: 3 integer stars, an existing pizza and the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}

    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 201

    body = res.json()

    try:
        assert body["stars"] == 3
        assert body["pizza_id"] == pizza_id
    finally:
        api.delete(f"/api/ratings/{body['id']}", headers=auth)


# Stars below 1 or above 5 are refused.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}


# Decimal, text and missing stars are refused.
@pytest.mark.parametrize(
    "case, expected_error",
    [
        pytest.param("decimal", DECIMAL_ERROR, id="decimal"),
        pytest.param("text", TEXT_ERROR, id="text"),
        pytest.param("missing", STARS_ERROR, id="missing"),
    ],
)
def test_invalid_stars_type(
    api, auth, pizza_id, case, expected_error
):
    new = {"pizza_id": pizza_id}

    if case == "decimal":
        new["stars"] = 3.5
    elif case == "text":
        new["stars"] = "3"

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": expected_error}


# A rating for a nonexistent pizza is refused.
def test_nonexistent_pizza_is_refused(api, auth):
    new = {"pizza_id": 999999999, "stars": 3}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": "pizza ID 999999999 not found"}


# Creating a rating without a token is refused.
def test_missing_token_is_refused(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}

    res = api.post("/api/ratings", json=new)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# Creating a rating with a short token is refused.
def test_short_token_is_refused(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    wrong_auth = {"Authorization": "token short"}

    res = api.post("/api/ratings", json=new, headers=wrong_auth)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}