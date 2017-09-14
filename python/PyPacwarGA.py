import _PyPacwar
import numpy
import random
from score import score

gene_options = [0, 1, 2, 3]

"""
Returns a list of list of genes corresponding to the population size.
"""
def initial_state(pop_size):
    return [[random.choice(gene_options) for i in xrange(50)] for i in xrange(pop_size)]

"""
Uses fitness proportionate selection
p_i = \frac{f_i}{\Sigma_{j=1}^{N} f_j}
where p_i determines the probability of being chosen
"""
def selection(population, scores, max_score):
    new_pop = []
    weights = map(lambda s: float(s) / max_score,scores)
    pop_idxs = xrange(len(population))
    for i in pop_idxs:
        while True:
            idx = random.choice(pop_idxs)
            if random.random() < weights[idx]:
                break
        new_pop.append(population[idx])
    return new_pop

def crossover(population):
    for i in xrange(len(population) / 2):
        x = random.choice(population)
        y = None
        while y != x:
            y = random.choice(population)
        cross_pt = random.randrange(0, len(population))
        

def mutation(population):

def main():
    iterations = 250
    population = initial_state(100)
    other_indiv = [3] * 50
    scores = [score(indiv, other_indiv) for indiv in population]
    max_score = max(scores)
    for i in xrange(iterations):
        population = selection(population, scores, max_score)
