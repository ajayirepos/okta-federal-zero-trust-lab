    Okta API Automation Examples
This document includes API examples used to demonstrate automation and REST integration capabilities.

    Python Example: Create User
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

Use Cases
      User provisioning
      Group assignment automation
      App assignment automation
      Token management
      Audit logging operations
