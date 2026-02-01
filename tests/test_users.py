from data.payloads import valid_user_payload


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