def clean_post(post):
  stack = []
  for letter in post:
    if letter.islower():
      stack.append(letter)
    else:
      if letter.lower() == stack[-1]:
        stack.pop()
  res = ''.join(stack)
  return res


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s"))