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

def edit_dna_sequence(dna_strand, m, n):
    curr = dna_strand
    while curr.next:
        for i in range(m - 1):
            curr = curr.next
        delete = curr.next
        i = 0
        if not delete.next:
            curr.next = None
            return dna_strand
        while delete.next and i < n:
            temp = delete.next
            curr.next = delete.next
            delete = temp
            i += 1
        curr = delete
    return dna_strand
    


dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))