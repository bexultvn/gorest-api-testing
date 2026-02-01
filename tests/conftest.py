import os
import pytest
from dotenv import load_dotenv
from utils.api_client import ApiClient

load_dotenv()

@pytest.fixture(scope="session")
def api():
    token = os.getenv("GOREST_TOKEN")
    if not token:
        raise RuntimeError("GOREST_TOKEN is not set")
    return ApiClient(token)
