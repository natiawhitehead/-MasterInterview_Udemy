# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped 
# while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that 
# if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null 
# node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:

    def helper(node1, node2, parent1, parentToright):
        if not node1 and not node2:
            return
        elif node1 and node2:
            node1.val += node2.val
            helper(node1.right, node2.right, node1, True)
            helper(node1.left, node2.left, node1, False)
        elif node2 and not node1:
            node1 = node2
            if parentToright:
                parent1.right = node1
            else:
                parent1.left = node1
            helper(None, node2.right, node1, True)
            helper(None, node2.left, node1, False)

    if root1 is None:
        return root2
    helper(root1, root2, root1, False)
    return root1
