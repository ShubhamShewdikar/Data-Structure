# Author :- Shubham Shewdikar
class node():
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class circularLinkList:
    def __init__(self):
        self.head = None
    
    def insertAtFirst(self, data):
        new_node = node(data)
        temp = self.head
        new_node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        
        self.head = new_node

    def deleteAtFirst(self, data):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = self.head.next
            self.head = temp.next

    def displayList(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break

obj = circularLinkList()
obj.insertAtFirst(2)
obj.displayList()
# obj.insertAtFirst(2)
