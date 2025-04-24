from collections import deque
def counting_flights(flights, i, j):
    n = len(flights)
    visited = set()
    q = deque()
    q.append((i, 0))
    visited.add(i)
    while q:
        (node, dist) = q.popleft()
        if node == j:
            return dist
        for k in range(n):
            if flights[node][k] == 1 and k not in visited:
                visited.add(k)
                q.append((k, dist + 1))

    return -1




flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))