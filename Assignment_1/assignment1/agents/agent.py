from abc import ABC, abstractmethod


class Agent(ABC):
    """An abstract search Agent."""
    @abstractmethod
    def search(self, gridworld):
        """
        Search the given gridworld for the path from the start state
        to the goal state with the minimum cost. The implementation
        of this method will be different for each agent!
        """
        pass
