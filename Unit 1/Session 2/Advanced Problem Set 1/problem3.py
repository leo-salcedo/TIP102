def remove_dupes(items):
    j = 1
    for i in range(1, len(items)):
        if items[i] != items[i - 1]:
            items[j] = items[i]
            j += 1
    return j


items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))