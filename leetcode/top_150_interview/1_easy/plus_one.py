"""
Type: Easy
66. Plus One
https://leetcode.com/problems/plus-one/submissions/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        while index != -1:
            if digits[index] != 9:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
                index -= 1
        return [1] + digits


if __name__ == "__main__":
    sol = Solution()
    digits = [4, 3, 2, 1]
    print(sol.plusOne(digits))