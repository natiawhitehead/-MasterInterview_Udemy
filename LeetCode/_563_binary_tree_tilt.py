# Given the root of a binary tree, return the sum of every tree node's tilt.

# The tilt of a tree node is the absolute difference between the sum of all left subtree node values 
# and all right subtree node values. If a node does not have a left child, then the sum of the left 
# subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.answer = 0

        def traverse(node):
            if node:
                if not node.left and not node.right: #for leaf nodes, sum of subtrees are 0  so it doesn't affect the answer
                    return node.val
                else:
                    left = traverse(node.left)
                    right = traverse(node.right)
                    self.answer += abs(left - right)
                    return left + right + node.val
            else:
                return 0
        traverse(root)
        return self.answer
