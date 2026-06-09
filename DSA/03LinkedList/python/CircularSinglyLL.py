# User defined Data types ko class ki help se create kar sakte hai.
class Node:
    def __init__(self, info, next=None): 
        self.data = info
        self.next = next
    

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head 
    
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            temp_head = self.head 
            # Loop until we reach the node that points back to head
            while temp_head.next != self.head:
                temp_head = temp_head.next 
            temp_head.next = temp 
            temp.next = self.head  # Complete the circle
        else:
            self.head = temp
            temp.next = self.head  # A single node points to itself
        
    def printLinkedList(self):
        if self.head is None:
            print("List is empty")
            return
            
        temp_head = self.head
        # Use a do-while approach using a flag or a while loop with a check
        while True:
            print(temp_head.data, end=" -> ")
            temp_head = temp_head.next
            if temp_head == self.head:
                break
        print("(HEAD)") # Visual anchor showing it looped back

    def insertAtHead(self, value):
        temp = Node(value)
        if self.head is not None:
            temp_head = self.head
            # Find tail node to update its next pointer to the new head
            while temp_head.next != self.head:
                temp_head = temp_head.next
            
            temp.next = self.head
            temp_head.next = temp
            self.head = temp  # Update structural head pointer
        else:
            self.head = temp
            temp.next = self.head

    def insertAfterNodeValue(self, value, nodeValue):
        if self.head is None:
            print("List is empty")
            return 0

        temp_head = self.head
        while True:
            if temp_head.data == nodeValue:
                temp = Node(value, temp_head.next)
                temp_head.next = temp
                return
            temp_head = temp_head.next
            if temp_head == self.head:
                break
                
        print(f"No node is present with value: {nodeValue}") 
        return 0
    
    def insertAtLocation(self, value, location):
        if location == 1:
            self.insertAtHead(value)
            return 0
            
        if self.head is None:
            print(f"Linked List has less elements than {location}")
            return 0

        temp_head = self.head
        # Loop to stop exactly BEFORE the insertion point
        for _ in range(location - 2):
            temp_head = temp_head.next
            # If we looped back to head prematurely, location out of bounds
            if temp_head == self.head:
                print(f"Linked List has less elements than {location}")
                return 0
                
        # One last lookahead check before calling insert after node
        self.insertAfterNodeValue(value, temp_head.data)

    def deleteNode(self, nodeValue):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None
        
        # Case 1: Node to delete is the head node
        if current.data == nodeValue:
            # If it's the only node in the list
            if current.next == self.head:
                self.head = None
                return
            
            # Find the tail node to re-link it to the new head
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
                
            self.head = current.next
            tail.next = self.head
            return 

        # Case 2: Node is somewhere else in the loop
        prev = current
        current = current.next
        while current != self.head:
            if current.data == nodeValue:
                prev.next = current.next
                return
            prev = current
            current = current.next
            
        print(f"No node is present with value: {nodeValue}")
    
# Verification of functions
cll = CircularLinkedList() 
cll.insertAtEnd(10)
cll.insertAtEnd(20)
cll.insertAtEnd(30)
cll.insertAtEnd(40)
cll.insertAtEnd(50)

print("Initial Circular List:")
cll.printLinkedList()

print("\nInserting 5 at Head:")
cll.insertAtHead(5)
cll.printLinkedList()

print("\nDeleting Node 30 and inserting 25 at location 4:")
cll.deleteNode(30)
cll.insertAtLocation(25, 4)
cll.printLinkedList()
