# User defined Data types ko class ki help se create kar sakte hai.
class Node:
    def __init__(self, info, next=None, prev=None): 
        self.data = info
        self.next = next  # Forward pointer
        self.prev = prev  # Backward pointer
    

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head 
    
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            temp_head = self.head 
            while temp_head.next is not None:
                temp_head = temp_head.next 
            temp_head.next = temp 
            temp.prev = temp_head  # Establishing the backward link
        else:
            self.head = temp
        
    def printLinkedList(self):
        temp_head = self.head
        if temp_head is None:
            print("List is empty")
            return
        while temp_head is not None: 
            print(temp_head.data, end="  ")
            temp_head = temp_head.next
        print() 

    def printLinkedListReverse(self):
        # Specially added to demonstrate backward traversal
        if self.head is None:
            print("List is empty")
            return
            
        temp_head = self.head
        # 1. Travel to the absolute end node
        while temp_head.next is not None: 
            temp_head = temp_head.next
            
        # 2. Trace backward using the .prev links
        while temp_head is not None:
            print(temp_head.data, end=" <- ")
            temp_head = temp_head.prev
        print("HEAD")
        
    def insertAtHead(self, value):
        temp = Node(value, next=self.head)
        if self.head is not None:
            self.head.prev = temp  # Update old head's back link
        self.head = temp

    def insertAfterNodeValue(self, value, nodeValue):
        temp_head = self.head
        while (temp_head is not None) and (temp_head.data != nodeValue):
            temp_head = temp_head.next
            
        if temp_head is None:
            print(f"No node is present with value: {nodeValue}") 
            return 0
        else:
            # Create node with correct forward and backward references
            temp = Node(value, next=temp_head.next, prev=temp_head)
            
            # If inserting somewhere in the middle, update the next node's backlink
            if temp_head.next is not None:
                temp_head.next.prev = temp
                
            temp_head.next = temp
    
    def insertAtLocation(self, value, location):
        if location == 1:
            self.insertAtHead(value)
            return 0
            
        if self.head is None:
            print(f"Linked List has less elements than {location}")
            return 0

        temp_head = self.head
        for _ in range(location - 2):
            if temp_head.next is None:
                print(f"Linked List has less elements than {location}")
                break
            temp_head = temp_head.next
        else:
            self.insertAfterNodeValue(value, temp_head.data)

    def deleteNode(self, nodeValue):
        if self.head is None:
            print("List is empty")
            return

        temp_head = self.head
        
        # Case 1: Node to delete is the head node
        if temp_head.data == nodeValue:
            self.head = temp_head.next
            if self.head is not None:
                self.head.prev = None  # Sever backlink of the new head
            return 

        # Case 2: Find the target node directly 
        # (In Doubly lists, look-ahead logic isn't strictly required since nodes know their previous neighbors)
        while temp_head is not None and temp_head.data != nodeValue:
            temp_head = temp_head.next

        # Case 3: Node found, clear pointers to free memory safely
        if temp_head is not None:
            # Bypass target forward link
            if temp_head.prev is not None:
                temp_head.prev.next = temp_head.next
                
            # Bypass target backward link
            if temp_head.next is not None:
                temp_head.next.prev = temp_head.prev
                
            # Free internal pointers to break circular reference memory cycles
            temp_head.next = None
            temp_head.prev = None
        else:
            print(f"No node is present with value: {nodeValue}")
    
# Verification of functions
dll = DoublyLinkedList() 
dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtEnd(30)
dll.insertAtEnd(40)
dll.insertAtEnd(50)

print("Forward Traversal:")
dll.printLinkedList()

print("\nBackward Traversal:")
dll.printLinkedListReverse()

print("\nDeleting Node 30 and inserting 25 at location 3:")
dll.deleteNode(30)
dll.insertAtLocation(25, 3)
dll.printLinkedList()
