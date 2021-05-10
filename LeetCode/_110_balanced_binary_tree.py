# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                leftHeight = left[1] + 1
                rightHeight = right[1] + 1
                return (left[0] and right[0] and abs(leftHeight-rightHeight) <= 1, max(leftHeight, rightHeight))
            else:
                return (True, 0)
        return dfs(root)[0]
