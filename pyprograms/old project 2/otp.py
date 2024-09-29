# Maximum number of attempts allowed
max_attempts = 3

# Initial attempt count
attempts = 0

# Loop until the user provides a correct password or reaches the maximum attempts
while attempts < max_attempts:
    password = input("Enter the password: ")

    if password == "kishwor" or password == "dulal":
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Wrong password. Attempts left: {max_attempts - attempts}")

# Check if the user has exhausted all attempts
if attempts == max_attempts:
    print("Too many failed attempts. Please try again later.")
