"""
Type: Easy
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        if len(strX) % 2 == 0:
            return strX[:int(len(strX)/2)] == strX[int(len(strX)/2):][::-1]
        else:
            return strX[:int(len(strX)/2)] == strX[int(len(strX)/2) + 1:][::-1]

x = 11
strX = str(x)
a = strX[: int(len(strX)/2)]
b = strX[int(len(strX)/2)::][::-1]
print(a, b)
solutiom = Solution()
print(solutiom.isPalindrome(x))

# strX = "12521"
# a = strX[:int(len(strX)/2)]
# b = strX[int(len(strX)/2) + 1:][::-1]
# print(a, b)
# print(a == b)
