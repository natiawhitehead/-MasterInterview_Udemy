# Given the root of a binary tree, check whether it is a mirror of itself(i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False
            return leftNode.val == rightNode.val and dfs(leftNode.right, rightNode.left) and dfs(leftNode.left, rightNode.right)

        return dfs(root.left, root.right)
