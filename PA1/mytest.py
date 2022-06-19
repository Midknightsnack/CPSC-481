from search import *

eight_puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0))

if __name__ == '__main__':
    
    print(eight_puzzle.find_blank_square((6, 3, 5, 1, 8, 4, 2, 0, 7)))
    print(eight_puzzle.actions((0, 1, 2, 3, 4, 5, 6, 7, 8))) # DOWN, RIGHT
    #print(eight_puzzle.result((0, 1, 2, 3, 4, 5, 6, 7, 8), 'DOWN'))
    #print(eight_puzzle.goal_test((1, 2, 3, 4, 5, 6, 7, 8, 0))) #true
    #print(eight_puzzle.goal_test((4, 8, 1, 6, 0, 2, 3, 5, 7))) #false
    #print(eight_puzzle.check_solvability((0, 1, 2, 3, 4, 5, 6, 7, 8)))
    print(astar_search(eight_puzzle, h=None, display=True).solution())
    #print(breadth_first_graph_search(eight_puzzle, h=None, display=True).solution())
    # print(depth_first_graph_search(eight_puzzle, h=None, display=True).solution())
    exit()

    g = Graph()
    g.connect('A', 'B')
    g.connect('A', 'C')
    g.connect('B', 'D')
    g.connect('B', 'E')
    g.connect('C', 'F')
    g.connect('C', 'G')
    g.connect('E', 'C')
    g.connect('E', 'F')
    g.connect('D', 'E')
    #print(g.nodes())
    g_problem = GraphProblem('A', 'D', g)
    #print(g_problem.actions('A'))
    #print(breadth_first_graph_search(g_problem).solution())
    print(depth_first_graph_search(g_problem).solution())
    #print(astar_search(eight_puzzle).solution())
