number = int(input("Enter the number: "))

if number == 19 or number == 16:
    print("The number is correct")
else:
    while number > 19 or number > 16:
        number = number - 1
        print(number)
