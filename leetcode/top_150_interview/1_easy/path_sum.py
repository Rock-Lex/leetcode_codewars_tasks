"""
Type: Easy
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
"""

from copy import copy
from typing import List, Optional

from icecream import ic


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deep_first_search(root: TreeNode, current_sum, target_sum) -> bool:
    if root is None:
        return False
    elif root.left is None and root.right is None:
        return current_sum + root.val == target_sum
    else:
        return (deep_first_search(root.left, current_sum + root.val, target_sum)
                or deep_first_search(root.right, current_sum + root.val, target_sum))


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return deep_first_search(root, 0, targetSum) if root else False


target_sum = 22
root = TreeNode(5,
                TreeNode(4,
                         TreeNode(11,
                                  TreeNode(7),
                                  TreeNode(2))),
                TreeNode(8,
                         TreeNode(13),
                         TreeNode(4,
                                  None,
                                  TreeNode(1))))
sol = Solution()
ic(sol.hasPathSum(root, target_sum))