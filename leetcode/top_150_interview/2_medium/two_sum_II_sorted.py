"""
Type: Medium
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while 1:
            sum = numbers[left] + numbers[right]
            if sum == target:
                break
            if sum < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]


class Solution2:
    def twoSum2(self, numbers, target):
        dict = {}
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target - num] + 1, i + 1]
            dict[num] = i


class BadSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            try:
                if target - value in numbers[index + 1:]:
                    index2 = numbers[index + 1:].index(target - value)
                    return [index + 1, index2 + len(numbers[:index + 1]) + 1]
            except Exception:
                continue


class VeryBadSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index_i, value_i in enumerate(numbers):
            for index_j, value_j in enumerate(numbers[index_i + 1:]):
                if value_i + value_j == target:
                    return [index_i + 1, index_j + len(numbers[:index_i + 1]) + 1]


if __name__ == '__main__':
    numbers = [0,0,3,4]
    target = 0
    sol = Solution()
    print(sol.twoSum(numbers, target))