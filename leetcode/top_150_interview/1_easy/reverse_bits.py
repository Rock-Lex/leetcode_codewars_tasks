"""
Type: Easy
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List, Optional
from icecream import ic


class MechanicSolution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


class Solution:
    def reverseBits(self, n: int) -> int:
        binary_n = format(n, '032b')
        str_n = str(binary_n)[::-1]
        return int(str_n, 2)


n = 43261596
sol = Solution()
ic(sol.reverseBits(n))