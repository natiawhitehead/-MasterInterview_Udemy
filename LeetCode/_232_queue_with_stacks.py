# Implement a first in first out(FIFO) queue using only two stacks. The implemented queue should support all
# the functions of a normal queue(push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def moveFromStackToStack(self, stack_from, stack_to):
        while len(stack_from):
            popped = stack_from.pop()
            stack_to.append(popped)

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.stack1.append(x)
        else:
            self.moveFromStackToStack(self.stack1, self.stack2)
            self.stack1.append(x)
            self.moveFromStackToStack(self.stack2, self.stack1)
        return self.stack1[-1]

    def pop(self) -> int:
        if len(self.stack1) == 0:
            return None
        else:
            popped = self.stack1.pop()
            return popped

    def peek(self) -> int:
        if len(self.stack1) == 0:
            return None
        else:
            return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)
