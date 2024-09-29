user_name = input("Enter your name: ")
user_pass_pin = input("Enter your password or PIN: ")

# Check if user_name is one of the specified names and user_pass_pin matches one of the specified credentials
if user_name in ['kishwor', 'unknone', 'hart'] and (user_pass_pin == 'blueking99' or user_pass_pin == '7894'):
    print("Login successful")
else:
    print("Incorrect credentials. Please try again.")
    exit()  # Exit the program after unsuccessful login

# The program continues with additional code if login is successful
print("Welcome!")

# Additional code can go here for actions after successful login
