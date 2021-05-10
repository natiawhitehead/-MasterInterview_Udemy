# Given the root of a Binary Search Tree and a target number k, return true 
# if there exist two elements in the BST such that their sum is equal to the given target.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        sortedArray = []

        def dfs(node):
            if node:
                dfs(node.left)
                sortedArray.append(node.val)
                dfs(node.right)

        dfs(root)
        left, right = 0, len(sortedArray) - 1
        while left < right:
            if sortedArray[left] + sortedArray[right] == k:
                return True
            elif sortedArray[left] + sortedArray[right] < k:
                left += 1
            else:
                right -= 1
        return False
