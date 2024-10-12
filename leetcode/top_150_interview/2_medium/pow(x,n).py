"""
Type: Medium
50. Pow(x, n)
https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List
from icecream import ic


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2

        return result


x = 2.0
n = 2
sol = Solution()
ic(sol.myPow(x, n))