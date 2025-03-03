import socket
import datetime

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen(1) # Allow 1 pending connection



while True:

    print("TCP Server is listening...")
    client_socket, client_address = server_socket.accept()
    start_time = datetime.datetime.now() 
    print(f"Connected to {client_address}")

    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

    # Echo back the data
    client_socket.sendall(b"ACK: " + data)
    client_socket.close()
    end_time = datetime.datetime.now()
    print("closed")
    print(f"time taken: {end_time - start_time} ")