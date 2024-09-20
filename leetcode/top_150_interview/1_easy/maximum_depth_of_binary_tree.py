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


def deep_first_search(root, deep):
    if root is None:
        return deep
    elif root.left is None and root.right is None:
        return deep + 1
    else:
        return max(deep_first_search(root.right, deep + 1), deep_first_search(root.left, deep + 1))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return deep_first_search(root, 0)


# root = [3, 9, 20, None, None, 15, 7]
root = TreeNode(3,  TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()
ic(sol.maxDepth(root))
