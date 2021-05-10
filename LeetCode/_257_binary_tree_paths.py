# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        answer = []

        def traverse(node, path):
            if node:
                if not node.left and not node.right:  # if it is a leaf, append to answer
                    path.append(str(node.val))
                    answer.append("".join(path))
                else:
                    traverse(node.left, path + [str(node.val), "->"])
                    traverse(node.right, path + [str(node.val), "->"])
        traverse(root, [])
        return answer
