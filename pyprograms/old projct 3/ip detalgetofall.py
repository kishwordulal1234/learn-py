import requests
import time


ip = input("inter the ip that you want to look  ")

reasult = requests.get(f"https://ipinfo.io/{ip}/json?token=15169923049280")

if  reasult.status_code == 200:
    print(reasult.json())
else:
    print("unable to featch data ")