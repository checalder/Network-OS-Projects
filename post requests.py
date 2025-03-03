import requests 

url = 'https://jsonplaceholder.typicode.com/posts'  # Changed to JSONPlaceholder API


data = {"title": "Sample Post", 
        "body": "This is an example post body.",
        "userId": 1 }

response = requests.post(url, json=data)

json = requests.get("https://jsonplaceholder.typicode.com/posts/101")

print(f"Status Code: {response.status_code}")
print("Response Body:", response.json())
print(json.json())