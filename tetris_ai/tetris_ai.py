import time, pygame, sys
import tetris_ai.tetris_base as game
from pygame.locals import *

counter = 0
generation = 0

def run_game(chromosome):
    global counter, generation, flag
    
    # Initialize Pygame
    pygame.init()

    # Set up the Pygame display
    size = [game.WINDOWWIDTH, game.WINDOWHEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tetris AI')

    # Initialize the game parameters
    game.FPS = int(100000000)
    game.main(isGame=False)
    max_score = 22000

    board = game.get_blank_board()
    last_fall_time = time.time()
    score = 0
    level, fall_freq = game.calc_level_and_fall_freq(score)
    falling_piece = game.get_new_piece()
    next_piece = game.get_new_piece()

    # Calculate best move
    chromosome.calc_best_move(board, falling_piece)

    num_used_pieces = 0
    removed_rows = [0, 0, 0, 0]  # Combos

    alive = True
    win = False

    flag = True

    # Game loop
    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game exited by user")
                pygame.quit()
                sys.exit()

        if falling_piece is None:
            # No falling piece in play, so start a new piece at the top
            falling_piece = next_piece
            next_piece = game.get_new_piece()

            # Decide the best move based on your weights
            chromosome.calc_best_move(board, falling_piece)

            # Update number of used pieces and the score
            num_used_pieces += 1
            score += 1

            # Reset last_fall_time
            last_fall_time = time.time()

            if not game.is_valid_position(board, falling_piece):
                # GAME-OVER: Can't fit a new piece on the board, so game over.
                alive = False
                counter += 1

        if time.time() - last_fall_time > fall_freq:
            if not game.is_valid_position(board, falling_piece, adj_Y=1):
                # Falling piece has landed, set it on the board
                game.add_to_board(board, falling_piece)

                # Bonus score for complete rows at once (40 pts for 1 row, 120 pts for 2 rows, 300 pts for 3 rows, 1200 pts for 4 rows)
                num_removed_rows = game.remove_complete_rows(board)
                if num_removed_rows == 1:
                    score += 40
                    removed_rows[0] += 1
                elif num_removed_rows == 2:
                    score += 120
                    removed_rows[1] += 1
                elif num_removed_rows == 3:
                    score += 300
                    removed_rows[2] += 1
                elif num_removed_rows == 4:
                    score += 1200
                    removed_rows[3] += 1

                falling_piece = None
            else:
                # Piece did not land, just move the piece down
                falling_piece['y'] += 1
                last_fall_time = time.time()

        # Stop condition
        if score > max_score:
            alive = False
            win = True
            counter += 1


        # Draw the game on the screen
        screen.fill(game.BGCOLOR)
        game.draw_board(board)
        game.draw_status(score, level, generation)
        game.draw_next_piece(next_piece)

        if falling_piece is not None:
            game.draw_piece(falling_piece)

        pygame.display.update()
        game.FPSCLOCK.tick(game.FPS)

        if counter == 40 and generation == 0:  
            generation += 1
            counter = 0
        elif counter == 20 and generation !=0: 
            generation += 1
            counter = 0

    # Save the game state
    game_state = [num_used_pieces, removed_rows, score, win]

    return game_state

