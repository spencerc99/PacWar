from _PyPacwar import battle

def score(left, right):
	rounds, left_survive, right_survive = battle(left, right)
	left = 0 if left_survive > right_survive else 1
	right = 1 - left

	lt_100 = (20, 0)
	lt_200 = (19, 1)
	lt_300 = (18, 2)
	lt_500 = (17, 3)
	gt_10 = (13, 7)
	gt_3 = (12, 8)
	gt_1_5 = (11, 9)
	tie = (10, 10)

	if rounds < 100:
		return lt_100[left], lt_100[right]
	elif rounds < 200:
		return lt_200[left], lt_200[right]
	elif rounds < 300:
		return lt_300[left], lt_300[right]
	elif rounds < 500:
		return lt_500[left], lt_500[right]
	else:
		ratio = left_survive * 1.0 / right_survive if left_survive > right_survive else right_survive * 1.0 / left_survive
		if ratio > 10:
			return gt_10[left], gt_10[right]
		elif ratio > 3:
			return gt_3[left], gt_3[right]
		elif ratio > 1.5:
			return gt_1_5[left], gt_1_5[right]
		return tie[left], tie[right]