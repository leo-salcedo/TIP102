def navigate_research_station(station_layout, observations):
  dictionary = {}
  for index, char in enumerate(station_layout):
    dictionary[char] = index
  curr_index = 0
  result = 0
  for char in observations:
    difference = abs(curr_index - dictionary[char])
    result += difference
    curr_index = dictionary[char]
  return result


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))