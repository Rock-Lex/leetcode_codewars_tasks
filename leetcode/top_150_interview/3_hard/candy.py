"""
Type: Hard
135. Candy
https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1: return 1
        candy = [1] * len(ratings)

        for i in range(0, len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candy[i + 1] = candy[i] + 1
        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
                candy[i - 1] = candy[i] + 1

        return sum(candy)


if __name__ == '__main__':
    sol = Solution()
    ratings = [1,2,87,87,87,2,1]
    ratings2 = [1,3,4,5,2]
    ratings3 = [1,6,10,8,7,3,2]

    print(sol.candy(ratings3))