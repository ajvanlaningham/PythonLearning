grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total / length
print(average)

# What's the worst data struture to store grades in?
grades = {80, 75, 90, 100} # set?
grades = (80, 75, 90, 100) # tuple?
grades = [80, 75, 90, 100] # list?
# answer: set for sure. You can't have duplicate grades! List is the best choice.
# If you do not need to add new things to variable, use a tuple.