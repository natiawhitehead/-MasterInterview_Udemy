# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    curNode = headA
    hashTable = {}
    while curNode:
        hashTable[curNode] = True
        curNode = curNode.next
    curNode = headB
    answer = None
    while curNode:
        if hashTable.get(curNode):
            answer = curNode
            break
        curNode = curNode.next
    return answer


def getIntersectionNodeWithNoMemory(headA: ListNode, headB: ListNode) -> ListNode:
    countA = 0
    countB = 0
    curNode = headA
    while curNode:
        countA += 1
        curNode = curNode.next
    curNode = headB
    while curNode:
        countB += 1
        curNode = curNode.next
    if countA > countB:
        dif = countA - countB
        while dif:
            headA = headA.next
            dif -= 1
    else:
        dif = countB - countA
        while dif:
            headB = headB.next
            dif -= 1
    answer = None
    while headA != headB:
        headA = headA.next
        headB = headB.next
    else:
        return headA
    return answer


Node5 = ListNode(5)
Node4 = ListNode(4, Node5)
Node3 = ListNode(8, Node4)
Node2 = ListNode(1, Node3)
Node1 = ListNode(4, Node2)

Node3_2 = ListNode(1, Node3)
Node2_2 = ListNode(6, Node3_2)
Node1_2 = ListNode(5, Node2_2)

print(getIntersectionNode(Node1, Node1_2).val)
print(getIntersectionNodeWithNoMemory(Node1, Node1_2).val)
