class Stack():
    def __init__(self):
        self._items = []
    def push(self, item):
        self._items.append(item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def is_empty(self):
        if self._items:
            return False
        else:
            return True
    def size(self):
        return len(self._items)
    

test = Stack()
print(test.push(34))
print(test.peek())

