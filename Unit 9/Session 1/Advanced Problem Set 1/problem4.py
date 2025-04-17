from collections import deque

class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def larger_order_tree(order_tree, order):
    if not order_tree:
        return TreeNode(None)
    
    def bfs(root, target):
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            
            if target.val in level:
                target_index = level.index(target.val)
                if target_index + 1 >= len(level):
                    return TreeNode(None)
                return TreeNode(level[target_index + 1])
        return TreeNode(None)
    
    return bfs(order_tree, order)



cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)