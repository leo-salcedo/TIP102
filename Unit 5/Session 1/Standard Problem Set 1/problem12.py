class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_list(head):
	result = ""
	current = head
	while current.next is not None:
		result += str(current.value)
        if current.next is not None:
            result += " -> "
        current = current.next
	return result




isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj


print(print_list(isabelle))