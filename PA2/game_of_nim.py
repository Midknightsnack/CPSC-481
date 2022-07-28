# Name: Bradley Diep
# CPSC 481-01 Summer 2022
# M/T/W 10:30 am - 1:30 pm

from hmac import new
from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        initial_board = board
        moves = [] 
        for row in range(0, len(initial_board)): # start from 0, stops at 4 (length of list)
            for x in range(1, initial_board[row]+1):
                moves.append((row, x))
        self.initial = GameState(to_move='MAX', utility=0, board=initial_board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        # create new board from the move
        new_board = []
        for row in range(0, len(state.board)): 
            if row == move[0]: 
                new_objects = state.board[row] - move[1]
                new_board.append(new_objects)
            else: 
                new_board.append(state.board[row])
                
        # create new possible moves fromo the new board
        new_moves = []     
        for row in range(0, len(new_board)): 
            for x in range(1, new_board[row]+1):
                new_moves.append((row, x))

        # whose turn it is to move
        if state.to_move == 'MAX':
            player = 'MIN'
        else:
            player = 'MAX'

        #  setting new utility
        empty_board = True
        for objects in new_board:
            if objects > 0: 
                empty_board = False
        
        # if new_state is not terminal, then new_utility=0
        # else: utility = -1/+1 depending on who won
        if empty_board: # game ends
            if player == 'MAX':       # MAX wins because MIN was forced to take final piece
                new_utility = 1
            else: 
                new_utility = -1
        else: 
            new_utility = 0          

        return GameState(to_move=player, utility=new_utility, board=new_board, moves=new_moves)

    # returns +1 if MAX wins, -1 if MIN wins 
    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'MAX' else -state.utility

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        cur_board = state.board
        for objects in cur_board:
            if objects == 0: 
                continue
            else: 
                return False
        return True

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move
    
    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance 
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    # print(nim.initial.board) # must be [0, 5, 3, 1] 
    # print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    # print(nim.result(nim.initial, (1,3) ))  
    # print(nim.actions(nim.initial))
    
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
