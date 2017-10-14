import _PyPacwar
import numpy
from score import score

# Example Python module in C for Pacwar
def main():

	ones   = [1]*50
	threes = [3]*50
	print "Example Python module in C for Pacwar"
	print "all ones versus all threes ..."
	(rounds,c1,c2) = _PyPacwar.battle(ones, threes)
	print "Number of rounds:", rounds
	print "Ones PAC-mites remaining:", c1
	print "Threes PAC-mites remaining:", c2
	top = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 0, 2, 3, 3, 3, 3, 3, 1, 3, 1, 2, 1, 2, 2, 3, 1, 3, 1, 2, 2, 1, 2, 2, 1, 1, 3, 1, 1, 3, 3, 1, 2, 1, 1, 3, 0]

	test = [1, 1, 2, 0, 1, 1, 1, 2, 3, 1, 3, 2, 1, 3, 3, 3, 1, 1, 0, 0, 1, 1, 2, 1, 1, 2, 1, 3, 2,
	1, 1, 2, 3, 1, 0, 2, 1, 2, 1, 1, 2, 3, 3, 1, 1, 3, 3, 3, 2, 1]
	print ""
	print "candidate vs all ones"
	(rounds,c1,c2) = _PyPacwar.battle(test, ones)
	print "Number of rounds:", rounds
	print "Test PAC-mites remaining:", c1
	print "Ones PAC-mites remaining:", c2
	print "score:", score(test, ones)

	test_threes = [3, 3, 3, 3, 3, 3, 2, 3, 0, 0, 0, 3, 2, 1, 1, 3, 1, 3, 2, 0, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 1, 1, 2, 1, 3, 1]
	print ""
	print "candidate vs all ones"
	(rounds,c1,c2) = _PyPacwar.battle(test_threes, threes)
	print "Number of rounds:", rounds
	print "Test PAC-mites remaining:", c1
	print "Threes PAC-mites remaining:", c2
	print "score:", score(test_threes, threes)

if __name__ == "__main__": main()
