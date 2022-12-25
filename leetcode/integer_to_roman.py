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

