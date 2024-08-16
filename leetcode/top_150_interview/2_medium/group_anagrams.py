"""
Type: Medium
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        groups_order = {}
        for el in strs:
            sorted_str = ''.join(sorted(el))
            group_el = groups_order.get(sorted_str, None)

            if group_el is None:
                groups_order[sorted_str] = [el]
            else:
                group_el.append(el)
                groups_order[sorted_str] = group_el

        for value in groups_order.values():
            groups.append(value)

        return groups


strs = ["eat","tea","tan","ate","nat","bat"]

sol = Solution()
ic(sol.groupAnagrams(strs))
