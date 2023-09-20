"""
Type: Medium
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Description:
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""



# Idea: Sort. List with indexes. Von oben nach unten gehen
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        # print(len(height))
        for i in range(0, len(height)):
            for j in range(0, len(height)):
                if i >= j:
                    continue
                if height[i] > height[j]:
                    area = height[j] * (j-i)
                else:
                    area = height[i] * (j-i)
                if area > maxArea:
                    maxArea = area
        return maxArea

if __name__ == '__main__':
    sol = Solution()
    list = [1,8,6,2,5,4,8,3,7]

    print(sol.maxArea(list))

