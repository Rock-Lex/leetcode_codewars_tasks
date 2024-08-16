"""
Type: Easy
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import Optional
from icecream import ic


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_i = ListNode(0)
        head_t = head_i
        while list1 or list2:
            if list1 == None:
                while list2:
                    head_t.next = ListNode(list2.val)
                    head_t = head_t.next
                    list2 = list2.next
                break
            if list2 == None:
                while list1:
                    head_t.next = ListNode(list1.val)
                    head_t = head_t.next
                    list1 = list1.next
                break
            if list1.val < list2.val:
                head_t.next = ListNode(list1.val)
                head_t = head_t.next
                list1 = list1.next
            else:
                head_t.next = ListNode(list2.val)
                head_t = head_t.next
                list2 = list2.next
        return head_i.next


l1 = ListNode(1)
l12 = l1.next = ListNode(2)
l13 = l12.next = ListNode(4)

l2 = ListNode(1)
l22 = l2.next = ListNode(3)
l23 = l22.next = ListNode(4)

sol = Solution()
head = sol.mergeTwoLists(l1, l2)

while head:
    ic(head.val)
    head = head.next
