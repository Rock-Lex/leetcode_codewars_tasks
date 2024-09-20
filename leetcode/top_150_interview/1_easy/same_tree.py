"""
Type: Easy
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
"""

from copy import copy
from typing import List, Optional

from icecream import ic


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deep_first_search(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val == q.val:
        return deep_first_search(p.left, q.left) and deep_first_search(p.right, q.right)
    return False


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return deep_first_search(p, q)



root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
ic(sol.isSameTree(root1, root2))
