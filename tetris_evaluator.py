from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from pygame.locals import *
import tetris_ai.tetris_ai as ai
from tetris_ai.chromosome import chromosome


class TetrisEvaluator(SimpleIndividualEvaluator):
    """Evaluator class for tetris game,
    responsible for defining a fitness evaluation method and evaluating it."""

    def __init__(self, ):
        super().__init__()

    def evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.

        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.

        Returns
        -------
        float
            The evaluated fitness value of the given individual.
        """
        fitness_value = 0
        individual_vector = individual.get_vector()
        print(individual_vector)
        chromo = chromosome(individual_vector)
        game_state = ai.run_game(chromo)
        fitness_value = game_state[2]

        return fitness_value


  