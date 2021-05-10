class Node:
    def __init__(self, value=0, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


class binarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        newNode = Node(val)
        if not self.root:
            self.root = newNode
        else:
            node = self.root
            while node:
                if val > node.value:
                    if node.right == None:
                        node.right = newNode
                        break
                    else:
                        node = node.right
                else:
                    if node.left == None:
                        node.left = newNode
                        break
                    else:
                        node = node.left

    def lookup(self, val):
        node = self.root
        while node:
            if node.value == val:
                return node
            elif val > node.value:
                node = node.right
            else:
                node = node.left
        return None

    def getMaxInLeftValAndDeleteDuplicate(self, node, parent):
        answer = node.value
        curNode = node
        left = curNode.left
        while curNode.right:
            parent = curNode
            curNode = curNode.right
            answer = curNode.val
            left = curNode.left
        if curNode.value > parent.value:
            parent.right = left
        else:
            parent.left = left
        return answer

    def remove(self, val):
        curNode = self.root
        key = val
        parent = None
        while curNode:
            if curNode.value == key:

                if not curNode.left and not curNode.right:  # no child
                    if parent is None:
                        return None
                    fromLeft = False
                    if parent and parent.value > key:
                        fromLeft = True

                    if fromLeft:
                        parent.left = None
                    else:
                        parent.right = None
                elif curNode.left and not curNode.right:  # only left child
                    if parent is None:
                        return curNode.left

                    fromLeft = False
                    if parent.value > key:
                        fromLeft = True
                    if fromLeft:
                        parent.left = curNode.left
                    else:
                        parent.right = curNode.left
                elif not curNode.left and curNode.right:  # only right child
                    if parent is None:
                        return curNode.right

                    fromLeft = False
                    if parent.value > key:
                        fromLeft = True
                    if fromLeft:
                        parent.left = curNode.right
                    else:
                        parent.right = curNode.right
                else:  # both right and left children
                    maxInLeft = self.getMaxInLeftValAndDeleteDuplicate(
                        curNode.left, curNode)
                    curNode.value = maxInLeft
                return
            elif curNode.value > key:
                parent = curNode
                curNode = curNode.left
            else:
                parent = curNode
                curNode = curNode.right


# myBST = binarySearchTree()
# myBST.insert(9)
# myBST.insert(4)
# myBST.insert(6)
# myBST.insert(20)
# myBST.insert(170)
# myBST.insert(15)
# myBST.insert(1)

# print(myBST.lookup(20))
# print(myBST.lookup(9))

# myBST.remove(20)
# print(myBST.lookup(20))
