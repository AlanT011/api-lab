import uuid


def new_user():
    return {
        "username": "lab-" + uuid.uuid4().hex[:12],
        "password": "Pizza-2026",
    }


# Registering an existing username is refused.
def test_duplicate_username_is_refused(api):
    user = new_user()

    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# A registered user cannot log in with a wrong password.
def test_wrong_password_is_refused(api):
    user = new_user()

    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    wrong = {**user, "password": "Wrong-password"}

    res = api.post("/api/users/token/login", json=wrong)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# Registration refuses an empty username.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}

    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}