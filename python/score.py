from _PyPacwar import battle
import inout

random_file = 'random_indivs.txt'
random_indivs = inout.read_indivs(random_file)
best_file = 'best_indivs.txt'
best_indivs = [pair[1] for pair in inout.read_pairs(best_file)]
top_file = 'top_indiv.txt'
top_indiv = inout.read_pairs(top_file)[1]

def top_battle_score(candidate):
    return score(candidate, top_indiv[0])

def best_battle_score(candidate):
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
