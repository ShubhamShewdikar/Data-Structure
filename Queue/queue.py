# Author :- Shubham Shewdikar
class Queue(object):

    def __init__(self, limit=10):
        self.rear = None,
        self.front = None,
        self.limit = 10,
        self.queue = [],
        self.size = 0

    def isFull(self):
        return self.size == self.limit

    def isEmpty(self):
        return self.size <= 0

    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow")
            return -1
        else:
            self.queue.append(data)
            if self.front is None:
                self.front = self.rear = 0
            else:
                self.rear = self.size
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            self.queue.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1

    def displayQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return [print(i) for i in self.queue]


if __name__ == '__main__':
    obj = Queue()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.displayQueue()
