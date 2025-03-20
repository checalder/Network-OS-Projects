import ipaddress  # Import ipaddress module for IP calculations

def analyse_ip(ip_str):
    """
    Analyzes an IP address and prints details about its network properties.
    
    Parameters:
        ip_str (str): The IP address with a subnet mask (CIDR notation).
    """
    # Create an IP interface object
    ip = ipaddress.ip_interface(ip_str)
    
    # Print general IP details
    print(f"Address: {ip.ip}")  # The specific IP address
    print(f"Network: {ip.network}")  # The network the IP belongs to
    print(f"Netmask: {ip.netmask}")  # The subnet mask
    print(f"Is private: {ip.ip.is_private}")  # Whether the IP is part of a private range
    print(f"Is global: {ip.ip.is_global}")  # Whether the IP is publicly routable
    print(f"Broadcast Address: {ip.network.broadcast_address}")  # The broadcast address of the network
    print(f"Usable addresses: {ip.network.num_addresses}")  # The number of addresses in the network
    
    # List all hosts in the network (only for small networks to avoid long output)
    if ip.network.num_addresses < 256:
        print("\nHosts in network:")
        for host in ip.network.hosts():
            print(host)

# Example usage
analyse_ip('192.168.1.1/24')  # Analyze a local network IP
