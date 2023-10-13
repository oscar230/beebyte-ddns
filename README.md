# Beebyte DDNS
Set DNS A-records using [Beebyte](https://www.beebyte.se/)'s API in a DynDNS/DDNS-like manner. Using [Mullvad's discovery services](https://mullvad.net/en/check) to resolve the clients ip.

## Background
[Beebyte](https://www.beebyte.se/) currently does **not** support DDNS for *non-subdomain-hostnames* (like abc.se), only subdomains (like sub.abc.se). This program uses [thier API](https://portal.beebyte.se/api/v1/) to achive this.

## Run
### Native
1. Get an [API key here](https://portal.beebyte.se/organisation/apikey/).
2. Install requirements and run.
```bash
$ pip install -r requirements.txt
$ INTERVAL=10 APIKEY=placeholder HOSTNAMES=placeholder.se python3 program.py
```
### Docker compose
```bash
$ docker compose up
```

## Developing
1. Set environment variables in `docker-compose.yml`.
2. Build.
3. Run.
```bash
$ docker compose build
$ docker compose up
```