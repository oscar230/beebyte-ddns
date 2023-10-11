import requests
from requests import Response

def ip() -> str:
    response: Response = requests.get("https://am.i.mullvad.net/ip")
    if response.status_code == 200:
        ip: str = response.text.lstrip().rstrip()
        return ip
    else:
        print("Failed, could not get ip!")
        exit(-1)