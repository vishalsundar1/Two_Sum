def two_sum(nums, target):
    hmap = {}
    for i, j in enumerate(nums):
        if target - j in hmap:
            return hmap[target - j], i
        hmap[j] = i

target = 9
num_arr = (2, 7 , 15, 1)
print(two_sum(num_arr, target))
