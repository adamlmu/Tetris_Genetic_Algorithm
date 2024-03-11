import matplotlib.pyplot as plt

class Information:
    """class for graph ploting"""

    def __init__(self):
        self.all_best_fitness = []
        self.all_worst_fitness = []
        self.all_average_fitness = []
        self.num_of_gen = []
        self.best_fitness = 0

    def read_file(self):
        with open("output.txt", "r") as my_file:
            lines = my_file.readlines()
            print(*lines)
            j = 0
            for i in range(2, len(lines), 6):
                best_fitness = float(lines[i][13:].strip())
                self.best_fitness = best_fitness if best_fitness > self.best_fitness else self.best_fitness
                self.all_best_fitness.append(best_fitness)
                worst_fitness = float(lines[i + 1][14:].strip())
                self.all_worst_fitness.append(worst_fitness)
                average_fitness = float(lines[i + 2][16:].strip())
                self.all_average_fitness.append(average_fitness)
                self.num_of_gen.append(j)
                j += 1

    def plot_graph(self):
        # x axis values
        x = self.num_of_gen
        # corresponding y axis values
        y1 = self.all_best_fitness
        y2 = self.all_worst_fitness
        y3 = self.all_average_fitness

        # plotting the points
        plt.plot(x, y1, color='blue', label="Best Fitness")
        plt.plot(x, y2, color='red', label="Worst Fitness")
        plt.plot(x, y3, color='green', label="Average Fitness")

        # naming the x axis
        plt.xlabel('Number of generations')
        # naming the y axis
        plt.ylabel('Fitness values')

        # giving a title to my graph
        plt.title('Fitness/Generations')

        # show a legend on the plot
        plt.legend()

        # Save the plot automatically
        plt.savefig('fitness_generations_plot.png')

        # function to show the plot
        plt.show()