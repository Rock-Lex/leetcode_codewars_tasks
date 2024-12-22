"""
Type: Medium
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_number = None
        counter = 0
        len_nums = len(nums)
        index = 0
        while index < len_nums:
            if cur_number != nums[index]:
                cur_number = nums[index]
                counter = 1
            else:
                counter += 1
                if counter > 2:
                    nums.pop(index)
                    index -= 1
                    len_nums -= 1
            index += 1
