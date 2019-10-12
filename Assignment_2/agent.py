from abc import ABC, abstractmethod


class Agent(ABC):
    """An abstract game-playing agent."""
    @abstractmethod
    def select_action(self, game, state):
        """
        Choose a move given some game state.
        The implementation of this method will be different for each agent!
        """
        pass
