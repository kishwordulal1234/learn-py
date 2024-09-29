import random as claw

name = input("inter your name ")
print("enter the numbe for 0 to 2  0 for rock 1 for paper 2 for sisor")
human = int(input("inter the number"))

claw = claw.randint(0,2)
if human > claw:
    print(f"you lose {name} robow was {claw}")
elif human < claw:
    print(f"you won {name} robot was {claw}")
elif human == claw:
    print(" it draw ty again")
while human == claw:
    human = int(input("inter the number"))
else:
    print("congrats")
    