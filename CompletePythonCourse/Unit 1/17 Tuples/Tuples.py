short_tuple = "Rolf", "Bob" #Technically correct
 
a_bit_clearer = ("Rolf", "Bob") #Easier to read

tuple_in_list = ["Rolf", "Bob"] #WRONG
tuple_in_list = [("Rolf", "Bob")] #Correct
##not_a_tuple = "Rolf", #trailing comma is bad

friends = ("Rolf", "Bob", "Anne")
friends = friends + ("Jen",)  #NOTE THE TRAILING COMMA

print(friends)