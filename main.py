import tetris_ai.tetris_base as game
import argparse
import eckity_main
from tetris_plot import Information

def main():
    eckity_main.eckity_algo()

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
        # plot graph and print stats
        info = Information()
        info.read_file()
        print(f"Best Fitness calculated: {info.best_fitness}")
        info.plot_graph()

    elif (args.game):
        # Just run the base game
        game.MANUAL_GAME = True
        game.main(isGame = True)