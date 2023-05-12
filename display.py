from problem import *
from math import inf

from minimax import *
import pygame

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 150, 0)
red = (255, 0, 0)

# State
n = 8
state = start_state(n)
depth_limit = 5
turn = 0

# Display
pygame.init()
display = pygame.display.set_mode([700, 800])
pygame.display.set_caption('Othello Game')
font = pygame.font.SysFont("comicsansms", 48)
ai_button = pygame.Rect(500, 680, 200, 50)
ai_text = font.render('AI Move', True, black)

# Piece Counter
black_pieces = font.render('Black: 2', True, black)
white_pieces = font.render('White: 2', True, black)

# Game loop
displaying = True
while displaying:

    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Window closed
            displaying = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse clicked
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                row = (y // 75)
                col = (x // 75)
                if ai_button.collidepoint(x, y):
                    if turn % 2 == 0:
                        v, move = black_value(state, alpha=-inf, beta=+inf, depth_limit=depth_limit)
                        state = next_state_black(state, move)
                        turn += 1
                        black_pieces = font.render('Black: ' + str(count_pieces(state, 'B')), True, black)
                        white_pieces = font.render('White: ' + str(count_pieces(state, 'W')), True, black)
                        if terminal_test(state):
                            break
                    else:
                        v, move = white_value(state, alpha=-inf, beta=+inf, depth_limit=depth_limit)
                        state = next_state_white(state, move)
                        turn += 1
                        black_pieces = font.render('Black: ' + str(count_pieces(state, 'B')), True, black)
                        white_pieces = font.render('White: ' + str(count_pieces(state, 'W')), True, black)
                        if terminal_test(state):
                            break
                else:
                    row = (y // 75)-2
                    col = x // 75
                    if row >= 0 and row < n and state[row][col] == ' ':
                        if turn % 2 == 0:
                            state[row][col] = 'B'
                            turn += 1
                            black_pieces = font.render('Black: ' + str(count_pieces(state, 'B')), True, black)
                            white_pieces = font.render('White: ' + str(count_pieces(state, 'W')), True, black)
                            if terminal_test(state):
                                break
                        else:
                            state[row][col] = 'W'
                            turn += 1
                            black_pieces = font.render('Black: ' + str(count_pieces(state, 'B')), True, black)
                            white_pieces = font.render('White: ' + str(count_pieces(state, 'W')), True, black)
                            if terminal_test(state):
                                break

    # Display update
    display.fill(green)

    # Draw vertical lines
    for i in range(9):
        pygame.draw.line(display, black, (i * 75, 75), (i * 75, 675), 2)

    # Draw horizontal lines
    for i in range(9):
        pygame.draw.line(display, black, (0, (i + 1) * 75), (600, (i + 1) * 75), 2)

    # Draw pieces
    for i in range(n):
        for j in range(n):
            if state[i][j] == 'B':
                pygame.draw.circle(display, black, (j * 75 + 38, i * 75 + 113), 30)
            elif state[i][j] == 'W':
                pygame.draw.circle(display, white, (j * 75 + 38, i * 75 + 113), 30)

    # Draw score
    black_score = sum([row.count('B') for row in state])
    white_score = sum([row.count('W') for row in state])
    score_text = font.render(f"Black: {black_score}  White: {white_score}", True, black)
    display.blit(score_text, (10, 670))

    # AI move button
    pygame.draw.rect(display, red, ai_button)
    display.blit(ai_text, (500, 670))

    # Update display
    pygame.display.flip()

pygame.quit()



