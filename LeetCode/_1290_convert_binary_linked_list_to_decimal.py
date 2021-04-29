# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# binary: 1001
# decimal 1 * 2 ^ 3 + 0 * 2 ^ 2 + 0 * 2 ^ 1 + 1 * 2 ^ 0

# The pattern here is we add the current digit, then as we move on to the next digit,
# we multiply all previous digits by 2. This way, we get the effect of multiplying each digit of binary by 2
# the correct number of times.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    answer = 0
    while head:
        answer = answer * 2 + head.val  # is the same as "answer = answer << 2 | head.val
        head = head.next
    return answer


Node3 = ListNode(1)
Node2 = ListNode(0, Node3)
Node1 = ListNode(1, Node2)

print(getDecimalValue(Node1))
