# implementing monte carlo tree search for othello game
from random import random
from problem import *
import random
import math

class Node:
    def __init__(self, state, turns, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.turns = turns
        self.playouts = 0
        self.action= action
        self.utility = utility(state)

def monte_carlo_tree_search(state,turn):
    root = Node(state,turn)

    for i in range(1000):
        leaf = select(root)
        child = expand(leaf)
        result = simulate(child)
        backpropagate(result, child)

    bestchild = max(root.children, key=lambda node: node.playouts)
    bestaction = bestchild.action

    return bestaction


def select(node):
    if not node.children:
        return node
    # Calculate UCB1 score for each child node
    scores = []
    for child in node.children:
        if child.playouts == 0:
            # Choose an unexplored node
            return child
        score = child.wins / child.playouts + 2* math.sqrt(math.log(node.playouts) / child.playouts)
        scores.append(score)
    # Select child node with highest UCB1 score
    index = scores.index(max(scores))
    return select(node.children[index])

def expand(node):
    if not node.children:
        if node.turns % 2 == 0:
            actions = action_list_black(node.state)
        else:
            actions = action_list_white(node.state)
        for action in actions:
            new_state = actions_move(node.state, action, node.turns)
            child = Node(new_state,node.turns + 1,node ,action)
            node.children.append(child)
    if node.children:
        return random.choice(node.children)
    else:
        return node


def actions_move(state, action, turns):
    if turns % 2 == 0:  # black's turn
        return next_state_black(state, action)
    else:  # white's turn
        return next_state_white(state, action)



def simulate(node):
    current_state = node.state

    if node.turns % 2 == 0:
        current_player = 'B'
    else:
        current_player = 'W'

    while True:
        if current_player == 'B':
            possible_moves = action_list_black(current_state)
        else:
            possible_moves = action_list_white(current_state)

        if len(possible_moves) == 0:
            break
        move = random.choice(possible_moves)
        current_state = actions_move(current_state, move, node.turns)
        current_player = 'B' if current_player == 'W' else 'W'

    return utility(current_state)

def backpropagate(result, node):
    node.playouts += 1
    if node.turns != result:
        node.wins += 1
    if node.parent:
        backpropagate(result, node.parent)

def backpropagate(result, node):
    node.playouts += 1
    if node.turns % 2 == 0:  # If turns is even, you're looking for a -1 utility to increment wins.
        if result == -1:
            node.wins += 1
    else:                   # If turns is odd, you're looking for a +1 utility to increment wins.
        if result == 1:
            node.wins += 1
    if node.parent:
        backpropagate(result, node.parent)



#
# n = 8
# state = start_state(n)
# for i in state:
#     print(i)
#
# turn = 0
# while True:
#     if turn % 2 == 0:  # black player's turn
#         action = action_list_black(state)
#         if len(action) == 0:
#             break
#         else:
#             action = monte_carlo_tree_search(state,turn)
#
#         state = next_state_black(state, action)
#         print("Black moves", action)
#
#     else:  # white player's turn
#         action = action_list_white(state)
#         if len(action) == 0:
#             break
#         else:
#             action = monte_carlo_tree_search(state,turn)
#
#         state = next_state_white(state, action)
#         print("White moves", action)
#
#     turn += 1
#
# # Print the final game state and utility value
# print("Final game state:")
# for row in state:
#     print(row)
# print("Utility value:", utility(state))


