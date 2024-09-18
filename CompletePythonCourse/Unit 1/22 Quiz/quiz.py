lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = []

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

player_one = {'name': 'player_one','numbers' : {13, 2, 8}}
player_two = {'name': 'player_two','numbers' : {4, 5, 6, 22, 13}}

players.append(player_one)
players.append(player_two)

player_one_correct = players[0]['numbers'].intersection(lottery_numbers)
player_two_correct = players[1]['numbers'].intersection(lottery_numbers)

# print(f"Player {players[0]['name']} got {len(player_one_correct)} numbers correct")
# print(f"Player {players[1]['name']} got {len(player_one_correct)} numbers correct")

for player in players:
    correct_numbers = player['numbers'].intersection(lottery_numbers)
    print(f"Player {player['name']} got {len(correct_numbers)} numbers correct")