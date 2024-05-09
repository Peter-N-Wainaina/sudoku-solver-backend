import sys
sys.path.append('/Users/peter/personal-workspace/personalProjects/sudokuSolver/backend') #TODO: How to make it so that it runs on different machines
from src import sudoku


def read_board(text_file):
    try: 
        with open(text_file) as file:
            contents = file.readlines()
            return contents
    except Exception as e:
        print(f"File Open Failed: {e}")

def create_board_from_file(file_name,board_size):
    contents = read_board(file_name)
    board = [[None for _ in range(board_size)] for _ in range(board_size)]
    for line in contents:
        line = line.replace(",","").strip()
        i,j,k = int(line[0]),int(line[1]),int(line[2])
        board[i][j] = k
    return board


valid_board_1 = create_board_from_file("data/valid_board_1.txt", 9)
valid_board_1 = sudoku.Sudoku(valid_board_1, (3,3))