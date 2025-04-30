# Task — Find a “7-minute pair” of songs

# Your station keeps a list of songs, each stored as a title plus its playback time in “M:SS” format.

# Management wants two different songs played back-to-back that add up to exactly 7 minutes (7 : 00).

# Write a function that, given the list, returns the titles of any two songs whose lengths sum to seven minutes.
#  
# If no such pair exists, return an empty list (or any empty container you prefer).

song_times_1 = [
    ("Sunrise",            "3:50"),
    ("Chasing Stars",      "2:30"),
    ("Lazy Sunday",        "3:41"),
    ("Ocean Breeze",       "2:29"),
    ("City Lights",        "2:48"),
    ("Golden Hour",        "3:19"),
    ("Night Drive",        "3:18"),
    ("Endless Road",       "4:55")
]

# find_pair(song_times_1)  ➜  ["Lazy Sunday", "Golden Hour"]   # 3:41 + 3:19 = 7:00
# BASICALLY TWO SUM - O(n) time and space and complexity

def function(song_times):
    time_to_song = {}
    for song, time in song_times:
        minutes, seconds = map(int, time.split(':'))
        total_time = minutes * 60 + seconds
        if (420 - total_time) in time_to_song:
            return [song, time_to_song[420 - total_time]]
        time_to_song[total_time] = song
    
    return []



print(function(song_times_1))