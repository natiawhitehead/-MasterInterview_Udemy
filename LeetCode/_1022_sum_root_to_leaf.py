# ou are given the root of a binary tree where each node has a value 0 or 1.  
# Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, 
# if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

# Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumRootToLeaf(root: TreeNode) -> int:
    answer = 0

    def traverse(node, strBinary):
        if node:
            strBinary += str(node.val)
            traverse(node.left, strBinary)
            traverse(node.right, strBinary)
            if not node.left and not node.right:
                answer += int(strBinary, 2)
    traverse(root, "")
    return answer
