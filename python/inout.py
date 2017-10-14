from __future__ import print_function

random_file = 'random_indivs.txt'
best_file = 'best_indivs.txt'
best_indivs = inout.read_pairs(best_file)
top_file = 'top_indiv.txt'
top_indiv = inout.read_pairs(top_file)
N = 25

def write_best(indiv, score):
    num_best = len(best_indivs)
    for i in range(num_best):
        if score > best_indivs[i][0]:
            best_indivs.insert(i, (score, indiv))
            write_list(best_file, best_indivs[:-1])
            return

    if num_best < N:
        best_indivs.append((score, indiv))
        write_list(best_file, best_indivs)


def write_list(fname, pairs):
    with open(fname, 'w') as f:
        f.truncate()
        map(lambda pair: print(pair_string(pair), file=f), pairs)

def write_random(indivs):
    with open(random_file, 'w' as f:
        f.truncate()
        map(lambda indiv: print(gene_string(indiv), file=f), indivs)

def gene_string(indiv):
    return reduce(lambda l,r: str(l) + ' ' + str(r), indiv)

def pair_string(pair):
    score = pair[0]
    indiv = pair[1]
    return str(score), gene_string(indiv)

def read_indivs(fname):
    with open(fname) as f:
        data = f.readlines()
    return [line.rstrip().split() for line in data]

def read_pairs(fname):
    with open(fname) as f:
        data = f.readlines()
    return [float(arr[0]), arr[1:] for indiv in [line.rstrip().split() for line in data]]
