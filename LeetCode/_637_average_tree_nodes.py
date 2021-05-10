# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
# Answers within 10-5 of the actual answer will be accepted.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: TreeNode) -> List[float]:
    listOfNodes = [root, "End"]
    answer = []
    tempSum = 0
    tempCount = 0
    while listOfNodes:
        curElement = listOfNodes.pop(0)
        if not curElement:
            continue
        if curElement != "End":
            tempSum += curElement.val
            tempCount += 1
            listOfNodes.append(curElement.right)
            listOfNodes.append(curElement.left)
        elif tempCount:
            listOfNodes.append("End")
            answer.append(tempSum/tempCount)
            tempSum = 0
            tempCount = 0
    return answer
