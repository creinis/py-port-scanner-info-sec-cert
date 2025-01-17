import socket
import re
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    ip = ""
    open_ports = []
    try:
        ip = socket.gethostbyname(target)
        print(f"Hostname: {target}, IP: {ip}")  # Debug print
        for port in range(port_range[0], port_range[1] + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)  # Aumente o timeout para 2 segundos
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"Port {port} is open")  # Debug print
                    open_ports.append(port)
                else:
                    print(f"Port {port} is closed")  # Debug print
        
    except socket.gaierror:
        if re.search('[a-zA-Z]', target):
            return "Error: Invalid hostname"
        return "Error: Invalid IP address"
    except socket.error:
        return "Error: Invalid IP address"
    
    hostname = None

    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.error:
        hostname = None

    if verbose:
        if hostname is None:
            return f"Open ports for {ip}\nPORT     SERVICE\n" + "\n".join([f"{port:<9}{socket.getservbyport(port)}" for port in open_ports])
        return f"Open ports for {hostname} ({ip})\nPORT     SERVICE\n" + "\n".join([f"{port:<9}{socket.getservbyport(port)}" for port in open_ports])
    
    return open_ports
