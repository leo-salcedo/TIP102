def is_symmetrical_title(title):
  l, r = 0, len(title) - 1
  while l < r:
    while title[l] == ' ' or title[l] in '!,.':
      l += 1
    while title[r] == ' ' or title[r] in '!,.':
      r -= 1
    if title[l].lower() != title[r].lower():
      return False
    l += 1
    r -= 1
  return True




print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 