from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.float_vector_creator import GAFloatVectorCreator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import FloatVectorUniformNPointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from time import process_time
from tetris_evaluator import TetrisEvaluator

def eckity_algo():
    start_time = process_time()
    output_file = open("output.txt", "w")

    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(creators=GAFloatVectorCreator(length=7, gene_creator=None, bounds=(-1.0, 1.0), events=None),
                      population_size=20,
                      # user-defined fitness evaluation method
                      evaluator=TetrisEvaluator(),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=True,
                      elitism_rate=0.0,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          VectorKPointsCrossover(probability=0.5, k=2),
                          FloatVectorUniformNPointMutation(n=3, probability=0.05, events=None)
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=True), 1)
                      ]),
        breeder=SimpleBreeder(),
        # executor='thread',
        max_workers=1,
        max_generation=15,
        statistics=BestAverageWorstStatistics()
    )

    # evolve the generated initial population
    algo.evolve()
    # Execute (show) the best solution
    print(algo.execute())
    output_file.close()

    print(f"Total time: {process_time() - start_time}")


