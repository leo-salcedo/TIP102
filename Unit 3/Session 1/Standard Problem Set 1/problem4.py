def engagement_boost(engagements):
    left, right = 0, len(engagements) - 1
    result = [0] * len(engagements)
    position = len(engagements) - 1  # Start filling from the end

    while left <= right:
        left_square = engagements[left] ** 2
        right_square = engagements[right] ** 2

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        
        position -= 1  # Move the position leftward

    return result


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))