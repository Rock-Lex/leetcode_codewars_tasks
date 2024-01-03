"""
Type: Easy
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []
        opening_brackets = ["(", "{", "["]
        closing_brackets = [")", "}", "]"]

        #     First Method
        for char in s:
            if opening_brackets.count(char) != 0:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    el = stack.pop()
                    if opening_brackets.count(el) != 0 and opening_brackets.index(el) == closing_brackets.index(char):
                        continue
                    else:
                        return False

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    task = "(("
    print(sol.isValid(s=task))
