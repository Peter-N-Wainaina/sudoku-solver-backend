import numpy as np
from math import floor

class Sudoku(object):
    
    def __init__(self, board, box_dims):
        """
        board: n by n matrix of Ints or None 
        box_dims: (k, m), the dimensions of the boxes within the board eg 3 by 3
                  for a 9 by 9 board.
        Precondition: k and m must fully divide n 
        """
        self.print_board(board)

        if self._is_valid_board(board, box_dims): #TODO:Maybe change to a try block 
            self.board = board
            self.size = len(board)
            self.box_height, self.box_width = box_dims
            self.row_bags = [set()] * self.size
            self.col_bags = [set()] * self.size
            self.box_bags = [set()] * ((self.size / self.box_height) *
                                        (self.size / self.box_width)) #TODO: How to index into these boxes
            self._fill_bags()
        else:
            raise self.InvalidBoard
        
    class InvalidBoard(Exception):
        pass

    def _get_box(self, cell):
        r, c = cell
        boxes_across = self.size / self.box_width
        return ((floor(r / self.size)) * boxes_across) + floor(c / self.size)

    def _fill_bags(self):
        #fill rows:
        for row in range(self.size):
            for col in range(self.size):
                cell = self.board[row][col]
                if cell is not None: 
                    self.row_bags[row].add(cell)
                    self.col_bags[col].add(cell)
                    self.box_bags[self._get_box((row, col))].add(cell)

    def possible_moves(self):
        """
        Returns a list of triples (i, j, k). (i,j) is the position in board where
        k is a valid move.
        """
        valid_moves = {x for x in range(1, self.size + 1)}
        pos_moves = []
        for row in range(self.size):
            for col in range(self.size):
                box = self._get_box((row, col))
                r_bag = self.row_bags[row] 
                c_bag = self.col_bags[col]
                b_bag = self.box_bags[box]
                cell_moves = valid_moves - (r_bag | c_bag | b_bag)
                for move in cell_moves:
                    pos_moves.append((row, col, move))
        return pos_moves

    def _is_valid_board(self, board, box_dims):
        """
        Returns True if board is a valid board, false otherwise.
        """
        n = len(board)
        box_row, box_col = box_dims

        def check_invalid_cell(cell, bag):
           return (type(cell) != int and cell is not None) or (cell not in range (1, n + 1)) or  (cell in bag) #TODO:Fix this!!! 

        def check_rows(board):
            for row in board:
                r_bag = set()
                for cell in row:
                    if check_invalid_cell(cell,r_bag):
                        print("This is the issue: ",cell)
                        return False
                    r_bag.add(cell)
            print("Row: This is True")
            return True
                    
        def check_boxes(board):
            for start_row in range(0, n, box_row):
                for start_col in range(0, n, box_col):
                    box_bag = set()
                    
                    for row in range(start_row, start_row + box_row):
                        for col in range(start_col, start_col + box_col):
                            cell = board[row][col]
                            if check_invalid_cell(cell,box_bag):
                                print("Box: This is False")
                                return False
                            box_bag.add(cell)
            print("Box: This is true")
            return True
        return check_rows(board) and check_rows(np.array(board).T) and check_boxes(board)

    def print_board(self, board):
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
            












        