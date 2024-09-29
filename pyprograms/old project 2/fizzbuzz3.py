num = int(input("inte rthe number "))

for litr in range(1, num + 1):
    if litr % 3 == 0 and litr % 5 == 0:
        print("FIZZBUZZ")
    elif litr % 3 == 0:
        print("FIZZ")
    elif litr % 5 == 0:
        print("BUZZ")
    else:
        print(litr)
        
        
        
        
    