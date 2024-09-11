"""
Type: Hard
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List
from icecream import ic



class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign_value = 1
        result = 0
        operations_stack = []

        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c in "+-":
                result += number * sign_value
                sign_value = -1 if c == '-' else 1
                number = 0
            elif c == '(':
                operations_stack.append(result)
                operations_stack.append(sign_value)
                result = 0
                sign_value = 1
            elif c == ')':
                result += sign_value * number
                result *= operations_stack.pop()
                result += operations_stack.pop()
                number = 0

        return result + number * sign_value


s = "(1+(4+5+2)-3)+(6+8)"
s = "2147483647"
s = "-2+ 1"
s = "1-(     -2)"
s = "1-11"
s = "- (3 + (4 + 5))"
sol = Solution()

ic(sol.calculate(s))
