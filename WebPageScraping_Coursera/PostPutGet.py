import requests as re
import json

#Using Get Requests
response = re.get("https://jsonplaceholder.typicode.com/posts")
data = json.loads(response.content)
print(data[0:2])

#Using POST Requests
r = re.post("https://jsonplaceholder.typicode.com/posts")
data = json.loads(r.content)
print(data)



