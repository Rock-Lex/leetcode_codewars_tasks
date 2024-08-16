"""
Type: Medium
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic

"""
Different Approach
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest


"""
First approach 
O(n*log n)
"""
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_seq = 0
        temp_seq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                temp_seq += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_seq = max(max_seq, temp_seq)
                temp_seq = 1
        return max(max_seq, temp_seq) if nums else 0


nums = [1,2,0,1]
sol = Solution()
ic(sol.longestConsecutive(nums))