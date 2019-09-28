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
        
        if not state:
            return None
        
        x = state[1]
        y = state[0]

        states = list()

        

        if x==0:
            if self.states[x+1][y] !='#':
                states.append((y, x+1))
        elif x == len(self.states) - 1:
            if self.states[x-1][y] != '#':
                states.append((y, x-1))
        else:
            if self.states[x+1][y] !='#':
                states.append((y, x+1))
            if self.states[x-1][y] != '#':
                states.append((y, x-1))
        

        if y==0:
            if self.states[x][y+1] !='#':
                states.append((y+1, x))
        elif y == len(self.states[0]) - 1:
            if self.states[x][y-1] != '#':
                states.append((y-1, x))
        else:
            if self.states[x][y+1] !='#':
                states.append((y+1, x))
            if self.states[x][y-1] != '#':
                states.append((y-1, x))
        

        return states




    def cost(self, state):
        
        if not state:
            return None
        x = state[0]
        y = state[1]

        if x >= len(self.states[0]) or x < 0:
            return None
        if y >= len(self.states) or y < 0:
            return None
        
        if self.states[y][x] == 's' or self.states[y][x] == 'g':
            return 1
        else:
            return self.states[y][x]
        
        
    def state_at(self, x, y):
        print(self.states[x][y])

