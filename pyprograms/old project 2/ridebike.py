height = float(input("inter your height "))

if height >3:
    print("your can go to ride bike")
else:
    print("your cant ride")
    
age = float(input("inter your age:"))
if  age <=18:
    print("for you price is 200")
    exit()
elif age >18:
    print("for you price is 1000")
    exit()
elif age >40:
    print("for tenagers it 2500")
else:
    print("sorry you cant  ride")
    exit()    

    