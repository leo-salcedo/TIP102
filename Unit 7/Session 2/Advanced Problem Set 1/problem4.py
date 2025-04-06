def next_greatest_letter(letters, target):
    new_char = chr(ord(target) + 1)
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] == new_char:
            return letters[mid]
        elif ord(letters[mid]) < ord(new_char):
            left = mid + 1
        else:
            right = mid - 1
    return letters[0]


letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))