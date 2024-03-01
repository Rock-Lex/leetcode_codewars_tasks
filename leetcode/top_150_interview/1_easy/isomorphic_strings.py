"""
Type: Easy
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translation = {}
        for index in range(len(s)):
            if s[index] not in translation and t[index] not in translation.values():
                translation[s[index]] = t[index]
                continue
            elif s[index] in translation and translation[s[index]] == t[index]:
                continue
            return False
        return True


if __name__ == '__main__':
    s = "foo"
    t = "bar"
    sol = Solution()
    print(sol.isIsomorphic(s, t))