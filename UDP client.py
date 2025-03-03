import socket
import datetime

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 1235)

while True:
    message = input("input message: ")
    print(f"send time: {datetime.datetime.now()}")

    message = message.encode()

    connection.sendto(message, server_address)