import requests
from config.config import settings

def call_github(
        url: str,
        auth_token: str,
        owner: str,
        repo: str
):
    api_url = url.format(owner,repo)
    endpoint = settings.base_url+api_url
    headers = {
        "Authorization" : "token {}".format(auth_token)
    }

    response = requests.get(
        url=endpoint,
        headers=headers
    )

    if not response.ok:
        print(response.raise_for_status, response.json())
    response.raise_for_status()

    return response.json()