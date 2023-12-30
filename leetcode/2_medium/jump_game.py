"""
Type: Medium
55. Jump Game
https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class FirstSolution:
    def canJump(self, nums: List[int]) -> bool:
        currCapacity = nums[0]
        for i in range(1, len(nums)):
            if currCapacity == 0:
                return False
            currCapacity -= 1
            currCapacity = max(currCapacity, nums[i])
        return True


class SecondSolution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i+nums[i])

        return True


# l = [2,3,1,1,4]
# l = [3,2,1,0,4]
l = [0]

solution = FirstSolution()
print(solution.canJump(l))