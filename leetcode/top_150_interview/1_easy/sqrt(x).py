"""
Type: Easy
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
"""
from icecream import ic


"""
Binary Search approach
Time complexity: O(log n)
Space complexity: O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid

        return right


x = 9
sol = Solution()
ic(sol.mySqrt(x))
