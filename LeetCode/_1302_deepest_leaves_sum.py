# Given the root of a binary tree, return the sum of values of its deepest leaves.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        maxLevel = 0
        answer = 0

        def dfs(node, level):
            nonlocal maxLevel, answer
            if node:
                if not node.right and not node.left:
                    if level > maxLevel:
                        maxLevel = level
                        answer = node.val
                    elif level == maxLevel:
                        answer += node.val
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
        dfs(root, 0)
        return answer

    def deepestLeavesSumWithBFS(self, root: TreeNode) -> int:
        answer = 0
        curLevel = [root]
        nextLevel = []
        while curLevel:
            answer = 0
            for curNode in curLevel:
                if curNode.left:
                    nextLevel.append(curNode.left)
                if curNode.right:
                    nextLevel.append(curNode.right)
                answer += curNode.val
            curLevel = nextLevel
            nextLevel = []
        return answer
