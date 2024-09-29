print(""" 
      
      
      
   ___      
  / _ \_____________/`/\+-/\'\'\
\_\(_)/_/ term calc -+-    -+-+-
 _//o\\_            \'\/+-\/`/`/
  /   \              \/-+--\/`/ 
                                                                            
""")

print("this is simple calculator")
num1 = eval(input("input yout 1 number:"))
num2 = eval(input("inter a seconf number:"))
print("""
+ for addition
- for substraction
* for multiplication
/ for devide 
% for reminder 
** for square
""")

operator = input(" enter either of this + - * / % ** : ")
print(""" 
      
      
      
      .--..--..--..--..--..--.
    .' \  (`._   (_)     _   \
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\
             ||       ||
             ||_.-.   ||_.-.
            (_.--__) (_.--__) 
            
            
            
            
            
            """)
if operator == "+":
    print(num1+num2)
elif  operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "%":
    print(num1%num2)
elif operator == "**":
    print(num1**num2)
else:
    print("invalid operator ")
    exit()
    
