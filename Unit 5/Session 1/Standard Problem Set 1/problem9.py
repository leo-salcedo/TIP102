class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy
timmy = Node("Timmy")
timmy.next = tommy
tom_nook.next = timmy
tom_nook.next = None
saharah = Node("Saharah")
tommy.next = saharah
print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 
