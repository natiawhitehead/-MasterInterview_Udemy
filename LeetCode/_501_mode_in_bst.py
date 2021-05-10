# Given the root of a binary search tree(BST) with duplicates, return all the mode(s)(i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        answer = []
        counter = 1
        maxCount = 0
        prevValue = None

        def traverse(node):
            nonlocal counter
            nonlocal prevValue
            nonlocal answer
            nonlocal maxCount
            if node:
                traverse(node.left)
                if prevValue is not None:
                    if node.val == prevValue:
                        counter += 1
                    else:
                        counter = 1
                if counter > maxCount:
                    maxCount = counter
                    answer = [node.val]
                elif counter == maxCount:
                    answer.append(node.val)
                prevValue = node.val
                traverse(node.right)
        traverse(root)
        return answer
