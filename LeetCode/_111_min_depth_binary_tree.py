# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if node:
                if node.left and node.right:
                    left = dfs(node.left)
                    right = dfs(node.right)
                    return min(left, right) + 1
                if not node.left and not node.right:
                    return 1
                if not node.left:
                    return dfs(node.right) + 1
                if not node.right:
                    return dfs(node.left) + 1
            else:
                return 0
        return dfs(root)
