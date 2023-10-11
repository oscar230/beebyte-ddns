# Beebyte DDNS
Set DNS A-records using [Beebyte](https://www.beebyte.se/)'s API in a DynDNS/DDNS-like manner. This using [Mullvad's discovery services](https://mullvad.net/en/check) to resolve the clients ip.

## Background
[Beebyte](https://www.beebyte.se/) currently does **not** support DDNS for *non-subdomain-hostnames* (like abc.se), only subdomains (like sub.abc.se). This program uses [thier API](https://portal.beebyte.se/api/v1/) to achive this.

## Run
1. Get an [API key here](https://portal.beebyte.se/organisation/apikey/).
2. Install requirements and run.
```bash
$ pip install -r requirements.txt
$ python3 program.py BEEBYTE_API_KEY a.se,b.de,c.no
```