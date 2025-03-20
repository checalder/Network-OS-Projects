import requests  # Import requests module for handling HTTP requests

# Define the API endpoint for posting data
url = 'https://jsonplaceholder.typicode.com/posts'  # Mock API for testing POST requests

# Define the JSON data payload to be sent in the POST request
data = {
    "title": "Sample Post",  # Title of the post
    "body": "This is an example post body.",  # Content of the post
    "userId": 1  # User ID associated with the post
}

# Send a POST request with the data in JSON format
response = requests.post(url, json=data)

# Print the response status code
print(f"Status Code: {response.status_code}")

# Print the response body returned by the server
print("Response Body:", response.json())

# Retrieve and print the post with ID 101 using a GET request
json_response = requests.get("https://jsonplaceholder.typicode.com/posts/101")
print(json_response.json())
