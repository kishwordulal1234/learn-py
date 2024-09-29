import random as rand

num = int(input("inter the number: "))
guess = rand.randint(0,10)

while num < 0 or guess > 10:
    print("please inter betwin 0 to 10")
if num > guess:
    print("guess is to high")
elif num < guess:
    print("guess is to low bro")
elif num == guess:
    print("you won bro")
while num != guess:
    num = int(input("inter the number: "))
    print("guess is wrong")
else:
    print("congrast come again")
    exit()
    
    