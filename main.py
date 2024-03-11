import tetris_ai.tetris_base as game
import argparse
import eckity_main
from tetris_plot import Information

def main(population_size, num_generations):
    eckity_main.eckity(population_size, num_generations)

if __name__ == "__main__":
    # Define argparse options
    parser = argparse.ArgumentParser(description="Tetris AI")
    parser.add_argument('--ga',
                        nargs='*',
                        metavar=('population_size', 'num_generations'),
                        type=int,
                        help='genetic algorithm (optional: provide population size and number of generations)')
    parser.add_argument('--game',
                        action='store_true',
                        help='base game without ga')

    args = parser.parse_args()

    if args.ga is not None and len(args.ga) >= 0:
        if len(args.ga) == 2:
            population_size, num_generations = args.ga
        else:
            # Use default values
            population_size, num_generations = 20, 15
        main(population_size, num_generations)
        # plot graph and print stats
        info = Information()
        info.read_file()
        print(f"Best Fitness calculated: {info.best_fitness}")
        info.plot_graph()

    elif args.game:
        # Just run the base game
        game.MANUAL_GAME = True
        game.main(isGame=True)