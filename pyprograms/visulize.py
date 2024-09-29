import time
import datetime

print("Welcome to Unknown Hart Bank")
print(datetime.datetime.now())

# Initialize user data
users = {
    "user1": {"password": "user23", "balance": 200},
    "user2": {"password": "kishwor", "balance": 300},
    "user3": {"password": "ravi", "balance": 500}
}

print("Please be patient, bank servers are loading...")
time.sleep(2)
print(datetime.datetime.now())

# User authentication
user_name = input("Enter your username: ")

if user_name in users:
    password = input("Please enter your password: ")
    if users[user_name]["password"] == password:
        print(f"Welcome {user_name}")
        time.sleep(1)
        
        while True:
            print("\nWhat would you like to do?")
            print("u - Update balance")
            print("w - Withdraw money")
            print("q - Quit")
            
            decision = input("Enter your choice: ").lower()
            
            if decision == "u":
                try:
                    add_amount = int(input("Enter amount to add: "))
                    if add_amount > 0:
                        users[user_name]["balance"] += add_amount
                        print(f"Balance updated. New balance: ${users[user_name]['balance']}.")
                    else:
                        print("Invalid amount. Please enter a positive number.")
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            
            elif decision == "w":
                try:
                    withdraw_amount = int(input("Enter amount to withdraw: "))
                    if withdraw_amount > 0:
                        if withdraw_amount <= users[user_name]["balance"]:
                            users[user_name]["balance"] -= withdraw_amount
                            print(f"Withdrawal successful. New balance: ${users[user_name]['balance']}.")
                        else:
                            print("Insufficient balance.")
                    else:
                        print("Invalid amount. Please enter a positive number.")
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            
            elif decision == "q":
                print("Exiting... Thank you for banking with us!")
                break
            
            else:
                print("Invalid option. Please choose again.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")
