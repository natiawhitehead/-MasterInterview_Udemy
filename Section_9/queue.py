class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, headNode=None):
        self.first = headNode
        self.last = headNode
        self.count = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = self.last.next
        self.count += 1

    def print(self):
        current = self.first
        stResult = ""
        if not current:
            stResult += "Empty stack\n"
        while current:
            stResult += str(current.value) + "-->"
            current = current.next
        print(stResult)

    def dequeue(self):
        if not self.first:
            return None
        else:
            if self.count == 1:
                self.last = None
            self.first = self.first.next
        self.count -= 1
        return self.first


myStack = Queue()
myStack.print()
myStack.enqueue(1)
myStack.enqueue(2)
myStack.enqueue(3)
myStack.enqueue(4)
myStack.print()
myStack.dequeue()
myStack.dequeue()
myStack.dequeue()
myStack.enqueue(7)
myStack.print()
myStack.dequeue()
myStack.dequeue()
myStack.print()
