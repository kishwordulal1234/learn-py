print("""  
          
 _       __ _  _              _ __        __ _            
| | ___ / _` |(_) _ _        | '_ \ __ _ / _` | ___       
| |/ _ \\__. || || ' \       | .__// _` |\__. |/ -_)      
|_|\___/|___/ |_||_||_|      |_|   \__/_||___/ \___|      

  \/________________        
 /     _____________)
/     /      _  _ |         
\/\/\/     (O) (O)|           
  |           ------, 
  |  _       ______/ 
  | (_      /   \  \
  |        /  ___\_ \       
  |        \      / / 
__|_________\______/
\______________\./__\   
 /     .       | \  |
 \    /_\   .  |  \ |\     
 |`\       /_\ |   \| \
      
""")

name = input("Enter your name: ")
password = input("Enter your password: ")

if name == "kishwor" and password == "7894":
    print("Login successful")
    input("Press enter to continue ...")
    print("""
      
      
    ____ 
   /# /_\_ 
  |  |/o\o\ 
  |  \\_/_/ 
 / |_   |   
|  ||\_ ~|  
|  ||| \/   
|  |||_     
 \//  |     
  ||  |     
  ||_  \    
  \_|  o|   
  /\___/    
 /  ||||__  
    (___)_) 
      
      """)
    print(f"How are you, {name} sir!")
    print(f"Welcome, {name} admin!")
    exit()

elif name == "kishwor" or password == "7894":
    print("Either your username or password is wrong")
    input("")
    print("Try again please")
    if name == "kishwor" and password != "7894":
        print("Login in with master key")
        master_key = input("Enter the master key: ")
        if master_key == "1916":
            print(f"Login successful, {name}")
        else:
            print("Master key is wrong")
            exit()

else:
    print("Welcome to juice shop")
    print("Available juices: mango, apple, and banana")
    product = input("Enter the juice that you want: ")
    if product == "mango":
        print(f"How many do you want, {name}?")
        quantity = int(input("Enter the amount you want: "))
        price = 15
        print(f"Total price: {quantity * price}")
    elif product == "apple":
        print(f"How many do you want, {name}?")
        quantity = int(input("Enter the amount you want: "))
        price = 25
        print(f"Total price: {quantity * price}")
    elif product == "banana":
        print(f"How many do you want, {name}?")
        quantity = int(input("Enter the amount you want: "))
        price = 250
        print(f"Total price: {quantity * price}")
    else:
        print("Thank you for visiting. Come again later.")
        exit()
