"""
Type: Medium
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next
        return dummy.next

"""
Solution for delete duplicates but leave one element 
"""
class Solution_else:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        if head.next == None:
            return head
        while 1:
            if dummy.next.val == dummy.val:
                cur = dummy
                while 1:
                    cur = cur.next
                    if cur.next == None:
                        dummy.next = None
                        break
                    elif cur.next.val != cur.val:
                        dummy.next = cur.next
                        break
            if dummy.next is not None and dummy.next.next is not None:
                dummy = dummy.next
            else:
                break
        return head


sol = Solution()
head = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=3))))))
print(sol.deleteDuplicates(head))


"""

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        prev = None
        if head.next == None:
            return head
        while 1:
            if dummy.next.val == dummy.val:
                cur = dummy
                while 1:
                    if cur.next == None:
                        if prev is not None:
                            prev.next = None
                            return head
                        else:
                            return None
                    elif cur.next.val != cur.val:
                        if prev is not None:
                            prev.next = None
                        else:
                            head = cur.next
                            dummy = head
                        break
                    cur = cur.next

            if dummy.next is not None and dummy.next.next is not None:
                prev = dummy
                dummy = dummy.next
            else:
                return head
                    
"""


