"""
Type: Medium
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left != right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    height = [2,3,4,5,18,17,6]
    sol = Solution()
    print(sol.maxArea(height))