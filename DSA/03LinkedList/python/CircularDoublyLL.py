# User defined Data types ko class ki help se create kar sakte hai.
class Node:
    def __init__(self, info, next=None, prev=None): 
        self.data = info
        self.next = next  # Forward pointer
        self.prev = prev  # Backward pointer
    

class CircularDoublyLinkedList:
    def __init__(self, head=None):
        self.head = head 
    
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            tail = self.head.prev  # CDLL allows O(1) access to tail!
            
            tail.next = temp
            temp.prev = tail
            temp.next = self.head
            self.head.prev = temp  # Complete the two-way circle
        else:
            self.head = temp
            temp.next = self.head
            temp.prev = self.head  # Points to itself both ways
        
    def printLinkedList(self):
        if self.head is None:
            print("List is empty")
            return
            
        temp_head = self.head
        while True:
            print(temp_head.data, end=" <=> ")
            temp_head = temp_head.next
            if temp_head == self.head:
                break
        print("(HEAD)") 

    def printLinkedListReverse(self):
        if self.head is None:
            print("List is empty")
            return
            
        # O(1) direct jump to tail using head's backlink
        tail = self.head.prev
        temp_tail = tail
        while True:
            print(temp_tail.data, end=" <=> ")
            temp_tail = temp_tail.prev
            if temp_tail == tail:
                break
        print("(TAIL-END)")
        
    def insertAtHead(self, value):
        temp = Node(value)
        if self.head is not None:
            tail = self.head.prev
            
            temp.next = self.head
            temp.prev = tail
            self.head.prev = temp
            tail.next = temp
            self.head = temp  # Update structural head pointer
        else:
            self.head = temp
            temp.next = self.head
            temp.prev = self.head

    def insertAfterNodeValue(self, value, nodeValue):
        if self.head is None:
            print("List is empty")
            return 0

        temp_head = self.head
        while True:
            if temp_head.data == nodeValue:
                # Setup pointers for new node
                temp = Node(value, next=temp_head.next, prev=temp_head)
                
                # Update surrounding node pointers
                temp_head.next.prev = temp
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
        for _ in range(location - 2):
            temp_head = temp_head.next
            if temp_head == self.head:
                print(f"Linked List has less elements than {location}")
                return 0
                
        self.insertAfterNodeValue(value, temp_head.data)

    def deleteNode(self, nodeValue):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        
        # Case 1: Search for the node to delete
        while True:
            if current.data == nodeValue:
                break
            current = current.next
            if current == self.head:
                print(f"No node is present with value: {nodeValue}")
                return

        # Case 2: If it's the only node left in the list
        if current.next == self.head and current.prev == self.head:
            self.head = None
            return

        # Case 3: Update surrounding pointers to isolate target node
        current.prev.next = current.next
        current.next.prev = current.prev

        # If we are deleting the structural head node, shift head down by one step
        if current == self.head:
            self.head = current.next

        # Break local node pointers to cleanly trigger Python garbage collection
        current.next = None
        current.prev = None
    
# Verification of functions
cdll = CircularDoublyLinkedList() 
cdll.insertAtEnd(10)
cdll.insertAtEnd(20)
cdll.insertAtEnd(30)
cdll.insertAtEnd(40)

print("Forward Cycle Display:")
cdll.printLinkedList()

print("\nBackward Cycle Display (Using O(1) Tail Link):")
cdll.printLinkedListReverse()

print("\nInserting 5 at head and deleting 30:")
cdll.insertAtHead(5)
cdll.deleteNode(30)
cdll.printLinkedList()
