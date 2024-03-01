"""
Type: Easy
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 1:
            return s in t
        is_subsequence = False
        s_indexes = range(len(s))
        s_index = 0
        for char in t:
            if char == s[s_index]:
                s_index += 1
                if s_index == s_indexes[-1] + 1:
                    return True
        return is_subsequence


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    sol = Solution()
    print(sol.isSubsequence(s, t))