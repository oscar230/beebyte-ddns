import myip
import beebyte
import dns
import os
import schedule

def job(hostname: str) -> None:
    print(f"Updating {hostname}...")
    my_ip_address = myip.ip()
    a_record_ips = beebyte.get_records_ip(api_key, hostname)

    if my_ip_address in a_record_ips:
        print(f"A-record {hostname} -> {my_ip_address} already exists")
        resolved_ip = dns.lookup(hostname)
        if resolved_ip and resolved_ip != my_ip_address:
            print(f"Warning: {hostname} resolves to {resolved_ip}")
        #elif resolved_ip == None:
            #print(f"Error, could not resolve {hostname} to verify A-record!")
    else:
        if a_record_ips:
            print(f"{hostname} -> {', '.join(a_record_ips)}, incorrect ip!")
        else:
            print(f"{hostname} not found")
        beebyte.set_record(api_key, hostname, my_ip_address)


if __name__ == "__main__":
    api_key = os.environ.get('APIKEY')
    if not api_key:
        print("Api key in environment variable APIKEY not set")
        exit(-1)
    hostnames = os.environ.get('HOSTNAMES')
    if not hostnames:
        print("No hostnaes set in environment variable HOSTNAMES, specify a comma-serperated list of hostnames")
        exit(-1)
    interval = os.environ.get('INTERVAL')
    if not hostnames:
        print("No interval set in environment variable INTERVAL, specify an integer that defines the amount of minutes in between job runs")
        exit(-1)

    for hostname in hostnames.split(','):
        schedule.every(10).minutes.do(job, hostname=hostname)
