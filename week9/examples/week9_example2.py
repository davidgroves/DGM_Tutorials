# Week9, Example2

import random

def roll_die():
    return(random.randint(1,6))

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





