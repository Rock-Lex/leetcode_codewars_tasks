"""
Type: Easy
383. Ransom Note
https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        vocabulary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        return sum(map(lambda x: vocabulary[x], s))


class WOWSolution:
    def romanToInt(self, s: str) -> int:
        vocabulary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        answer = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for symbol in s:
            answer += vocabulary[symbol]
        return answer


class OKSolution:
    def romanToInt(self, s: str) -> int:
        vocabulary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = 0

        for i in range(len(s)):
            if i < len(s) - 1 and vocabulary[s[i]] < vocabulary[s[i + 1]]:
                answer -= vocabulary[s[i]]
            else:
                answer += vocabulary[s[i]]

        return answer


class BadSolution:
    def romanToInt(self, s: str) -> int:
        vocabulary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = 0
        jump = False
        for index, symbol in enumerate(s):
            if jump:
                jump = False
                continue
            if index != len(s) - 1:
                if symbol == "I":
                    if s[index+1] == "V":
                        jump = True
                        answer += 4
                        continue
                    if s[index+1] == "X":
                        jump = True
                        answer += 9
                        continue

                if symbol == "X":
                    if s[index+1] == "L":
                        jump = True
                        answer += 40
                        continue
                    if s[index+1] == "C":
                        jump = True
                        answer += 90
                        continue

                if symbol == "C":
                    if s[index + 1] == "D":
                        jump = True
                        answer += 400
                        continue
                    if s[index + 1] == "M":
                        jump = True
                        answer += 900
                        continue
            answer += vocabulary[symbol]

        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("IV"))
