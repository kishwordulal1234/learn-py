num = int(input("inter the number "))
num1 = num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in num1:
    print(i)
    if i == num1:
        break
    elif i != num1:
        print("trying to find")
else:
    print("password found")