import requests
import json
import datetime
import time

url = "https://server.duinocoin.com/users/"

user = ['alfiansetia', 'alfinetwork', 'alfi']


btot = 0
mtot = 0
now = datetime.datetime.now()
waktu_sekarang = now.strftime("%Y-%m-%d %H:%M")


print('Waktu Sekarang : ' + waktu_sekarang +'\n')
for x in user:
    try :
        get = requests.get(url+x)
    except:
        print('Error Connection..\n')
    else :
        js = json.loads(get.text)
        u = js['result']['balance']['username']
        b = js['result']['balance']['balance']
        m = js['result']['miners']
        btot = btot + float(b)
        mtot = mtot +int(len(m))
        t = f"""Balance {u} : {b} \nMiners : {len(m)} \n """
        print(t)
        time.sleep(2)
print("Total Miners : " + str(mtot))
print("Total Balance : " + str(btot))
