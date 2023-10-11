import requests
import sys
from requests import Response
import base64
import myip

def update_ddns(hostnames, api_key) -> None:
    ip: str = myip.ip()
    for hostname in hostnames.split(','):
        url = f"https://dynupdate.beebyte.se/nic/update?hostname{hostname}&myip={ip}"
        credentials: str = f"beebyte:{api_key}"
        headers: dict = {
            "Authorization": f"Basic {base64.b64encode(credentials.encode('ascii')).decode('ascii')}",
            "User-Agent": "Python script for DDNS"
        }
        response: Response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result: str = response.text.lstrip().rstrip()
            if result == "good":
                print(f"OK\t{hostname} -> {ip}")
            elif result == "nochg":
                print(f"No change, the IP for {hostname} may already be set to {ip} or this client might be considered abusive")
            elif result == "badauth":
                print("Bad authentication!")
            elif result == "notfqdn":
                print(f"{hostname} needs to be a fully qualified domain name (FQDN)")
            elif result == "nohost":
                print(f"{hostname} does not exist in the DDNS service for this user")
            elif result == "numhost":
                print("Too many hosts specified")
            elif result == "abuse":
                print(f"{hostname} is blocked for update abuse")
            elif result == "badagent":
                print("User agent incorrect or HTTP method not permitted")
            elif result == "dnserr":
                print("DNS error!")
            elif result == "911":
                print("Service faulty or under maintenance")
            else:
                print(f"Unkown return \"{result}\"")
        else:
            print(f"Failed, HTTP status:{str(response.status_code)}")

if __name__ == "__main__":
    api_key: str = sys.argv[1]
    hostnames: str = sys.argv[2]
    update_ddns(hostnames, api_key)
