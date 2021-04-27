# implementing linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def print(self):
        node = self.head
        answer = ""
        while node is not None:
            answer += str(node.value) + "-->"
            node = node.next
        print(answer + "None")

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.count += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
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
                curNode = self.getByIndex(index-1)
                tempNext = curNode.next
                curNode.next = newNode
                newNode.next = tempNext
                self.count += 1

    def remove(self, index):
        if index < 0 or index >= self.count:
            print("index out of range")
            return
        if index == 0:
            self.head = self.head.next
        else:
            prevNode = self.getByIndex(index-1)
            prevNode.next = prevNode.next.next
            if index == self.count - 1:
                self.tail = prevNode
        self.count -= 1


myLinkedList = LinkedList(10)
myLinkedList.append(4)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(1, 12)
myLinkedList.insert(3, 11)
myLinkedList.insert(6, 6)
myLinkedList.print()
myLinkedList.remove(6)
myLinkedList.append(33)
myLinkedList.print()
