import socket

def lookup(hostname) -> str:
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"Error, could not lookup domain name {hostname}")
        exit(-1)