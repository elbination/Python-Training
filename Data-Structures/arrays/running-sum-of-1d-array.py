# https://leetcode.com/problems/running-sum-of-1d-array/
def running_sum(nums):
    total = 0
    result = []
    for i in range(len(nums)):
        total += nums[i]
        result.append(total)

    return result
