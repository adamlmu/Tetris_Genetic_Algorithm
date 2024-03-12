import tetris_ai.tetris_base as game

class chromosome():
    def __init__(self, weights):
        self.weights = weights
        self.score   = 0

    def calc_best_move(self, board, piece):
        """Calculate best movement
        Select the best move based on the chromosome weights.

        """
        best_X     = 0          # Best position in X
        best_R     = 0          # Best rotation
        best_Y     = 0          # Best position in Y
        best_score = -100000    # Best score

        # Calculate the total the holes and blocks above holes before play
        num_holes_bef, num_blocking_blocks_bef = game.calc_initial_move_info(board)
        for r in range(len(game.PIECES[piece['shape']])):
            # Iterate through every possible rotation
            for x in range(-2,game.BOARDWIDTH-2):
                #Iterate through every possible position
                movement_info = game.calc_move_info(board, piece, x, r, \
                                                    num_holes_bef, \
                                                    num_blocking_blocks_bef)
 
                # Check if it's a valid movement
                if (movement_info[0]):
                    # Calculate movement score
                    movement_score = 0
                    for i in range(1, len(movement_info)):
                        movement_score += self.weights[i-1]*movement_info[i]

                    # Update best movement
                    if (movement_score > best_score):
                        best_score = movement_score
                        best_X = x
                        best_R = r
                        best_Y = piece['y']

        piece['y'] = -2
        piece['x'] = best_X
        piece['rotation'] = best_R

        return best_X, best_R
