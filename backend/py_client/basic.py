import requests

# endpoint = "https://github.com/"
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
# Application Programming Interface

# get_response = requests.get(endpoint, json={"query": "Hello World"})  # HTTP Request
get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello World"})  # HTTP Request
# print(get_response.text) # print raw text response
# We Want REST API's 
# print(get_response.status_code)
print(get_response.json()) # print raw text response

# REST API --> WEB API
# HTTP REQUEST -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
# print(get_response.text) # print raw text response
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.1",
#     "X-Amzn-Trace-Id": "Root=1-62c58b8a-1a98baf053a6dd8255b9bc21"
#   },
#   "json": null,
#   "method": "GET",
#   "origin": "154.6.28.89",
#   "url": "https://httpbin.org/anything"
# }
# Python Dictionary
# print(get_response.status_code)
# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.1', 'X-Amzn-Trace-Id': 'Root=1-62c58bff-12f5f3955786fed606c078d0'}, 'json': None, 'method': 'GET', 'origin': '154.6.28.89', 'url': 'https://httpbin.org/anything'}