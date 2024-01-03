"""
Type: Medium
134. Gas Station
https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        gas_tank, start_index = 0, 0

        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]

            if gas_tank < 0:
                start_index = i + 1
                gas_tank = 0

        return start_index


class ToSlowSolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if self.startTravel(i, gas, cost):
                    return i
                else:
                    continue
        return -1

    def startTravel(self, i, gas, cost):
        stations = [*range(i, len(gas))] + [*range(0, i)] + [i]
        tank = 0
        for i in stations:
            if gas[i] + tank < cost[i]:
                return False
            tank += gas[i]
            tank -= cost[i]
        return True

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

# gas = [2,3,4]
# cost = [3,4,3]

solution = Solution()
print(solution.canCompleteCircuit(gas, cost))
