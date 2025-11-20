import requests

okta_domain = "https://trial-6169156.okta.com"
api_token = "YOUR_API_TOKEN"

headers = {
    "Authorization": f"SSWS {api_token}",
    "Content-Type": "application/json"
}

data = {
    "profile": {
        "firstName": "Test",
        "lastName": "User",
        "email": "test.user@ajayi-labs.gov",
        "login": "test.user@ajayi-labs.gov"
    }
}

resp = requests.post(f"{okta_domain}/api/v1/users?activate=true",
                     headers=headers, json=data)

print(resp.json())
