from .agent import Agent

from queue import PriorityQueue
# Manhattan distance as the heuristic
 
def manhattan_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


class GBFS(Agent):
    def search(self, gridworld):
        
        start = gridworld.initial_state
        goal = gridworld.goal_state

        nodes_expanded = 0

        pq = PriorityQueue()
        seen = set()

        pq.put((manhattan_distance(start, goal), start, [start]))

        while not pq.empty():
            heuristic, state, path = pq.get(block = False)
            seen.add(state)

            if state == goal:
                cost = 0
                for i in range(1, len(path)):
                    cost += gridworld.cost(path[i])
                return path, cost, nodes_expanded
            
            nodes_expanded += 1

            for neighbor in gridworld.successors(state):
                """
                if (neighbor not in seen and not self.exists_in_pq(pq, state)):
                    pq.put((manhattan_distance(neighbor, goal), neighbor, path + [neighbor]))
                elif (neighbor not in seen and self.get_pq_value(pq, neighbor) > manhattan_distance(neighbor, goal)):
                    pq.put((manhattan_distance(neighbor, goal), neighbor, path + [neighbor]))
                """
                if neighbor not in seen:
                    pq.put((manhattan_distance(neighbor, goal), neighbor, path + [neighbor]))
                
        return ([], 0, nodes_expanded)

        
    def exists_in_pq(self, pq, state):
        for item in pq.queue:
            if item[1] == state:
                return True
        return False

    def get_pq_value(self, pq, state):
        if not self.exists_in_pq(pq, state):
            return None
        for item in pq.queue:
            if item[1] == state:
                return item[0]