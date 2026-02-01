import pytest
import requests

BASE_URL = "https://gorest.co.in/public/v2"


# -------------------------------------------------
# GET USERS
# -------------------------------------------------

# TC-001 — Get users list
@pytest.mark.smoke
def test_get_users_list(api):
    response = api.get("/users")
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

    user = users[0]
    assert all(field in user for field in ["id", "name", "email", "gender", "status"])


# TC-002 — Get user by valid ID
@pytest.mark.smoke
def test_get_user_by_valid_id(api, created_user):
    user_id = created_user["id"]

    response = api.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


# TC-003 — Get user by non-existing ID
@pytest.mark.negative
def test_get_user_by_non_existing_id(api):
    response = api.get("/users/999999999")
    assert response.status_code == 404


# -------------------------------------------------
# CREATE USER (POST)
# -------------------------------------------------

# TC-004 — Create user with valid payload
@pytest.mark.smoke
def test_create_user_success(api, valid_user_payload):
    response = api.post("/users", valid_user_payload)
    assert response.status_code == 201

    user = response.json()
    assert "id" in user
    assert user["email"] == valid_user_payload["email"]

    # cleanup
    api.delete(f"/users/{user['id']}")


# TC-005 — Create user with empty payload
@pytest.mark.negative
def test_create_user_empty_payload(api):
    response = api.post("/users", {})
    assert response.status_code == 422


# TC-006 — Create user with invalid email
@pytest.mark.negative
def test_create_user_invalid_email(api, valid_user_payload):
    valid_user_payload["email"] = "invalid_email"

    response = api.post("/users", valid_user_payload)
    assert response.status_code == 422


# TC-007 — Create user with missing required field (name)
@pytest.mark.negative
def test_create_user_missing_name(api, valid_user_payload):
    valid_user_payload.pop("name")

    response = api.post("/users", valid_user_payload)
    assert response.status_code == 422


# TC-008 — Create user with missing required field (email)
@pytest.mark.negative
def test_create_user_missing_email(api, valid_user_payload):
    valid_user_payload.pop("email")

    response = api.post("/users", valid_user_payload)
    assert response.status_code == 422


# TC-009 — Create user without authorization
@pytest.mark.auth
@pytest.mark.negative
def test_create_user_without_authorization(valid_user_payload):
    response = requests.post(
        f"{BASE_URL}/users",
        json=valid_user_payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    assert response.status_code == 401


# -------------------------------------------------
# UPDATE USER (PUT)
# -------------------------------------------------

# TC-010 — Update existing user
@pytest.mark.smoke
def test_update_existing_user(api, created_user, update_user_payload):
    user_id = created_user["id"]

    response = api.put(f"/users/{user_id}", update_user_payload)
    assert response.status_code == 200

    updated = response.json()
    assert updated["id"] == user_id
    assert updated["name"] == update_user_payload["name"]
    assert updated["status"] == update_user_payload["status"]


# TC-011 — Update user with invalid payload
@pytest.mark.negative
def test_update_user_invalid_payload(api, created_user):
    user_id = created_user["id"]

    response = api.put(f"/users/{user_id}", {"email": "invalid_email"})
    assert response.status_code == 422


# TC-012 — Update non-existing user
@pytest.mark.negative
def test_update_non_existing_user(api, update_user_payload):
    response = api.put("/users/999999999", update_user_payload)
    assert response.status_code == 404


# TC-013 — Update user without authorization
@pytest.mark.auth
@pytest.mark.negative
def test_update_user_without_authorization(created_user):
    user_id = created_user["id"]

    response = requests.put(
        f"{BASE_URL}/users/{user_id}",
        json={"name": "Hacker"},
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    # GoREST security behavior
    assert response.status_code == 404


# -------------------------------------------------
# DELETE USER
# -------------------------------------------------

# TC-014 — Delete existing user
@pytest.mark.smoke
def test_delete_existing_user(api, created_user):
    user_id = created_user["id"]

    response = api.delete(f"/users/{user_id}")
    assert response.status_code == 204

    check = api.get(f"/users/{user_id}")
    assert check.status_code == 404


# TC-015 — Delete non-existing user
@pytest.mark.negative
def test_delete_non_existing_user(api):
    response = api.delete("/users/999999999")
    assert response.status_code == 404


# TC-016 — Delete user without authorization
@pytest.mark.auth
@pytest.mark.negative
def test_delete_user_without_authorization(created_user):
    user_id = created_user["id"]

    response = requests.delete(
        f"{BASE_URL}/users/{user_id}",
        headers={
            "Accept": "application/json",
        },
    )

    # GoREST security behavior
    assert response.status_code == 404
