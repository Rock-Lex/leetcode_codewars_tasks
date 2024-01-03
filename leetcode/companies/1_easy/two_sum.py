"""
Type: Easy
1. Two Sum
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] not in nums:
                continue
            j = nums.index(target - nums[i])
            if j == i: continue
            return [i, j]




# nums = [2,7,11,15]
nums = [3,3]
# target = 9
target = 6

solution = Solution()
print(solution.twoSum(nums=nums, target=target))