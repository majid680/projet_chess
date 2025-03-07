import numpy as np
import textwrap
from pieces import pieces_dict, is_check

from config import PIECE_IMAGES

class Board():
    def __init__(self, type : str ='classic'):
        if type == 'classic':
            self.scheme = textwrap.dedent("""\
            R N B Q K B N R 
            P P P P P P P P 
            . . . . . . . . 
            . . . . . . . . 
            . . . . . . . . 
            . . . . . . . . 
            p p p p p p p p 
            r n b q k b n r
            """
            )

        else:
            raise ValueError(f'Chess type {type} is not implemented')
        
        # Construct board with objects
        self.board = self.init_board()

        # Init variables
        self.turn = 'white'
        self.last_piece = None # Last piece that played

    def init_board(self):
        '''
        Function that generate the board based on self.scheme. Elements of the board are objects:
        - None objects when '.'
        - Chess pieces from the dict `pieces_dict`

        Lowercase letters stand for white pieces while uppercase stand for black pieces.
        '''
        # Init chess board using numpy array with strings
        board = np.empty((8,8), dtype=object)

        # TODO: Écrire votre code ici
                    
        return board

    def piece_at(self, coordinate : tuple):
        return self.board[coordinate] if self.board[coordinate] else None

    def switch_turn(self):
        '''
        Function that update self.turn
        '''
        # TODO: Écrire votre code ici et retirer pass
        pass
    
    def move_piece(self, start_pos, end_pos):
        '''
        Function that:
        - update self.board
        - update the piece that moved and remove any captured piece
        - update self.last_piece
        '''
        # TODO: Écrire votre code ici et retirer pass
        pass

    def push(self, start_pos, end_pos):
        # Move piece
        self.move_piece(start_pos, end_pos)

        # Check for promotion
        self.promotion()

        # Update scheme
        self.update_scheme()

        # Switch turn
        self.switch_turn()
    
    def update_scheme(self):
        board = [PIECE_IMAGES[f'{s.get_color()}_{s.get_name()}'] if not s is None else '.' for s in self.board.flat]
        self.scheme = " ".join([s  if not i%8==0 or i==0 else f'\n{s}' for i, s in enumerate(board)])

    def get_board(self):
        return self.board
    
    def get_last_piece(self):
        return self.last_piece
    
    def get_turn(self):
        return self.turn
    
    def is_mate(self):
        if is_check(self, self.get_turn()):
            return all([s.legal_moves(self) == [] for s in self.board.flat if not s is None and s.get_color() == self.get_turn()])
        return False

    def promotion(self):
        for i in [0, 7]:
            for j in range(8):
                if not self.board[i,j] is None:
                    if self.board[i,j].name == 'pawn':
                        prom = input('Choose your promotion (q:queen, r:rook, n:knight or b:bishop): ')
                        self.board[i,j] = pieces_dict[prom](start_pos=(i, j), color=self.board[i,j].color)
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.scheme


if __name__=='__main__':
    board = Board()
    print(board)
