def greet(name,dprt,age):
    print(f"Hello, {name}!")
    print(f" you  are from dep {dprt}")
    print(f"you are {age } year old ")
    

n = input(" input you name ")
d = input("input your deparment")
a = int(input("inter yoy age "))

greet(name=n, dprt=d, age=a)