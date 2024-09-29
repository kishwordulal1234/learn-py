import random as rmd


print(" the maxium limit is from 1 to 99999")

length = int(input("type the length of password you want :): "))

charrector_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+/|}{"
password = ""

while length > 99999:
    print("please inter the number under the limit ")
    length = int(input("type the length of password you want :): "))
for i in range(length):
    password += rmd.choice(charrector_set)
    print(f"your generated password is {password}")
    
    
    

    
    
