# Implements the game of Othello.

# Returns two black pieces and two white pieces in diagonal
def start_state(n):
    board = [[' ' for i in range(n)] for j in range(n)]
    mid = n // 2

    board[mid - 1][mid - 1] = 'W'
    board[mid][mid] = 'W'

    board[mid - 1][mid] = 'B'
    board[mid][mid - 1] = 'B'

    return board

# Returns a list of actions available.
def action_list_black(state):
    n = len(state)
    actions = []
    for i in range(n):
        for j in range(n):
            if state[i][j] == 'B':
                # check move up
                if i > 1 and state[i-1][j] == 'W':
                    for k in range(2, i+1):
                        if state[i-k][j] == 'B':
                            break
                        elif state[i-k][j] == ' ':
                            actions.append((i-k,j))
                            break
                # check move down
                if i < n-2 and state[i+1][j] == 'W':
                    for k in range(2, n-i):
                        if state[i+k][j] == 'B':
                            break
                        elif state[i+k][j] == ' ':
                            actions.append((i+k,j))
                            break
                # check move left
                if j > 1 and state[i][j-1] == 'W':
                    for k in range(2, j+1):
                        if state[i][j-k] == 'B':
                            break
                        elif state[i][j-k] == ' ':
                            actions.append((i,j-k))
                            break
                # check move right
                if j < n-2 and state[i][j+1] == 'W':
                    for k in range(2, n-j):
                        if state[i][j+k] == 'B':
                            break
                        elif state[i][j+k] == ' ':
                            actions.append((i,j+k))
                            break
                # check move up-left diagonal
                if i > 1 and j > 1 and state[i-1][j-1] == 'W':
                    for k in range(2, min(i+1, j+1)):
                        if state[i-k][j-k] == 'B':
                            break
                        elif state[i-k][j-k] == ' ':
                            actions.append((i-k,j-k))
                            break
                # check move up-right diagonal
                if i > 1 and j < n-2 and state[i-1][j+1] == 'W':
                    for k in range(2, min(i+1, n-j)):
                        if state[i-k][j+k] == 'B':
                            break
                        elif state[i-k][j+k] == ' ':
                            actions.append((i-k,j+k))
                            break
                # check move down-left diagonal
                if i < n-2 and j > 1 and state[i+1][j-1] == 'W':
                    for k in range(2, min(n-i, j+1)):
                        if state[i+k][j-k] == 'B':
                            break
                        elif state[i+k][j-k] == ' ':
                            actions.append((i+k,j-k))
                            break
                # check move down-right diagonal
                if i < n-2 and j < n-2 and state[i+1][j+1] == 'W':
                    for k in range(2, min(n-i, n-j)):
                        if state[i+k][j+k] == 'B':
                            break
                        elif state[i+k][j+k] == ' ':
                            actions.append((i+k,j+k))
                            break
    return actions

def action_list_white(state):
    n = len(state)
    actions = []
    for i in range(n):
        for j in range(n):
            if state[i][j] == 'W':
                # check move up
                if i > 1 and state[i-1][j] == 'B':
                    for k in range(2, i+1):
                        if state[i-k][j] == 'W':
                            break
                        elif state[i-k][j] == ' ':
                            actions.append((i-k,j))
                            break
                # check move down
                if i < n-2 and state[i+1][j] == 'B':
                    for k in range(2, n-i):
                        if state[i+k][j] == 'W':
                            break
                        elif state[i+k][j] == ' ':
                            actions.append((i+k,j))
                            break
                # check move left
                if j > 1 and state[i][j-1] == 'B':
                    for k in range(2, j+1):
                        if state[i][j-k] == 'W':
                            break
                        elif state[i][j-k] == ' ':
                            actions.append((i,j-k))
                            break
                # check move right
                if j < n-2 and state[i][j+1] == 'B':
                    for k in range(2, n-j):
                        if state[i][j+k] == 'W':
                            break
                        elif state[i][j+k] == ' ':
                            actions.append((i,j+k))
                            break
                # check move up-left diagonal
                if i > 1 and j > 1 and state[i-1][j-1] == 'B':
                    for k in range(2, min(i+1, j+1)):
                        if state[i-k][j-k] == 'W':
                            break
                        elif state[i-k][j-k] == ' ':
                            actions.append((i-k,j-k))
                            break
                # check move up-right diagonal
                if i > 1 and j < n-2 and state[i-1][j+1] == 'B':
                    for k in range(2, min(i+1, n-j)):
                        if state[i-k][j+k] == 'W':
                            break
                        elif state[i-k][j+k] == ' ':
                            actions.append((i-k,j+k))
                            break
                # check move down-left diagonal
                if i < n-2 and j > 1 and state[i+1][j-1] == 'B':
                    for k in range(2, min(n-i, j+1)):
                        if state[i+k][j-k] == 'W':
                            break
                        elif state[i+k][j-k] == ' ':
                            actions.append((i+k,j-k))
                            break
                # check move down-right diagonal
                if i < n-2 and j < n-2 and state[i+1][j+1] == 'B':
                    for k in range(2, min(n-i, n-j)):
                        if state[i+k][j+k] == 'W':
                            break
                        elif state[i+k][j+k] == ' ':
                            actions.append((i+k,j+k))
                            break
    return actions

