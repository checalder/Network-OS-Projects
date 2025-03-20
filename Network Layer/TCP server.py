import socket  # Import socket module for networking functionality
import datetime  # Import datetime module to log connection timestamps

# Create a TCP server socket
# AF_INET specifies IPv4, SOCK_STREAM specifies TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to localhost on port 1234
server_socket.bind(('localhost', 1234))

# Listen for incoming connections (max 1 pending connection)
server_socket.listen(1)

while True:
    print("TCP Server is listening...")
    
    # Accept an incoming client connection
    client_socket, client_address = server_socket.accept()
    
    # Log the connection start time
    start_time = datetime.datetime.now()
    print(f"Connected to {client_address}")
    
    # Receive data from the client (up to 1024 bytes)
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    
    # Echo back the received data with an ACK prefix
    client_socket.sendall(b"ACK: " + data)
    
    # Close the client socket after sending response
    client_socket.close()
    
    # Log connection end time and print duration
    end_time = datetime.datetime.now()
    print("Connection closed")
    print(f"Time taken: {end_time - start_time}")
