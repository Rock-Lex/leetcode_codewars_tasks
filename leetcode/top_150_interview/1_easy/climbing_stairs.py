"""
Type: Easy
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150
"""
from icecream import ic


"""
Space optimization for Tabulation
"""
class Solution4:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr


"""
Tabulation
"""
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


"""
Recursion with Memoization
"""
class Solution2:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]

"""
Recursion
(Slow): O(2^n)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


n = 4
"""
1. 2 2
2. 1 1 1 1
3. 2 1 1
4. 1 1 2
5. 1 2 1
"""
sol = Solution2()
ic(sol.climbStairs(n))