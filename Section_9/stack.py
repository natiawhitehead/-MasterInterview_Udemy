class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, headNode=None):
        self.top = headNode
        self.bottom = headNode
        self.count = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
            self.bottom = newNode
        else:
            oldHead = self.top
            self.top = newNode
            self.top.next = oldHead
        self.count += 1

    def print(self):
        current = self.top
        stResult = ""
        if not current:
            stResult += "Empty stack\n"
        while current:
            stResult += str(current.value) + "-->"
            current = current.next
        print(stResult)

    def pop(self):
        if not self.top:
            return None
        else:
            if self.count == 1:
                self.bottom = None
            oldHead = self.top
            self.top = self.top.next
        self.count -= 1
        return oldHead


myStack = Stack()
myStack.print()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.print()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.push(7)
myStack.pop()
myStack.pop()
myStack.print()
