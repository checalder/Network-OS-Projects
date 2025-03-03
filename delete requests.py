import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.delete(url)

print(response.status_code)#it is a mock json api so it will return 200
print(response.json())#it will return the deleted post