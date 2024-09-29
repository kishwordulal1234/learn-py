import requests
import json

ip = input(" inter the ip address ")


reasult = requests.get(f'https://ipinfo.io/{ip}/json?token=15169923049280')


if reasult.status_code == 200:
    tl = reasult.json()
    print(tl)
else:
    print(' unable to feathch data ')
    
    
    
