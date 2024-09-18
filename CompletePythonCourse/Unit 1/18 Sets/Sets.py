#Sets do not hold order
#Sets do not contain duplicated values (hashSet)

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")  #puts "Jen" in Art friends somewhere, randomly

print(art_friends)

art_friends.remove("Jen")
print(art_friends)