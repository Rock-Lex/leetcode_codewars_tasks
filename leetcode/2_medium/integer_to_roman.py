<<<<<<< HEAD:leetcode/medium/integer_to_roman.py
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

=======
"""
Type: Medium
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        zif = num % 10
        des = 0
        sot = 0
        tis = 0
        dict = {'1': "I", '5':"V", '10': "X", '50':"L", '100':"C", '500':"D", '1000':"M"}
        answ = ""

        num = int(num / 10)
        if(num >= 1):
            des = num % 10
            num = int(num / 10)
            if (num >= 1):
                sot = num % 10
                num = int(num / 10)
                if (num >= 1):
                    tis = num % 10

        # Desyatki

        # if des







        # Zifri
        if 3 >= zif >= 0:
            for i in range (1, zif + 1):
                answ += (dict['1'])
        if zif == 4:
            answ += dict['1'] + dict['5']
        if 9 > zif >= 5:
            answ += dict['5']
            for i in range (1, zif - 5 + 1):
                answ += dict['1']
        if zif == 9:
            answ += dict['1'] + dict['10']



        return answ


if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(9))

>>>>>>> 04661a3c12b184bbebebb63fcd9e25b5899abbb5:leetcode/2_medium/integer_to_roman.py
