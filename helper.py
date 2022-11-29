import socket


def validate_ip_address_string(ip_string: str):
    try:
        socket.inet_aton(ip_string)
        return True
    except Exception as e:
        return False
