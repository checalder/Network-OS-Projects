import ipaddress
import socket

def analyse_ip(ip_str):

    # Create an IP interface object
    ip = ipaddress.ip_interface(ip_str)
    print(f"Address: {ip.ip}")
    print(f"Network: {ip.network}")
    print(f"Netmask: {ip.netmask}")
    print(f"Is private: {ip.ip.is_private}")
    print(f"Is global: {ip.ip.is_global}")
    print(f"Broadcast Address: {ip.network.broadcast_address}")
    print(f"usable adresses are {ip.network.num_addresses}")
    
    # List all hosts in the network
    if ip.network.num_addresses < 256: # Only for small networks
        print("\nHosts in network:")
    for host in ip.network.hosts():
        print(host)


# Example usage
analyse_ip('192.168.1.1')