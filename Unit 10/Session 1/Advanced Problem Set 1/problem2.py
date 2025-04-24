from collections import defaultdict
def find_center(terminals):
    frequency = defaultdict(int)
    n = len(terminals)
    for i in range(n):
        for j in terminals[i]:
            frequency[j] += 1
    
    for key in frequency:
        if frequency[key] == n:
            return key
    return -1


terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))