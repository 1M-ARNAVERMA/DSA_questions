def twoSum(nums, target):
    Hmap = {}  # Value : Index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in Hmap:
            return [Hmap[diff], i]
        Hmap[n] = i
    return

nums = [4, 6, 4, 5]
target = 10

print(twoSum(nums, target))
