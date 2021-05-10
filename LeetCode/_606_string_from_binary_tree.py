# Given the root of a binary tree, construct a string consists of parenthesis and integers from a binary tree with 
# the preorder traversing way, and return it.

# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between 
# the string and the original binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        answer = []

        def traverse(node):
            if node:
                answer.append(str(node.val))
                if not node.left and not node.right:
                    return
                answer.append("(")
                traverse(node.left)
                answer.append(")")
                if node.right:
                    answer.append("(")
                    traverse(node.right)
                    answer.append(")")
        traverse(root)
        answerString = "".join(answer)
        return answerString
