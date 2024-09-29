import random as claw

print("""
      
      
 / \--------------------------------------------------------------, 
 \_,|                                                             | 
    |          o for rock
           1 for paper 
      2 for siseor   | 
    |  ,------------------------------------------------------------
    \_/___________________________________________________________/ 
      
      
      
      
      
      
     """)
rock = 0
paper = 1
seasor = 2

hand = int(input("inter the num as according: "))
ai_hand = claw.randint(0,2)

while hand < 0 or hand > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
    hand = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))
if hand > ai_hand:
    print(f"you won by {hand}")
elif hand < ai_hand:
    print(f"ai won by {ai_hand}")
elif hand == ai_hand:
    print(f"both equal")
while hand == ai_hand:
    hand = int(input("inter the num as according: "))
else:
    print("game over")