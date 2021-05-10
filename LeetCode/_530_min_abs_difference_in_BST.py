# Given the root of a Binary Search Tree(BST), return the minimum absolute difference between the values of any 
# two different nodes in the tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        sortedArray = []

        def traverse(node):
            if node:
                traverse(node.left)
                sortedArray.append(node.val)
                traverse(node.right)
        traverse(root)
        answer = 100000000
        for i in range(len(sortedArray)-1):
            answer = min(answer, abs(sortedArray[i] - sortedArray[i+1]))
        return answer
