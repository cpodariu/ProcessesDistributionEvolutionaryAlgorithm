import random


class Individ:
    def __init__(self, list, problem):
        self.list = list
        self.problem = problem
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        computers = [0 for i in range(len(self.problem.matrix[0]))]
        for i, j in enumerate(self.list):
            computers[j] += self.problem.matrix[i][j]
        return max(computers)

    def mutate(self, probability):
        for i, j in enumerate(self.list):
            if random.uniform(0, 1) < probability:
                self.list[i] = random.randint(0, len(self.problem.matrix[0]) - 1)
                self.fitness = self.calc_fitness()

    @staticmethod
    def crossover(individ1, individ2):
        # pivot = random.randint(0, len(individ1.list) - 1)
        pivot = int(len(individ1.list)/2)
        newlist = Individ(individ1.list[0:pivot] + individ2.list[pivot:], individ1.problem)
        return newlist

    @staticmethod
    def get_random_individ(problem):
        list = []
        for i in range(len(problem.matrix)):
            list.append(random.randint(0, len(problem.matrix[0]) - 1))
        return Individ(list, problem)