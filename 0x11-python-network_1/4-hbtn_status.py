import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

if response.status_code == 200:
    body = response.text
    print("- Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
else:
    print("Error occurred. Status code:", response.status_code)

