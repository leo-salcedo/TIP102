def make_divisible_by_3(nums):
    res = 0
    for num in nums:
        r = num % 3
        res += min(r, 3 - r)
    return res



nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))