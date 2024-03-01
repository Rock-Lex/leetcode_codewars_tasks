"""
Type: Medium
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
"""
import math
from typing import List
from icecream import ic
import time


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pass


class BadSolution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answ = []
        sum_answ = 0
        best_len = -1
        i = 0
        l_nums = len(nums)
        while 1:
            if i != l_nums and sum_answ < target:
                answ.append(nums[i])
                sum_answ += nums[i]
                i += 1
            if sum_answ >= target:
                if best_len == - 1:
                    best_len = len(answ)
                    sum_answ -= answ.pop(0)
                    continue
                best_len = min(len(answ), best_len)
                sum_answ -= answ.pop(0)
                continue
            if i == l_nums:
                if len(answ) <= 0 or sum_answ < target: break
                else:
                    sum_answ -= answ.pop(0)
                    continue
        return max(best_len, 0)


# target = 15
target = 7

nums = [2,3,1,2,4,3]

sol = Solution()
ic(sol.minSubArrayLen(target, nums))

