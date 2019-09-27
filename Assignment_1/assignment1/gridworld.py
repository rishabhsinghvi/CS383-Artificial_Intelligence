class Gridworld:
    states = None
    initial_state = None
    goal_state = None

    def __init__(self, filename):
        with open(filename) as file:
            self.states = [list(line) for line in file.read().splitlines()]
            for y, line in enumerate(self.states):
                for x, value in enumerate(line):
                    if value.isnumeric():
                        line[x] = int(value)
                    if value == 's':
                        self.initial_state = (x, y)
                    if value == 'g':
                        self.goal_state = (x, y)
        

    def successors(self, state):
        # TODO
        if not state:
            return None
        x = state[0]
        y = state[1]

        reachable_states = list()

        if x == 0
        pass
        
        

    def cost(self, state):
        # TODO
        if not state:
            return None
        x = state[0]
        y = state[1]

        if x >= len(self.states) or x < 0:
            return None
        if y >= len(self.states[0]) or y < 0:
            return None
        
        if self.states[x][y].isnumeric():
            return self.states[x][y]
        else:
            return 1
        

