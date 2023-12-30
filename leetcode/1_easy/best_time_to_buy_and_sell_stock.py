"""
Type: Easy
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
"""

from copy import copy
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for el in prices[1:]:
            if el < minPrice:
                minPrice = el
            if el - minPrice > maxProfit:
                maxProfit = el - minPrice
        return maxProfit


class NoSolution:
    def maxProfit(self, prices: List[int]) -> int:
        sortedPrices = copy(prices)
        sortedPrices.sort()
        return self.comparePrices(prices, sortedPrices)

    def comparePrices(self, prices, sortedPrices):
        minIndex = prices.index(sortedPrices[0])
        maxIndex = prices.index(sortedPrices[len(sortedPrices) - 1])
        if maxIndex > minIndex: return sortedPrices[len(sortedPrices) - 1] - sortedPrices[0]
        elif maxIndex == minIndex: return 0
        else:
            try:
                a = sortedPrices[len(sortedPrices) - 1]
                b = sortedPrices[len(sortedPrices) - 2]
            except Exception as e:
                return 0
            if sortedPrices[1] - sortedPrices[0] < sortedPrices[len(sortedPrices) - 1] - sortedPrices[len(sortedPrices) - 2]:
                return self.comparePrices(prices, sortedPrices[:-1])
            else:
                return self.comparePrices(prices, sortedPrices[1:])



l = [7, 1, 5, 3, 6, 4]
# l = [7,6,4,3,1]
# l = [1, 2, 3, 4, 5, 6]

solution = Solution()
print(solution.maxProfit(l))
