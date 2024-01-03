"""
Type: Medium
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        vocabulary = {'1000': "M", '900': 'CM', '500': "D", '400': "CD", '100': "C", '90': "XC", '50': "L", '40': "XL",
                      '10': "X", '9': "IX", '5': "V", '4': "IV", '1': "I"}
        roman_num = ""

        for key, value in vocabulary.items():
            while num >= int(key):
                num -= int(key)
                roman_num += value

        return roman_num


if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(1994))

