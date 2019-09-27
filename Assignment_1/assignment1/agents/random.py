import random
from .agent import Agent


class RandomSearch(Agent):
    def search(self, gridworld):
        state = gridworld.initial_state
        path = [state]
        cost = 0
        nodes_expanded = 0
        while not state == gridworld.goal_state:
            successors = gridworld.successors(state)
            state = successors[random.randint(0, len(successors) - 1)]
            path.append(state)
            cost += gridworld.cost(state)
            nodes_expanded += 1
        return path, cost, nodes_expanded
