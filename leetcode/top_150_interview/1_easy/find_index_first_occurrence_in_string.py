"""
Type: Easy
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1

        occurrence_index = -1
        is_occurrence = False
        for i, el in enumerate(haystack):
            index = i
            for j, char in enumerate(needle):
                if char != haystack[index]:
                    break
                elif j == len(needle) - 1:
                    is_occurrence = True
                index += 1
                if index == len(haystack): break
            if is_occurrence:
                occurrence_index = i
                break
        return occurrence_index


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issipi"
    sol = Solution()
    print(sol.strStr(haystack, needle))
