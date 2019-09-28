from .agent import Agent

from queue import PriorityQueue


def manhattan_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])



class AStar(Agent):
    def search(self, gridworld):
        start = gridworld.initial_state
        goal = gridworld.goal_state

        nodes_expanded = 0

        pq = PriorityQueue()
        seen = set()

        pq.put((0 + manhattan_distance(start, goal), start, [start]))

        while not pq.empty():
            heuristic, state, path = pq.get(block = False)
            seen.add(state)

            if state == goal:
                return path, self.get_cost(gridworld, path), nodes_expanded
            
            nodes_expanded += 1

            for neighbor in gridworld.successors(state):
#                print(neighbor)
                """
                if (neighbor not in seen and not self.exists_in_pq(pq, state)):
                    pq.put((self.get_cost(gridworld, path + [neighbor]) + manhattan_distance(neighbor, goal), neighbor, path + [neighbor]))
                elif (neighbor not in seen and (self.get_pq_value(pq, neighbor) > (self.get_cost(gridworld, path + [neighbor]) + gridworld.cost(neighbor)))):
                    pq.put((self.get_cost(gridworld, path + [neighbor]) + manhattan_distance(neighbor, goal), neighbor, path + [neighbor]))
                """

                if neighbor not in seen:
                     pq.put((self.get_cost(gridworld, path + [neighbor]) + manhattan_distance(neighbor, goal), neighbor, path + [neighbor]))
                
            #print(pq.queue)
        
        return ([], 0, 0)


        pass

    
    def get_cost(self, gw, path):
        cost = 0
        for i in range(1, len(path)):
            cost += gw.cost(path[i])
        return cost

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

