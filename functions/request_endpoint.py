import requests
from .request_github import call_github
from config.config import settings

def request_endpoint(data: list):
    for i in range(len(data['api_endpoints'])):
        resp = call_github(
            url=data["api_endpoints"][i],
            auth_token=settings.github_key,
            owner="dbt-labs",
            repo="dbt"
        )
        print(resp)
    return None