# Given the root of a binary search tree, rearrange the tree in in-order so that the 
# leftmost node in the tree is now the root of the tree, and every node has no left child and only one 
# right child.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(self, root: TreeNode) -> TreeNode:
    root2 = TreeNode(0)
    root3 = self.root2

    def attachToRight(root):
        if root is None:
            return
        attachToRight(root.left)
        root2.right = TreeNode(root.val)
        root2 = root2.right
        attachToRight(root.right)
    attachToRight(root)
    return root3.right
