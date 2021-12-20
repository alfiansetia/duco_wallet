import requests
import json

url = "https://server.duinocoin.com/users/"

user = ['alfiansetia', 'alfinetwork', 'alfi']

for x in user:
    get = requests.get(url+x)
    js = json.loads(get.text)
    u = js['result']['balance']['username']
    b = js['result']['balance']['balance']
    m = js['result']['miners']
    t= f"""balance {u} : {b} \nminers : {len(m)} \n """
    print(t)
