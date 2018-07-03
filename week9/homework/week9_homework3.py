# Week9, Homework4

import random
import statistics
import matplotlib.pyplot as plt

def roll_die():
    return random.randint(1,6)

def roll_to_start():
    turns_to_start = 0
    while True:
        turns_to_start += 1
        if roll_die() == 6:
            return turns_to_start

def bounce(square_landed_on):
    return 30 - (square_landed_on - 30)

def end_square(square_landed_on):
    # Ladders
    if square_landed_on == 3:
        return 22
    if square_landed_on == 5:
        return 8
    if square_landed_on == 11:
        return 26
    if square_landed_on == 20:
        return 29

    # Snakes
    if square_landed_on == 17:
        return 4
    if square_landed_on == 19:
        return 7
    if square_landed_on == 21:
        return 9
    if square_landed_on == 27:
        return 1

    # No snake or ladder, but passed 30 ?
    if square_landed_on > 30:
        return bounce(square_landed_on)
        pass

    # This is just where we are.
    return square_landed_on

def game():
    position = 1

    # Calculate how many turns it took to roll a 6 to start.
    turns = roll_to_start()

    # Play out the game
    while True:
        turns += 1
        position = end_square(position + roll_die())

        # Have we won ?
        if position == 30:
            return turns

####################
### MAIN PROGRAM ###
####################

number_of_games = 10000
turns = []          # A list with the turncount of each game played.

for i in range(number_of_games):
    turns.append(game())

print (f"Mean of number of turns: {statistics.mean(turns):.2f}")
print (f"Median of number of turns: {statistics.median(turns):.2f}")

try:
    print (f"Mode of number of turns: {statistics.mode(turns):.2f}")
except statistics.StatisticsError:
    print (f"There is no unique mode")

print (f"Standard Deviation of number of turns: {statistics.stdev(turns):.2f}")
print (f"Variance of number of turns: {statistics.variance(turns):.2f}")

# Draw a histogram
plt.hist(turns, 100)
plt.xlabel("Turns")
plt.ylabel("Games")
plt.title("Number of games that take X turns")
plt.show()
