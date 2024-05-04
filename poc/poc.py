"""
This  module contains poc code for a sudoku solver
"""

import numpy as np
#NOTE:The contents of the file are lines of tuples (i,j,k) separated by a comma 
     #where i and j are valid indices on the board, with a valid value as k.


class Sudoku():
    def __init__(self,board):
        self.board = board 

    def get_possible_moves(self):
        # TODO document why this method is empty
        pass 



def is_solved(board): #NOTE:Assumes 9 by 9 board
    n = len(board)

    def check_rows(board):
        for row in board:
            row_contents = set()
            for cell in row:
                if cell in range(1, n + 1):
                    row_contents.add(int(cell))
            if len(row_contents) != n:
                return False
        return True 
    
    def check_boxes(board):
        box_size = 3  
        
        for start_row in range(0, n, box_size):
            for start_col in range(0, n, box_size):
                box_contents = set()
                
                for row in range(start_row, start_row + box_size):
                    for col in range(start_col, start_col + box_size):
                        cell = board[row][col]
                        if cell in range(1, n + 1):
                            box_contents.add(int(cell))

                if len(box_contents) != n:
                    print(box_contents)
                    return False
        return True

    return check_rows(board) and check_rows(np.array(board).T) #and  check_boxes(board)

def print_board(board):
    """
    Prints a formatted  n by n board to terminal
    """
    n = len(board)
    b_str = ""
    for i in range(n):
        row = "|"
        for j in range(n):
            cell = str(board[i][j])
            row +=  cell + " |"
        b_str += (row  + "\n")
        b_str += ("_"*len(row) + "\n")
    print(b_str)

def read_board(text_file):
    try: 
        with open(text_file) as file:
            contents = file.readlines()
            return contents
    except Exception as e:
        print(f"File Open Failed: {e}")

def create_board_from_file(file_name,board_size):
    contents = read_board(file_name)
    board = [[" " for _ in range(board_size)] for _ in range(board_size)]
    for line in contents:
        line = line.replace(",","").strip()
        i,j,k = int(line[0]),int(line[1]),line[2]
        board[i][j] = int(k)
    return board



def get_cell_moves(cell, board):
    #Assumes a 3 by 3 board

    #collect set of moves on its row, column, box. Get their union. Subtract this
    #from all possible moves eg 1..9 if 9 by 9

    #cell is a tuple (i, j) of the indices to this cell in the board
    all_moves = {1,2,3}
    row, col = cell

    invalid_moves = set()
    this_row = board[row]  
    this_col = (np.array(board).T)[col]
    for r_cell, c_cell in zip(this_row, this_col):
        if r_cell is not None:
            invalid_moves.add(r_cell)
        if c_cell is not None:
            invalid_moves.add(c_cell)

    return all_moves - invalid_moves

def get_board_moves(board):
    b_size = 3
    board_moves = []
    for i in range(b_size):
        for j in range(b_size):
            if board[i][j] is not None:
                cell_moves = get_cell_moves((i,j), board)
                if cell_moves == {}: #Meaning a non-none cell has no possible moves
                    return []  #TODO:Refactor to make another function responsible for this
                for move in cell_moves:
                    board_moves.append((i,j,move))
                
    return board_moves

def make_move(board,move):
    i,j = move[0], move[1]
    board[i][j] = move[2]

def undo_move(board,move):
    i,j = move[0], move[1]
    board[i][j] = None

def solve_sudoku(board):
    """
    Input: An n by n sudoku board, possible unsolved
    Output: A valid solution to the sudoku
    """
    if is_solved(board):
        return board
    
    moves = get_board_moves(board)
    print(moves)
    if moves == []:
        return None
    # print(moves)
    # print(board)
    for move in moves:
        print(board)
        make_move(board, move)
        print(board)
        new_board = solve_sudoku(board)
        if new_board is not None:
            return new_board
        else:
            undo_move(board, move)
    
    return None #should never get here


    



board_file = "./test.txt"
#init_board = create_board_from_file(board_file,9)

three_by_three = [[1, 2, 3],
                 [2, 3, None],
                 [3, 1, None]]
#board_moves = get_board_moves(three_by_three)

if __name__ == "__main__":
    # print("Initial board\n")
    # print_board(init_board)
    # print(is_solved(init_board))
    print("three by three")
    #print(three_by_three)


    print(solve_sudoku(three_by_three))
    print(get_board_moves(three_by_three))

    #print(three_by_three)

    # make_move(three_by_three, (1,0,2))
    # print(three_by_three)
    # undo_move(three_by_three, (1,0,2))
    # print(three_by_three)
    #(is_solved(three_solved))




#three_solved = [[1, 2, 3], 
#                 [2, 3, 1],
#                 [3, 1, 2]
#                 ]