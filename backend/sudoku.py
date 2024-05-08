import numpy as np

class Sudoku(object):
    
    def __init__(self, board, box_dims):
        """
        board: n by n matrix of Ints or None 
        box_dims: (k, m), the dimensions of the boxes within the board eg 3 by 3
                  for a 9 by 9 board.
        Precondition: k and m must fully divide n 
        """

        if self.is_valid_board(board):
            self.board = board
            self.board_size = len(board)
            self.box_height, self.box_width = box_dims
            self.row_bags = [set()] * self.board_size
            self.col_bags = [set()] * self.board_size
            self.box_bags = [set()] * ((self.board_size / self.box_height) * (self.board_size / self.box_width)) #TODO: How to index into these boxes
        else:
            raise self.InvalidBoard
        
    class InvalidBoard(Exception):
        pass





    
    def is_valid_board(self, board, box_dims):
        """
        Returns True if board is a valid board, false otherwise.
        """
        n = len(board)
        box_row, box_col = box_dims

        def check_invalid_cell(cell, bag):
           return (type(cell) != int and cell is not None) or (cell not in range (1, n + 1)) or  (cell in bag)

        def check_rows(board):
            for row in board:
                r_bag = set()
                for cell in row:
                    if check_invalid_cell(cell,r_bag):
                        return False
                    r_bag.add(cell)
            return True
                    
        def check_boxes(board):
            for start_row in range(0, n, box_row):
                for start_col in range(0, n, box_col):
                    box_bag = set()
                    
                    for row in range(start_row, start_row + box_row):
                        for col in range(start_col, start_col + box_col):
                            cell = board[row][col]
                            if check_invalid_cell(cell,box_bag):
                                return False
                            box_bag.add(cell)
            return True
        return check_rows(board) and check_rows(np.array(board).T) and check_boxes(board)

        












        
