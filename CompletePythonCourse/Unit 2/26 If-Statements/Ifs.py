friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
    print("This runs too.")  # within the if block

print("This runs no matter what")  # it's out of the if block

if user_name == friend:
    print("Hello, friend!")
else:
    print("Hello, stranger!")

print(bool(5))

if 5:               #Reminder, 5 is "truthy"
    print("Runs.")

if user_name:       #If the user inputs something, this will be true. If they input nothing, it will not be
    print("We know your name")


friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]
user_name == input("Enter your name: ")

if user_name in friends:
    print("Hello, Friend!")
elif user_name in family:
    print("Hello, Family!")
else:
    print("I don't know you..")