import argparse
from assignment1.agents import AStar, BFS, RandomSearch, GBFS, UCS
from assignment1.gridworld import Gridworld

agents = {
    "astar": AStar,
    "bfs": BFS,
    "gbfs": GBFS,
    "ucs": UCS,
    "random": RandomSearch
}

def run():
    # Parse command line arguments.
    parser = argparse.ArgumentParser(
        description='Run the given agent algorithm on the given gridworld.')
    parser.add_argument(
        'agent', help='The agent, one of: [astar, bfs, random]')
    parser.add_argument('filename', help='Path to a gridworld, e.g. gw/1.txt')
    args = parser.parse_args()

    # Create the agent and gridworld,
    # and run the search.
    agent = agents[args.agent]()
    gridworld = Gridworld(args.filename)
    solution, cost, nodes_expanded = agent.search(gridworld)

    # Print the results.
    print('solution', solution)
    print('cost', cost)
    print('nodes_expanded', nodes_expanded)


if __name__ == '__main__':
    run()
