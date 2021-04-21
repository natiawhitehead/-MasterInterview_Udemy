# Given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.

def xorOperation(n, start):
    answer = start
    for i in range(1, n):
        next = start + 2 * i
        answer = answer ^ next
    return answer


print(xorOperation(5, 0))
