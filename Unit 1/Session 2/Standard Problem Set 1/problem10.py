def good_pairs(pile1, pile2, k):
	res = 0
	for i in range(len(pile1)):
		for j in range(len(pile2)):
			if pile1[i] % (pile2[j] * k) == 0:
				res += 1
	return res



pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))