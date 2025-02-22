def delete_minimum_elements(hunny_jar_sizes):
	res = []
	while hunny_jar_sizes:
		minn = min(hunny_jar_sizes)
		res.append(minn)
		hunny_jar_sizes.remove(minn)
	return res


hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))