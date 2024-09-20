"""
Type: Easy
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150
"""

from copy import copy
from typing import List, Optional

from icecream import ic


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deep_first_search(root_left: Optional[TreeNode], root_right: Optional[TreeNode]) -> bool:
    if not root_left and not root_right:
        return True
    elif not root_left or not root_right:
        return False
    return root_left.val == root_right.val and deep_first_search(root_left.left, root_right.right) and deep_first_search(root_left.right, root_right.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return deep_first_search(root.left, root.right)


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
sol = Solution()
ic(sol.isSymmetric(root))