class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    def recurse(node1, node2):
        if not node1 and not node2:
            return True
        if node1 and not node2:
            return False
        if not node1 and node2:
            return False
        if node1.val != node2.val:
            return False
        if node1.val == node2.val:
            return True and recurse(node1.left, node2.left) and recurse(node1.right, node2.right)

    return recurse(root1, root2)


"""
      1                1
     / \              / \
    2   3            2   3  
"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

"""
      1                1
     /                  \
    2                    2  
"""

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))