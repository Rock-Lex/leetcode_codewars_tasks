"""
Type: Easy
342. Power of Four
https://leetcode.com/problems/power-of-four/
"""

import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 and (math.log(n, 4) - int(math.log(n, 4)) == 0 or n == 1): return True
        return False


num = 8
# num = 16
# num = -16

solution = Solution()
print(solution.isPowerOfFour(num))
