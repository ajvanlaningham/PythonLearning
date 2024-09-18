friend1 = "Rolf"
friend2 = "Bob"
friend3 = "Anne"

print(f"{friend1}, {friend2}, {friend3}")

friends = ["Rolf", "Bob", "Anne"]
print(friends[0])

print(len(friends)) # "len" for "length"/"count"

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]  #list of lists/objects

print(friends[0][0])  #this will print "Rolf"

print(friends[1][1]) #prints Bob's Age "(30)"

friends.append(["Jen", 31]) # Adds someone to the end of the list

print(friends)

friends.remove("Anne") ## will cause an error because "Anne" by herself is not in the list
friends.remove(["Anne", 27])
print(friends)