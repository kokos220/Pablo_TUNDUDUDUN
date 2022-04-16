import urllib.request
import requests

opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())

print("**************************************************************************")

response = requests.get("https://httpbin.org/get")
print(response.content)
print(f'Database - {type(response.content)}')

print("**************************************************************************")

response = requests.get("https://httpbin.org/get")
print(response.text)
print(f'Database - {type(response.text)}')

print("**************************************************************************")

response = requests.post("https://httpbin.org/post", data='Test data', headers={'h1': 'Test title'})
print(response.text)