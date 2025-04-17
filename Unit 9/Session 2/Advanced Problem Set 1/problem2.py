from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def count_cookie_paths(root, target_sum):
    def recurse(node, current, target):
        if not node:
            return 0
        current += node.val
        if current == target:
            return 1
        return recurse(node.left, current, target) + recurse(node.right, current, target)
    
    return recurse(root, 0, target_sum)





# Using build_tree() function included at the top of the page
cookie_nums = [10, 5, 8, 3, 7, 12, 4]
cookies1 = build_tree(cookie_nums)


cookie_nums = [8, 4, 12, 2, 6, None, 10]
cookies2 = build_tree(cookie_nums)

print(count_cookie_paths(cookies1, 22)) 
print(count_cookie_paths(cookies2, 14))

