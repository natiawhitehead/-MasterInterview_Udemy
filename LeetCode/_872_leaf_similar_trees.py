# Consider all the leaves of a binary tree, from left to right order, 
# the values of those leaves form a leaf value sequence.

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        sequence = []
        sequence2 = []

        def traverseTree(node, sequence):
            if node:
                if not node.right and not node.left:
                    sequence.append(node.val)
                traverseTree(node.left, sequence)
                traverseTree(node.right, sequence)
        traverseTree(root1, sequence)
        traverseTree(root2, sequence2)
        if len(sequence) != len(sequence2):
            return False
        for i in range(len(sequence)):
            if sequence[i] != sequence2[i]:
                return False
        return True
