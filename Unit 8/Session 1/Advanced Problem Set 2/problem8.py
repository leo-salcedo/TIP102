class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_symmetric(root):
    def recurse(node1, node2):
        if not node1 and not node2:
            return True
        if (not node1 and node2) or (node1 and not node2):
            return False
        if node1.val != node2.val:
            return False
        return recurse(node1.left, node2.right) and recurse(node1.right, node2.left)
    
    return recurse(root.left, root.right)
        


"""
        A
      /   \
     B     B
    / \   / \
   C  D   D  C
"""
coral1 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('D'), TreeNode('C')))


"""
        A
      /   \
     B     B
    / \   / \
   C  D   C  D
"""
coral2 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('C'), TreeNode('D')))

print(is_symmetric(coral1))
print(is_symmetric(coral2))