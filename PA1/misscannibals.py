# Name: Bradley Diep
# CPSC 481-01 Summer 2022
# M/T/W 10:30 am - 1:30 pm

from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    # YOUR CODE GOES HERE
    def goal_test(self, state):
        return state == self.goal
    
    
    def actions(self, state):
        action_seq = []
        possible_actions = ['MM', 'MC', 'CC', 'M', 'C']

        # iterate through all possible actions and test whether they are possible depending on the state
        for action in possible_actions:
            right_cann_b4 = self.C - state[1]
            right_miss_b4 = self.M - state[0]
            
            next_state = self.result(state, action)    
            right_cann = self.C - next_state[1]
            right_miss = self.M - next_state[0]

            # invalid states on whether more cannibals are on left bank or right bank
            # checking if there's enough missionaries/cannibals on one side to perform the action
            # left to right
            if (state[2] == True): 
                if state[0] < action.count('M'):
                    continue
                if state[1] < action.count('C'):
                    continue
                
            # right to left
            if (state[2] == False): 
                if right_miss_b4 < action.count('M'):
                    continue
                if right_cann_b4 < action.count('C'):
                    continue
                
            # left to right (check if more cannibals than missionaries and if all missionaries on left)
            if (next_state[1] > next_state[0]) and (next_state[0] > 0):
                continue
            
            # right to left (check if more cannibals than missionaries and if all missionaries on right)
            if (right_cann > right_miss) and (right_miss > 0):
                continue
            
            action_seq.append(action)
            
        return action_seq
        
        
    def result(self, state, action):
        # crossing to right river bank
        if state[2] == True:
            old_m = state[0]
            cross_over_m = action.count('M')
            new_miss = old_m - cross_over_m
        
            old_c = state[1]
            cross_over_c = action.count('C')
            new_cann = old_c - cross_over_c
        else:
        # crossing to left river bank
            old_m = state[0]
            cross_over_m = action.count('M')
            new_miss = old_m + cross_over_m
        
            old_c = state[1]
            cross_over_c = action.count('C')
            new_cann = old_c + cross_over_c
        
        # checking where boat is and switching its state
        if state[2] == True:
            river_left = False
        else:
            river_left = True
            
        return (new_miss, new_cann, river_left)

    
if __name__ == '__main__':
    mc = MissCannibals(3,3)
    # print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']
    # print(mc.result((2,2, False), 'M'))
	
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
