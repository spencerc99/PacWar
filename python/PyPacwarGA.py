import _PyPacwar
import numpy
import random
import score
import inout

gene_options = [0, 1, 2, 3]
NUM_INDICES = 10

"""
Returns a list of list of genes corresponding to the population size.
"""
def initial_state(pop_size):
    return [[random.choice(gene_options) for i in xrange(50)] for i in xrange(pop_size)]

def selection(population, scores):
    # return stochastic_selection(population, scores, max_score)
    return normal_selection(population, scores)

def normal_selection(population, scores):
    edge = int(len(population) * 0.1)
    scores_asc = sorted(enumerate(scores), key=lambda s: s[1])
    pop_idxs = [s[0] for s in scores_asc[edge:]]
    keep_idxs = [s[0] for s in scores_asc[len(population) - edge:]]
    return [population[i] for i in pop_idxs], [population[i] for i in keep_idxs]


"""
Uses fitness proportionate selection
p_i = \frac{f_i}{\Sigma_{j=1}^{N} f_j}
where p_i determines the probability of being chosen
"""
def stochastic_selection(population, scores):
    new_pop = []
    max_score = max(scores)
    weights = map(lambda s: float(s) / max_score,scores)
    pop_idxs = xrange(len(population))
    for i in pop_idxs:
        while True:
            idx = random.choice(pop_idxs)
            if random.random() < weights[idx]:
                break
        new_pop.append(population[idx])
    return new_pop

def crossover(population, crossover_pct):
    return indices_crossover(population, crossover_pct)

def index_crossover(population, crossover_pct):
    children = []
    for i in xrange(int(len(population) * crossover_pct) / 2):
        x = population.pop(random.randint(0, len(population) - 1))
        y = population.pop(random.randint(0, len(population) - 1))
        cross_pt = random.randrange(0, 50)
        c1 = x[:cross_pt] + y[cross_pt:]
        c2 = y[:cross_pt] + x[cross_pt:]
        children.append(c1)
        children.append(c2)
    return population + children

def indices_crossover(population, crossover_pct):
    children = []
    indices = [0, 50]
    all_indices = list(xrange(1, 50))
    for i in range(NUM_INDICES):
        c = random.choice(all_indices)
        all_indices.remove(c)
        indices.append(c)
    indices.sort()
    for i in xrange(int(len(population) * crossover_pct) / 2):
        x = population.pop(random.randint(0, len(population) - 1))
        y = population.pop(random.randint(0, len(population) - 1))
        c1 = []
        c2 = []
        for j in xrange(len(indices) - 1):
            start = indices[j]
            end = indices[j+1]
            c1 += x[start:end] if random.random() < .5 else y[start:end]
            c2 += x[start:end] if random.random() < .5 else y[start:end]
        children.append(c1)
        children.append(c2)
    return population + children

def mutate(population, mutation_pct):
    for indiv in population:
        for i in range(50):
            choice = random.random()
            if choice < mutation_pct:
                indiv[i] = int(choice * 1000) % 100 / 25

def score_func(indiv, other_indiv):
    # return score.score(indiv, other_indiv)
    # return score.random_battle_score(indiv)
    # return score.best_battle_score(indiv)
    # return score.top_battle_score(indiv)
    return score.overall_score(indiv)

def main():
    score.init_best()
    iterations = 200
    population = initial_state(256)
    other_indiv = [[gene]*50 for gene in gene_options]
    crossover_pct = 1
    mutation_pct = .02
    best = (0, [])
    for i in xrange(iterations):
        scores = [score_func(indiv, other_indiv) for indiv in population]
        idx, best_score = max(enumerate(scores), key=lambda x: x[1])
        if best_score > best[0]:
            best = (best_score, population[idx])
        if (i == 25 and best_score < 6) or (i == 50 and best_score < 7) or (i == 100 and best_score < 8) or (i == 150 and best_score < 13): # Early termination for bad population
            break
        print i, best_score
        population, keep = normal_selection(population, scores)
        population = crossover(population, crossover_pct)
        population += keep
        mutate(population, mutation_pct)

    print "Max score", best[0]
    score.write_best(best[1])

if __name__ == "__main__":
    for i in range(500):
        print "        ", i
        print "===================\n" * 5
        main()
