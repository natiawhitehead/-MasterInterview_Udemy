# Given a non-empty special binary tree consisting of nodes with the non-negative value, 
# where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, 
# then this node's value is the smaller value among its two sub-nodes. More formally, 
# the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output - 1 instead.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        minValue = root.val
        secondMin = None
        nodes = [root]
        def bfs(node):
            nonlocal secondMin
            while nodes:
                curNode = nodes.pop(0)
                if curNode != "end":
                    if curNode.val != minValue:
                        if secondMin:
                            secondMin = min(secondMin, curNode.val)
                        else:
                            secondMin = curNode.val
                    if curNode.left:
                        nodes.append(curNode.left)
                    if curNode.right:
                        nodes.append(curNode.right)
                else:
                    if secondMin:
                        break
                    if nodes:
                        nodes.append("end")

        bfs(root)
        if not secondMin:
            secondMin = -1
        return secondMin
