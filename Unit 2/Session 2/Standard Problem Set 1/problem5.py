def distinct_averages(species_populations):
  sett = set()
  while len(species_populations) > 0:
    minimum = min(species_populations)
    maximum = max(species_populations)
    average = ((minimum + maximum) / 2)
    sett.add(average)
    if minimum == maximum:
      species_populations.remove(maximum)
    else:
      species_populations.remove(minimum)
      species_populations.remove(maximum)
  return len(sett)
      


species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 