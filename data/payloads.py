import uuid


def valid_user_payload():
    unique_email = f"qa_{uuid.uuid4().hex[:8]}@example.com"

    return {
        "name": "Test User",
        "email": unique_email,
        "gender": "male",
        "status": "active",
    }


def update_user_payload():
    return {
        "name": "Updated User",
        "status": "inactive",
    }
