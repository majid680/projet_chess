from copy import deepcopy 
import itertools

# Define parent class called Piece
class Piece():
    def __init__(self, start_pos, color):
        self.pos = start_pos
        self.color = color
        self.move_count = 0
        self.name = None
    
    def get_pos(self):
        return self.pos
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_move_count(self):
        return self.move_count
    
    def set_new_pos(self, pos):
        self.pos = pos
        self.move_count+=1
    
    def get_moves(self):
        # Define dummy
        moves = []
        return moves
    
    def legal_moves(self, board):
        '''
        Method that returns all possible moves of a piece, NOT ignoring checks. These move are called legal moves.
        Legal_moves correspond to the coordinates of the different squares the piece can reach legally.
        '''
        board_init = deepcopy(board) # Generate a copy of the board for tests
        moves = self.get_moves(board)
        legal_moves = []

        # TODO: Écrire votre code ici

        return legal_moves
    

# Define individual chess pieces
class Pawn(Piece):
    def __init__(self, start_pos, color):
        super().__init__(start_pos, color)
        self.name = 'pawn'
    
    def get_moves(self, board):
        '''
        Method that returns all available moves of a piece, ignoring checks. Moves correspond to the coordinates of
        the different squares the piece can reach.
        '''
        board_arr = board.get_board()
        moves = [] # List of the possible movements

        # Add standard moves
        if self.get_color() == 'white':
            move = sum_coordinates(self.get_pos(), (-1, 0))
            if move[0] >= 0:
                if board_arr[move] is None:
                    moves.append(move) # One step
                    move = sum_coordinates(self.get_pos(), (-2, 0)) # two steps
                    if self.get_move_count() == 0 and board_arr[move] is None:
                        moves.append(move)
        else:
            move = sum_coordinates(self.get_pos(), (1, 0))
            if move[0] <= 7:
                if board_arr[move] is None:
                    moves.append(move)
                    move = sum_coordinates(self.get_pos(), (2, 0)) # two steps
                    if self.get_move_count() == 0 and board_arr[move] is None:
                        moves.append(move)
        
        # Add capture move
        if self.get_color() == 'white':
            move = sum_coordinates(self.get_pos(), (-1, 1))
            if move[0] >= 0 and move[1] <=7:
                if not board_arr[move] is None:
                    if  board_arr[move].get_color() == 'black':
                        moves.append(move) # Capture right
            move = sum_coordinates(self.get_pos(), (-1, -1))
            if move[0] >= 0 and move[1] >=0:
                if not board_arr[move] is None:
                    if board_arr[move].get_color() == 'black':
                        moves.append(move) # Capture left
        else:
            move = sum_coordinates(self.get_pos(), (1, 1))
            if move[0] <= 7 and move[1] <=7:
                if  not board_arr[move] is None:
                    if  board_arr[move].get_color() == 'white':
                        moves.append(move) # Capture right
            move = sum_coordinates(self.get_pos(), (1, -1))
            if move[0] <= 7 and move[1] >=0:
                if not board_arr[move] is None:
                    if board_arr[move].get_color() == 'white':
                        moves.append(move) # Capture left
        return moves


class Knight(Piece):
    def __init__(self, start_pos, color):
        super().__init__(start_pos, color)
        self.name = 'knight'

    def get_moves(self, board):
        '''
        Method that returns all available moves of a piece, ignoring checks. Moves correspond to the coordinates of
        the different squares the piece can reach.
        '''
        moves = [] # List of the possible movements
        board_arr = board.get_board()
        
        # TODO: Écrire votre code ici

        return moves


class Rook(Piece):
    def __init__(self, start_pos, color):
        super().__init__(start_pos, color)
        self.name = 'rook'

    def get_moves(self, board):
        '''
        Method that returns all available moves of a piece, ignoring checks. Moves correspond to the coordinates of
        the different squares the piece can reach.
        '''
        moves = [] # List of the possible movements
        board_arr = board.get_board()
        
        # TODO: Écrire votre code ici
        
        return moves


class Bishop(Piece):
    def __init__(self, start_pos, color):
        super().__init__(start_pos, color)
        self.name = 'bishop'

    def get_moves(self, board):
        '''
        Method that returns all available moves of a piece, ignoring checks. Moves correspond to the coordinates of
        the different squares the piece can reach.
        '''
        moves = [] # List of the possible movements
        board_arr = board.get_board()

        # TODO: Écrire votre code ici

        return moves


class Queen(Piece):
    def __init__(self, start_pos, color):
        super().__init__(start_pos, color)
        self.name = 'queen'

    def get_moves(self, board):
        '''
        Method that returns all available moves of a piece, ignoring checks. Moves correspond to the coordinates of
        the different squares the piece can reach.
        '''
        moves = [] # List of the possible movements
        board_arr = board.get_board()

        # TODO: Écrire votre code ici

        return moves


class King(Piece):
    def __init__(self, start_pos, color):
        super().__init__(start_pos, color)
        self.name = 'king'

    def get_moves(self, board):
        '''
        Method that returns all available moves of a piece, ignoring checks. Moves correspond to the coordinates of
        the different squares the piece can reach.
        '''
        moves = [] # List of the possible movements
        board_arr = board.get_board()

        # TODO: Écrire votre code ici

        return moves


# Utils functions
def is_check(board, color):
    '''
    This function evaluate if a given position contains a check for a given color. It returns True if there is
    a check or False if not
    '''
    board_arr = board.get_board()

    # TODO: Écrire votre code ici

    return False


def sum_coordinates(a,b):
    return tuple(map(sum, zip(a, b)))


pieces_dict = {
            'p':Pawn,
            'r':Rook,
            'n':Knight,
            'b':Bishop,
            'q':Queen,
            'k':King,
        }

