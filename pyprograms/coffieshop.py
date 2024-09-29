import time 

print("Welcome to the coffee shop!")
time.sleep(1)
print("What would you like to have?")
print('Press Enter to search for an item.')
input()
print("Loading available items...")
time.sleep(3)
print("These are the available items: tea, milk, coffee.")

item = input("Enter the item that you would like to have: ").lower()

if item == 'milk':
    print("Milk is available.")
    price = 60
    user_money = int(input("Please provide the money: "))
    if user_money == price:
        print("You have paid the exact amount.")
        exit()
    elif user_money > price:
        print(f"Your change is {user_money - price}. Have a good day, sir!")
        exit()
    elif user_money < price:
        print("You don't have enough money.")
        print("Would you like to terminate the purchase or repay? If terminate, please input 'q', if repay 'r'.")
        opt = input("Enter the option that you like: ").lower()
        while True:
            if opt == 'q':
                print("Thank you for shopping with us.")
                exit()
            elif opt == 'r':
                user_money = int(input("Please provide the money: "))
                if user_money >= price:
                    if user_money > price:
                        print(f"Your change is {user_money - price}. Have a good day, sir!")
                    else:
                        print("You have paid the exact amount. Enjoy!")
                    exit()
                else:
                    print("You still don't have enough money. Please try again.")
            else:
                print("Invalid option. Please enter 'q' or 'r'.")
                opt = input("Enter the option that you like: ").lower()

elif item == 'tea':
    print("Tea is available.")
    price = 25
    user_money = int(input("Please provide the money: "))
    if user_money == price:
        print("You have paid the exact amount.")
        exit()
    elif user_money > price:
        print(f"Your change is {user_money - price}. Have a good day, sir!")
        exit()
    elif user_money < price:
        print("You don't have enough money.")
        print("Would you like to terminate the purchase or repay? If terminate, please input 'q', if repay 'r'.")
        opt = input("Enter the option that you like: ").lower()
        while True:
            if opt == 'q':
                print("Thank you for shopping with us.")
                exit()
            elif opt == 'r':
                user_money = int(input("Please provide the money: "))
                if user_money >= price:
                    if user_money > price:
                        print(f"Your change is {user_money - price}. Have a good day, sir!")
                    else:
                        print("You have paid the exact amount. Enjoy!")
                    exit()
                else:
                    print("You still don't have enough money. Please try again.")
            else:
                print("Invalid option. Please enter 'q' or 'r'.")
                opt = input("Enter the option that you like: ").lower()

elif item == 'coffee':
    print("Coffee is available.")
    price = 160
    user_money = int(input("Please provide the money: "))
    if user_money == price:
        print("You have paid the exact amount.")
        exit()
    elif user_money > price:
        print(f"Your change is {user_money - price}. Have a good day, sir!")
        exit()
    elif user_money < price:
        print("You don't have enough money.")
        print("Would you like to terminate the purchase or repay? If terminate, please input 'q', if repay 'r'.")
        opt = input("Enter the option that you like: ").lower()
        while True:
            if opt == 'q':
                print("Thank you for shopping with us.")
                exit()
            elif opt == 'r':
                user_money = int(input("Please provide the money: "))
                if user_money >= price:
                    if user_money > price:
                        print(f"Your change is {user_money - price}. Have a good day, sir!")
                    else:
                        print("You have paid the exact amount. Enjoy!")
                    exit()
                else:
                    print("You still don't have enough money. Please try again.")
            else:
                print("Invalid option. Please enter 'q' or 'r'.")
                opt = input("Enter the option that you like: ").lower()

else:
    print("Sorry, that item is not available.")
