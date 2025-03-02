def best_set(votes):
    dictionary = {}
    for id in votes:
        if votes[id] not in dictionary:
            dictionary[votes[id]] = 1
        else:
            dictionary[votes[id]] = dictionary[votes[id]] + 1
    print(dictionary)
    max_key = max(dictionary, key=dictionary.get)
    res = ""
    for artist in dictionary:
        if dictionary[artist] == dictionary[max_key]:
            res = artist
    return res


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))