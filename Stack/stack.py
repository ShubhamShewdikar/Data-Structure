# Author :- Shubham Shewdikar
class Stack():
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print("Stack Overflow")
            return -1
        else:
            self.stack.append(data)
    def pop(self):
        if len(self.stack) <= 0:
            print("Stack is Empty")
            return -1
        else:
            self.stack.pop()
    
    def display(self):
        if not self.stack:
            print("Stack is empty nothing to display")
        else:
            return [print(i) for i in self.stack]

if __name__ == '__main__':
    obj = Stack()
    obj.display()
    obj.push(1)
    obj.push(2)
    obj.display()
    obj.pop()
    obj.display()