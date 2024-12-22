"""
Type: Medium
137. Single Number II
https://leetcode.com/problems/single-number-ii/description/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            if i + 2 >= len(nums):
                return nums[-1]
            if nums[i] != nums[i + 1]:
                return nums[i] if nums[i + 1] == nums[i + 2] else nums[i+1]
            if nums[i + 1] != nums[i + 2]:
                return nums[i + 1] if nums[i + 2] == nums[i] else nums[i+2]
            i += 3
