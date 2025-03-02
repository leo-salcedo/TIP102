def prioritize_observations(observed_species, priority_species):
    frequency = {}
    for species in observed_species:
        if species in priority_species:
            if species not in frequency:
                frequency[species] = 1
            else:
                frequency[species] += 1
            
    front = []
    back = []
    for species in priority_species:
        for i in range(frequency[species]):
            front.append(species)
    for species in observed_species:
        if species not in priority_species:
            back.append(species)
    front.extend(sorted(back))
    return front

        
  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species2, priority_species2)) 