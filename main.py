import tetris_ai.tetris_base as game
import tetris_ai.tetris_ai as ai
import tetris_ai.analyser as analyser
import matplotlib.pyplot as plt
import argparse
import eckitty_main

def main():
    eckitty_main.eckity()

if __name__ == "__main__":
    # Define argparse options
    parser = argparse.ArgumentParser(description="Tetris AI")
    parser.add_argument('--ga',
                        action='store_true',
                        help='genetic algorithm')
    parser.add_argument('--game',
                        action='store_true',
                        help='base game without ga')

    args = parser.parse_args()

    if (args.ga):
        main()

    elif (args.game):
        # Just run the base game
        game.MANUAL_GAME = True
        game.main(isGame = True)