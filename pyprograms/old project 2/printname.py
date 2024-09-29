user_name = input("Enter your name: ")
user_password = input("Enter your password or PIN: ")

if user_name == 'kishwor' and user_password == 'blueking99':
    print("Login successful")
    input("Press Enter to continue...")
    print(f"Welcome admin {user_name}")
elif user_name == 'kishwor' or user_password == 'blueking99':
    print("Either username or password is correct. Verify that you are admin.")
    input("Press Enter to continue...")
elif user_name == 'kishwor' : 
    print(f"login sucessful {user_name}")  
elif user_password == 'blueking99' :
    print(f"login sucessful {user_name}")
    exit()        

    master_key = input("Please enter the master key: ")
    if master_key == '7894':
        print(f"Login successful. Welcome {user_name}")
    else:
        print("Master key incorrect. Access denied.")
        exit()
else:
    print("You have tried too many times.")
    bullet_key1 = input("Enter the bullet login code: ")
    bullet_key2 = input("Enter the second bullet login code: ")

    if bullet_key1 == '1916' or bullet_key2 == '1619':
        print("Login successful")
        print(f"Welcome admin {user_name}")
    else:
        print("You have been blocked. Access denied.")
        exit()
