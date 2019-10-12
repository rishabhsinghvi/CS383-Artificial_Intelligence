from .agent import Agent
import queue

class BFS(Agent):
    def search(self, gridworld):
        start = gridworld.initial_state
        cost = 0
        nodes_expanded = 0

        explored = set()
        to_visit = queue.Queue()
        to_visit.put((0, start, [start]))
        
        start = True
        while queue:
            
            cost ,state, path = to_visit.get()
            if state == gridworld.goal_state:
                return path, cost, nodes_expanded

            if state in explored:
                continue
            
            explored.add(state) # add to already seen list
            
            nodes_expanded += 1

            
            neighbors = gridworld.successors(state)

            for neighbor in neighbors:
                to_visit.put((cost + gridworld.cost(neighbor), neighbor, path + [neighbor]))
            
        return [], 0, nodes_expanded


