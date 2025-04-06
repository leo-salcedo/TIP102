def reverse_orders(orders):
    order_list = orders.split(" ")
    res = []
    recurse(order_list, res)
    return " ".join(res)

def recurse(order_list, res):
    if not order_list:
        return
    else:
        res.append(order_list.pop())
        recurse(order_list, res)


print(reverse_orders("Bagel Sandwich Coffee"))