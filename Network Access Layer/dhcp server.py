import ipaddress

address = "192.10.1.1/24"

ip = ipaddress.ip_interface(address)

ips = ip.network.hosts()

server = {
    "ips" : ip.network.hosts(),
    "leases": {}
}