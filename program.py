import requests
import sys
from requests import Response
import base64
import myip
import beebyte



if __name__ == "__main__":
    api_key: str = sys.argv[1]
    hostnames: str = sys.argv[2]

    ip = myip.ip()

    for hostname in hostnames.split(','):
        records: list[str] = beebyte.get_records_ip(api_key, hostname)
        if len(records) == 0:
            print(f"No current A-records for {hostname}")
            beebyte.set_record(api_key, hostname, ip)
        elif any(item == ip for item in records):
            print(f"A A-record for {hostname} -> {ip} already exists")
            