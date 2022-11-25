# Runtime: 94 ms, faster than 71.33% of Python online submissions for Two Sum.
# Memory Usage: 14.6 MB, less than 9.26% of Python online submissions for Two Sum.

def twoSum(nums, target):
    values_dict = {}
    for index, value in enumerate(nums): 
        if target - value in values_dict:
            return [values_dict[target - value], index] 
        else:
            values_dict[value] = index

print(twoSum([1, 2, 3, 4, 5], 6))
