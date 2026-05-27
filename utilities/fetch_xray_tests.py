import requests

CLIENT_ID = "0BFD533F559248BEA5F5FFC8F68779F1"
CLIENT_SECRET = "39feac3726f7be48379e5f36ecc06a924e8a9e784a9b3a4a2b70037cbcc794a0"

def get_token():
    url = "https://eu.xray.cloud.getxray.app/api/v2/authenticate"

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    response = requests.post(url, json=payload)
    token = response.text.strip('"')

    print("TOKEN GENERATED")
    return token


def fetch_tests():
    token = get_token()

    url = "https://eu.xray.cloud.getxray.app/api/v2/graphql"

    query = {
        "query": """
        {
          getTests(
  jql: "project = XSP AND labels in (released4run, daily1)",
  limit: 10
) {
            results {
              jira(fields: ["key"])
            }
          }
        }
        """
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=query, headers=headers)

    print("XRAY RESPONSE:")
    print(response.json())


if __name__ == "__main__":
    fetch_tests()