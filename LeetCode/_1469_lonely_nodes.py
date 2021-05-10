# In a binary tree, a lonely node is a node that is the only child of its parent node. 
# The root of the tree is not lonely because it does not have a parent node.

# Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. 
# Return the list in any order.

class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
            self.answer = []
            self.helper(root)
            return self.answer

    def helper(self, node):
        if node is None:
            return
        if node.right and not node.left:
            self.answer.append(node.right.val)
            self.helper(node.right)
        elif node.left and not node.right:
            self.answer.append(node.left.val)
            self.helper(node.left)
        else:
            self.helper(node.left)
            self.helper(node.right)
