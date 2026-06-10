class CircularQueue:
    """
    A space-efficient Circular Queue (Ring Buffer) implemented using a 
    fixed-size array and mathematical modulo mapping to wrap pointers around.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """Check if the circular queue contains no elements."""
        return self.front == -1

    def is_full(self):
        """Check if the next available entry slot matches the current front index."""
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        """Calculate the current number of elements inside the circular ring."""
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        # Handle wrapped state math
        return self.capacity - (self.front - self.rear - 1)

    def enqueue(self, value):
        """
        Adds an item to the rear of the ring buffer, recycling empty spaces.
        Time Complexity: O(1)
        """
        if self.is_full():
            print(f"Queue Overflow! Cannot enqueue '{value}'. Buffer is entirely full.")
            return False

        # If it is the first element being inserted
        if self.is_empty():
            self.front = 0

        # Mathematically wrap the rear pointer around if it hits the capacity bound
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        return True

    def dequeue(self):
        """
        Removes and returns the item sitting at the front of the circular ring.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from an empty ring buffer.")
            return None

        removed_value = self.queue[self.front]
        self.queue[self.front] = None  # Explicitly clear reference to free memory

        # Case 1: The last remaining element was just removed, reset the queue completely
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Case 2: Mathematically wrap the front pointer around to the next slot
            self.front = (self.front + 1) % self.capacity

        return removed_value

    def peek(self):
        """View the next element up for removal without removing it."""
        if self.is_empty():
            print("Inspection Note: Circular Queue is empty.")
            return None
        return self.queue[self.front]

    def display_queue(self):
        """Render the accurate linear sequence of elements currently active in the ring."""
        if self.is_empty():
            print("Circular Queue: [Empty Loop]")
            return

        print("FRONT -> ", end="")
        index = self.front
        while True:
            print(f"[{self.queue[index]}]", end=" -> ")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print("REAR (Loop Connected)")

    def print_raw_array_layout(self):
        """Debug helper to view the actual under-the-hood contiguous memory array layout."""
        print(f"Raw Internal List Snapshot: {self.queue} | Front Index: {self.front} | Rear Index: {self.rear}")


# ==============================================================================
# RUNTIME ARCHITECTURE VERIFICATION
# ==============================================================================
if __name__ == "__main__":
    print("=== Constructing Fixed Size Ring Buffer (Capacity = 3) ===")
    stream_buffer = CircularQueue(3)

    print("\n--- Phase 1: Filling Up Capacity ---")
    stream_buffer.enqueue("Packet_A")
    stream_buffer.enqueue("Packet_B")
    stream_buffer.enqueue("Packet_C")
    stream_buffer.display_queue()
    stream_buffer.print_raw_array_layout()

    print("\n--- Phase 2: Triggering Overflow Condition ---")
    stream_buffer.enqueue("Packet_D")  # Should safely print an overflow note

    print("\n--- Phase 3: Dequeuing Elements to Free Up Memory Slots ---")
    print(f"Processed: {stream_buffer.dequeue()}")
    print(f"Processed: {stream_buffer.dequeue()}")
    stream_buffer.display_queue()
    stream_buffer.print_raw_array_layout()

    print("\n--- Phase 4: Recycling Old Memory (Wrapping Around) ---")
    print("Enqueuing Packet_D and Packet_E into the empty spaces left behind...")
    stream_buffer.enqueue("Packet_D")
    stream_buffer.enqueue("Packet_E")
    
    # Notice how the display loop reads correctly, even though D and E are physically at the start of the array
    stream_buffer.display_queue()
    stream_buffer.print_raw_array_layout()
    print(f"Active elements count: {stream_buffer.size()}")
