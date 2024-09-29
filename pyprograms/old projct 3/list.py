thislist = ["apple", "banana", "cherry"]


thislist = thislist + ["cat", "rat"]

#print(thislist[0:2])
k =thislist.index("apple")
sr = len(thislist)
print(thislist)
print(k)
#print(sr)
#thislist.remove("apple")
#thislist[1] = "kishwor"
#print(thislist)

#pe = thislist.extend(["people", "manty"])
#print(pe)
#print(thislist)

#thislist.pop(4)
#print(thislist)


mov1 = input("inter the movie 1: ")
mov2 = input(" inter the second movie ")

mov3 = input("inte rthe 3rd movie ")


ltm = []
ltm.append("i")
ltm.extend(["toilet", "ltm"])
ltm = ltm + [mov1, mov2, mov3]


print(ltm)
