"""
Type: Medium
172. Factorial trailing zeros
https://leetcode.com/problems/factorial-trailing-zeroes/description/
"""

from icecream import ic


class SolutionEfficient:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        i = 5
        while i <= n:
            fives += n // i
            i *= 5
        return fives


class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return n * factorial(n-1)

        n = factorial(n)
        ic(n)
        counter = 0
        while n % 10 == 0:
            n //= 10
            counter += 1

        return counter




n = 30
sol = Solution()
ic(sol.trailingZeroes(n))