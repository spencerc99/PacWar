from __future__ import print_function

"""
f: Opened file
indiv: Array of [0,1,2,3] - length 50

Writes indiv to file.
"""
def write_indiv(f, indiv):
    gene_string = reduce(lambda l,r: str(l) + ' ' + str(r), indiv)
    print(gene_string, file=f)

"""
f: Opened file
indivs: Array of 'gene'

Writes indivs to file.
"""
def write_list(f, indivs):
    map(lambda indiv: write_indiv(f, indiv), indivs)

"""
fname: File name

Reads array of indivs from the file.
"""
def read(fname):
    with open(fname) as f:
        data = f.readlines()
    return [indiv.strip().split() for indiv in data]
