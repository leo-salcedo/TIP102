def post_compare(draft1, draft2):
  stack1 = []
  stack2 = []
  for letter in draft1:
    if stack1:
      if letter == '#':
        stack1.pop()
      else:
        stack1.append(letter)
    else:
      if letter != '#':
        stack1.append(letter)
  for letter in draft2:
    if stack2:
      if letter == '#':
        stack2.pop()
      else:
        stack2.append(letter)
    else:
      if letter != '#':
        stack2.append(letter)
  return ''.join(stack1) == ''.join(stack2)


print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 