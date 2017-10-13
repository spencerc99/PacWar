from __future__ import print_function

def write(f, gene):
    print(reduce(lambda l,r: str(l) + ' ' + str(r), gene), file=f)

def write_list(f, genes):
    print(f, genes)
    map(lambda gene: write(f, gene), genes)

def read(f):
    with open(f) as file:
        data = file.readlines()
    return [gene.strip().split() for gene in data]
