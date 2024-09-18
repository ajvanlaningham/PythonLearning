art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)  #in Art, but not Science
science_but_not_art = science_friends.difference(art_friends)  #in science but not art

print(art_but_not_science)
print(science_but_not_art)

not_in_both = art_friends.symmetric_difference(science_friends)  #Not in both
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)  # In Both

all_friends = art_friends.union(science_friends)
print(all_friends) # Will only print Jen once!