user_name = input("inter your name: ")
user_password = input("inter your password:")

if user_name == 'kishwor' and user_password == 'blueking99' : 
    print("login sucessfull")
    input("enter to continue ")
    print(f"you are welcome admin {user_name}")
else : 
    print("please try again letter ")
    exit()
#if either password or user name is correct 
if user_name == 'kishwor' or   user_password == 'blueking99' : 
    print("either password or user is correce please verify that you are admin")
    input()
    master_key = input("please inter the master key ")
    if master_key == 7894 :
        print(f"login sucessful welcome {user_name}")
else : 
    print("you have try to many time ")
    bollet_key1 = input("inter the bullet login code")
    bollet_key2 = input("input the second bullet key ")
if bollet_key1 == 1916 or bollet_key2 == 1619 : 
    print("login sucessful")
    print(f" welcome admin {user_name}")
else : 
    print("you have been blocked")
    exit()
    
    