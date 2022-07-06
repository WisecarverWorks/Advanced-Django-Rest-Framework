import requests

endpoint = "http://localhost:8000/api/products/2/"

get_response = requests.get(endpoint, json={"title": "Abc123", "content": "Hello World", "price": "124"})

print(get_response.json())

