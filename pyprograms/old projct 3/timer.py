import time
tmt = int(input("inter the time for count down"))
for secons in range(tmt-1,-1,-1):
    print(secons)
    time.sleep(1)
print("allha hau akabar")