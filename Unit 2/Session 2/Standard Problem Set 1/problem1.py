def most_endangered(species_list):
    name = ""
    minimum = float('inf')
    for species in species_list:
        if minimum > species["population"]:
            minimum = species["population"]
            name = species["name"]
    return name




species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))