# Creating a rating returns its ID, stars and pizza ID.
def test_create_rating(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 5}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 201

    body = res.json()

    try:
        assert body["stars"] == 5
        assert body["pizza_id"] == pizza_id
        assert isinstance(body["id"], int)
    finally:
        api.delete(f"/api/ratings/{body['id']}", headers=auth)


# The owner can read the saved rating.
def test_read_rating(api, auth, rating):
    res = api.get(f"/api/ratings/{rating['id']}", headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# The owner can update the rating's stars.
def test_update_rating(api, auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 4}, headers=auth)
    assert res.status_code == 200
    assert res.json()["stars"] == 4


# Deleting a rating makes subsequent reads return 404.
def test_delete_rating(api, auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=auth)
    assert res.status_code == 204

    res = api.get(path, headers=auth)
    assert res.status_code == 404