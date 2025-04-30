# Given a list of trasnactions 
# transactions = [["customer1", event_32, "7000"],
# ["customer1", event_36, “5000"],
# ["customer2”, event_39, “3000”]]
# Return the amount of events each customer had and how much money spent.
# Output example: Customer 1: (2, 12000), Customer 3: (1, 3000)


def function(transactions):
    customer_to_event_data = {}
    for customer, event, money in transactions:
        event_money = int(money)
        if customer not in customer_to_event_data:
            customer_to_event_data[customer] = (1, event_money)
        else:
            total_events, total_money = customer_to_event_data[customer]
            customer_to_event_data[customer] = (total_events + 1, total_money + event_money)
    return customer_to_event_data

    
transactions = [["customer1", "event_32", "7000"], 
                ["customer1", "event_36", "5000"],
                ["customer2", "event_39", "3000"]]

print(function(transactions))