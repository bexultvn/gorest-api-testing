from data.payloads import valid_user_payload,update_user_payload
import requests
BASE_URL = "https://gorest.co.in/public/v2"


#TC-001 — Get users list
def test_get_users_list(api):
    response = api.get("/users")
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

    user = users[0]
    assert "id" in user
    assert "name" in user
    assert "email" in user
    assert "gender" in user
    assert "status" in user


#TC-002 — Get user by valid ID
def test_get_user_by_valid_id(api):
    users_response = api.get("/users")
    user_id = users_response.json()[0]["id"]

    response = api.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


#TC-003 — Get user by non-existing ID
def test_get_user_by_non_existing_id(api):
    response = api.get("/users/999999999")
    assert response.status_code == 404


#TC-004 — Create user with valid payload
def test_create_user_success(api):
    payload = valid_user_payload()

    response = api.post("/users", payload)
    assert response.status_code == 201

    user = response.json()
    assert "id" in user
    assert user["email"] == payload["email"]


#TC-005 — Create user with empty payload
def test_create_user_empty_payload(api):
    response = api.post("/users", {})
    assert response.status_code == 422


#TC-006 — Create user with invalid email
def test_create_user_invalid_email(api):
    payload = valid_user_payload()
    payload["email"] = "invalid_email"
    response = api.post("/users",payload)
    assert response.status_code == 422

#TC-007 — Create user with missing required field (name)
def test_create_user_missing_name(api):
    payload = valid_user_payload()
    payload.pop("name")

    response = api.post("/users", payload)
    assert response.status_code == 422


#TC-008 — Create user with missing required field (email)
def test_create_user_missing_email(api):
    payload = valid_user_payload()
    payload.pop("email")

    response = api.post("/users", payload)
    assert response.status_code == 422


#TC-009 — Create user without authorization
def test_create_user_without_authorization():
    payload = valid_user_payload()

    response = requests.post(
        url=f"{BASE_URL}/users",
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )

    assert response.status_code == 401


#TC-010 — Update existing user
def test_update_existing_user(api):
    create_resp = api.post("/users",valid_user_payload())
    assert create_resp.status_code == 201

    user = create_resp.json()
    user_id = user["id"]

    update_payload = update_user_payload()
    update_resp = api.put(f"/users/{user_id}",update_payload)
    assert update_resp.status_code == 200

    updated_user = update_resp.json()
    assert updated_user["id"] == user_id
    assert updated_user["name"] == update_payload["name"]
    assert updated_user["status"] == update_payload["status"]


#TC-011 — Update user with invalid payload
def test_update_user_invalid_payload(api):
    create_resp = api.post("/users",valid_user_payload())
    assert create_resp.status_code == 201

    user_id = create_resp.json()["id"]

    update_resp = api.put(
        f"/users/{user_id}",
        {"email": "invalid_email"}
    )

    assert update_resp.status_code == 422


#TC-012 — Update non-existing user
def test_update_non_existing_user(api):
    non_existing_user_id = 999999999
    payload = update_user_payload()

    response = api.put(f"/users/{non_existing_user_id}",payload)
    assert response.status_code == 404


#TC-013 — Update user without authorization
def test_update_user_without_authorization(api):
    create_resp = api.post("/users",valid_user_payload())
    assert create_resp.status_code == 201

    user_id = create_resp.json()["id"]

    update_resp = requests.put(
        f"{BASE_URL}/users/{user_id}",
        json={"name": "Hacker"},
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )

    # GoREST returns 404 for unauthorized update to avoid resource disclosure
    assert update_resp.status_code == 404


#TC-014 — Delete existing user
def test_delete_existing_user(api):
    create_resp = api.post("/users", valid_user_payload())
    assert create_resp.status_code == 201

    user_id = create_resp.json()["id"]

    delete_resp = api.delete(f"/users/{user_id}")
    assert delete_resp.status_code == 204

    get_resp = api.get(f"/users/{user_id}")
    assert get_resp.status_code == 404


# TC-015 — Delete non-existing user
def test_delete_non_existing_user(api):
    non_existing_user_id = 999999

    response = api.delete(f"/users/{non_existing_user_id}")
    assert response.status_code == 404


#TC-016 — Delete user without authorization
def test_delete_user_without_authorization(api):
    create_resp = api.post("/users", valid_user_payload())
    assert create_resp.status_code == 201

    user_id = create_resp.json()["id"]

    delete_resp = requests.delete(
        f"{BASE_URL}/users/{user_id}",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )

    # GoREST returns 404 for unauthorized delete to avoid resource disclosure
    assert delete_resp.status_code == 404
