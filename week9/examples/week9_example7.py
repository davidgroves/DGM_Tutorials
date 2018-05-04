# Week9, Example7

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

    while True:
        turns += 1

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
plt.title("Number of games that take X turns")
plt.show()
