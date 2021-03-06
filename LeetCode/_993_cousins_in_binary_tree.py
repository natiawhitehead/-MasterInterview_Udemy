# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        nodes = [(root, None), "end"]
        xFound = False
        yFound = False
        xParent = None
        xParent = None

        def bfs():
            nonlocal xFound, yFound
            while nodes:
                curNode = nodes.pop(0)
                if curNode != "end":
                    if curNode[0].right:
                        nodes.append((curNode[0].right, curNode[0].val))
                    if curNode[0].left:
                        nodes.append((curNode[0].left, curNode[0].val))
                    if curNode[0].val == x:
                        xFound = True
                        xParent = curNode[1]
                    if curNode[0].val == y:
                        yFound = True
                        yParent = curNode[1]
                else:
                    if xFound and yFound and xParent != yParent:
                        return True
                    if nodes:
                        nodes.append("end")
                    xFound = False
                    yFound = False
            return False
        return bfs()
