import socket

def lookup(hostname) -> str:
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None