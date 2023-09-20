"""
Type: Medium
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

My solution
Runtime: 58 ms (56.72%)
Memory Usage: 13.4 MB (93.65%)
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        answ = ListNode()
        list = []

        while l1.val is not None or l2.val is not None:
            if l1.val is None and l2.val is not None:
                num = l2.val
            elif l2.val is None and l1.val is not None:
                num = l1.val
            else:
                num = l1.val + l2.val

            if l1.next is None and l2.next is None:
                if num >= 10:
                    list.append(num % 10)
                    list.append(1)
                else:
                    list.append(num)
                break

            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = 0

            if num >= 10:
                list.append(num % 10)
                l1.val += 1
            else:
                list.append(num)

        print(list)
        count = 0
        answ = ListNode()
        for el in list:
            if count == 0:
                count += 1
                l1.val = el
                answ = l1
                continue
            else:
                if l1.next is not None:
                    l1 = l1.next
                    l1.val = el
                else:
                    l1.next = ListNode(val=el)
                    l1 = l1.next
        return answ


def main():
    solution = Solution()

    l1 = ListNode()
    l12 = ListNode()
    l13 = ListNode()
    l14 = ListNode()
    l2 = ListNode()
    l21 = ListNode()
    l22 = ListNode()

    l1.val = 2
    l12.val = 4
    l13.val = 3
    l14.val = 8

    l2.val = 5
    l21.val = 6
    # l22.val = 6

    l1.next = l12
    l12.next = l13
    l13.next = l14
    l2.next = l21
    # l21.next = l22

    # l1.val = 0
    # l2.val = 0

    answ = solution.addTwoNumbers(l1, l2)

    while True:
        print(answ.val)
        if answ.next is None:
            break
        answ = answ.next



if __name__ == "__main__":
    main()
