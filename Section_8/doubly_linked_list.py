# implementing linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.count = 1

    def getByIndex(self, index):
        if(index < 0 or index >= self.count):
            print("index out of range")
            return None
        else:
            curNode = self.head
            for i in range(self.count):
                if i == index:
                    return curNode
                curNode = curNode.next
            return None

    def print(self, reverse=False):
        answer = ""
        if reverse:
            node = self.tail
        else:
            node = self.head

        while node is not None:
            answer += str(node.value) + "<->"
            if reverse:
                node = node.prev
            else:
                node = node.next
        print(answer + "None")

    def append(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.count += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.count += 1

    def insert(self, index, value):
        if index < 0 or index > self.count:
            print("index out of range")
            return
        else:
            newNode = Node(value)
            if index == 0:
                self.prepend(value)
            elif index == self.count:
                self.append(value)
            else:
                curNode = self.getByIndex(index)
                tempNext = curNode.next
                curNode.next = newNode
                newNode.prev = curNode
                newNode.next = tempNext
                tempNext.prev = newNode
                self.count += 1

    def remove(self, index):
        if index < 0 or index >= self.count:
            print("index out of range")
            return
        if index == 0:
            self.head = self.head.next
            self.head.next = None
        else:
            curNode = self.getByIndex(index)
            tempPrev = curNode.prev
            tempNext = curNode.next
            if tempNext is not None:
                tempNext.prev = tempPrev
            tempPrev.next = tempNext
            if index == self.count - 1:
                self.tail = tempPrev
        self.count -= 1


# myLinkedList = LinkedList(10)
# myLinkedList.append(4)
# myLinkedList.append(16)
# myLinkedList.prepend(1)
# myLinkedList.insert(1, 12)
# myLinkedList.insert(3, 11)
# myLinkedList.insert(6, 6)
# myLinkedList.print()
# myLinkedList.remove(5)
# myLinkedList.print()
# myLinkedList.print(True)

myList2 = LinkedList(11)
myList2.insert(1, 3)
myList2.print()
myList2.remove(1)
myList2.print()
myList2.print(True)