def next_state_black(state, action):
    if action is None:
        return state

    i, j = action
    n = len(state)
    new_state = [row[:] for row in state]
    new_state[i][j] = 'B'
    flip_list = []


    for k in range(1, n - i):
        if new_state[i + k][j] == 'W':
            flip_list.append((i+k, j))
        elif new_state[i + k][j] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break

    flip_list = []
    for k in range(1, i + 1):
        if new_state[i - k][j] == 'W':
            flip_list.append((i-k, j))
        elif new_state[i - k][j] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break

    flip_list = []
    for k in range(1, n - j):
        if new_state[i][j + k] == 'W':
            flip_list.append((i, j+k))
        elif new_state[i][j + k] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break

    flip_list = []
    for k in range(1, j + 1):
        if new_state[i][j - k] == 'W':
            flip_list.append((i, j-k))
        elif new_state[i][j - k] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break

    flip_list = []
    # check up-left diagonal
    for k in range(1, min(i+1, j+1)):
        if new_state[i- k][j - k] == 'W':
            flip_list.append((i -k, j-k))
        elif new_state[i-k][j - k] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break

    flip_list = []
    # check up-right diagonal
    for k in range(1,min(i+1, n-j)):
        if new_state[i-k][j + k] == 'W':
            flip_list.append((i-k, j+k))
        elif new_state[i-k][j + k] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break

    flip_list = []
    # check down-left diagonal
    for k in range(1, min(n-i, j+1)):
        if new_state[i+k][j - k] == 'W':
            flip_list.append((i+k, j-k))
        elif new_state[i+k][j - k] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break



    flip_list = []
    # check down-right diagonal
    for k in range(1, min(n-i, n-j)):
        if new_state[i+k][j + k] == 'W':
            flip_list.append((i+k, j+k))
        elif new_state[i+k][j + k] == 'B':
            for r, c in flip_list:
                new_state[r][c] = 'B'
            break
        else:
            break

    return new_state





def next_state_white(state, action):
    if action is None:
        return state

    i,j = action
    n = len(state)
    new_state = [row[:] for row in state]
    new_state[i][j] = 'W'
    flip_list = []
    # check up
    for k in range(1, n - i):
        if new_state[i + k][j] == 'B':
            flip_list.append((i + k, j))
        elif new_state[i + k][j] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    flip_list = []
    for k in range(1, i + 1):
        if new_state[i - k][j] == 'B':
            flip_list.append((i - k, j))
        elif new_state[i - k][j] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    flip_list = []
    for k in range(1, n - j):
        if new_state[i][j + k] == 'B':
            flip_list.append((i, j + k))
        elif new_state[i][j + k] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    flip_list = []
    for k in range(1, j + 1):
        if new_state[i][j - k] == 'B':
            flip_list.append((i, j - k))
        elif new_state[i][j - k] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    flip_list = []
    # check up-left diagonal
    for k in range(1, min(i + 1, j + 1)):
        if new_state[i - k][j - k] == 'B':
            flip_list.append((i - k, j - k))
        elif new_state[i - k][j - k] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    flip_list = []
    # check up-right diagonal
    for k in range(1, min(i + 1, n - j)):
        if new_state[i - k][j + k] == 'B':
            flip_list.append((i - k, j + k))
        elif new_state[i - k][j + k] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    flip_list = []
    # check down-left diagonal
    for k in range(1, min(n - i, j + 1)):
        if new_state[i + k][j - k] == 'B':
            flip_list.append((i + k, j - k))
        elif new_state[i + k][j - k] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    flip_list = []
    # check down-right diagonal
    for k in range(1, min(n - i, n - j)):
        if new_state[i + k][j + k] == 'B':
            flip_list.append((i + k, j + k))
        elif new_state[i + k][j + k] == 'W':
            for r, c in flip_list:
                new_state[r][c] = 'W'
            break
        else:
            break

    return new_state



def utility(state):
    num_black = 0
    num_white = 0
    for row in state:
        for col in row:
            if col == 'B':
                num_black += 1
            elif col == 'W':
                num_white += 1


    if num_black > num_white:
        return 1
    elif num_white > num_black:
        return -1
    else:
        return 0



def terminal_test(state):
    return not action_list_black(state) and not action_list_white(state)

def count_pieces(state, player):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == player:
                count += 1
    return count
