from collections import Counter

def max_species_copies(raised_species, target_species):
  raised_count = Counter(raised_species)
  target_count = Counter(target_species)
  min_ratio = float('inf')
  for species in target_species:
    min_ratio = min(min_ratio, raised_count.get(species, 0) // target_count[species])
  return min_ratio


raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2