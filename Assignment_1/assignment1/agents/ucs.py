from .agent import Agent
import queue

class UCS(Agent):
    def search(self, gridworld):
        
        goal = gridworld.goal_state
        start = gridworld.initial_state
        path = []

        cost = 0
        nodes_expanded = 0

        pq = queue.PriorityQueue()
        seen = set()

        pq.put((0, start, [start]))

        while not pq.empty():
            cost, state, path = pq.get(block = False)
            seen.add(state)

            #print(state)

            if state == goal:
                return path, cost, nodes_expanded
            
            
            nodes_expanded += 1
            
            for neighbor in gridworld.successors(state):
                if (neighbor not in seen and not self.exists_in_pq(pq, neighbor)):
                    pq.put((cost + gridworld.cost(neighbor), neighbor, path + [neighbor]))
                elif (neighbor not in seen and self.get_pq_value(pq, neighbor) > (cost + gridworld.cost(neighbor))):
                    pq.put((cost + gridworld.cost(neighbor), neighbor, path + [neighbor]))
                    
     
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
        