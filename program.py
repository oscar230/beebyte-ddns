import requests
import sys
from requests.auth import HTTPBasicAuth
from requests import Response
import base64

def myip() -> str:
    response: Response = requests.get("https://am.i.mullvad.net/ip")
    if response.status_code == 200:
        ip: str = response.text.lstrip().rstrip()
        print("IP=" + ip)
        return ip
    else:
        print("Could not get ip.")
        exit(-1)

def update_ddns(hostnames, api_key) -> None:
    ip: str = myip()
    for hostname in hostnames.split(','):
        url = f"https://dynupdate.beebyte.se/nic/update?hostname{hostname}&myip={ip}"
        credentials: str = f"beebyte:{api_key}"
        headers: dict = {
            "Authorization": f"Basic {base64.b64encode(credentials.encode('ascii')).decode('ascii')}",
            "User-Agent": "Python script for DDNS"
        }
        response: Response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Set\t{hostname} -> {ip}")
        else:
            print(f"Failed for hostname {hostname}! (HTTP Status {str(response.status_code)})")

if __name__ == "__main__":
    api_key: str = sys.argv[1]
    hostnames: str = sys.argv[2]
    update_ddns(hostnames, api_key)
