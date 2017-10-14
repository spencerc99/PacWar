import random
import inout

n = 25

def generate_random_gene():
    return [random.choice(xrange(4)) for i in xrange(50)]

def main():
    genes = [generate_random_gene() for i in xrange(n)]
    inout.write_random(genes)

if __name__ == '__main__': main()
