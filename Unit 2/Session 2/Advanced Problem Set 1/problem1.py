from collections import Counter

def find_balanced_subsequence(art_pieces):
    count = Counter(art_pieces)
    max_length = 0

    for num in count:
        if num + 1 in count:  # Check if there is a number (num + 1)
            max_length = max(max_length, count[num] + count[num + 1])

    return max_length

            



art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))