import os
import uuid
import pytest
from utils.api_client import ApiClient
from dotenv import load_dotenv
load_dotenv()


# API CLIENT (AUTH)
@pytest.fixture(scope="session")
def api():
    """
    Authenticated API client using Bearer Token.
    """
    token = os.getenv("GOREST_TOKEN")
    if not token:
        raise RuntimeError("GOREST_TOKEN is not set")

    return ApiClient(token)


# PAYLOAD FIXTURES
@pytest.fixture
def valid_user_payload():
    """
    Generates a valid user payload with unique email.
    """
    return {
        "name": "Test User",
        "email": f"qa_{uuid.uuid4().hex[:8]}@example.com",
        "gender": "male",
        "status": "active",
    }


@pytest.fixture
def update_user_payload():
    """
    Payload for updating an existing user.
    """
    return {
        "name": "Updated User",
        "status": "inactive",
    }


# TEST DATA SETUP + CLEANUP
@pytest.fixture
def created_user(api, valid_user_payload):
    """
    Creates a user before the test and deletes it after the test.
    Ensures test isolation and no leftover data in API.
    """
    create_response = api.post("/users", valid_user_payload)
    assert create_response.status_code == 201

    user = create_response.json()
    user_id = user["id"]

    yield user

    # cleanup (disconnect test data from API)
    api.delete(f"/users/{user_id}")
