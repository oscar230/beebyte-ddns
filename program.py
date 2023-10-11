import sys
import myip
import beebyte
import dns

if __name__ == "__main__":
    api_key: str = sys.argv[1]
    hostnames: str = sys.argv[2]

    ip = myip.ip()
    for hostname in hostnames.split(','):
        a_record_ips: list[str] = beebyte.get_records_ip(api_key, hostname)

        if any(item == ip for item in a_record_ips):
            print(f"A-record {hostname} -> {ip} already exists")
            resolved_ip = dns.lookup(hostname)
            if resolved_ip != ip:
                print(f"Warning: {hostname} resolves to {resolved_ip}")
        else:
            if len(a_record_ips) > 0:
                print(f"{hostname} -> {', '.join(a_record_ips)}, incorrect ip!")
            else:
                print(f"{hostname} not found")
            beebyte.set_record(api_key, hostname, ip)