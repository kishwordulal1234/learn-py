import os 




ip = input("inter the ip: ")
n = input('''inter the choise  
          
          a for aggrasive scan
          
          b for normal and 
          
          c for vuln and d for all
          
          '''  )




if n == "a":
    print(os.system(f"nmap {ip} -A" ))
elif n == "b":
    print(os.system(f"nmap {ip}"))
elif n == "c":
    pprint(os.system(f"nmap {ip} -vuln"))
elif n == "d":
    print(os.system(f"nmap {ip} -A -vuln"))
else:
    (" print invalid choise")