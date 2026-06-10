class Node:
    """
    Individual data node container.
    Maintains bidirectional pointers for O(1) front and rear traversal.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Forward link
        self.prev = None  # Backward link


class LinkedListDeque:
    """
    Double-Ended Queue (Deque) engineered to guarantee strict O(1) performance
    for structural additions and removals at both Front and Rear boundaries.
    """
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0  # Private counter for tracking size in O(1) time

    def is_empty(self):
        """Check if the deque contains no elements."""
        return self.front is None

    def size(self):
        """Return the exact number of active elements in O(1) time."""
        return self._size

    def insert_front(self, value):
        """
        Inserts an item at the absolute front boundary of the deque.
        Time Complexity: O(1) -> Standard pointer reassignments.
        """
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front  # Point new node to the old head
            self.front.prev = new_node  # Point old head back to the new node
            self.front = new_node       # Move structural front pointer to new node
            
        self._size += 1

    def insert_rear(self, value):
        """
        Inserts an item at the absolute rear boundary of the deque.
        Time Complexity: O(1) -> Standard pointer reassignments.
        """
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear  # Point new node back to old tail
            self.rear.next = new_node  # Point old tail forward to new node
            self.rear = new_node       # Move structural rear pointer to new node
            
        self._size += 1

    def delete_front(self):
        """
        Removes and returns the item sitting at the absolute front boundary.
        Time Complexity: O(1) -> Instant separation without memory shifts.
        """
        if self.is_empty():
            print("Deque Underflow! Cannot delete from the front of an empty deque.")
            return None
        
        removed_node = self.front
        removed_value = removed_node.data
        
        self.front = self.front.next  # Move front pointer one step forward
        
        if self.front is None:
            self.rear = None  # The structure is now completely empty
        else:
            self.front.prev = None  # Sever backlink to the old deleted node
            
        self._size -= 1
        del removed_node  # Clear variable instance reference
        return removed_value

    def delete_rear(self):
        """
        Removes and returns the item sitting at the absolute rear boundary.
        Time Complexity: O(1) -> Instant separation without memory shifts.
        """
        if self.is_empty():
            print("Deque Underflow! Cannot delete from the rear of an empty deque.")
            return None
        
        removed_node = self.rear
        removed_value = removed_node.data
        
        self.rear = self.rear.prev  # Move rear pointer one step backward
        
        if self.rear is None:
            self.front = None  # The structure is now completely empty
        else:
            self.rear.next = None  # Sever forward link to the old deleted node
            
        self._size -= 1
        del removed_node  # Clear variable instance reference
        return removed_value

    def peek_front(self):
        """Glance at the front node value without altering structural links."""
        if self.is_empty():
            print("Inspection Note: Deque front is empty.")
            return None
        return self.front.data

    def peek_rear(self):
        """Glance at the rear node value without altering structural links."""
        if self.is_empty():
            print("Inspection Note: Deque rear is empty.")
            return None
        return self.rear.data

    def display_deque(self):
        """Render the complete linear layout from front to rear."""
        if self.is_empty():
            print("Deque Blueprint: [Empty]")
            return
            
        print("FRONT <=> ", end="")
        temp_head = self.front
        while temp_head is not None:
            print(f"[{temp_head.data}]", end=" <=> ")
            temp_head = temp_head.next
        print("REAR")


# ==============================================================================
# RUNTIME ARCHITECTURE VERIFICATION
# ==============================================================================
if __name__ == "__main__":
    print("=== Constructing High Performance Bidirectional Deque ===")
    history_manager = LinkedListDeque()

    print("\n--- Phase 1: Constant Time Boundary Insertions ---")
    history_manager.insert_rear("Page_002")  # Middle base
    history_manager.insert_front("Page_001") # Insert before base
    history_manager.insert_rear("Page_003")  # Insert after base
    history_manager.insert_front("Home_Dashboard") # Insert at extreme peak
    history_manager.display_deque()
    print(f"Current Cache Size: {history_manager.size()}")

    print("\n--- Phase 2: Structural Peak Peeking ---")
    print(f"Front Node Value: {history_manager.peek_front()}")
    print(f"Rear Node Value:  {history_manager.peek_rear()}")

    print("\n--- Phase 3: High Efficiency Boundary Deletions ---")
    print(f"Popped from Front: {history_manager.delete_front()}")
    print(f"Popped from Rear:  {history_manager.delete_rear()}")
    
    print("\n--- Phase 4: Final Inspection Snapshot ---")
    history_manager.display_deque()
    print(f"Remaining Cache Size: {history_manager.size()}")
