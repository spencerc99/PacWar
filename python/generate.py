import random
import io

f = 'battle_indivs.txt'
n = 25

def generate_random_gene():
    return [random.choice(xrange(4)) for i in xrange(50)]

def main():
    open(f, 'w').close() # Clears the file
    genes = [generate_random_gene() for i in xrange(n)]
    io.write_list(f, genes)

if __name__ == "__main__": main()
