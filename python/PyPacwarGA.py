import _PyPacwar
import numpy
import random

gene_options = [0, 1, 2, 3]

"""
Returns a list of list of genes corresponding to the population size.
"""
def initial_state(pop_size):
    return [[random.choice(gene_options) for i in range(50)] for i in range(pop_size)]

def selection(population):
