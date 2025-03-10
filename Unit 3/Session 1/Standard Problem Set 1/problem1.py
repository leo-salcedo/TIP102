def is_valid_post_format(posts):
  # Understand - Ensure string is balanced
  # Plan - Use a stack to keep track of all opening braces, loop through string, if opening brace push to stack,
  # otherwise check if top element of stack is same type as current closing brace, if it is then pop, otherwise return false.
  # first check if stack is empty before trying to pop, then return if length of stack = 0 at end
  # Implement 
  stack = []
  for char in posts:
    if char in "([{":
      stack.append(char)
    elif char ==  ")":
      if len(stack) == 0:
        return False
      else:
        if stack[-1] == "(":
          stack.pop()
    elif char == "]":
      if len(stack) == 0:
        return False
      else:
        if stack[-1] == "[":
          stack.pop()
    elif char == "}":
        if len(stack) == 0:
            return False
        else:
            if stack[-1] == "{":
                stack.pop()
  return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]")) # ([)]