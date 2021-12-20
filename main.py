import requests
import json

url = "https://server.duinocoin.com/users/"

user = ['alfiansetia', 'alfinetwork', 'alfi']
btot = 0
mtot = 0

for x in user:
    get = requests.get(url+x)
    js = json.loads(get.text)
    u = js['result']['balance']['username']
    b = js['result']['balance']['balance']
    m = js['result']['miners']
    btot = btot + float(b)
    mtot = mtot +int(len(m))
    t = f"""Balance {u} : {b} \nMiners : {len(m)} \n """
    print(t)
print("Total Miners : " + str(mtot))
print("Total Balance : " + str(btot))
