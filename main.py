import pygame

import config
from board import Board

# Initialize Pygame
pygame.init()

PYGAME_DICT = {}

for piece in config.PIECE_IMAGES.keys():
    PYGAME_DICT[piece] = pygame.image.load(f"images/{piece}.png")
    PYGAME_DICT[piece] = pygame.transform.scale(PYGAME_DICT[piece], (config.SQUARE_SIZE, config.SQUARE_SIZE))

def draw_board(screen):
    for row in range(config.BOARD_SIZE):
        for col in range(config.BOARD_SIZE):
            color = config.WHITE if (row + col) % 2 == 0 else config.GRAY
            pygame.draw.rect(screen, color, (col * config.SQUARE_SIZE, row * config.SQUARE_SIZE, config.SQUARE_SIZE, config.SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(config.BOARD_SIZE):
        for col in range(config.BOARD_SIZE):
            piece = board.piece_at((row, col))
            if not piece is None:
                screen.blit(PYGAME_DICT[f'{piece.get_color()}_{piece.get_name()}'], (col * config.SQUARE_SIZE, row * config.SQUARE_SIZE))

def draw_legal_moves(screen, legal_moves):
    for move in legal_moves:
        move_row = move[0]
        move_col = move[1]
        pygame.draw.circle(screen, config.HIGHLIGHT, (move_col * config.SQUARE_SIZE + config.SQUARE_SIZE // 2, move_row * config.SQUARE_SIZE + config.SQUARE_SIZE // 2), 10)

def get_square_from_mouse(pos):
    col, row = pos[0] // config.SQUARE_SIZE, pos[1] // config.SQUARE_SIZE
    return (row, col)

def win(winner_message, screen):
    """
    Affichage d'un message lorsqu'il y a un gagnant
    """
    screen.fill((0, 0, 0))

    # Afficher le message du gagnant 
    draw_text(winner_message, config.WIDTH // 2, config.HEIGHT // 3, (255, 255, 255), 48, screen)
    draw_text("'R' TO RESTART", config.WIDTH // 2, config.HEIGHT // 2, (255, 255, 255), 36, screen)

    # Mise à jour de l'affichage
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Réinitialisation du jeu
                    pygame.quit()
                    exit()

def draw_text(text, x, y, color, size, screen):
    """
    Cette fonction permet d'écrire du texte sur la fenêtre du jeu, à des positions spécifiques.
    """
    font = pygame.font.SysFont("Consolas", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    # Pygame screen
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("Chess")

    # Initialize board
    board = Board()

    # Init variables
    selected_piece = None
    legal_moves = []
    running = True

    # Start game
    while running:
        screen.fill((0, 0, 0))
        draw_board(screen)
        draw_pieces(screen, board)
        draw_legal_moves(screen, legal_moves)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square_from_mouse(event.pos)
                piece = board.piece_at(square)
                
                if selected_piece is None:
                    if piece and piece.get_color() == board.get_turn():
                        selected_piece = piece
                        legal_moves = piece.legal_moves(board)
                else:
                    move = square
                    if move in selected_piece.legal_moves(board):
                        board.push(selected_piece.get_pos(), move)
                    if board.is_mate():
                        message = 'BLACK WINS !' if board.get_turn() != 'black' else 'WHITE WINS !'
                        win(message, screen)
                    else:
                        selected_piece = None
                        legal_moves = []

    pygame.quit()

if __name__=='__main__':
    main()