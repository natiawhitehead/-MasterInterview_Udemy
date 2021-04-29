# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    if head is None:
        return
    curNode = head.next
    prevNode = head
    while curNode:
        if prevNode.val == curNode.val:
            prevNode.next = curNode.next
        else:
            prevNode = curNode
        curNode = curNode.next
    return head


Node6 = ListNode(3)
Node5 = ListNode(3, Node6)
Node4 = ListNode(3, Node5)
Node3 = ListNode(2, Node4)
Node2 = ListNode(1, Node3)
Node1 = ListNode(1, Node2)

newHead = deleteDuplicates(Node1)
stringRepr = ""
while newHead:
    stringRepr += "-->" + str(newHead.val)
    newHead = newHead.next
print(stringRepr)
