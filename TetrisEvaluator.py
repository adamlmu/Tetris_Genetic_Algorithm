from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
import random, time, pygame, sys
from pygame.locals import *
import tetris_ai.tetris_base as game
import tetris_ai.tetris_ai as ai
import tetris_ai.ga as ga #TD take the chromosome class elsewhere

# TDL: figure out how to get from a vector to a score

class TetrisEvaluator(SimpleIndividualEvaluator):
    """Evaluator class for super mario game,
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
        chromo = ga.Chromosome(individual_vector)
        game_state = ai.run_game(chromo, 600, 20000, False)
        chromo.calc_fitness(game_state)
        fitness_value = chromo.score

        return fitness_value


  