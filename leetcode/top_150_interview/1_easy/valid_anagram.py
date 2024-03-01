"""
Type: Easy
242. Valid Anagram

https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_vocabulary = {}
        t_vocabulary = {}

        for i in range(len(s)):
            s_vocabulary[s[i]] = s_vocabulary.get(s[i], 0) + 1
            t_vocabulary[t[i]] = t_vocabulary.get(t[i], 0) + 1

        return s_vocabulary == t_vocabulary


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))