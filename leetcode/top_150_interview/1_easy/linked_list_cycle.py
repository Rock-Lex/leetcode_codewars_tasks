"""
Type: Easy
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import Optional

from icecream import ic


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
(Floyd's Cycle Detection) Solution
2x Faster as the first one
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False


"""
O(n) Solution
"""
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        cache = []
        cache.append(head)
        while 1:
            if head.next == None:
                break
            head = head.next

            if head in cache:
                return True
            else:
                cache.append(head)

        return False


head = ListNode(10)

head2 = head.next = ListNode(15)
head3 = head2.next = ListNode(7)
head4 = head3.next = head

sol = Solution()
ic(sol.hasCycle(head))