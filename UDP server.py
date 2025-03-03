import socket
import datetime

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 1235))

print("UDP Server is listening...")

while True:

    data = server_socket.recv(2048)#dont need client address unlike tcp
    
    message = data.decode()

    print(f"Received: {message}")

    with open("wk5_logs", "a") as file:#with is used to open files in python
        #'wb' specifies the mode the process will be in. wb means overwrite whatever we create, 'a' would append to end of file, etc
        #the process is accessed by its file keyword
        if not data:
            break
        
        file.write(f"{datetime.datetime.now()}\n{message}\n\n")

    print(f"recieve time: {datetime.datetime.now()}")