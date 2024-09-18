friend_ages = {"Rolf": 24, "Adam" : 30, "Anne" : 27}  #Key/Value Pairs, preserves order, no duplicates

print(friend_ages["Rolf"])  #Returns 24

friend_ages["Bob"] = 20    #Adds key "Bob" and value "24"
friend_ages["Rolf"] = 25    #updates "Rolf to 25

print(friend_ages)

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

friend = friends[0]
print(friend["name"])

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]

friend_ages = dict(friends) # turn friends into a dictionary
print(friend_ages)