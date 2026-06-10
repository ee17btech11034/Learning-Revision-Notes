'''
    We can use Array for queue implimentaion but `append(item)` will take O(1) but "pop(0)" will take O(n) to shift left elements. Better to use Linked list.
'''
class Node:
    """
    Individual data node container.
    Allocated dynamically across non-contiguous heap spaces.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    """
    FIFO Queue implementation engineered to guarantee strict O(1) performance
    across all structural changes by entirely preventing array memory shifts.
    """
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0  # Private size counter for O(1) length checks

    def is_empty(self):
        """Check if the queue contains no elements."""
        return self.front is None

    def size(self):
        """Return the exact number of active elements in O(1) time."""
        return self._size

    def enqueue(self, value):
        """
        Adds an item to the rear of the queue.
        Time Complexity: O(1) -> Instantly links via structural tracking pointer.
        """
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node  # Attach new node to the old tail
            self.rear = new_node       # Reassign the tail pointer to the new node
            
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.
        Time Complexity: O(1) -> Zero memory shifts or array copies executed.
        """
        if self.is_empty():
            print("Queue Underflow Exception! Cannot pop from an empty queue.")
            return None
        
        # Isolate target value
        removed_node = self.front
        removed_value = removed_node.data
        
        # Advance structural front pointer by one step to break the old link
        self.front = self.front.next
        
        # If the queue is now empty, ensure the rear pointer drops its reference
        if self.front is None:
            self.rear = None
            
        self._size -= 1
        
        # Explicit clean up for isolated node to assist Python garbage collection
        del removed_node
        
        return removed_value

    def peek(self):
        """
        Glance at the front node value without altering structural links.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Queue Inspection Note: Structure is completely empty.")
            return None
        return self.front.data

    def display_queue(self):
        """
        Iterate and render structural alignment on screen.
        Time Complexity: O(n)
        """
        if self.is_empty():
            print("Queue Blueprint: [Empty]")
            return
            
        print("FRONT -> ", end="")
        temp_head = self.front
        while temp_head is not None:
            print(f"[{temp_head.data}]", end=" -> ")
            temp_head = temp_head.next
        print("REAR")


# ==============================================================================
# RUNTIME ARCHITECTURE VERIFICATION
# ==============================================================================
if __name__ == "__main__":
    print("=== Constructing High Performance Linked Queue ===")
    order_pipeline = LinkedListQueue()

    print("\n--- Phase 1: Dynamic O(1) Enqueue Processing ---")
    order_pipeline.enqueue("Order_001")
    order_pipeline.enqueue("Order_002")
    order_pipeline.enqueue("Order_003")
    order_pipeline.display_queue()
    print(f"Current Pipeline Volume: {order_pipeline.size()}")

    print("\n--- Phase 2: Instantaneous Peek Operation ---")
    print(f"Next Up For Processing: {order_pipeline.peek()}")

    print("\n--- Phase 3: High Efficiency O(1) Dequeue Execution ---")
    print(f"Dispatched: {order_pipeline.dequeue()}")
    print(f"Dispatched: {order_pipeline.dequeue()}")
    
    print("\n--- Phase 4: Current Structural Pipeline Status ---")
    order_pipeline.display_queue()
    print(f"Remaining Pipeline Volume: {order_pipeline.size()}")

    print("\n--- Phase 5: Clearing Remaining Inventory ---")
    print(f"Dispatched: {order_pipeline.dequeue()}")
    print(f"Is Pipeline Empty?: {order_pipeline.is_empty()}")
