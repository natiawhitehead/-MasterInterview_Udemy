# Given the root node of a binary search tree, return the sum of values of all nodes
# with a value in the range[low, high].
# import sys
# sys.path.append("./Section_10")
# import binary_search_tree as BST
# this solution will work for any binary tree, not just binary search tree


def rangeSumBT(root, low: int, high: int) -> int:
    if root == None:
        return 0
    else:
        left = rangeSumBT(root.left, low, high)
        right = rangeSumBT(root.right, low, high)

        if root.val >= low and root.val <= high:
            return root.val + left + right
        else:
            return left + right


def rangeSumBST(root, low: int, high: int) -> int:
    if root == None:
        return 0
    else:
        if root.value >= low and root.value <= high:
            rootval = root.value
            right = rangeSumBST(root.right, low, high)
            left = rangeSumBST(root.left, low, high)
        elif root.value < low:
            right = rangeSumBST(root.right, low, high)
            left = 0
            rootval = 0
        else:
            left = rangeSumBST(root.left, low, high)
            right = 0
            rootval = 0
        return left + right + rootval


# myBST = BST.binarySearchTree()
# myBST.insert(9)
# myBST.insert(4)
# myBST.insert(6)
# myBST.insert(20)
# myBST.insert(170)
# myBST.insert(15)
# myBST.insert(1)

# print(rangeSumBST(myBST.root, 1, 9))
