class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    def recurse(node):
        if not node:
            return 0
        if node.val == '+':
            return calculate_yield(node.left) + calculate_yield(node.right)
        elif node.val == '-':
            return calculate_yield(node.left) - calculate_yield(node.right)
        elif node.val == '*':
            return calculate_yield(node.left) * calculate_yield(node.right)
        elif node.val == '/':
            return calculate_yield(node.left) // calculate_yield(node.right)
        else:
            return node.val
    return recurse(root)



"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))