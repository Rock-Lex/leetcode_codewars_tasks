"""
Type: Medium
274. H-Index
https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxCitations = max(c)
        hIndex = citations[0]


c = [3,0,6,1,5]
solution = Solution()
print(solution.hIndex(c))