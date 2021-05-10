# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of 
# every node never differs by more than one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def binarySearch(left, right):
            if left > right:
                return
            midIndex = (left + right) // 2
            curNode = TreeNode(nums[midIndex])
            curNode.left = binarySearch(left, midIndex - 1)
            curNode.right = binarySearch(midIndex + 1, right)
            return curNode
        return binarySearch(0, len(nums)-1)
