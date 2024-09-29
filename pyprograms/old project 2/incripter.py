text = str(input("Enter text to encrypt using ASCII algorithm: "))

if not text.isalpha():
    print("Please enter the text only")

while not text.isalpha():
    text = str(input("Enter text to encrypt using ASCII algorithm: "))

# Use ord() on each character separately
for word in text:
    ascii_value = ord(word)  # Get ASCII value
    print(f"The encrypted value of '{word}' is {ascii_value}")



drycpt = int(input("inter the value to difcript "))
print(f" your dicripted value is {chr(drycpt)}")