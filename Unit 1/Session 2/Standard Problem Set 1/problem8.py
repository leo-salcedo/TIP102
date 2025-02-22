def exclusive_elemts(lst1, lst2):
	res = []
	for elem in lst1:
		if elem not in lst2:
			res.append(elem)
	for elem in lst2:
		if elem not in lst1:
			res.append(elem)
	return res




lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))