def longest_subsequence(s):
    seen = set()
    result = ''
    left, right = 0, 0
    while right < len(s):
        if s[right] not in seen:
            seen.add(s[right])
            max_length = max(max_length, (right - left + 1))
            right += 1
        else:
            seen.remove(s[left])
            left += 1
     
    return max_length



print(longest_subsequence("abcabcbb"))  # Output: 3
print(longest_subsequence("bbbbb"))     # Output: 1
print(longest_subsequence("pwwkew"))    # Output: 3
print(longest_subsequence(""))          # Output: 0
print(longest_subsequence("abcdef"))    # Output: 6
