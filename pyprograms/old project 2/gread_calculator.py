print("thi is a simple grade calculator ")
name = input("inter your name ")
print("""calculator.py   

    .-----.
   .' -   - '.
  /  .-. .-.  \
  |  | | | |  |
   \ \o/ \o/ /
  _/    ^    \_
 | \  '---'  / |
 / /`--. .--`\ \
/ /'---` `---'\ \
'.__.       .__.'
    `|     |`
     |     \
     \      '--.
      '.        `\
        `'---.   |
              ) /
              \/
              
              
              
              
              
              """)

gpa = input("inter your mark: ")
gpa = int(gpa)
print("""
      
      

A+   = 90 - 100
A    = 80 - 90 
B+   = 70 - 80
B    = 60 - 70
C+   = 50 - 60
C    = 40 - 50
D+   = 30 - 40
E    = 20 - 30
F    = 10 - 20

  this is grading system     
      
      """)
if gpa >=90:
    print(f"congrast {name} your gpa is A+ ")
elif gpa >=80:
    print(f"congrast {name} your gpa ia A ")
elif gpa>=70:
    print(f"congrast {name} your gpa ia B+ ")
elif gpa >=60:
    print(f"congrast {name} your gpa ia B ")
elif gpa>=50:
    print(f"congrast {name} your gpa ia C+ ")
elif gpa >=40:
    print(f"congrast {name} your gpa ia C ")
elif gpa>=30:
    print(f"congrast {name} your gpa ia D+ ")
elif gpa >=20:
    print(f"congrast {name} your gpa ia E ")
elif gpa>=10:
    print(f"congrast {name} your gpa ia F ") 
elif gpa <=10:
    print(f"i am sorry {name} but your failed please better luck next time ")
else :
    print("please inter a valid grade")
    exit()
  



















