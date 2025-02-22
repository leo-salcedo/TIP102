def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    minn, maxx = min(nums), max(nums)
    for num in nums:
        if num != minn and num != maxx:
            return num
    return -1





nums = [3, 2, 1, 4]
# [1, 2, 3, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))