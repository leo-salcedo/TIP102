def num_airline_regions(is_connected):
    def dfs(node, is_connected):
        if node in visited:
            return
        visited.add(node)
        for i in range(len(is_connected[node])):
                if is_connected[node][i] == 1 and i not in visited:
                    dfs(i, is_connected)
    
    visited = set()
    result = 0
    for i in range(len(is_connected)):
        if i not in visited:
             result += 1
             dfs(i, is_connected)
    return result




is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 