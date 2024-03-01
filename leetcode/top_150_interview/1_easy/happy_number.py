"""
Type: Easy
202. Happy Number
https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        num_dict = {}
        while num != 1:
            digits = list(map(int, str(num)))
            num = 0
            for digit in digits:
                num += digit ** 2
            if num_dict.get(num) is not None: return False
            num_dict[num] = num
        return True


"""
    Tortoise hare technique
"""
class Solution2:
    def isHappy(self, n: int) -> bool:
        # 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow != fast and fast != 1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast == 1

    def squared(self, n):
        result = 0
        while n > 0:
            last = n % 10
            result += last * last
            n = n // 10
        return result


if __name__ == '__main__':
    n = 2
    sol = Solution()
    print(sol.isHappy(n))
