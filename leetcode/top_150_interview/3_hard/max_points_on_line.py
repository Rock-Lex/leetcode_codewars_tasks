"""
Type: Hard
149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150
"""

from icecream import ic
from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    @staticmethod
    def maxPoints(points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        def normalize_slope(dx, dy):
            if dx == 0:
                return float('inf'), 0
            if dy == 0:
                return 0, 0
            g = gcd(dy, dx)
            if dx < 0:
                dx, dy = -dx, -dy
            return (dy // g, dx // g)

        max_points = 0

        for i in range(len(points)):
            slope_count = defaultdict(int)
            current_max = 0

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                slope = normalize_slope(dx, dy)
                slope_count[slope] += 1
                current_max = max(current_max, slope_count[slope])

            max_points = max(max_points, current_max + 1)

        return max_points


import unittest


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        test_cases = [
            ([[1,1],[2,2],[3,3]], 3),
            ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4)
        ]

        for points, expected_output in test_cases:
            self.assertEqual(expected_output, Solution.maxPoints(points=points))


if __name__ == '__main__':
    unittest.main()