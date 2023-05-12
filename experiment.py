from problem import *
from random import random
from minimax import *
import random
from time import time


# Initialize variables
turn = 0
depth_limit = 8
n = 9
state = start_state(n)
before = time()

# Game loop
i = 0
while i<10:
    while True:
        if turn % 2 == 0:  # player 1(random)
            action = action_list_black(state)
            if len(action) == 0:
                break
            else:
                # Play randomly
                action = random.choice(action_list_black(state))

            state = next_state_black(state, action)
            #print("Player-1", action, "and",utility(state), time() - before, "seconds.")
        else:  # player 2 (minmax)
            action = action_list_white(state)
            if len(action) == 0:
                break
            else:
                value, move = white_value(state, alpha=-inf, beta=+inf, depth_limit=depth_limit)

            state = next_state_white(state, move)
            #print("MinMax", move , "and",utility(state), time() - before, "seconds.")

        turn += 1
    # Print the final game state and utility value
    #print("Final game state:")
    #for row in state:
    #    print(row)
    Utility_value = utility(state)
    if Utility_value == -1:
        print("Minmax Player Won and ", time() - before, "seconds.")
    elif Utility_value == 1:
        print("Random Player Won and ", time() - before, "seconds.")
    else:
        print("The game is a Tie and ", time() - before, "seconds.")

    i += 1
    state = start_state(n)


