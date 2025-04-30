# You are managing the promotions at a large retail store. Our store sends customized
# coupons to customers, based on their purchase history. These coupons are provided
# in the form of [Customer, Department, Value($)].

# Our customers prefer coupons for specific departments when they have them. These
# preferences are provided in an ordered list, from most popular to least popular.

# For example:
# preferences = ["Electronics", "Clothing", "Furniture", "Toys"]

# Given the constraints:
#     - Only one coupon can be used per customer
#     - A customer will receive a maximum of one coupon per department
#     - Customers will always choose to use the coupon for the most preferred department they have
#     - If a customer has a coupon for Electronics and Furniture, they will use the Electronics coupon, regardless of value

# We would like to calculate the expected cost of this promotion by department. Given a list of coupons issued
# and the list of preferred departments, write a function that returns the coupon cost per department.

# n = number of preferences
# m = number of coupons



# Time complexity - O(n + m)
# Space complexity - O(n + m)
def optimal(coupons, preferences):
    preference_rank = {}
    for i in range(len(preferences)): # Create preference rank map with department as key and rank as value
        preference_rank[preferences[i]] = len(preferences) - i

    customer_coupon = {} # Customers as keys and most preferred coupon as value
    for coupon in coupons:
        if coupon[0] not in customer_coupon: # If first customer seen add first coupon data
            customer_coupon[coupon[0]] = (coupon[1], int(coupon[2]))
        
        current_department, current_value = coupon[1], int(coupon[2])
        if preference_rank[current_department] > preference_rank[customer_coupon[coupon[0]][0]]: # Compare best coupon to current coupon
            customer_coupon[coupon[0]] = (current_department, current_value)
    
    result = {}
    for department, value in customer_coupon.values(): # Sum up department costs
        if department not in result:
            result[department] = 0
        result[department] += value
    
    return result

    



# Time complexity - O(n * m)
# Space complexity - O(n + m)
def suboptimal(coupons, preferences):
    used_coupons = set()
    result = {}
    for preference in preferences: # Loop through all preferences
        result[preference] = 0 # Initialize key value pair
        for coupon in coupons: # Loop through all coupons for each preference
            if coupon[1] == preference: # If coupon department matches preference
                if coupon[0] not in used_coupons: # If customer has not already used a coupon
                    used_coupons.add(coupon[0])
                    result[preference] += int(coupon[2]) # Update preference cost
    
    return result



coupons1 = [
    ["Customer1", "Electronics", "10"],
    ["Customer2", "Toys", "5"],
    ["Customer3", "Electronics", "15"],
    ["Customer4", "Furniture", "20"],
    ["Customer3", "Toys", "10"],
    ["Customer3", "Clothing", "5"],
    ["Customer2", "Clothing", "8"],
    ["Customer1", "Furniture", "12"]
]

preferences1 = ["Electronics", "Clothing", "Furniture", "Toys"]

print(suboptimal(coupons1, preferences1))
print(optimal(coupons1, preferences1))