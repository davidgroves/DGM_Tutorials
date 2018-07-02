# Week9, Example5

import random

def roll_die():
    return random.randint(1,6)

end_position = {}

# Fill in 1 to 30 with the same position.
# This would be like a board with no snakes or ladders.
for i in range(1,31):
    end_position[i] = i

# Ladders
end_position[3] = 22
end_position[5] = 8
end_position[11] = 26
end_position[20] = 29

# Snakes
end_position[17] = 4
end_position[19] = 7
end_position[21] = 9
end_position[27] = 1

# At the start of the game, the player has taken 0 turns and is on square 1.
pos = 1
turns = 0

def game():
    turns = 0
    while True:
        # A turn has been taken
        turns += 1

        # Roll the dice and move forward that far.
        prospective_position = pos + roll_die()

        # If we haven't overshot, we do what we used to do.
        if prospective_position <= 30:
            pos = end_position[prospective_position]

        # If we have overshot, we need to bounce.
        if prospective_position > 30:
            pos = end_position[30 - (prospective_position - 30)]

        # Check for winning
        if pos == 30:
            return turns

        print(pos)

