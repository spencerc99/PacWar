from __future__ import print_function

def write_gene(f, gene):
    gene_string = reduce(lambda l,r: str(l) + ' ' + str(r), gene)
    print(gene_string, file=f)

def write_list(f, genes):
    map(lambda gene: write_gene(f, gene), genes)

def read(fname):
    with open(fname) as f:
        data = f.readlines()
    return [gene.strip().split() for gene in data]
