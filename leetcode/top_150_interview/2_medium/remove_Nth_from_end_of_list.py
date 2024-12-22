"""
Type: Medium
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_counter = self.len_of_nodes(head)

        if n == 1 and 1 == nodes_counter:
            return None
        if n == nodes_counter:
            head = head.next
            return head

        cur = head
        for _ in range(nodes_counter - n - 1):
            cur = cur.next

        cur.next = cur.next.next

        return head

    def len_of_nodes(self, head):
        nodes_counter = 1
        while head.next:
            head = head.next
            nodes_counter += 1
        return nodes_counter


sol = Solution()
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6))))))
print(sol.reverseBetween(head, 2, 5))