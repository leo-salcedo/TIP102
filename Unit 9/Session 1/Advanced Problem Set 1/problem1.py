from collections import deque
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    if not design:
        return []
    q = deque()
    q.append(design)
    res = []
    while q:
        same_level = []
        for i in range(len(q)):
            current = q.popleft()
            same_level.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        res.append(same_level)
    return res

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))