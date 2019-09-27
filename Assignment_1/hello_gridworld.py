from assignment1.gridworld import Gridworld


def run():
    gridworld = Gridworld('gw/1.txt')
    print("Hello Gridworld!")
    print(gridworld.states)

if __name__ == '__main__':
    run()
