import random

from domain.Individ import Individ


class Population:
    def __init__(self, size, problem, mutation_probability):
        self.generation = 0
        self.size = size
        self.problem = problem
        self.individs = [Individ.get_random_individ(problem) for i in range(size)]
        self.fitness_sum = self.calc_fitness_sum()
        self.mutation_probability = mutation_probability
        # self.print_population()
        self.stats = [min(x.fitness for x in self.individs)]

    def calc_fitness_sum(self):
        sum = 0
        for i in self.individs:
            sum += i.fitness
        self.fitness_sum = sum
        return sum

    def natural_selection_v2(self):
        self.individs.sort(key=lambda x: x.fitness, reverse=False)
        self.individs = self.individs[:int(len(self.individs)/2)]

    def natural_selection(self):
        new_gen = []
        for i in self.individs:
            if random.uniform(0, 1) < (self.fitness_sum - i.fitness)/self.fitness_sum:
                new_gen.append(i)
        if len(new_gen) < 2:
            self.natural_selection()
        else:
            self.individs = new_gen

    def funky_func(self):
        while len(self.individs) < self.size:
            self.individs.append(Individ.crossover(random.choice(self.individs), random.choice(self.individs)))

    def mutate(self):
        for i in self.individs:
            i.mutate(self.mutation_probability)

    def get_next_gen(self):
        self.natural_selection_v2()
        self.funky_func()
        self.mutate()
        self.calc_fitness_sum()
        self.generation += 1
        self.stats.append(min(x.fitness for x in self.individs))
        # self.print_population()

    def get_best(self):
        return min(x.fitness for x in self.individs)

    def print_population(self):
        print("======== Gen: " + str(self.generation) + " with fitness sum: " + str(self.fitness_sum) + " =============")
        for i in self.individs:
            print(str(i.list) + " " + str(i.fitness))