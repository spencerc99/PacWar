import random
import inout

fname = 'battle_indivs.txt'
n = 25

def generate_random_gene():
    return [random.choice(xrange(4)) for i in xrange(50)]

def main():
    f = open(fname, 'w')
    f.truncate()
    genes = [generate_random_gene() for i in xrange(n)]
    inout.write_list(f, genes)

if __name__ == '__main__': main()
