"""
Type: Easy
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        shortest_length = len(min(strs, key=len))
        longest_prefix = ""
        compare_char = ""
        for index_char in range(shortest_length):
            for i, el in enumerate(strs):
                if i == 0:
                    compare_char = el[index_char]
                    continue
                if compare_char == el[index_char]:
                    if i == len(strs) - 1:
                        longest_prefix += compare_char
                else:
                    break
            if index_char == len(longest_prefix): return longest_prefix
        return longest_prefix


if __name__ == '__main__':
    sol = Solution()
    strs = ["cir","car"]

    ic(sol.longestCommonPrefix(strs))