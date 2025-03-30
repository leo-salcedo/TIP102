class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
	    print(current.value, end=" -> " if current.next else "\n")
	    current = current.next

def split_protein_chain(protein, k):
    pass