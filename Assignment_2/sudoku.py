from constraint import *

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.size = 9
    
    def solve_sudoku(self):
        sudoku = Problem()

        indices = [(row, col) for row in range(9) for col in range(9)]
        
