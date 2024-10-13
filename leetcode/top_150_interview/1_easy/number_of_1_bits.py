"""
Type: Easy
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/description/?envType=study-plan-v2&envId=top-interview-150
"""

from icecream import ic
import unittest


class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

        return res


class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        binary_n = format(n, '032b')
        return binary_n.count('1')


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        test_cases = [
            (11, 3),
            (128, 1)
        ]

        for num, expected_output in test_cases:
            self.assertEqual(expected_output, Solution.hammingWeight(n=num))


if __name__ == '__main__':
    unittest.main()
    # Solution.hammingWeight(n=11)