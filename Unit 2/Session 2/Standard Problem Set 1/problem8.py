from collections import Counter

def num_equiv_species_pairs(species_pairs):
  frequency = Counter(tuple(sorted(pair)) for pair in species_pairs)
  count = 0
  for pair in frequency:
    n = frequency[pair]
    count += (n * (n - 1) // 2)
  return count

species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))