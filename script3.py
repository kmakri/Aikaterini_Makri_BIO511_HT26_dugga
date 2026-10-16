# question 4
import random

# random.randint(1, 6) # generates an int from 1 to 6
# randint() method returns an integer number selected element from the specified range

# a)
games_amount = 20
dict = {"ALICE": 0, "BOB": 0, "DRAW": 0} # create dictionary with outcomes as the keys and numbers of times each outcome occured as values

for i in range(games_amount):
    roll_a = random.randint(1, 6) # each player throws a rice
    roll_b = random.randint(1, 6)

    if roll_a > roll_b: # if statements for each possible outcome
        dict["ALICE"] += 1 # if alice wins, add 1 to alice's total
    elif roll_b > roll_a: # if bob wins, add 1 to his total
        dict["BOB"] += 1
    else: # if draw, then add 1 to its total
        dict["DRAW"] += 1

print(dict)

# b)
games_played = int(input("How many games do you want to play? "))
player_1 = str(input("Who is player 1? "))
player_2 = str(input("Who is player 2? "))

def dice(rounds):
    results = {player_1: 0, player_2: 0, "DRAW": 0} # create dictionary with outcomes as the keys and numbers of times each outcome occured as values

    for i in range(rounds):
        roll_a = random.randint(1, 6) # each player throws a rice
        roll_b = random.randint(1, 6)

        if roll_a > roll_b: # if statements for each possible outcome
            results[player_1] += 1 
        elif roll_b > roll_a: 
            results[player_2] += 1
        else: # if draw, then add 1 to its total
            results["DRAW"] += 1
    return results 

game_summary = dice(games_played)
print(game_summary)