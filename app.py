import requests

# ----------------------------
# CONFIG
# ----------------------------
BASE_URL = "https://amiapp.dpdc.org.bd"
TENANT_CODE = "DPDC"
CUSTOMER_NUMBER = "29112136"

# ----------------------------
# STEP 1: GET BEARER TOKEN
# ----------------------------
def get_bearer_token():
    url = f"{BASE_URL}/auth/login/generate-bearer"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "clientid": "auth-ui",
        "clientsecret": "0yFsAl4nN9jX1GGkgOrvpUxDarf2DT40",
        "tenantcode": TENANT_CODE,
    }

    response = requests.post(url, headers=headers, json={}, timeout=15)
    response.raise_for_status()

    data = response.json()
    print(data)
    return data["access_token"]


# ----------------------------
# STEP 2: CALL USAGE SERVICE
# ----------------------------
def get_usage_data(token):
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
                    customerNumber: "{CUSTOMER_NUMBER}"
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


# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    try:
        token = get_bearer_token()
        print("Bearer token received\n")

        usage_data = get_usage_data(token)
        print("Usage Service Response:\n")
        print(usage_data)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
