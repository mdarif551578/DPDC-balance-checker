import requests
from config import BASE_URL, TENANT_CODE, CLIENT_ID, CLIENT_SECRET


def get_bearer_token() -> str:
    url = f"{BASE_URL}/auth/login/generate-bearer"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "clientid": CLIENT_ID,
        "clientsecret": CLIENT_SECRET,
        "tenantcode": TENANT_CODE,
    }

    response = requests.post(url, headers=headers, json={}, timeout=15)
    response.raise_for_status()

    return response.json()["access_token"]


def get_usage_data(customer_number: str, token: str) -> dict:
    url = f"{BASE_URL}/usage/usage-service"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {token}",
        "accessToken": token,
        "tenantCode": TENANT_CODE,
    }

    payload = {
        "query": f"""
        query {{
            postBalanceDetails(
                input: {{
                    customerNumber: "{customer_number}"
                    tenantCode: "{TENANT_CODE}"
                }}
            ) {{
                accountId
                customerName
                customerClass
                mobileNumber
                emailId
                accountType
                balanceRemaining
                connectionStatus
                customerType
                minRecharge
            }}
        }}
        """
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()

    return response.json()
