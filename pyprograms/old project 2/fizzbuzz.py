num = int(input("Enter the number: "))

for apt in range(1, num + 1):
    if apt % 3 == 0 and apt % 5 == 0:
        print("FizzBuzz")
    elif apt % 3 == 0:
        print("Fizz")
    elif apt % 5 == 0:
        print("Buzz")
    else:
        print(apt)
