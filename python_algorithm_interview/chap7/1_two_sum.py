"""
https://leetcode.com/problems/two-sum
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len((nums))):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([3, 2, 4], 6))


def two_sum_other(nums: List[int], target: int) -> List[int]:
    temp = {}
    for i, e in enumerate(nums):
        temp[e] = i

    for i, e in enumerate(nums):
        sub = target - e
        if sub in temp and i != temp[sub]:
            return [nums.index(e), temp[sub]]


print(two_sum_other([4, 0, 2, 3, 1], 3))
