from game import Game, State
from random_agent import RandomAgent
from minimax_agent import MinimaxAgent
import random
from eval_fns import *
import math

if __name__ == '__main__':
    g = Game(5)

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
    min_player = MinimaxAgent(open_cells, 2, False)

    #max_player = RandomAgent()
    max_player = MinimaxAgent(my_eval_2, 2, False)

    # Run a complete game between the two players
    #g.play(min_player, max_player, verbose=True)

    total_games = 0
    min_player_wins = 0
    max_player_wins = 0
    num_trials = 3
    for _ in range(0, num_trials):
        utility, moves = g.play(min_player, max_player, verbose = False)
        if utility == -1:
            min_player_wins += 1
        elif utility == 1:
            max_player_wins += 1
        
        total_games += 1
    

    print("\n\n\nTotal Games: "+ str(total_games))
    print("MinPlayer Wins: " + str(min_player_wins))
    print("MaxPlayer Wins: " + str(max_player_wins))


