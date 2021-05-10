# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest 
# leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is 
# separated by the null value(See examples).

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root: 'Node') -> int:
    if not root:
        return 0
    def traverse(node):
        if not node:
            return 0
        maxSum = 0
        for child in node.children:
            maxSum = max(maxSum,traverse(child)+1)
        return maxSum
    return traverse(root) + 1
