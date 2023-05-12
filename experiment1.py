from mcts import *
from problem import *
from random import random
import random
from time import time

turn = 0
n = 9
state = start_state(n)
before = time()

i = 0
while i<10:
    while True:
        if turn % 2 == 0:  # Random player's turn
            action = action_list_black(state)
            if len(action) == 0:
                break
            else:
                # Play randomly
                action = random.choice(action_list_black(state))
            state = next_state_black(state, action)
            #print("Random Player", action)
        else:  # MCTS player's turn
            action = action_list_white(state)
            if len(action) == 0:
                break
            else:
                action = monte_carlo_tree_search(state,turn)
            state = next_state_white(state, action)
            #print("White moves", action)
        turn += 1

    # Print the final game state and utility value
    #print("Final game state:")
    #for row in state:
        #print(row)
    #print("Utility value:", utility(state))
    Utility_value = utility(state)
    if Utility_value == -1:
        print("MCTS Won and utility value", time() - before, "seconds.")
    elif Utility_value == 1:
        print("Random Player Won and utility value", time() - before, "seconds.")
    else:
        print("The game is a Tie and utility value", time() - before, "seconds.")

    i += 1
    state = start_state(n)