"""
Type: Medium
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic


"""
3. Solution

Different approach.
Left right pointers
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = {}
        best_len = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in sub_string:
                sub_string[s[right]] = s[right]
                best_len = max(best_len, len(sub_string))
            else:
                while s[right] in sub_string:
                    sub_string.pop(s[left])
                    left += 1
                sub_string[s[right]] = s[right]
        return best_len


"""
2. Solution

Optimized Fist Solution. Replace list with dict. Element search O(1)
"""
class BadSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = {}
        best_len = 0
        for index in range(len(s)):
            for el in s[index:]:
                if sub_string.get(el, None) is not None:
                    sub_string = {}
                    break
                sub_string[el] = el
                best_len = max(best_len, len(sub_string))
        return best_len


"""
1. Solution

O(n^2)
"""
class BadSolution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = []
        best_len = 0
        for index in range(len(s)):
            for el in s[index:]:
                if el in sub_string:
                    sub_string = []
                    break
                sub_string.append(el)
                best_len = max(best_len, len(sub_string))
        return best_len


s = "abcabcbb"

sol = Solution()
ic(sol.lengthOfLongestSubstring(s))
