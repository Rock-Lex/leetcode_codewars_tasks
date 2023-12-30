"""
Type: Medium
55. Jump Game II
https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = farthest
        return ans

# Doesnt work!!!!
class NoSolution:
    def jump(self, nums: List[int]) -> int:
        targetIndex = len(nums) - 1
        numJumps = 0
        currentCapacity = nums[0]
        reachable = nums[0]
        for i in range(1, len(nums)):
            currentCapacity -= 1
            if reachable >= targetIndex:
                return numJumps + 1
            if currentCapacity != max(reachable, i + nums[i]):
                reachable = max(reachable, i + nums[i])
                numJumps += 1
        return numJumps

    def jump2(self, nums: List[int]) -> int:
        targetIndex = len(nums) - 1
        numJumps = 0
        reachable = nums[0]
        for i in range(1, len(nums)):
            if reachable >= targetIndex:
                return numJumps + 1
            if reachable != max(reachable, i + nums[i]):
                reachable = max(reachable, i + nums[i])
                numJumps += 1
        return numJumps

    def jump3(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        targetIndex = len(nums) - 1
        numJumps = 0
        reachable = nums[0]
        endOfJump = nums[0]

        for i in range(len(nums)):
            if reachable >= targetIndex:
                return numJumps + 1
            endOfJump -= 1
            if endOfJump == 0:
                numJumps += 1
                endOfJump = reachable - i
            if reachable != max(reachable, i + nums[i]):
                reachable = max(reachable, i + nums[i])
        return numJumps

    def jump4(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        targetIndex = len(nums) - 1
        numJumps = 0
        reachable = nums[0]
        endOfJump = nums[0]

        for i in range(len(nums)):
            if reachable >= targetIndex:
                return numJumps + 1
            endOfJump -= 1
            if reachable != max(reachable, i + nums[i]):
                reachable = max(reachable, i + nums[i])
                if reachable >= targetIndex:
                    return numJumps + 1
            if endOfJump == 0:
                numJumps += 1
                endOfJump = reachable - i
        return numJumps

    def jump5(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        targetIndex = len(nums) - 1
        numJumps = 0
        reachable = 0
        endOfJump = 1
        counter = 0

        for i in range(len(nums)):
            endOfJump -= 1
            if endOfJump == 0 or reachable != max(reachable, i + nums[i]):
                if max(reachable, i + nums[i]) >= targetIndex or endOfJump == 0:
                    numJumps += 1
                else:
                    counter = reachable

                # numJumps += 1
                reachable = max(reachable, i + nums[i])
                endOfJump = reachable - i
            counter -= 1
            if counter == 0:
                numJumps += 1
            if reachable >= targetIndex:
                break
        return numJumps



# l = [2,3,1,1,4]
# l = [2,3,0,1,4]
# l = [1,2]
# l = [1,2,1,1,1]
l = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
# l = [5,9,3,2,1,0,2,3,3,1,0,0]
# l = [3,4,3,1,0,7,0,3,0,2,0,3]
# l = [9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]
# l = [1,2,3]
# l = [0]

solution = Solution()
print(solution.jump(l))