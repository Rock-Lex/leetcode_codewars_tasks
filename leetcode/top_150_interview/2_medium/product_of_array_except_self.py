"""
Type: Medium
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j = len(nums) - 1
        answear = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            answear[i] *= pre
            pre *= nums[i]
            answear[j] *= post
            post *= nums[j]
            j -= 1
        return answear


# l = [1,2,3,4]
l = [-1,1,0,-3,3]

solution = Solution()
print(solution.productExceptSelf(l))
