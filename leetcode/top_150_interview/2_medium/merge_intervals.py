"""
Type: Medium
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        merged_intervals = []

        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals


intervals = [[1,3]]
sol = Solution()
ic(sol.merge(intervals))