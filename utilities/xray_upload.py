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
    return response.text.strip('"')


def upload_results():
    token = get_token()

    url = "https://eu.xray.cloud.getxray.app/api/v2/import/execution/cucumber"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    file_path = "reports/cucumber.json"

    with open(file_path, "rb") as file:
        response = requests.post(url, headers=headers, data=file)

    print("UPLOAD RESPONSE:")
    print(response.text)


if __name__ == "__main__":
    upload_results()