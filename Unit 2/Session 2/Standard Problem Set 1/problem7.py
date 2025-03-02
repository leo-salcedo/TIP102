import re

def count_unique_species(ecosystem_data):
  list = re.split(r'[a-zA-Z]+', ecosystem_data)
  sett = set()
  for element in list:
    if len(element) > 0:
      sett.add(int(element))
  return len(sett)


ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))