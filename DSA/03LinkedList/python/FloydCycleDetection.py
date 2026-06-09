class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CyclicLL:
    def __init__(self):
        self.head = None

    def has_cycle(self):
        """Phase 1: Detect if a cycle exists in the Linked List. Not necessary that tail opoint to head."""
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps

            if slow == fast:
                return True           # Cycle detected!
                
        return False                  # Fast reached the end, no cycle

    def find_and_remove_cycle(self):
        """Phase 2 & 3: Find the starting point of the cycle and break it safely."""
        slow = self.head
        fast = self.head
        cycle_exists = False

        # Phase 1: Standard Detection Loop
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_exists = True
                break

        if not cycle_exists:
            print("No cycle found in the list.")
            return

        # Phase 2: Find the exact entry point of the cycle
        slow = self.head  # Reset slow pointer to head
        while slow != fast:
            slow = slow.next
            fast = fast.next  # Move fast at 1 step speed now

        cycle_start_node = slow
        print(f"Cycle detected! It starts at node with value: {cycle_start_node.data}")

        # Phase 3: Locate the tail node and break the circular link
        tail_pointer = cycle_start_node
        while tail_pointer.next != cycle_start_node:
            tail_pointer = tail_pointer.next

        tail_pointer.next = None  # Breaking the loop cleanly
        print("The circular loop has been safely severed. List is now linear.")


# ==========================================
# Verification & Test Case Setup
# ==========================================
if __name__ == "__main__":
    # Create nodes: 10 -> 20 -> 30 -> 40 -> 50
    ll = CyclicLL()
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)

    # Link nodes linearly
    ll.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    print(f"Initial Check (Linear List) - Has Cycle?: {ll.has_cycle()}")

    # Dynamically inject a cycle: Link 50 back to 30 (Loop: 30 -> 40 -> 50 -> 30)
    n5.next = n3
    print(f"Post-Injection Check (Circular Loop) - Has Cycle?: {ll.has_cycle()}")

    # Automatically identify entry node and break the circular constraint
    ll.find_and_remove_cycle()

    print(f"Final Validation Check - Has Cycle?: {ll.has_cycle()}")
