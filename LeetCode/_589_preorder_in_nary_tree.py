# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is 
# separated by the null value(See examples)

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def preorder(root: 'Node') -> list[int]:
    answer = []
    def traverse(node):
        if not node:
            return
        answer.append(node.val)
        for child in node.children:
                traverse(child)
    traverse(root)
    return answer
