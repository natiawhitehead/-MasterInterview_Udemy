# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer
            if node:
                left = dfs(node.left) + 1
                right = dfs(node.right) + 1
                answer = max(answer, left + right)
                return max(left, right)
            else:
                return -1
        dfs(root)
        return answer
