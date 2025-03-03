import socket
import subprocess
import requests



def get_homepage():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# create the socket object
    server_address = ("amazon.com", 80)
    client_socket.connect(server_address)# connect the socket to a website
    #send get request
    request = "GET / HTTP/1.1\r\nHost: amazon.com\r\n\r\n"#must be in this exact format with these spaces, if there was a space at the start of a new line it would be considered a new header
    client_socket.send(request.encode())
    #recieve response
    response = client_socket.recv(4096)
    print(response.decode())
    #close socket
    client_socket.close()

def get_homepage_requests(url):
    response = requests.get(url)
    print(response.text)
#get_ip("youtube.com") 
get_homepage()
print("\n\n\n\n\n\n\n")
get_homepage_requests("https://www.amazon.com")