import random
from agent import Agent


class RandomAgent(Agent):
    def select_action(self, game, state):
        actions = game.get_actions(state)
        return actions[random.randint(0, len(actions)-1)]
