# Given two arrays of integers nums and index. Your task is to create target array under the following rules:

# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

# It is guaranteed that the insertion operations will be valid.

def createTargetArray(nums, index):
    answer = [None] * len(nums)
    for i in range(len(nums)):
        if answer[index[i]] is None:
            answer[index[i]] = nums[i]
        else:
            shiftArray(answer, index[i])
            answer[index[i]] = nums[i]
    return answer


# find empty slot and move array to make index[i]th slot available
def shiftArray(nums, index):
    temp = nums[index]
    index += 1
    while nums[index] is not None:
        nextValue = nums[index]
        nums[index] = temp
        temp = nextValue
        index += 1
    nums[index] = temp


nums, index = [0, 1, 2, 3, 4], [0, 1, 2, 2, 1]
print(createTargetArray(nums, index))
