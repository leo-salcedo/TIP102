from collections import defaultdict

# You're given a list of logs representing user activity on various resources in an online system. Each log entry contains a timestamp (in seconds), a user ID, and a resource ID.

# Your task is to find the user who accessed the most unique resources.

# If multiple users have accessed the same maximum number of unique resources, return any one of them.

# Write a function that takes a list of logs and returns the user ID who accessed the most unique resources.


logs = [
    ["120", "user_3", "resource_2"],
    ["300", "user_5", "resource_1"],
    ["500", "user_4", "resource_1"],
    ["60", "user_2", "resource_1"],
    ["700", "user_1", "resource_3"],
    ["900", "user_5", "resource_4"],
    ["1100", "user_1", "resource_2"],
    ["1200", "user_3", "resource_1"],
    ["800", "user_6", "resource_3"],
    ["1500", "user_2", "resource_1"],
    ["1800", "user_4", "resource_5"],
    ["400", "user_3", "resource_2"],
    ["2000", "user_3", "resource_4"],
    ["50", "user_7", "resource_2"],
    ["2400", "user_8", "resource_6"],
    ["2600", "user_9", "resource_5"],
    ["2200", "user_6", "resource_3"],
    ["1400", "user_2", "resource_1"],
    ["3000", "user_11", "resource_7"],
    ["3200", "user_1", "resource_8"],
    ["3600", "user_2", "resource_6"],
    ["3800", "user_5", "resource_9"],
    ["1300", "user_4", "resource_1"],
    ["2800", "user_10", "resource_3"],
    ["100", "user_9", "resource_1"],
    ["4000", "user_8", "resource_1"]
]

def function(logs):
    users_to_resource = defaultdict(set)
    max_resources = float('-inf')
    for timestamp, user, resource in logs:
        users_to_resource[user].add(resource)
        max_resources = max(max_resources, len(users_to_resource[user]))
    for user, resource_set in users_to_resource.items():
        if len(resource_set) == max_resources:
            return user
    return ''

print(function(logs))