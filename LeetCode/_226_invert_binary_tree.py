# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        def traverse(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return root
