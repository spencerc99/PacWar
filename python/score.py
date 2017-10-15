from _PyPacwar import battle
from sys import platform
import inout

def init_best():
    return [pair[1] for pair in inout.read_pairs(best_file)]

random_file = 'random_indivs.txt'
random_indivs = inout.read_indivs(random_file)
best_file = 'spencer_indivs.txt' if platform == "darwin" else 'austin_indivs.txt'
best_indivs = init_best()
N = 25

def write_best(indiv, s):
    best_indivs = init_best()
    num_best = len(best_indivs)
    best_indivs = [(overall_score(indiv), indiv) for indiv in best_indivs]
    best_indivs.append((s, indiv))
    best_indivs.sort(reverse=True, key=lambda x: x[0])
    if num_best < N:
        inout.write_list(best_file, best_indivs)
    else:
        inout.write_list(best_file, best_indivs[:-1])

def overall_score(candidate):
    return 0.25 * random_battle_score(candidate) + \
        0.65 * best_battle_score(candidate) + \
        0.1 * top_battle_score(candidate)

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

# spencer = [0,1,3,0,0,3,0,0,1,1,1,1,0,0,2,0,3,0,0,0,1,3,3,3,2,3,2,2,3,3,2,3,3,2,3,3,2,3,3,1,0,3,1,3,0,1,3,3,1,0]
#
# print score(spencer,)

# for indiv in best_indivs:
    # print score(best_indivs[0], indiv)
