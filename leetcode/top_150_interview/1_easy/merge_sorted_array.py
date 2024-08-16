"""
Type: Easy
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""
from copy import copy
from typing import List
from icecream import ic


"""
Merge Sort Solution
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        nums1_copy = copy(nums1)
        nums2_copy = copy(nums2)
        n1 = 0
        n2 = 0
        while 1:
            if n1 == m and n2 == n:
                break
            if n1 == m:
                nums1[i] = nums2_copy[n2]
                i += 1
                n2 += 1
                continue
            if n2 == n:
                nums1[i] = nums1_copy[n1]
                i += 1
                n1 += 1
                continue
            if nums1_copy[n1] < nums2_copy[n2]:
                nums1[i] = nums1_copy[n1]
                i += 1
                n1 += 1
            else:
                nums1[i] = nums2_copy[n2]
                i += 1
                n2 += 1
        ic(nums1)


"""
Simple python Solution
"""
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        for el in nums2:
            nums1[i] = el
            i += 1
        nums1.sort()
        ic(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

solution = Solution()
ic(solution.merge(nums1, m, nums2, n))