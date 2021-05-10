# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and 
# node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def isSubtree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and isSubtree(node1.left, node2.left) and isSubtree(node1.right, node2.right)

        def findSubtree(node):
            if node:
                if node.val == subRoot.val:
                    isSub = isSubtree(node, subRoot)
                    if isSub:
                        return True
                left = findSubtree(node.left)
                right = findSubtree(node.right)
                return left or right
            return False

        return findSubtree(root)
