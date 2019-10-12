"""
Evaluation functions for use with Minimax search.
We have supplied you with one example function to get started.
An evaluation function should return an estimate of the utility of a state.
Thus, it should be high when max is winning and low when min is winning, and
it should be bounded by the terminal utilities +1 and -1.
Any evaluation function should return the utility when given a terminal state.
Keep these criteria in mind when writing your evaluation functions.
"""


def open_cells(game, state):
    """
    Estimates utility from the number of open cells next to the current player.
    More open cells is preferable to fewer.
    """
    if game.is_terminal(state):
        return game.utility(state)
    else:
        # the number of open cells next to the current player
        open_cells = {cell for (cell, _) in game.get_actions(state)}

        # there are at best 8 open cells, so score is near 1 when things are
        # "good" for the current player, and near 0 when things are "bad"
        score = len(open_cells) / 8
        return -score if state.min_to_play else score


def my_eval_1(game, state):
    """
    Write your own evaluation function here.
    Your functions must take two arguments, a game and a state.

    Hint: Think about why open_cells is not a very good evaluation function!
    How might you improve it?
    """
    pass


def my_eval_2(game, state):
    """
    Write your second evaluation function here.
    """
    pass


def my_best(game, state):
    """
    Call whichever one of your two functions you think is better
    and return the result here.
    """
    pass
