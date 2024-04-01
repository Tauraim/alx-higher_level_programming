import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email as a URL parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Create a POST request with the encoded data
req = urllib.request.Request(url, data=data, method='POST')

# Send the request and read the response
with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')

print(body)
