# implementing javascript array(object with integerbased keys/indexes)
class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise Exception("Array is empty")
        self.data.pop(self.length-1)
        self.length -= 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Index out of bound")
        item = self.data[index]
        self.shiftItems(index)

    def print(self):
        print(self.data)

    def shiftItems(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        self.pop()


ar = MyArray()
ar.push('a')
ar.push('b')
ar.push('c')
ar.push('d')
ar.print()
ar.delete(4)
ar.print()
