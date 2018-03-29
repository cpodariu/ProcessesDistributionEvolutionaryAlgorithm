import time
import matplotlib.pyplot as plt
from domain import Problem
from Controller import Controller
from domain.Population import Population

pb = Problem.Problem(Controller().read_string(0))
def cool_test_30():
    maxims = []
    for i in range(30):
        pop = Population(40, pb, 0.01)
        while pop.generation < 1000:
            pop.get_next_gen()
        maxims.append(pop.get_best())
        print(str(i) + " " + str(maxims[i]))
    plt.plot(maxims)
    plt.show()

def cool_test_once():
    population = Population(100, pb, 0.001)

    t_end = time.time() + 10
    while time.time() < t_end:
        population.get_next_gen()

    plt.plot(population.stats)
    plt.show()

# cool_test_30()
cool_test_once()