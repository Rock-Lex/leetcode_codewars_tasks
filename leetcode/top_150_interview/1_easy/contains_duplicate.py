"""
Type: Easy
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        numbers = {}
        for index, num in enumerate(nums):
            if num in numbers and index - numbers[num] <= k:
                return True
            numbers[num] = index
        return False


class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = {}
        for index, num in enumerate(nums):
            num_index = numbers.get(num)
            if num_index is None:
                numbers[num] = index
                continue
            if abs(num_index - index) <= k:
                return True
            numbers[num] = index
        return False


if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 1
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))