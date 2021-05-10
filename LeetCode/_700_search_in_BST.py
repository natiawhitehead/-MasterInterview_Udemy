# You are given the root of a binary search tree(BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def searchBST(root: TreeNode, val: int) -> TreeNode:
    def traverse(node, val):
        if node:
            if node.val == val:
                return node
            elif node.val > val:
                return traverse(node.left, val)
            else:
                return traverse(node.right, val)
    return traverse(root, val)
