"""
Type: Medium
61. Rotate List
https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        list_len = self.len_of_nodes(head)
        k = k % list_len

        head = self.rotate(head, k, list_len)

        return head

    def rotate(self, head, k, l):
        if k == 0:
            return head
        cur = head
        for _ in range(l - k - 1):
            cur = cur.next

        end = cur
        cur = cur.next
        new_head = ListNode(cur.val)
        new_dummy = new_head

        for _ in range(k - 1):
            cur = cur.next
            new_dummy.next = ListNode(cur.val)
            new_dummy = new_dummy.next

        end.next = None
        new_dummy.next = head

        return new_head

    def len_of_nodes(self, head):
        nodes_counter = 1
        while head.next:
            head = head.next
            nodes_counter += 1
        return nodes_counter


class SlowSolution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        list_len = self.len_of_nodes(head)
        k = k % list_len

        for _ in range(k):
            head = self.rotate(head)

        return head

    def rotate(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        while head.next is not None and head.next.next is not None:
            head = head.next
        dummy.val = head.next.val
        head.next = None
        return dummy

    def len_of_nodes(self, head):
        nodes_counter = 1
        while head.next:
            head = head.next
            nodes_counter += 1
        return nodes_counter