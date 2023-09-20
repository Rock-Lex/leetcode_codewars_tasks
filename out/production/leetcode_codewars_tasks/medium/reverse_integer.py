"""
Type: Medium
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Description:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            num = int(str(x)[::-1])
            if num <= -2**31 or num >= 2**31 - 1:
                return 0
            return num
        num = int("-" + str(x)[1:][::-1])
        if num <= -2**31 or num >= 2**31 - 1:
            return 0
        return num


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(-1534236469))

