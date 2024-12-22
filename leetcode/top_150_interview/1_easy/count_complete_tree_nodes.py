"""
Type: Easy
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
DFS
"""
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

"""
BFS
"""

class Soution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])  # Initialize the queue with the root node
        count = 0  # Node counter

        while queue:
            node = queue.popleft()  # Remove the front node from the queue
            count += 1  # Increment the count for the current node

            # Add the left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return count

