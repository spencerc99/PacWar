import _PyPacwar
import numpy
import random
import score
import inout

gene_options = [0, 1, 2, 3]

"""
Returns a list of list of genes corresponding to the population size.
"""
def initial_state(pop_size):
    return [[random.choice(gene_options) for i in xrange(50)] for i in xrange(pop_size)]

def selection(population, scores):
    # return stochastic_selection(population, scores, max_score)
    return normal_selection(population, scores)

def normal_selection(population, scores):
    edge = int(len(population) * 0.2)
    scores_asc = sorted(enumerate(scores), key=lambda s: s[1])
    pop_idxs = [s[0] for s in scores_asc[edge:]]
    keep_idxs = [s[0] for s in scores_asc[len(population) - edge:]]
    # print "pop, keep", len(pop_idxs), len(keep_idxs)
    return [population[i] for i in pop_idxs], [population[i] for i in keep_idxs]


"""
Uses fitness proportionate selection
p_i = \frac{f_i}{\Sigma_{j=1}^{N} f_j}
where p_i determines the probability of being chosen
"""
def stochastic_selection(population, scores):
    new_pop = []
    # print scores
    # print max_score
    max_score = max(scores)
    if max_score == 0:
        print scores
    weights = map(lambda s: float(s) / max_score,scores)
    pop_idxs = xrange(len(population))
    for i in pop_idxs:
        # print pop_idxs
        # print weights
        while True:
            idx = random.choice(pop_idxs)
            if random.random() < weights[idx]:
                break
        new_pop.append(population[idx])
    return new_pop

def crossover(population, crossover_pct):
    return index_crossover(population, crossover_pct)

def index_crossover(population, crossover_pct):
    children = []
    for i in xrange(int(len(population) * crossover_pct) / 2):
        # x = random.choice(population)
        # population.remove(x)
        x = population.pop(random.randint(0, len(population) - 1))
        y = population.pop(random.randint(0, len(population) - 1))
        # y = random.choice(population)
        # population.remove(y)
        cross_pt = random.randrange(0, 50)
        c1 = x[:cross_pt] + y[cross_pt:]
        c2 = y[:cross_pt] + x[cross_pt:]
        children.append(c1)
        children.append(c2)
    return population + children

def mutate(population, mutation_pct):
    for indiv in population:
        for i in range(50):
            if random.random() < mutation_pct:
                indiv[i] += 1
                indiv[i] %= 4 # moves it to the right one

def score_func(indiv, other_indiv):
    # return score.score(indiv, other_indiv)
    # return score.random_battle_score(indiv)
    # return score.best_battle_score(indiv)
    # return score.top_battle_score(indiv)
    return score.overall_score(indiv)

def main(storing=False):
    iterations = 25
    population = initial_state(200)
    other_indiv = [[gene]*50 for gene in gene_options]
    crossover_pct = 1
    mutation_pct = .005
    for i in xrange(iterations):
        scores = [score_func(indiv, other_indiv) for indiv in population] # Only caring about our score
        print max(scores)
        population, keep = normal_selection(population, scores)
        population = crossover(population, crossover_pct)
        population += keep
        mutate(population, mutation_pct)

    scores = [score_func(indiv, other_indiv) for indiv in population]
    # print population
    print scores
    idx, found_max_score = max(enumerate(scores), key=lambda x: x[1])
    print "Population with max score: ", population[idx]
    print "Max score", found_max_score
    inout.write_best(population[idx], found_max_score)

# def store(candidate):
#     with open("best_indivs.txt", "a") as f:
#         f.write(' '.join([str(gene) for gene in candidate]) + "\n")

if __name__ == "__main__":
    for i in range(10):
        main(True)
    # main(True)
