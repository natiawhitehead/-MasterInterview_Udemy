# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node 
# down to the farthest leaf node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    def traverse(node):
        if node is None:
            return 0
        return max(traverse(node.left), traverse(node.right)) + 1
    return traverse(root)
