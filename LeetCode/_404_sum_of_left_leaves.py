# Given the root of a binary tree, return the sum of all left leaves.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.answer = 0

        def traverse(node, cameFromLeft):
            if node:
                if not node.left and not node.right and cameFromLeft:
                    self.answer += node.val
                traverse(node.left, True)
                traverse(node.right, False)
        traverse(root, False)
        return self.answer
