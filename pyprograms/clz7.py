'''while True:
    try:
        num1 = int(input("inter the number "))
        num2 = int(input("inter the number "))
        print(num1+num2)
    except ValueError:
        print("invalid input")'''


'''while True:
    try:
        num1 = int(input("inter the number1 "))
        num2 = int(input("inter the number 2 "))
        if num1 > num2:
            print(f"{num1} is greater ")
        else:
            print(f"{num2} is greater ")
    except ValueError:
            print("invalid option") '''      
            
            
            
            



while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))

        if num1 > num2 and num1 > num3:
            print(f"{num1} is the greatest")
        elif num2 > num1 and num2 > num3:
            print(f"{num2} is the greatest")
        elif num3 > num1 and num3 > num2:
            print(f"{num3} is the greatest")
        else:
            print("All numbers are equal")
    except ValueError:
        print("Invalid input. Please enter a valid number.")