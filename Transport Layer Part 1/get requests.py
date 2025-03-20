import socket  # Import socket module for low-level network communication
import requests  # Import requests module for simplified HTTP requests

def get_homepage():
    """
    Function to manually fetch a webpage's HTML content using a raw HTTP GET request.
    Uses a TCP socket to establish a connection with the target web server.
    """
    # Create a TCP socket (IPv4 + Stream-based connection)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address (Amazon homepage on port 80 for HTTP)
    server_address = ("amazon.com", 80)
    
    # Connect to the web server
    client_socket.connect(server_address)
    
    # Construct a raw HTTP GET request string (must be formatted exactly)
    request = "GET / HTTP/1.1\r\nHost: amazon.com\r\n\r\n"
    
    # Send the GET request to the server
    client_socket.send(request.encode())
    
    # Receive and decode the server's response (up to 4096 bytes)
    response = client_socket.recv(4096)
    print(response.decode())
    
    # Close the socket connection
    client_socket.close()

def get_homepage_requests(url):
    """
    Function to fetch a webpage using the `requests` module for convenience.
    
    Parameters:
        url (str): The URL of the webpage to retrieve.
    """
    response = requests.get(url)
    print(response.text)

# Fetch the Amazon homepage using both methods
get_homepage()  # Raw socket-based request
print("\n" * 5)  # Separate the outputs
get_homepage_requests("https://www.amazon.com")  # Requests module-based request
