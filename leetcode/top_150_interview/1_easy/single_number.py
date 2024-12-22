"""
Type: Easy
136. Single Number
https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150
"""

from collections import deque
from typing import Optional


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answ = 0
        switch = True
        for el in sorted(nums):
            if switch:
                answ += el
                switch = False
                continue
            answ -= el
            switch = True

        return answ