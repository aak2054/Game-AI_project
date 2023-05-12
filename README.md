# Game-AI_project
## Othello Game Implementation with Minimax and MCTS Algorithms

This is a Python implementation of the Othello (also known as Reversi) game using the Minimax and Monte Carlo Tree Search (MCTS) algorithms for the AI opponent. The game is played on an 8x8 board, with two players, Black and White. The game is won by the player with the most pieces on the board at the end of the game.

## Getting Started
To get started with the project, you will need to install Python and the Pygame library. You can do this by following these steps:

Install Python from the official website: https://www.python.org/downloads/
Install Pygame using pip: pip install pygame

Once you have installed Python and Pygame, you can run the game by running the display.py file for graphical interface game play. To run the experiments, run the experiment.py, experiment1.py, or experiment2.py files.

## Game Rules
The game is played on an 8x8 board with 64 discs, which are white on one side and black on the other. The game starts with two black discs and two white discs placed in the center of the board. Black always moves first.

A move consists of placing a disc of the player's color on the board in a position that "outflanks" one or more of the opponent's discs. A disc or row of discs is outflanked when it is surrounded at the ends by discs of the opposite color. The outflanked discs are then flipped over to the player's color.

If a player cannot make a legal move, they must pass their turn. The game ends when both players pass their turn consecutively, or when the board is full. The player with the most discs of their color on the board at the end of the game wins

## AI Algorithms
This implementation uses two different algorithms for the AI opponent: Minimax and MCTS.

## Minimax
The Minimax algorithm is a decision-making algorithm that works by searching through all possible moves to a certain depth, evaluating each move's potential outcome, and selecting the best move based on the evaluation. The AI opponent in this game uses the Minimax algorithm with alpha-beta pruning to determine its moves.

## MCTS
The Monte Carlo Tree Search (MCTS) algorithm is another decision-making algorithm that works by simulating a large number of random games and selecting the best move based on the results of those simulations. The AI opponent in this game also uses the MCTS algorithm to determine its moves.

## Graphical Interface
The display.py file provides a graphical interface for the Othello game. It uses the Pygame library to draw the board and the pieces, and to handle user input.

To run the game with the graphical interface, run the display.py file.

## Experiments
The project includes three experiments that compare the performance of the Minimax and MCTS algorithms:

experiment.py: plays Random Player vs Minimax Player
experiment1.py: plays Random Player vs MCTS Player
experiment2.py: plays MCTS Player vs Minimax Player

In each experiment, the AI player (either Minimax or MCTS) plays against a random player. The results of the experiments are output to the console and include the number of games won by each player and the average time taken for each move.

## Project Structure
The project is structured as follows:

- display.py: the main file to run the game
- problem.py: contains the game rules and functions
- minimax.py: contains the Minimax algorithm implementation
- mcts.py: contains the MCTS algorithm implementation
- experiment.py: plays Random Player vs Minmax Player
- experiment1.py: plays Random Player vs MCTS Player
- experiment2.py: plays MCTS Player vs Minmax Player


## Credits
This project was created by Anamo Kisho. Feel free to use this code as a reference or for personal/educational purposes.
