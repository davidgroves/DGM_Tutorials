# Week9, Homework3

import collections
import random
import matplotlib.pyplot as plt

def roll_die():
    return random.randint(1,6)

end_position = {}

for i in range(1,31):
    end_position[i] = i

end_position[3] = 22
end_position[5] = 8
end_position[11] = 26
end_position[20] = 29

end_position[17] = 4
end_position[19] = 7
end_position[21] = 9
end_position[27] = 1

total_turns = 0
shortest_game = 999999999   # Make our short game really long.
longest_game = 0            # Make our long game really short.

def game():
    pos = 1
    turns = 0
    can_move = False

    while True:
        turns += 1

        # We can't move until we roll a 6.
        if can_move == False:
            if roll_die() == 6:
                can_move = True
        else:
            prospective_position = pos + roll_die()

            if prospective_position <= 30:
                pos = end_position[prospective_position]

            if prospective_position > 30:
                pos = end_position[30 - (prospective_position - 30)]

            if pos == 30:
                return turns

number_of_games = 10000
turn_count = collections.defaultdict(int)

for i in range(number_of_games):
    turn_count[game()] += 1

plt.bar(turn_count.keys(), turn_count.values())
plt.xlabel("Turns")
plt.ylabel("Games")

# Work out the mean game length.
# And while at it, work out the modal game length as well.
total_turns = 0
mode_count = 0
mode_length = 0

for length, gamecount in turn_count.items():
    total_turns += (length * gamecount)
    if gamecount > mode_count:
        mode_length = length
        mode_count = gamecount

mean_turns = total_turns / number_of_games

# Build up a title string
title = "Number of games that take X turns\n"
title += f"Mean Game Length = {str(mean_turns)}\n"
title += f"Modal Game Length = {str(mode_length)}\n"

plt.title(title)
plt.show()
