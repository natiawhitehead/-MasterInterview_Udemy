# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. 
# Each group of children is separated by the null value(See examples)

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



def postorder(root: 'Node') -> list[int]:
    answer = []
    def traverse(node):
        if not node:
            return
        for child in node.children:
            traverse(child)
        answer.append(node.val)
    traverse(root)
    return answer
