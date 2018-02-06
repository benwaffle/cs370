class Stack(object):
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items) - 1]

     def size(self):
         return len(self.items)

class Queue(object):
    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def enqueue(self, item):
        return self.left.push(item)

    def _checkRight(self):
        if self.right.size() == 0:
            while self.left.size() > 0:
                self.right.push(self.left.pop())

    def dequeue(self):
        self._checkRight()
        return self.right.pop()

    def front(self):
        self._checkRight()
        return self.right.peek()

if __name__ == '__main__':
    q = Queue()
    n = int(input())
    for _ in range(n):
        s = input()
        if s[0] == '1':
            q.enqueue(int(s[2:]))
        elif s[0] == '2':
            q.dequeue()
        elif s[0] == '3':
            print(q.front())
