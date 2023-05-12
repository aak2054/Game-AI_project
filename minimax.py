from problem import *
from math import inf


def black_value(state, alpha, beta,depth_limit):
    action = action_list_black(state)
    if len(action) ==0:
        current_utility = utility(state)
        return current_utility,None
    if depth_limit == 0:
        return evaluate(state),None

    v, move = -inf, None
    for a in action:
        v2, a2 = white_value(next_state_black(state, a), alpha, beta,depth_limit-1)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta:
            return v, move

    return v, move

def white_value(state, alpha, beta,depth_limit):
    action = action_list_white(state)
    if len(action) == 0:
        current_utility = utility(state)
        return current_utility, None

    if depth_limit == 0:
        return evaluate(state),None

    v, move = +inf, None

    for a in action:
        v2, a2 = black_value(next_state_white(state, a), alpha, beta,depth_limit-1)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            return v, move

    return v, move

def evaluate(state):
    num_black = 0
    num_white = 0
    for row in state:
        for col in row:
            if col == 'B':
                num_black += 1
            elif col == 'W':
                num_white += 1

    val = (num_black - num_white)/ (len(state) ** 2)
    return val




# # Initialize variables
# turn = 0
# depth_limit = 5
# n = 8
# state = start_state(n)
# # Game loop
# while True:
#     if turn % 2 == 0:  # black player's turn
#         action = action_list_black(state)
#         if len(action) == 0:
#             break
#         else:
#             value, move = black_value(state, alpha=-inf, beta=+inf, depth_limit=depth_limit)
#
#         state = next_state_black(state, move)
#         print("Black moves", move)
#     else:  # white player's turn
#         action = action_list_white(state)
#         if len(action) == 0:
#             break
#         else:
#             value, move = white_value(state, alpha=-inf, beta=+inf, depth_limit=depth_limit)
#
#         state = next_state_white(state, move)
#         print("White moves", move)
#
#     turn += 1
#
# # Print the final game state and utility value
# print("Final game state:")
# for row in state:
#     print(row)
# print("Utility value:", utility(state))


