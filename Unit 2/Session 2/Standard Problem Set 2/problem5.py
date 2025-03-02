def is_route_covered(trips, start_dest, end_dest):
  start, end = False, False
  for trip in trips:
    if start_dest >= trip[0] and start_dest <= trip[1]:
      start = True
    elif end_dest >= trip[0] and end_dest <= trip[1]:
      end = True
  return start and end

trips1 = [[1, 2], [3, 4], [5, 6]]
start_dest1, end_dest1 = 2, 5

trips2 = [[1, 10], [10, 20]]
start_dest2, end_dest2 = 21, 21

trips3 = [[1, 2], [3, 5]]
start_dest3, end_dest3 = 2, 5

print(is_route_covered(trips1, start_dest1, end_dest1))
print(is_route_covered(trips2, start_dest2, end_dest2))
print(is_route_covered(trips3, start_dest3, end_dest3))