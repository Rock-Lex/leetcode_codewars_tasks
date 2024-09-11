"""
Type: Medium
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150
"""
import math
from typing import List
from icecream import ic


class Solution:
    class Solution:
        def evalRPN(self, tokens: List[str]) -> int:
            tokens_stack = []
            for el in tokens:
                match el:
                    case "+":
                        second = tokens_stack.pop()
                        first = tokens_stack.pop()
                        res = first + second
                        tokens_stack.append(res)
                    case "-":
                        second = tokens_stack.pop()
                        first = tokens_stack.pop()
                        res = first - second
                        tokens_stack.append(res)
                    case "*":
                        second = tokens_stack.pop()
                        first = tokens_stack.pop()
                        res = first * second
                        tokens_stack.append(res)
                    case "/":
                        second = tokens_stack.pop()
                        first = tokens_stack.pop()
                        res = first / second
                        res = math.floor(res) if res > 0 else math.ceil(res)
                        tokens_stack.append(res)
                    case _:
                        tokens_stack.append(int(el))
            return tokens_stack.pop()


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["4","13","5","/","+"]
sol = Solution()
ic(sol.evalRPN(tokens))
