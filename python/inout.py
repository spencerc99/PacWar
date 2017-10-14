from __future__ import print_function

random_file = 'random_indivs.txt'
random_indivs = inout.read_indivs(random_file)
best_file = 'best_indivs.txt'
best_indivs = inout.read_pairs(best_file)
top_file = 'top_indiv.txt'
top_indiv = inout.read_pairs(top_file)

def write_best(indiv, score):
    for i in range(len(best_indivs)):
        if score > best_indivs[i][0]:
            if i == 0:
                write_list(top_file, [(score, indiv)])
            best_indivs.insert(i, (score, indiv))
            break
    write_list(best_file, best_indivs[:-1])
    gene_string = reduce(lambda l,r: str(l) + ' ' + str(r), indiv)
    print(gene_string, file=f)

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
