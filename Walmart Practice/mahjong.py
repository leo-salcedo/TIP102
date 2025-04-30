# Question 1

# A simplified Mahjong-style mini-game is under development.

# Each tile bears a single digit 0 – 9. Within a hand, tiles may be arranged only as

# pairs: exactly two identical tiles, or

# triples: exactly three identical tiles.

# Examples

# “333344466” → one triple of 3 s, one triple of 4 s, one pair of 6 s.

# “55557777” → one triple of 5 s, one pair of 5 s, one triple of 7 s.

# A hand is complete if all tiles can be partitioned into any number of triples (possibly zero) and exactly one pair.
#  
# No tile may belong to more than one group.

# Implement a function that, given an unordered string of tiles, returns true when the hand is complete and false otherwise.

from collections import defaultdict

def function(tiles):
    tile_to_count = defaultdict(int)
    for tile in tiles:
        tile_to_count[tile] += 1
    
    foundPair = False
    for tile, count in tile_to_count.items():
        if count == 2 and foundPair:
            return False
        if count == 2:
            foundPair = True
            continue
        if count % 3 != 0:
            return False
    return True and foundPair



string1 = "33344466"
string2 = "5557777"
string3 = "333222"

print(function(string1))
print(function(string2))
print(function(string3))
