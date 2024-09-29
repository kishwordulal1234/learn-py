import time 
import os 


send = int(input("inthger the number that you wnat to count from "))
for bomb in range(send-1,-1,-1):
    time.sleep(1)
    print(bomb)
os.system("neofetch")