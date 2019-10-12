from constraint import *

digits = range(1, 10)

row_digits = '123456789'
col_digits = row_digits

# Each element in the board has own identifier, using row and cols
element = [row + col for row in row_digits for col in col_digits]

# List of rows
rows = [[row + col for col in col_digits] for row in row_digits]

# List of columns
cols = [[row + col for row in row_digits] for col in col_digits]

# List of squares
squares = [['11', '12', '13', '21', '22', '23', '31', '32', '33'],
['14', '15', '16', '24', '25', '26', '34', '35', '36'],
['17', '18', '19', '27', '28', '29', '37', '38', '39'],

['41', '42', '43', '51', '52', '53', '61', '62', '63'],
['44', '45', '46', '54', '55', '56', '64', '65', '66'],
['47', '48', '49', '57', '58', '59', '67', '68', '69'],

['71', '72', '73', '81', '82', '83', '91', '92', '93'],
['74', '75', '76', '84', '85', '86', '94', '95', '96'],
['77', '78', '79', '87', '88', '89', '97', '98', '99']
]


# We need to check all three
group = [rows, cols, squares]

def solve_sudoku(board):
    sudoku = Problem()

    for i in range(0, 81):
        el = element[i]
        value = board[i]

        if value not in digits:
            sudoku.addVariable(el, digits)
        else:
            sudoku.addVariable(el, [value])
    
    for x in group:
        for y in x:
            sudoku.addConstraint(AllDifferentConstraint(), y)
   

    return len(sudoku.getSolutions())



def main():
    sudoku1 = [
        0, 0, 4, 0, 3, 0, 0, 1, 0,
        9, 0, 0, 5, 0, 0, 2, 4, 6,
        0, 0, 0, 4, 0, 0, 0, 0, 0,

        0, 0, 5, 3, 0, 0, 0, 0, 0,
        0, 8, 0, 0, 7, 0, 0, 2, 0,
        0, 0, 0, 0, 0, 4, 3, 0, 0,

        0, 0, 0, 0, 0, 7, 0, 0, 0,
        5, 3, 7, 0, 0, 6, 0, 0, 9,
        0, 6, 0, 0, 4, 0, 5, 0, 0
    ]


    sudoku2 = [
        0, 0, 4, 0, 3, 0, 0, 1, 0,
        9, 0, 0, 5, 0, 0, 2, 4, 6,
        0, 0, 0, 4, 0, 0, 0, 0, 0,

        0, 0, 5, 3, 0, 0, 0, 0, 0,
        0, 8, 0, 0, 7, 0, 0, 2, 0,
        0, 0, 0, 0, 0, 4, 1, 0, 0,
        
        0, 0, 0, 0, 0, 7, 0, 0, 0,
        5, 3, 7, 0, 0, 6, 0, 0, 9,
        0, 6, 0, 0, 4, 0, 5, 0, 0
    ]


    sudoku3 = [
        0, 0, 4, 0, 3, 0, 0, 1, 0,
        9, 0, 0, 5, 0, 0, 2, 4, 6,
        0, 0, 0, 4, 0, 0, 0, 0, 0,

        0, 0, 5, 3, 0, 0, 0, 0, 0,
        0, 8, 0, 0, 7, 0, 0, 2, 0,
        0, 0, 0, 0, 0, 4, 7, 0, 0,
        
        0, 0, 0, 0, 0, 7, 0, 0, 0,
        5, 3, 7, 0, 0, 6, 0, 0, 9,
        0, 6, 0, 0, 4, 0, 5, 0, 0
    ]


    sudoku4 = [
        0, 0, 4, 0, 3, 0, 0, 1, 0,
        9, 0, 0, 5, 0, 0, 2, 4, 6,
        0, 0, 0, 4, 0, 0, 0, 0, 0,

        0, 0, 5, 3, 0, 0, 0, 0, 0,
        0, 8, 0, 0, 7, 0, 0, 2, 0,
        0, 0, 0, 0, 0, 4, 6, 0, 0,
        
        0, 0, 0, 0, 0, 7, 0, 0, 0,
        5, 3, 7, 0, 0, 6, 0, 0, 9,
        0, 6, 0, 0, 4, 0, 5, 0, 0
    ]

    sudoku5 = [
        0, 0, 4, 0, 3, 0, 0, 1, 0,
        9, 0, 0, 5, 0, 0, 2, 4, 6,
        0, 0, 0, 4, 0, 0, 0, 0, 0,

        0, 0, 5, 3, 0, 0, 0, 0, 0,
        0, 8, 0, 0, 7, 0, 0, 2, 0,
        0, 0, 0, 0, 0, 4, 8, 0, 0,
        
        0, 0, 0, 0, 0, 7, 0, 0, 0,
        5, 3, 7, 0, 0, 6, 0, 0, 9,
        0, 6, 0, 0, 4, 0, 5, 0, 0
    ]

    sudoku6 = [
        0, 0, 4, 0, 3, 0, 0, 1, 0,
        9, 0, 0, 5, 0, 0, 2, 4, 6,
        0, 0, 0, 4, 0, 0, 0, 0, 0,

        0, 0, 5, 3, 0, 0, 0, 0, 0,
        0, 8, 0, 0, 7, 0, 0, 2, 0,
        0, 0, 0, 0, 0, 4, 9, 0, 0,
        
        0, 0, 0, 0, 0, 7, 0, 0, 0,
        5, 3, 7, 0, 0, 6, 0, 0, 9,
        0, 6, 0, 0, 4, 0, 5, 0, 0
    ]

    print(solve_sudoku(sudoku1))
    print(solve_sudoku(sudoku2))
    print(solve_sudoku(sudoku3))
    print(solve_sudoku(sudoku4))
    print(solve_sudoku(sudoku5))
    print(solve_sudoku(sudoku6))
    


if __name__ == "__main__":
    main()










