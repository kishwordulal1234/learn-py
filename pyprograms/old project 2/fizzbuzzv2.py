num = int(input("inter the number "))

for apt in range(1, num + 1):
    if apt % 3 == 0 and apt % 5 == 0:
        print("fizzbuzz")
    elif apt % 3 == 0:
        print('fizz')
    elif apt % 5 == 0:
        print("buzz")
    else:
        print(apt)