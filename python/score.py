from _PyPacwar import battle
from sys import platform
import inout


random_file = 'random_indivs.txt'
random_indivs = inout.read_indivs(random_file)
best_file = 'spencer_indivs.txt' if platform == "darwin" else 'austin_indivs.txt'
best_indivs = [pair[1] for pair in inout.read_pairs(best_file)]

def init_best():
    best_indivs = [pair[1] for pair in inout.read_pairs(best_file)]

N = 100

def sort_best():
    init_best()
    best = [(overall_score(i), i) for i in best_indivs]
    best.sort(reverse=True, key=lambda x: x[0])
    inout.write_list(best_file, best)

def write_best(indiv):
    init_best()
    num_best = len(best_indivs)
    best_indivs.append(indiv)
    best = [(overall_score(i), i) for i in best_indivs]
    best.sort(reverse=True, key=lambda x: x[0])
    if num_best < N:
        inout.write_list(best_file, best)
    else:
        inout.write_list(best_file, best[:N])
    sort_best()

def overall_score(candidate):
    return 0.1 * random_battle_score(candidate) + \
        0.9 * best_battle_score(candidate)

def top_battle_score(candidate):
    if not best_indivs:
        return 0
    return score(candidate, best_indivs[0])

def best_battle_score(candidate):
    if not best_indivs:
        return 0
    return sum([score(candidate, other) for other in best_indivs]) / float(len(best_indivs))

def random_battle_score(candidate):
 	return sum([score(candidate, other) for other in random_indivs]) / float(len(random_indivs))

def score(candidate, compare):
	rounds, candidate_survive, compare_survive = battle(candidate, compare)
	i = 0 if candidate_survive > compare_survive else 1

	lt_100 = (20, 0)
	lt_200 = (19, 1)
	lt_300 = (18, 2)
	lt_500 = (17, 3)
	gt_10 = (13, 7)
	gt_3 = (12, 8)
	gt_1_5 = (11, 9)
	tie = (10, 10)

	if rounds < 100:
		return lt_100[i]
	elif rounds < 200:
		return lt_200[i]
	elif rounds < 300:
		return lt_300[i]
	elif rounds < 500:
		return lt_500[i]
	else:
		if candidate_survive == 0 or compare_survive == 0:
			return lt_500[i]
		ratio = candidate_survive * 1.0 / compare_survive if candidate_survive > compare_survive else compare_survive * 1.0 / candidate_survive
		if ratio > 10:
			return gt_10[i]
		elif ratio > 3:
			return gt_3[i]
		elif ratio > 1.5:
			return gt_1_5[i]
		return tie[i]

# mine = "0 0 0 2 0 0 0 0 1 1 1 1 2 2 2 2 0 0 3 0 1 2 1 1 2 1 3 2 3 2 2 3 1 2 3 1 3 2 3 1 3 3 1 3 3 0 0 3 1 1".split()
# print overall_score(mine)

def best_grid(num_top):
    init_best()
    print ' ' * 4 + reduce(lambda x,y: str(x) + ' ' * (3 - len(str(y))) + str(y), xrange(num_top))
    for against, indiv in enumerate(best_indivs):
        disp = [score(best_indivs[i], indiv) for i in xrange(num_top)]
        print str(against) + ' ' * (5 - len(str(against)) - len(str(disp[0]))) + reduce(lambda x,y: str(x) + ' ' * (3 - len(str(y))) + str(y), disp)

def best_lt_grid(num_top):
    init_best()
    print ' ' * 4 + reduce(lambda x,y: str(x) + ' ' * (3 - len(str(y))) + str(y), xrange(num_top))
    for against, indiv in enumerate(best_indivs):
        disp = [score(best_indivs[i], indiv) for i in xrange(num_top)]
        loss_tie_disp = ['D' if d < 5 else 'L' if d < 10 else 'T' if d == 10 else ' ' for d in disp]
        print str(against) + ' ' * (4 - len(str(against))) + reduce(lambda x,y: x + ' ' * 2 + y, loss_tie_disp)

def against_best(test):
    init_best()
    for against, indiv in enumerate(best_indivs):
        print against, score(test, indiv)

def against_lt_best(test):
    init_best()
    for against, indiv in enumerate(best_indivs):
        d = score(test, indiv)
        print against, 'D' if d < 5 else 'L' if d < 10 else 'T' if d == 10 else ' '

def confirm_scores():
    init_best()
    for indiv in best_indivs:
        print overall_score(indiv)

test1 = "0 3 1 0 0 0 0 0 0 3 1 3 0 0 2 0 3 3 3 3 3 2 3 1 2 1 1 2 1 1 2 1 3 1 1 1 2 1 1 3 1 1 3 1 1 2 0 1 3 1".split()
test2 = [0, 3, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 2, 0, 0, 3, 2, 3, 3, 3, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 3, 0, 1, 1, 1, 2, 3, 1, 1, 2, 0]
# print overall_score(test1)
# best_grid(5)
# best_lt_grid(5)
# against_best(test1)
# against_best(test2)
# against_lt_best(test1)
