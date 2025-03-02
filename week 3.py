import socket

def get_ip(web_url):
    ip = socket.gethostbyname(web_url)
    print(ip)

get_ip("youtube.com") 