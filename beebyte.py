import requests
import sys
from requests import Response
import base64
import json

USER_AGENT: str = "DDNS Script"

def set_record(api_key: str, hostname: str, ip: str) -> None:
    url = f"https://portal.beebyte.se/api/v1/domain/{hostname}/record/"
    headers: dict = {
        "API-KEY": api_key,
        "User-Agent": USER_AGENT
    }
    data = {
        "name": hostname,
        "ttl": 1800,
        "record_type": "A",
        "record_data": ip,
        "overwrite": True
    }
    response: Response = requests.post(url, data=data, headers=headers)
    if response.status_code == 201:
        print(f"Set {ip} for {hostname} (A-record)")
    else:
        print(f"Failed to create A-record! Got status code {response.status_code} and response text {response.text}")
        exit(-1)

def get_records_ip(api_key: str, hostname: str) -> list[str]:
    url = f"https://portal.beebyte.se/api/v1/domain/{hostname}/record/"
    headers: dict = {
        "API-KEY": api_key,
        "User-Agent": USER_AGENT
    }
    response: Response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [obj["record_data"] for obj in response.json() if obj["record_type"] == "A"]
    else:
        print(f"Failed to get records for hostname {hostname}! Got status code {response.status_code} and response text {response.text}")
        exit(-1)

def update_ddns(api_key: str, hostname: str, ip: str) -> None:
    url = f"https://dynupdate.beebyte.se/nic/update?hostname{hostname}&myip={ip}"
    credentials: str = f"beebyte:{api_key}"
    headers: dict = {
        "Authorization": f"Basic {base64.b64encode(credentials.encode('ascii')).decode('ascii')}",
        "User-Agent": USER_AGENT
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