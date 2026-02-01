import requests


BASE_URL = "https://gorest.co.in/public/v2"


class ApiClient:
    def __init__(self, token: str):
        if not token:
            raise ValueError("API token is required")

        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def get(self, endpoint: str):
        return requests.get(
            url=f"{self.base_url}{endpoint}",
            headers=self.headers,
        )

    def post(self, endpoint: str, payload: dict):
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.headers,
        )

    def put(self, endpoint: str, payload: dict):
        return requests.put(
            url=f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.headers,
        )

    def delete(self, endpoint: str):
        return requests.delete(
            url=f"{self.base_url}{endpoint}",
            headers=self.headers,
        )
