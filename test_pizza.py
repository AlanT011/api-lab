import requests

SITE = "https://quickpizza.grafana.com"
AUTH = {"Authorization": "token abcdef0123456789"}
VEGETARIAN = {"mustBeVegetarian": True}


# A vegetarian pizza has a name and only vegetarian ingredients.
def test_vegetarian_pizza():
    res = requests.post(
        SITE + "/api/pizza",
        json=VEGETARIAN,
        headers=AUTH,
    )
    assert res.status_code == 200

    pizza = res.json()["pizza"]
    assert pizza["name"] != ""

    for ingredient in pizza["ingredients"]:
        assert ingredient["vegetarian"] is True, ingredient["name"]


# A pizza request without authentication is refused.
def test_pizza_without_token_is_refused():
    res = requests.post(SITE + "/api/pizza", json=VEGETARIAN)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}