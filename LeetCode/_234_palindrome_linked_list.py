# Given the head of a singly linked list, return true if it is a palindrome.
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    array = []
    curNode = head
    while curNode:
        array.append(curNode.val)
        curNode = curNode.next
    i, j = 0, len(array)-1
    while i < j:
        if array[i] != array[j]:
            return False
        i += 1
        j -= 1
    return True


def getMiddleNode(head) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def revereseList(head):
    prev = None
    cur = head
    while cur:
        tempNext = cur.next
        cur.next = prev
        prev = cur
        cur = tempNext
    return prev


def isPalindromeWithoutMemory(head: ListNode) -> bool:
    middleNode = getMiddleNode(head)
    newHead = revereseList(middleNode)
    curNode = head
    newListCurr = newHead
    while curNode and newListCurr:
        if curNode.val != newListCurr.val:
            return False
        curNode = curNode.next
        newListCurr = newListCurr.next
    return True


Node4 = ListNode(1)
Node3 = ListNode(2, Node4)
Node2 = ListNode(2, Node3)
Node1 = ListNode(1, Node2)

print(isPalindrome(Node1))
print(isPalindromeWithoutMemory(Node1))
