# Merge two sorted linked lists and return it as a sorted list. The list should be made by
#  splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    curNode1 = l1
    curNode2 = l2
    answerNext = None
    answerHead = None
    while curNode1 or curNode2:
        noNeedToContinue = True
        nextNode = None
        if curNode1 and curNode2:
            noNeedToContinue = False
            if curNode1.val <= curNode2.val:
                nextNode = curNode1
                curNode1 = curNode1.next
            else:
                nextNode = curNode2
                curNode2 = curNode2.next
        elif curNode1 and not curNode2:
            nextNode = curNode1
        else:
            nextNode = curNode2

        if answerNext is None:
            answerNext = nextNode
            answerHead = nextNode
        else:
            answerNext.next = nextNode
            answerNext = answerNext.next
        if noNeedToContinue:
            break
    return answerHead


list2Node3 = ListNode(4)
list2Node2 = ListNode(3, list2Node3)
list2Node1 = ListNode(1, list2Node2)
list1Node3 = ListNode(4,)
list1Node2 = ListNode(2, list1Node3)
list1Node1 = ListNode(1, list1Node2)

newHead = mergeTwoLists(list1Node1, list2Node1)
stringRepr = ""
while newHead:
    stringRepr += "-->" + str(newHead.val)
    newHead = newHead.next
print(stringRepr)
