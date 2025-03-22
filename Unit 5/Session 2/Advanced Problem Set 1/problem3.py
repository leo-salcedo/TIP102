class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    frequency = {}
    curr = head
    while curr:
        if curr.value not in frequency:
            frequency[curr.value] = 1
        else:
            frequency[curr.value] += 1
        curr = curr.next
    # Complete frequency map
    print(frequency)
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    
    while curr:
        if frequency[curr.value] > 1:
            prev.next = curr.next  # Remove curr from the list
        else:
            prev = curr  # Only move prev if no deletion
        curr = curr.next
        
    return dummy.next



head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))