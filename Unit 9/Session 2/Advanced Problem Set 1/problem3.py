from collections import defaultdict
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_popular_cookie_combo(root):
    frequency = defaultdict(0)
    def dfs(node):
        if not node:
            return 0
        frequency[node.val] += 1 
        return node.val + dfs(node.left) + dfs(node.right)
    
    if not root:
        return 0 
    
    result_left = dfs(root.left)
    frequency[result_left] = frequency.get(result_left, 0) += 1



cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))


cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

print(most_popular_cookie_combo(cookies1))  
print(most_popular_cookie_combo(cookies2)) 