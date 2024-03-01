"""
Type: Medium
15. 3Sum
https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                if sum_of_three > 0:
                    right -= 1
                elif sum_of_three < 0:
                    left += 1
                else:
                    answer.add((nums[i], nums[left], nums[right]))
                    right -= 1
                    left += 1
        return list(answer)


if __name__ == '__main__':
    # numbers = [-1,0,1,2,-1,-4]
    numbers = [-1,0,1]
    sol = Solution()
    print(sol.threeSum(numbers))