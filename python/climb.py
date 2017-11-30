import random
import math
import score
import itertools

def hill_climbing(candidate, n, l):
    solutions = []
    current = candidate
    best_score = score.overall_score(current)
    print best_score
    i = 0
    while True:
        cand_score, cand = select_best_neighbor(current)
        if cand_score > best_score:
            print i, cand_score
            current = cand
            best_score = cand_score
            i+=1
        else:
            break
    return current

def select_neighbor(cand):
    neigh = list(cand)
    mutate = random.choice(range(len(neigh)))
    neigh[mutate] = random.choice(range(4))
    return neigh


def select_best_neighbor(cand):
    poss_cands = []
    best = (0, None)
    for i in range(len(cand)):
        for j in range(1, 4):
            poss_cand = list(cand)
            poss_cand[i] = (poss_cand[i] + j) % 4
            cur = score.overall_score(poss_cand)
            if cur > best[0]:
                best = (cur, poss_cand)
    return best

if __name__ == "__main__":
    candidate = "0 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0 3 0 3 3 1 3 3 3 2 3 2 2 3 2 2 3 2 2 2 3 3 3 3 1 3 3 1 3 1 1 0 3 1 0".split()
    candidate = [int(c) for c in candidate]
    final = hill_climbing(candidate, 100, 1000)
    print ' '.join([str(s) for s in final])
