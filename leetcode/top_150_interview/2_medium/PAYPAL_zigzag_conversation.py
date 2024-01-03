"""
Type: Medium
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/submissions/865832924/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

My solution:
Runtime: 77ms (Beats 75.54%)
Memory: 14Mb (Beats 76.16%)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        list = []
        for i in range(numRows):
            list.append("")
        trans = numRows
        index = 0

        for i in s:
            #  Fill the vertical line
            if index % (numRows + (numRows - 2)) == 0 or index == 0:
                ind = index
                for j in range(numRows):
                    if ind > len(s) - 1:
                        continue
                    list[j] += s[ind]
                    ind += 1

            #  Fill the transition line
            elif index == trans:
                pos = numRows - 2
                ind = index
                for j in range(numRows - 2):
                    if ind > len(s) - 1:
                        continue
                    list[pos] += s[ind]
                    # Add Spaces
                    # strInd = 0
                    # for string in list:
                    #     if strInd != pos:
                    #         list[strInd] += " "
                    #     strInd += 1
                    pos -= 1
                    ind += 1
                trans += numRows + numRows - 2
            index += 1

        result = ""
        for el in list:
            result += el

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
    # print(sol.convert("PAYPALISHIRING", 4))
    # print(sol.convert("ABCDE", 4))
    # print(sol.convert("ABCDE", 1))
