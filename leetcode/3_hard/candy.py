"""
Type: Hard
135. Candy
https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1: return 1
        candys = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if i == 0:
                if ratings[i + 1] > ratings[i]:
                    candys[i + 1] += 1
                elif ratings[i + 1] < ratings[i]:
                     candys[i] += 1
            else:
                if ratings[i + 1] > ratings[i]:
                    candys[i + 1] = candys[i] + 1
        return sum(candys)
# 5
# l = [1,0,2]
# 4
l = [1,2,2]

# solution = Solution()
# print(solution.candy(l))

n = 10
for i in range(n-2,-1,-1):
    print(i)