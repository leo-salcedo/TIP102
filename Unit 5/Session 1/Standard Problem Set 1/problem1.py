class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
	    if (len(new_catchphrase) > 20) or (not new_catchphrase.isalpha()):
            print("Invalid catchphrase")
        else:
            print("Catchphrase updated")
            catchphrase = new_catchphrase

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)