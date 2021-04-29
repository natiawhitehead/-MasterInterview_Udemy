# Given the head of a linked list and two integers m and n. Traverse the linked list and remove some nodes
# in the following way:

# Start with the head as the current node.
# Keep the first m nodes starting with the current node.
# Remove the next n nodes
# Keep repeating steps 2 and 3 until you reach the end of the list.
# Return the head of the modified list after removing the mentioned nodes.

# Follow up question: How can you solve this problem by modifying the list in -place?

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    take, leave = m, n
    curNode = head
    prevNode = head
    while curNode:
        while take and curNode:
            take -= 1
            prevNode = curNode
            curNode = curNode.next
        while leave and curNode:
            curNode = curNode.next
            leave -= 1
        prevNode.next = curNode
        take, leave = m, n
    return head


Node13 = ListNode(13)
Node12 = ListNode(12, Node13)
Node11 = ListNode(11, Node12)
Node10 = ListNode(10, Node11)
Node9 = ListNode(9, Node10)
Node8 = ListNode(8, Node9)
Node7 = ListNode(7, Node8)
Node6 = ListNode(6, Node7)
Node5 = ListNode(5, Node6)
Node4 = ListNode(4, Node5)
Node3 = ListNode(3, Node4)
Node2 = ListNode(2, Node3)
Node1 = ListNode(1, Node2)

newHead = deleteNodes(Node1, 2, 3)
while newHead:
    print(newHead.val)
    newHead = newHead.next
