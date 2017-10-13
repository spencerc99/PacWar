from __future__ import print_function

"""
f: Opened file
gene: Array of [0,1,2,3] - length 50

Writes gene to file.
"""
def write_gene(f, gene):
    gene_string = reduce(lambda l,r: str(l) + ' ' + str(r), gene)
    print(gene_string, file=f)

"""
f: Opened file
genes: Array of 'gene'

Writes genes to file.
"""
def write_list(f, genes):
    map(lambda gene: write_gene(f, gene), genes)

"""
fname: File name

Reads array of genes from the file.
"""
def read(fname):
    with open(fname) as f:
        data = f.readlines()
    return [gene.strip().split() for gene in data]
