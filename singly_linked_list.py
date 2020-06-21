class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, data):
        new_node = node(data)
        if self.head:
            new_node.next = self.head
        
        self.head = new_node

    def insertTail(self, data):
        if self.head is None:
            self.insertHead(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node(data)

    def deleteHead(self):
        if self.head:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp
        else:
            print("List is Empty")

    def deleteTail(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
            if temp.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
            return temp

    def setAtAnIndex(self,index,data):
        current = self.head

        if current is None:
            raise IndexError("Index id out of range")
        for _ in range(index):
            if current.next is None:
                raise IndexError("Index id out of range")
            current = current.next
        current.data = data
            
    def getAtAnIndex(self,index):
        current = self.head

        if current is None:
            raise IndexError("Index id out of range")
        for _ in range(index):
            if current.next is None:
                raise IndexError("Index id out of range")
            current = current.next
        print(current.data)

    def reverse(self):
        if self.head and self.head.next is None:
            print(self.head)
        
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev            



    def displayList(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

obj = linkedList()
obj.insertTail(1)
# obj.displayList()
obj.insertTail(2)
obj.insertTail(3)
obj.insertTail(4)
obj.displayList()
# obj.deleteTail()
# obj.displayList()
# obj.insertHead(0)
# obj.displayList()
print("-------------")
# obj.getAtAnIndex(2)
# obj.setAtAnIndex(0,60)
obj.reverse()
obj.displayList()

