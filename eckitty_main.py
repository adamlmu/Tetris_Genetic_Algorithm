# from eckity.algorithms.simple_evolution import SimpleEvolution
# from eckity.breeders.simple_breeder import SimpleBreeder
# from eckity.creators.ga_creators.float_vector_creator import GAFloatVectorCreator
# from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
# from eckity.genetic_operators.mutations.vector_n_point_mutation import VectorNPointMutation
# from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
# from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
# from eckity.subpopulation import Subpopulation
# from time import process_time
# from TetrisEvaluator import TetrisEvaluator

# def main():
#     start_time = process_time()

#     # Initialize the evolutionary algorithm
#     algo = SimpleEvolution(
#         Subpopulation(creators=GAFloatVectorCreator(length=7, gene_creator=None, bounds=(-1.0, 1.0), events=None),
#                       population_size=50,
#                       # user-defined fitness evaluation method
#                       evaluator=TetrisEvaluator(),
#                       # maximization problem (fitness is sum of values), so higher fitness is better
#                       higher_is_better=True,
#                       elitism_rate=0.0,
#                       # genetic operators sequence to be applied in each generation
#                       operators_sequence=[
#                           VectorKPointsCrossover(probability=0.5, k=2),
#                           VectorNPointMutation(n=2, probability=0.05, arity=1, events=None)
#                       ],
#                       selection_methods=[
#                           # (selection method, selection probability) tuple
#                           (TournamentSelection(tournament_size=4, higher_is_better=True), 1)
#                       ]),
#         breeder=SimpleBreeder(),
#         # executor='thread',
#         max_workers=1,
#         max_generation=20,
#         statistics=BestAverageWorstStatistics()
#     )

#     # evolve the generated initial population
#     algo.evolve()
#     # Execute (show) the best solution
#     print(algo.execute())

#     print(f"Total time: {process_time() - start_time}")


# if __name__ == '__main__':
#     main()

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.float_vector_creator import GAFloatVectorCreator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_n_point_mutation import VectorNPointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from time import process_time
from TetrisEvaluator import TetrisEvaluator
import pygame
from multiprocessing import Process

def pygame_main():
    pygame.init()
    # Your Pygame-related code here

def main():
    start_time = process_time()

    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(creators=GAFloatVectorCreator(length=7, gene_creator=None, bounds=(-1.0, 1.0), events=None),
                      population_size=50,
                      # user-defined fitness evaluation method
                      evaluator=TetrisEvaluator(),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=True,
                      elitism_rate=0.0,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          VectorKPointsCrossover(probability=0.5, k=2),
                          VectorNPointMutation(n=2, probability=0.05, arity=1, events=None)
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=True), 1)
                      ]),
        breeder=SimpleBreeder(),
        # executor='thread',
        max_workers=1,
        max_generation=20,
        statistics=BestAverageWorstStatistics()
    )

    # Create a Process targeting the pygame_main function
    pygame_process = Process(target=pygame_main)

    # Start the process
    pygame_process.start()

    # evolve the generated initial population
    algo.evolve()
    # Execute (show) the best solution
    print(algo.execute())

    # Wait for the Pygame process to finish
    pygame_process.join()

    print(f"Total time: {process_time() - start_time}")

if __name__ == '__main__':
    main()
