# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
# connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:
    hashTable = {}
    curNode = head
    while hashTable.get(curNode) is None and curNode:
        hashTable[curNode] = True
        curNode = curNode.next
    if curNode:
        return True
    else:
        return False


# If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.
# If there is a cycle, both pointers will land at the same node
def hasCycleWithoutMemory(head: ListNode) -> bool:
    if not head:
        return
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


Node4 = ListNode(-4)
Node3 = ListNode(0, Node4)
Node2 = ListNode(2, Node3)
Node1 = ListNode(3, Node2)
pos = Node2
Node4.next = pos


print(hasCycle(Node1))
print(hasCycleWithoutMemory(Node1))
