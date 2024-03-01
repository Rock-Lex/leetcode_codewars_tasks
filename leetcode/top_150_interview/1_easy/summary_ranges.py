"""
Type: Easy
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answ = []
        temp_str = ""
        started = False
        for i in range(0, len(nums)):
            if i + 1 == len(nums):
                if started:
                    temp_str += f"->{nums[i]}"
                    answ.append(temp_str)
                    break
                else:
                    answ.append(str(nums[i]))
                    break
            if nums[i] + 1 == nums[i + 1]:
                if not started:
                    temp_str = str(nums[i])
                    started = True
                else:
                    continue
            else:
                if started:
                    started = False
                    temp_str += f"->{nums[i]}"
                    answ.append(temp_str)
                else:
                    answ.append(str(nums[i]))

        return answ


nums = [0,1,2,4,5,7]

sol = Solution()
ic(sol.summaryRanges(nums))


