# Given a binary search tree(BST), find the lowest common ancestor(LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
#  two nodes p and q as the lowest node in T that has both p and q as descendants(where we allow a node to be a 
#  descendant of itself).”

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = None

        def traverse(node, p_val, q_val):
            if node:
                if node.val < p_val and node.val < q_val:
                    traverse(node.right, p_val, q_val)
                elif node.val > p_val and node.val > q_val:
                    traverse(node.left, p_val, q_val)
                else:
                    self.answer = node
                    return
        if p.val > q.val:
            traverse(root, q.val, p.val)
        else:
            traverse(root, p.val, q.val)
        return self.answer
