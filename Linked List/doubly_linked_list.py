# Author :- Shubham Shewdikar
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.prev = None 
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    def insertAfter(self, prev, data):
        new_node = Node(data)

        if prev is None:
            print("invalid")
        
        new_node.next = prev.next
        new_node.prev = prev
        prev.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def displayList(self, last=None):
        if self.head is None:
            print("List is Empty")
        else:
            node = self.head
            print("\nTraversal in Forward direction")
            while node is not None:
                print(node.data, end=" ")
                last = node
                node = node.next
            
            print("\nTraversal in Reverse direction")
            while last is not None:
                print(last.data, end=" ")
                last = last.prev

    def displayListFromAnyNode(self, node=None, last=None):
        if self.head is None:
            print("List is Empty")
        
        print("\nTraversal in Forward direction")
        while node is not None:
            print(node.data, end=" ")
            last = node
            node = node.next
        print("\nTraversal in Reverse direction")
        while last is not None:
            print(last.data, end=" ")
            last = last.prev


obj = DoublyLinkList()

obj.insertAtBegining(0)
obj.insertAtEnd(10)
obj.insertAfter(obj.head, 5)
obj.displayListFromAnyNode(obj.head)
