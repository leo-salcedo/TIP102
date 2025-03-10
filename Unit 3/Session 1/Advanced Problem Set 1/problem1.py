def arrange_guest_arrival_order(arrival_pattern):
  stack = []
  result = []
  for i in range(len(arrival_pattern) + 1):
    # Push the next digit (starting from 1)
        stack.append(str(i + 1))
        
        # If at the end or the current pattern character is 'I', empty the stack
        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                result.append(stack.pop())
    
  return "".join(result)

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  