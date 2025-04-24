from collections import deque
def get_all_destinations(flights, start):
    q = deque()
    visited = set()
    q.append(start)
    result = []
    while q:
        current = q.popleft()
        visited.add(current)
        result.append(current)
        if current in flights:
            for neighbor in flights[current]:
                if neighbor not in visited:
                    q.append(neighbor)
    return result



flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))