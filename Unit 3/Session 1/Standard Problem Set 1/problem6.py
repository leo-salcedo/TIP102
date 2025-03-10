def edit_post(post):
  list = post.split(" ")
  cock = []
  for word in list:
    stack = []
    for letter in word:
      stack.append(letter)
    reverse_word = []
    while stack:
      reverse_word.append(stack.pop())
    cock.append(''.join(reverse_word))
  result = ' '.join(cock)
  return result


print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 