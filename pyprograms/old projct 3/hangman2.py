import random 
print(" welcomew to hang man game ")

word = ["apple", "banan", "cat"]

word_chosen = random.choise(word)

print(" you have 10 chance ")

display_word = []

for letter in word_chosen:
    display_word += "_"
    
    
print(display_word)

