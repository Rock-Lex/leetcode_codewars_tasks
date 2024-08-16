"""
Type: Medium
57. Insert Interval
https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pass


intervals = [[1,3],[6,9]]
newInterval = [2,5]
sol = Solution()
ic(sol.insert(intervals, newInterval))
