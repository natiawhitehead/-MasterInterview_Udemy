# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def traverse(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            left = traverse(node.left, val)
            right = traverse(node.right, val)
            return left and right
        return traverse(root, root.val)
