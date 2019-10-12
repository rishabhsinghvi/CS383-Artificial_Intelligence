from game import Game, State
from random_agent import RandomAgent
from minimax_agent import MinimaxAgent
import random
from eval_fns import *
import math

if __name__ == '__main__':
    g = Game(7)

    # Example of setting a custom start state for the game
    # g.set_init_state(State(
    #      board=[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    #      min_pos=(1, 0),
    #      max_pos=(1, 1),
    #      min_to_play=True
    # ))

    

    # You can set the random seed to make your tests repeatable
    # random.seed(43110)

    # Create the agents to play in the game
    min_player = MinimaxAgent()
    #max_player = RandomAgent()
    max_player = RandomAgent()

    # Run a complete game between the two players
    #g.play(min_player, max_player, verbose=True)

    total_games = 0
    minimax_wins = 0
    for _ in range(0, 50):
        utility, moves = g.play(min_player, max_player, verbose = False)
        if utility == -1:
            minimax_wins += 1
        total_games += 1
    

    print("\n\n\nTotal Games: "+ str(total_games))
    print("MiniMax Wins: "+ str(minimax_wins))


