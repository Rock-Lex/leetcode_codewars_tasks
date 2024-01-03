"""
Type: Medium
274. H-Index
https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for index, citation in enumerate(citations):
            if index >= citation:
                return index
        return len(citations)


if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([3,0,6,1,5]))

