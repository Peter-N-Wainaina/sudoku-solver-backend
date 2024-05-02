"""
This  module contains poc code for a sudoku solver
"""

#NOTE:The contents of the file are lines of tuples (i,j,k) separated by a comma 
     #where i and j are valid indices on the board, with a valid value as k.


class Sudoku():
    def __init__(self,board):
        self.board = board 

    def get_possible_moves(self):
        # TODO document why this method is empty
        pass 


        







def print_board(board):
    """
    Prints a formatted  n by n board to terminal
    """
    n = len(board)
    b_str = ""
    for i in range(n):
        row = "|"
        for j in range(n):
            cell = board[i][j]
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

def create_board_from_file(fileName,board_size):
    contents = read_board(fileName)
    board = [[" " for _ in range(board_size)] for _ in range(board_size)]
    for line in contents:
        line = line.replace(",","").strip()
        i,j,k = int(line[0]),int(line[1]),line[2]
        board[i][j] = k
    return board

def solve_sudoku(board):
    """
    Input: An n by n sudoku board, possible unsolved
    Output: A valid solution to the sudoku
    """
    pass



board_file = "./test.txt"
init_board = create_board_from_file(board_file,4)
if __name__ == "__main__":
    print("Initial board\n")
    print_board(init_board)
