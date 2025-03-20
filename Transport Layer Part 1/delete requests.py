import requests  # Import requests module to handle HTTP requests

# Define the URL of the resource to be deleted
url = 'https://jsonplaceholder.typicode.com/posts/1'  # Mock API for testing DELETE requests

# Send a DELETE request to the specified URL
response = requests.delete(url)

# Print the status code returned by the server
# In this mock API, it will return 200 (successful deletion)
print(response.status_code)

# Print the JSON response from the server
# The API typically returns the deleted post details
print(response.json())
