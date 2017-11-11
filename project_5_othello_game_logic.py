# Shanaya Ukuwela. ID: 56649043.

import collections

NONE = 0
BLACK = 'B' 
WHITE = 'W'

class Othello:
    def __init__(self, rows, columns, first_play, center_disc, justifier):
        self._rows = rows
        self._columns = columns
        self._center_disc = center_disc
        self._total_black_discs = 0
        self._total_white_discs = 0
        self._justifier = justifier
        self._turn = first_play
        self._board = []
        self.all_pieces_to_flip = []
        self._available_spaces = []

    def get_rows(self):
        return self._rows

    def get_columns(self):
        return self._columns

    def start_game_board(self):

        for row in range(self._rows):
            self._board.append([])
            for column in range(self._columns):
                self._board[-1].append(NONE)

        if self._center_disc == 'B':
            self._board[round(self._rows/2)-1][round(self._columns/2)-1] = BLACK
            self._board[round(self._rows/2)][round(self._columns/2)] = BLACK
            self._board[round(self._rows/2)-1][round(self._columns/2)] = WHITE
            self._board[round(self._rows/2)][round((self._columns)/2)-1] = WHITE
        elif self._center_disc == 'W':
            self._board[round(self._rows/2)-1][round(self._columns/2)-1] = WHITE
            self._board[round(self._rows/2)][round(self._columns/2)] = WHITE
            self._board[round(self._rows/2)-1][round(self._columns/2)] = BLACK
            self._board[round(self._rows/2)][round((self._columns)/2)-1] = BLACK

    def print_board(self):    
        for row in range(self._rows):
            row_str = ''
            for column in range(self._columns):
                if self._board[row][column]==0:
                    pixel=". "
                    row_str += pixel
                elif self._board[row][column]=="B":
                    black = 'B '
                    row_str += black
                else:
                    white = 'W '
                    row_str += white
            print(row_str[:-1])

    def track_discs(self):
        """Prints total disc count for each color"""
        self._total_black_discs = 0
        self._total_white_discs = 0
        for column in self._board:
            for disc in column:
                if disc == BLACK:
                    self._total_black_discs += 1
                elif disc == WHITE:
                    self._total_white_discs += 1
        return ('B: {}  W: {}'.format(self._total_black_discs, self._total_white_discs))
            
    def switch_turns(self):
        """Switches to opposite player's turn"""
        if self._turn == BLACK:
            self._turn = WHITE
        else:
            self._turn = BLACK
        
    def display_turn(self):
        """Displays who's turn it is to play"""
        if self._turn == BLACK:
            return("TURN: B")
        else:
            return("TURN: W")

    def opposite_turn(self):
        """Returns opposite player's turn"""
        if self._turn == BLACK:
            return WHITE
        else:
            return BLACK

    def _place_disc(self, row, column, disc):
        self._board[row][column] = disc

    def check_all_directions(self, row, column):
        """
        checks various directions where pieces can be flipped if the user
        input is valid
        """
        N = [-1,0]
        E = [0,1]
        S = [1,0]
        W = [0,-1]
        NE = [-1,1]
        NW = [-1,-1]
        SE = [1, 1]
        SW = [1,-1]
        row -= 1
        column -= 1
        changing_row = 0
        changing_col = 0
        cont_change_row = 0
        cont_change_col = 0
        directions = [N,E,S,W,NE,NW,SW,SE]
        if self._available_space(row, column) == True:#checks to see if move can be made in the first place
            for x,y in directions:
                try:
                    changing_row = row
                    changing_col = column
                    changing_row += x
                    changing_col += y
                    if self.is_move_on_board(changing_row+1,changing_col+1) == True:
                        if self._board[changing_row][changing_col] == self.opposite_turn():
                            self._search_direction([x,y],changing_row, changing_col, row, column)
                    else:
                        continue
                except IndexError:
                    continue
        else:
            return

    def _search_direction(self, direction, current_row, current_col, row, column)-> list:
        """
        takes the opponent's color, direction of search, and last spot and returns a list of
        locations of pieces to flip
        """
        pieces_to_flip = []
        
        while True:
            try:
                if self.is_move_on_board(current_row+1,current_col+1):
                    if self._get_color(current_row, current_col) == self.opposite_turn():
                        pieces_to_flip.append((row,column))
                        pieces_to_flip.append((current_row, current_col))
                        current_row += direction[0]
                        current_col += direction[1]
                    elif self._get_color(current_row, current_col) == self._turn:
                        self.all_pieces_to_flip.append(pieces_to_flip)
                        break
                    elif self._get_color(current_row, current_col) == NONE:
                        return []
                    else:
                        return []
                else:
                    return pieces_to_flip
            except IndexError:
                pieces_to_flip = []
                return pieces_to_flip
   

    def reset_all_pieces_to_flip(self):
        """resets all_pieces_to_flip list to an empty list to use for each move"""
        self.all_pieces_to_flip = []

    def get_all_pieces_to_flip(self) -> list:
        """Appends all moves that can be flipped in each direction into a
    list"""
        return self.all_pieces_to_flip

    def get_board(self):
        return self._board
    
    def flip_pieces(self)->None:
        "takes a list of locations of pieces to flip and flips them"
        for row in self.all_pieces_to_flip:
            for disc_space in row:
                self._place_disc(disc_space[0], disc_space[1], self._turn)
               

    def is_valid_move(self) -> str:
        """checks list of pieces to flip to see if they are valid moves"""
        if all(len(row) == 0 for row in self.all_pieces_to_flip):
            return False
        else:
            return True

    def _get_color(self, row, col)->str:
        "takes a row and col and returns str representing color of piece there"
        return self._board[row][col]

    def who_wins(self):
        """Prints who wins the game"""
        if self._justifier == '<':
            if self._total_black_discs < self._total_white_discs:
                return("WINNER: B")
            elif self._total_white_discs < self._total_black_discs:
                return("WINNER: W")
            else:
                return('WINNER: NONE')
        elif self._justifier == '>':
            if self._total_black_discs > self._total_white_discs:
                return("WINNER: B")
            elif self._total_white_discs > self._total_black_discs:
                return("WINNER: W")
            else:
                return('WINNER: NONE')

    def any_spaces(self):
        """Checks to see if any more moves can be made"""

        self.all_pieces_to_flip = []
        
        for row in enumerate(self._board):
            for space in row:
                if type(space) == list:
                    for element in enumerate(space):
                        self.check_all_directions((row[0]+1), (element[0]+1))

        if self.is_valid_move() == True:
            return True
        else:
            return False
    
    def is_move_on_board(self, row, column) -> bool:
        """Checks to see if player inputted move outside of board boundaries"""
        if (row-1) < 0:
            return False
        elif (row-1) > self._rows:
            return False
        elif (column-1) < 0:
            return False
        elif(column-1) > self._columns:
            return False
        else:
            return True

    def _available_space(self, row, column) -> bool:
        """Returns True or False depending on if a disc exists at row, column or not"""
        if self._board[row][column] == WHITE or self._board[row][column] == BLACK:
            return False
        else:
            return True


                
        
    
