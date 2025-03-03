import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 333))
print("udp ready to recieve")
while True:
    data, client_address =  server.recvfrom(2048)
    print(f"Received data from {client_address}: {data.decode()}")
