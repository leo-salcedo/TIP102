def reverse_list(lst):
    l, r = 0, len(lst) - 1
    while l < r:
        lst[l], lst[r] = lst[r], lst[l]
        l += 1
        r -= 1
    return lst



lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))