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

def middle_match(head, val):
    length = 0
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        length += 1
    return slow.value == val if length % 2 == 1 else slow.next.value == val


kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))
tournament_tracks = Node("Rainbow Road", Node("Bowser Castle", Node("Sherbet Land", Node("Yoshi Valley"))))

print(middle_match(kart_choices, "Wild Wing"))
print(middle_match(tournament_tracks, "Bowser Castle"))