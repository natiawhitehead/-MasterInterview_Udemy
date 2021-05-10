# Given the root of a Binary Search Tree(BST), 
# return the minimum difference between the values of any two different nodes in the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        answer = 100000000
        self.prevValue = -100000000

        def traverse(node):
            nonlocal answer
            if node:
                traverse(node.left)
                answer = min(answer, node.val - self.prevValue)
                self.prevValue = node.val
                traverse(node.right)
        traverse(root)
        return answer
