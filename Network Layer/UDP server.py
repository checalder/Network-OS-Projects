import socket  # Import socket module for networking
import datetime  # Import datetime module for logging timestamps

# Create a UDP server socket
# AF_INET specifies IPv4, SOCK_DGRAM specifies UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the server to localhost on port 1235
server_socket.bind(('localhost', 1235))

print("UDP Server is listening...")

while True:
    # Receive data from any client (up to 2048 bytes)
    data, client_address = server_socket.recvfrom(2048)
    
    # Decode the received message
    message = data.decode()
    
    # Print the received message
    print(f"Received from {client_address}: {message}")
    
    # Append the received message to a log file with a timestamp
    with open("udp_logs.txt", "a") as file:
        if not data:
            break  # Stop if no data is received
        file.write(f"{datetime.datetime.now()}\n{message}\n\n")
    
    # Print the time message was received
    print(f"Receive time: {datetime.datetime.now()}")
