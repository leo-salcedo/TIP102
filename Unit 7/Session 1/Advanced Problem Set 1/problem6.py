def evaluate_ternary_expression_recursive(expression):
    def helper(i):
        # Base case: return a digit or boolean value if it's just that
        if i >= len(expression) or expression[i] not in 'TF?:':
            return expression[i], i
        
        # Current character should be a condition (either 'T' or 'F')
        condition = expression[i]
        i += 2  # Skip over '?' after the condition
        
        # Recursively evaluate the true_expression
        true_result, i = helper(i)
        
        # Skip over the ':' separating true and false expressions
        i += 2
        
        # Recursively evaluate the false_expression
        false_result, i = helper(i)
        
        # Return the appropriate result based on the condition
        if condition == 'T':
            return true_result, i
        else:
            return false_result, i
    
    # Start the recursive evaluation from the first character
    result, _ = helper(0)
    return result
    


print(evaluate_ternary_expression_recursive("T?2:3"))
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))