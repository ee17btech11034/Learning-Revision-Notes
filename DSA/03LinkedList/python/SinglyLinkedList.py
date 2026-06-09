# User defined Data types ko class ki help se create kar sakte hai.
class Node:
    def __init__(self, info, next=None): # self is just like 'this' keyword in other languages.
        self.data = info
        self.next = next
    

class SinglylinkedList:
    def __init__(self, head=None):
        self.head = head 
    
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            temp_head = self.head 
            while temp_head.next is not None:
                temp_head = temp_head.next 
            temp_head.next = temp 
        else:
            self.head = temp
        
    def printLinkedList(self):
        temp_head = self.head
        while temp_head is not None: 
            print(temp_head.data, end="  ")
            temp_head = temp_head.next
        print() # New line print karne ke liye

    def printLinkedList2(self):
        # Handle empty list safely
        if self.head is None:
            print("List is empty")
            return
            
        temp_head = self.head
        while temp_head.next is not None: 
            print(temp_head.data, end=" -> ")
            temp_head = temp_head.next
        print(temp_head.data)
        
    def insertAtHead(self, value):
        temp = Node(value, self.head)
        self.head = temp

    def insertAfterNodeValue(self, value, nodeValue):
        temp_head = self.head
        while (temp_head is not None) and (temp_head.data != nodeValue):
            temp_head = temp_head.next
            
        if temp_head is None:
            print(f"No node is present with value: {nodeValue}") # Fixed JS string substitution syntax bug
            return 0
        else:
            temp = Node(value, temp_head.next)
            temp_head.next = temp
    
    def insertAtLocation(self, value, location):
        if location == 1:
            self.insertAtHead(value)
            return 0
            
        # Clear separation for empty list safety
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
            # Fully safe now, temp_head cannot be None
            self.insertAfterNodeValue(value, temp_head.data)

    def deleteNode(self, nodeValue):
        if self.head is None:
            print("List is empty")
            return

        temp_head = self.head
        
        # Case 1: Agar head node ko hi delete karna hai
        if temp_head.data == nodeValue:
            self.head = temp_head.next
            return # Must return early to prevent continuing logic

        # Case 2: Node find karo (Look-ahead validation ke saath takki crash na ho)
        while temp_head.next is not None and temp_head.next.data != nodeValue:
            temp_head = temp_head.next

        # Case 3: Pointers update karo agar node match mil gaya hai
        if temp_head.next is not None:
            temp_head.next = temp_head.next.next
        else:
            print(f"No node is present with value: {nodeValue}")
    
sll1 = SinglylinkedList() 
sll1.insertAtEnd(10)
sll1.insertAtEnd(20)
sll1.insertAtEnd(30)
sll1.insertAtEnd(40)
sll1.insertAtEnd(50)
sll1.printLinkedList()
