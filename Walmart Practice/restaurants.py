# Given a friend’s liked restaurants and a list of other customers' likes:
# 1. Identify customers who share at least 2 restaurants with the friend.
# 2. From those customers, count how often they like restaurants the friend hasn’t liked.
# 3.Recommend the restaurant with the highest count. If tied, return any. If none, return None.


# friend_likes_1_1 = [1, 4, 10]
# likes_data_1 = [
# [10, 7, 1, 8, 6]    # Two restaurants are in common (1, 10)    Count the other restaurants (7, 8, 6) once.
#    [8, 3, 7, 2, 1]     # Only restaurant 1 is in common.          Don't count any of these.
#    [6, 7, 10, 4, 5]    # Two restaurants in common.               Count (6, 7, 5) once.
#    [4, 3, 8, 6]        # Only restaurant 4 is in common.          Don't count any of these.
#    [1, 6, 10, 4, 8]    # Three restaurants in common (1, 4, 10)   Count (6, 8) once.
# ]

# recommendations(likes_data_1, friend_likes_1_1)  # Output: 6

from collections import defaultdict

def recommendations(likes_data, friend_likes):
    friend_likes_set = set(friend_likes)
    other_restaurant_count = defaultdict(int)
    for other_customer in likes_data:
        other_customer_set = set(other_customer)
        if len(other_customer_set & friend_likes_set) >= 2:
            for other_restaurant in (other_customer_set - friend_likes_set):
                other_restaurant_count[other_restaurant] += 1
    if not other_restaurant_count:
        return None
    max_frequency = max(other_restaurant_count.values())
    for other_restaurant in other_restaurant_count:
        if other_restaurant_count[other_restaurant] == max_frequency:
            return other_restaurant


friend_likes_1_1 = [1, 4, 10]

likes_data_1 = [
[10, 7, 1, 8, 6],    # Two restaurants are in common (1, 10)    Count the other restaurants (7, 8, 6) once.
   [8, 3, 7, 2, 1],     # Only restaurant 1 is in common.          Don't count any of these.
   [6, 7, 10, 4, 5],    # Two restaurants in common.               Count (6, 7, 5) once.
   [4, 3, 8, 6],        # Only restaurant 4 is in common.          Don't count any of these.
   [1, 6, 10, 4, 8],    # Three restaurants in common (1, 4, 10)   Count (6, 8) once.
]

print(recommendations(likes_data_1, friend_likes_1_1))