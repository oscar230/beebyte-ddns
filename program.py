import sys
import myip
import beebyte
import dns

if __name__ == "__main__":
    api_key = sys.argv[1]
    hostnames = sys.argv[2]

    my_ip_address = myip.ip()
    for hostname in hostnames.split(','):
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
