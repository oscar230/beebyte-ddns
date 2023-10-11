import requests

def ip() -> str:
    response = requests.get("https://am.i.mullvad.net/ip")
    if response.status_code == 200:
        return response.text.strip()
    else:
        print("Failed, could not get ip!")
        exit(-1)
