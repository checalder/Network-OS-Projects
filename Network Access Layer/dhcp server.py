import ipaddress  # Importing the ipaddress module to handle IP-related operations

# Define the network address space
address = "192.10.1.1/24"  # This represents the network with a subnet mask of 255.255.255.0

# Create an IP interface object from the address
ip = ipaddress.ip_interface(address)

# Retrieve all possible host addresses within the network
ips = ip.network.hosts()  # This generates an iterator over all valid host addresses

# Define a dictionary to store server-related information
server = {
    "ips": ip.network.hosts(),  # Available IP addresses in the network
    "leases": {}  # Dictionary to track IP leases assigned to clients
}
