import requests
import json

url_oi = "http://127.0.0.1:4000/oi"
url_processar = "http://127.0.0.1:4000/processar"

headers = {'Accept': 'application/json', 'x-access-tokens': '769db7cf-9d6b-4496-9645-3bd51799583a'}

r = requests.get(url_oi, headers=headers, verify=False)
print(r)
print(r.json())

path_img = ''

files = {'file': open(path_img, 'rb')}

r = requests.post(url_processar, files=files, headers=headers)
print(r)
print(r.json())

