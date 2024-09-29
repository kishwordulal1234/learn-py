text = str(input("inter the value to incript "))

if not text.isalpha:
    print("please inter the text ")
while not text.isalpha:
    text = str(input("inter the value to incript "))
for encrypt_value in text:
    rans = ord(encrypt_value)
    print(f" your incrypted value of {encrypt_value} is {rans} ")