import requests

endpoint = "https://httpbin.org.status/200/"
endpoint = "https://www.github.com/adfsdf"
endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/?abc=123"

get_response = requests.post(endpoint, json={"title": "hellow world", 'price': '12'})
print(get_response.text)
print(get_response.status_code)

print(get_response.json())

