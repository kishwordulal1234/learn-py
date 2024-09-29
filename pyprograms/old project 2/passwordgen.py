import random as rmd

# Prompt the user to enter the desired password length
length = int(input("Enter the length of the password: "))

# Define the character set to choose from
character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+/|}{"

# Initialize an empty string to hold the final password
final_password = ""

# Generate the password by randomly selecting characters
for _ in range(length):
    final_password += rmd.choice(character_set)

# Print the generated password
print(f"Your generated password is: {final_password}")
