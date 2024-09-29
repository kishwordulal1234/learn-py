number = input("inter the pin code to login :) ")
number = int(number)
username = input("inter the user name ")


if number == 7894 and username == 'kishwor' :
    print("login in sucess sucessful")
    input("press enter to continue:")
    print("welcome admin")
    exit()
else :
    print("please try gain letter with user name or password ")
if number == 7894 or username == 'kishwor' : 
    print("verify you are admin")
    login_qn = input("inter your master code")
    if login_qn == '1916' or login_qn == '1619' :
        print("verification sucessful")
        print("welcome admin")
        exit()
else :
    print("pleasse continue to verify") 
name = input("inter your name ")
if name.startswith("kishwor") :
    print("hello kishwor")
else : 
    print("pleas login eithr using pin or username")
    exit()
