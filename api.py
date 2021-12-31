import json
import requests
import os
import sys

api_token = os.getenv("CAT_API_TOKEN")
if not api_token:
    raise SystemExit("No valid API token provided")


def get_random_photo_url() -> str:
    response = requests.get(
        "https://api.thecatapi.com/v1/images/search", headers={"x-api-key": api_token}
    )

    if response.status_code != 200:
        print(response, file=sys.stderr)

    response.raise_for_status()
    return response.json()[0].get("url")
